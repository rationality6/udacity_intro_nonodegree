import random


class Baseball_Engine(object):

    def __init__(self):
        self.random_number_list = random.sample(range(1, 10), 3)
        # print self.random_number_list

    def input_filter(self, user_input):
        """
        Check the numbers and convert it to list
        """
        input_list = [int(i) for i in str(user_input)]
        if 3 < len(input_list):
            print "It's three numbers. it's too many."
        elif 3 > len(input_list):
            print "Tt's three numbers. it's too small"
        else:
            return self.check_score(input_list)

    def check_score(self, user_input_list):
        """
        check scores and return list
        """
        for i in range(0, 3):
            for j in range(0, 3):
                if self.random_number_list[i] == user_input_list[j] and i == j:
                    self.strike += 1
                elif self.random_number_list[i] == user_input_list[j] and i != j:
                    self.ball += 1
        self.tried += 1
        print "Strikes : {}".format(self.strike)
        print "Balls : {}".format(self.ball)
        print "Tried : {}".format(self.tried)
        return user_input_list

    def play(self):
        """
        main routine
        """
        self.total_score
        self.tried = 0
        while True:
            self.strike = 0
            self.ball = 0
            user_input = raw_input('Type your guess > ')
            user_input_list = self.input_filter(user_input)
            if self.random_number_list == user_input_list:
                print "You won. Tried : {}".format(self.tried)
                return True


if __name__ == "__main__":
    game = Baseball_Engine()
    game.play()
