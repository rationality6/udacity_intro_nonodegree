import os
import sys
from random import randrange


class Buyer:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def get_more_money(self):
        add_money = 20
        self.money += add_money


class Item:

    def __init__(self, item_name, stock, price):
        self.item_name = item_name
        self.stock = stock
        self.price = price

    def stock_left(self):
        return "%s left %s." % (self.item_name, self.stock)

    def buy_one(self, buyer):
        if self.stock > 0:
            if buyer.money >= self.price:
                stock_count = 1
                buyer.money -= self.price
                self.stock -= stock_count
                return "Here is your %s %s" % (self.item_name, buyer.name)
            else:
                print("Get more money")
                out_of_money(buyer)
        else:
            return "{0} is out".format(self.item_name)


class VendingMachine():

    def __init__(self, items):
        def total_item_counter(items):
            count = 1
            total_item = 0
            for i in items:
                total_item += count
            return total_item

        self.how_many_items_got = total_item_counter(items)
        self.items = items

    def greeting_buyer(self, buyer):
        return "Would you like to drink? %s?" % buyer.name

    def input_print_text_maker(self):
        final_print = ""
        for item in range(0, self.how_many_items_got):
            final_print += "%s." % item + \
                "{} ".format(self.items[item].item_name)
        return final_print

    def choice_printer(self, user_input, buyer):
        for item in range(0, self.how_many_items_got):
            if user_input == str(item):
                print(self.items[item].buy_one(buyer))
                print(self.items[item].stock_left())

    def main_loop(self, buyer):
        """
        Main loop for UI
        """
        os.system('clear')

        while buyer.money >= 0:
            print("You have : %s" % buyer.money)
            user_input = input(self.input_print_text_maker())
            os.system('clear')
            self.choice_printer(user_input, buyer)

            # if user_input == '1':
            #     select_list = [coffee, water, juice, coca_cola, milk]
            #     random_select_num = randrange(0, 5)
            #     print("God knows the number..")
            #     print(select_list[random_select_num].buy_one(buyer))
            #     print(select_list[random_select_num].stock_left())


def out_of_money(buyer):
    while True:
        print("You have : %s" % buyer.money)
        print("You are out of money. Choose what you do")
        user_input = input("1.Get more money, 2.Get more stock, 3.Exit : ")
        if user_input == "1":
            buyer.get_more_money()
            print(buyer.money)
            return
        elif user_input == "2":
            pass
        elif user_input == "3":
            sys.exit()
        else:
            print("Wrong type")

if __name__ == '__main__':

    john = Buyer('John', 120)

    coffee = Item('Coffee', 7, 20)
    juice = Item('Juice', 2, 10)
    water = Item('Water', 4, 5)
    coca_cola = Item('Coca cola', 2, 8)
    milk = Item('Milk', 4, 9)
    coconut_milk = Item('Coconut Milk', 4, 15)

    items = [coffee, juice, water, coca_cola, milk, coconut_milk]

    ven1 = VendingMachine(items)
    ven1.main_loop(john)


# 주석넣기
# 아이템 오브젝트량 계산 자동화
# 게임 분기라인 개선
# 총 stock 계산해서 분기문
