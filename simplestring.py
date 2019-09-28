import random

class SimpleStringCombiner:
    def __init__(self, wl):
        self.wordlist = wl  
        self.sprinkles = False #random symbols intermixed
        self.sprinkleset = ['_', '$'] # _, +, $, etc...
        self.sprinkledensity = 0.05 #idk, seems about right...
        self.maxwordlength = 25
        self.minwordlength = 12

    def random_word(self, file):
        #waterman's reservoir algorithm
        f = open(file)
        line = next(f)
        for num, aline in enumerate(f, 2):
            if random.randrange(num): continue
            line = aline
        f.close()
        return line

    def new(self, num):
        num = random.randint(1, num)
        retry = True
        while retry:
            words = []
            retry = False
            for i in range(num):
                words.append(self.random_word(self.wordlist))
            word = ""
            for w in words:
                w = w.capitalize()
                w = w.strip()
                word += w
            if (len(word) > self.maxwordlength) or (len(word) < self.minwordlength):
                retry = True
        # pass through, adding sprinkles
        if self.sprinkles:
            for i in range(len(word) -1):
                sprinkle_index = random.randint(0, len(self.sprinkleset) -1)
                if random.random() < self.sprinkledensity:
                    word = word[:i] + self.sprinkleset[sprinkle_index] + word[i:]
        return word



#main
wordlist = "mit_simplewords.txt"
ssc = SimpleStringCombiner(wordlist)
ssc.sprinkles = True
print(ssc.new(5))