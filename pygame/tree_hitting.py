class tree_hitting:

    def __init__(self):
        self.hit_point = 5
        self.treehit = 0

    def main_loop(self):
        while self.treehit < 10:
            print "Choose what you want to do"
            user_input = raw_input("1.hit 2.rest : ")

            if user_input == '1':
                if self.hit_point > 0:
                    self.treehit += 1
                    self.hit_point -= 2
                    print "%s times hit. hit point %s" % (self.treehit, self.hit_point)
                else:
                    print "You need rest!"
            elif user_input == '2':
                self.hit_point += 1
                print "You rested hit point : %s" % self.hit_point
            else:
                print "Type wrong."
        print "You got a love."

if __name__ == "__main__":
    game = tree_hitting()
    game.main_loop()
