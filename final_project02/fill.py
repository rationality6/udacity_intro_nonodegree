import os


def num_blanks_maker(answers):
    """
    input: list of answers
    output: list of blanks
    """
    blanks = []
    converter = 1
    for i in range(0, len(answers)):
        result = "__{0}__".format(i + converter)
        blanks.append(result)
    return blanks


def answer_mixer(score, answers):
    """
    input: list of answers
    output: mixed answers
    """
    num_blanks = num_blanks_maker(answers)

    counter = 0
    quiz_list = []
    while(counter < len(answers)):
        if score <= counter:
            quiz_list.append(num_blanks[counter])
        else:
            quiz_list.append(answers[counter])
        counter += 1
    return quiz_list


def winning():
    """
    Exiting
    """
    print("You won")
    exit()


def easy_blanks(tried, score, intro_check, answers):
    """
    inputs: tried, score, intro_check, answers.
    output: easy level messages
    """
    quiz_list = answer_mixer(score, answers)
    if tried == 0 and intro_check == False:
        print("You've chosen easy!\n\nYou will get 5 guesses per problem \n")
    print("The current paragraph reads as such:\nA common first thing to do in a language is display")
    print("'Hello {0}!' In {1} this is particularly easy; all you have to do".format(
        quiz_list[0], quiz_list[1]))
    print("is type in:")
    print("{0} \"Hello {1}!\"".format(quiz_list[2], quiz_list[0]))
    print("Of course, that isn't a very useful thing to do. However, it is an")
    print("example of how to output to the user using the {0} command, and".format(
        quiz_list[2]))
    print("produces a program which does something, so it is useful in that capacity.\n")
    print("It may seem a bit odd to do something in a Turing complete language that")
    print("can be done even more easily with an {0} file in a browser, but it's".format(
        quiz_list[3]))
    print("a step in learning {0} syntax, and that's really its purpose.\n\n".format(
        quiz_list[1]))
    if score == 4:
        winning()
    print("score : ", score)
    print("tried : ", tried)
    print("")


def medium_blanks(tried, score, intro_check, answers):
    """
    inputs: tried, score, intro_check, answers.
    output: medium level messages
    """
    quiz_list = answer_mixer(score, answers)
    if tried == 0 and intro_check == False:
        print("You've chosen medium!\n\nYou will get 5 guesses per problem\n")
    print("The current paragraph reads as such:\n")
    print("A {0} is created with the def keyword.  You specify the inputs a".format(
        quiz_list[0]))
    print("{0} takes by adding {1} separated by commas between the parentheses.".format(
        quiz_list[0], quiz_list[1]))
    print("{0}s by default returns {1} if you don't specify the value to retrun.".format(
        quiz_list[0], quiz_list[2]))
    print("{0} can be standard data types such as string, integer, dictionary, tuple,".format(
        quiz_list[1]))
    print("and {0} or can be more complicated such as objects and lambda functions.\n\n".format(
        quiz_list[3]))
    if score == 4:
        winning()
    print("score : ", score)
    print("tried : ", tried)
    print("")


def hard_blanks(tried, score, intro_check, answers):
    """
    inputs: tried, score, intro_check, answers.
    output: hard level messages
    """
    quiz_list = answer_mixer(score, answers)
    if tried == 0 and intro_check == False:
        print("You've chosen hard!\n\nYou will get 5 guesses per problem\n")
    print("The current paragraph reads as such:\n"
          )
    print("When you create a {0}, certain {1}s are automatically".format(
        quiz_list[0], quiz_list[1]))
    print("generated for you if you don't make them manually. These contain multiple")
    print("underscores before and after the word defining them.  When you write")
    print("a {0}, you almost always include at least the {1} {2}, defining".format(
        quiz_list[0], quiz_list[2], quiz_list[1])
    )
    print("variables for when {0}s of the {1} get made.  Additionally, you generally".format(
        quiz_list[3], quiz_list[0]))
    print("want to create a {0} {1}, which will allow a string representation".format(
        quiz_list[4], quiz_list[0]))
    print("of the method to be viewed by other developers.\n")
    print("You can also create binary operators, like {0} and {1}, which".format(
        quiz_list[5], quiz_list[6]))
    print("allow + and - to be used by {0} of the {1}.  Similarly, {2},".format(
        quiz_list[3], quiz_list[0], quiz_list[7]))
    print("{0}, and {1} allow {2}s of the {3} to be compared".format(
        quiz_list[8], quiz_list[9], quiz_list[3], quiz_list[0]))
    print("(with <, >, and ==).\n\n"
          )
    if score == 10:
        winning()
    print("score : ", score)
    print("tried : ", tried)
    print("")


def question_number(score):
    """
    adding +1 number for human
    """
    num = score + 1
    return "What should be substituted in for __{0}__? ".format(num)


def difficulty_set():
    """
    input: Difficulty level user want
    output: Difficulty level
    """
    did_before = False
    while(True):
        os.system('clear')
        print("Please select a game difficulty by typing it in")
        print("Possible choices include easy, medium, and hard.")
        if did_before == True:
            print('Type again')
        difficulty = input("Type : ")
        if difficulty == 'easy':
            return 'easy'
        elif difficulty == 'medium':
            return 'medium'
        elif difficulty == 'hard':
            return 'hard'
        else:
            did_before = True


def difficulty_logic(the_answer, score, score_max, tried, tried_max, intro_check, difficulty):
    """
    main game logic
    """
    while(score <= score_max and tried < tried_max):
        os.system('clear')
        if difficulty == 'easy':
            easy_blanks(tried, score, intro_check, the_answer)
        if difficulty == 'medium':
            medium_blanks(tried, score, intro_check, the_answer)
        if difficulty == 'hard':
            hard_blanks(tried, score, intro_check, the_answer)
        user_answer = input(question_number(score))
        intro_check = True
        if the_answer[score] == user_answer:
            score += 1
            tried = 0
        else:
            tried += 1


def main_game(difficulty):
    """
    main game function
    input: difficulty level
    output: main UI
    """
    tried = 0
    score = 0
    tried_max = 5
    score_max = 4
    hardmod_score_max = 10
    intro_check = False
    easy_answer = ['world', 'python', 'print', 'html']
    midium_answer = ['function', 'arguments', 'None', 'list']
    hard_answer = ['class', 'method', '__init__', 'instance',
                   '__repr__', "__add__", "__sub__", "__lt__", "__gt__", "__eq__"]
    if difficulty == 'easy':
        difficulty_logic(easy_answer, score, score_max,
                         tried, tried_max, intro_check, difficulty)
    if difficulty == 'medium':
        difficulty_logic(midium_answer, score, score_max,
                         tried, tried_max, intro_check, difficulty)
    if difficulty == 'hard':
        difficulty_logic(hard_answer, score, hardmod_score_max,
                         tried, tried_max, intro_check, difficulty)

# run

main_game(difficulty_set())
