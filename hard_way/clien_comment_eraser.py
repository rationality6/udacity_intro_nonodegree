import re
import time
import ssl
import sys
import urllib
from http.cookiejar import CookieJar
from lxml import etree
from urllib.parse import urlparse, parse_qs


BASE_URL = 'https://www.clien.net'
M_BASE_URL = 'http://m.clien.net'
MY_ID = 'sdhee21'               # 아이디
MY_PASSWORD = 'PkgZR7hYWnfE7T'   # 비밀번호
SEARCH_DEPTH = 999              # [다음검색]을 누르는 횟수
REPLACE_WITH = '.'              # 바꿀 댓글 내용
MAXLEN_LOG_COMMENT = 15

TABLE_ID_LIST = [               # 테이블 ID
    'park',                     # 모두의 공원
    # 'cm_iphonien',              # 아이포니앙
    # 'cm_coffee',                # 클다방
]


def http_req(opener, url, formdata={}, method='GET'):
    data_encode = urllib.parse.urlencode(formdata, True)

    if method == 'GET':
        if formdata is not None and formdata != {}:
            url = url + '?' + data_encode
        response = opener.open(url)
    elif method == 'POST':
        response = opener.open(url, data_encode.encode('utf-8'))

    doc = response.read().decode(
        'utf-8', 'ignore').encode('utf-8')  # clear encoding problem

    return doc, etree.HTML(doc)


def init():
    cj = CookieJar()
    https_sslv3_handler = urllib.request.HTTPSHandler(
        context=ssl.SSLContext(ssl.PROTOCOL_SSLv3))
    opener = urllib.request.build_opener(
        https_sslv3_handler, urllib.request.HTTPCookieProcessor(cj))
    formdata = {
        'mb_id': MY_ID,
        'mb_password': MY_PASSWORD,
    }
    opener.addheaders.append(('Accept-Language', 'ko-KR'))
    http_req(opener, BASE_URL + '/cs2/bbs/login_check.php', formdata, 'POST')

    return opener


def search_posts(opener, table_id):
    print('\n *** {} 게시판 검색 시작 ***'.format(table_id))

    formdata = {
        'bo_table': table_id,
        'bo_style': 'lists',
        'sfl': 'mb_id_comment',
        'stx': MY_ID,
    }
    next_page_url = M_BASE_URL + '/cs3/board'

    for i in range(SEARCH_DEPTH):
        _, tree = http_req(opener, next_page_url, formdata)
        entries = tree.xpath(
            '//div[@class="paging"]/a[text()="다음검색"]')  # 다음검색 링크

        if len(entries) < 1:
            print('\n *** 오류? 다음검색 버튼을 찾을 수 없습니다. ***')
            return

        formdata = parse_qs(urlparse(entries[0].get('href')).query)
        next_page_url = M_BASE_URL + '/cs3/board'

        # 글 목록
        entries = tree.xpath('//table[@class="tb_lst_normal"]/tbody/'
                             'tr[.//span[@class="lst_tit" and text()[normalize-space()]] '
                             'and not(.//span[@class="lst_category"]/img)]')
        # list(map(print, [e.find('.//span[@class="lst_tit"]').text for e in
        # entries])) # debug

        for j, entry in enumerate(entries):
            subject = entry.find('.//span[@class="lst_tit"]')
            p = re.compile(r"(?<=location.href\=')(.*)(?=')")
            link_url = p.findall(entry.find(
                './/td[@class="cell_tit"]/div').get('onclick'))[0]
            post_id = parse_qs(link_url)['wr_id'][0]

            if j == 0:
                print('')

            print('# 댓글 검색 중: {} 번글: {}'.format(post_id, subject.text), end='')

            delete_comments(opener, next_page_url + link_url, post_id)

        if 'spt' not in formdata or int(formdata['spt'][0]) > 0:
            print('\n *** {} 게시판 끝까지 찾았습니다. ***'.format(table_id))
            return

        print('.', end='')
        sys.stdout.flush()
        time.sleep(0.9)


def delete_comments(opener, post_url, post_id):
    _, tree = http_req(opener, post_url)
    entries = tree.xpath('//div[(@class="reply" or @class="reply_add") '
                         'and (.//a[@class="btn_reply_modify"] or .//a[@class="btn_reply_del"])]')

    print(' (내 댓글 {}개)'.format(len(entries)),
          end='' if len(entries) > 0 else '\n')

    for entry in entries:
        comment_text = entry.find('.//div[@class="reply_txt scalable"]').text
        modify_href = entry.find('.//a[@class="btn_reply_modify"]').get('href')

        p = re.compile(r'(?<=\()(.*)(?=\))')
        table_id, comment_id = re.split(
            ',\s*', p.findall(modify_href)[0].replace("'", ''))

        doc, _ = http_req(opener,
                          M_BASE_URL + '/cs3/board?bo_style=comment_delete&bo_table={}&wr_id={}'
                          .format(table_id, comment_id))

        if '답변코멘트가 존재하므로' in doc.decode('utf-8'):
            formdata = {
                'w': 'cu',
                'bo_table': table_id,
                'wr_id': post_id,
                'comment_id': comment_id,
                # 'sca': '', 'sfl': '', 'stx': '', 'spt': '',
                'page': '1',
                # 'cwin': '', 'is_good': '',
                'wr_content': REPLACE_WITH,
            }
            time.sleep(0.3)
            http_req(opener,
                     M_BASE_URL +
                     '/cs3/board/comment_write_excute/'.format(
                         table_id, comment_id),
                     formdata,
                     method='POST')

            if comment_text == REPLACE_WITH:
                print(' == 이미 수정')
                continue
            else:
                print(' == 댓글 수정 완료: "{}" -> "{}"'.format(comment_text[:MAXLEN_LOG_COMMENT],
                                                          REPLACE_WITH), end='')
        else:
            print(' == 댓글 삭제 완료: ' + comment_text[:MAXLEN_LOG_COMMENT], end='')

        print('')
        time.sleep(0.3)

if __name__ == '__main__':
    opener = init()

    for table_id in TABLE_ID_LIST:
        search_posts(opener, table_id)

    opener.close()
