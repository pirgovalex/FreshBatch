with open("cats.txt") as f:
    content = f.read()
    
    @classmethod
    def CATS123(cls):
        x = letter_count = content.count(' cat ')
        y = letter_count2 = content.count(' whiskers ')
        if letter_count > letter_count2:
            print(str.upper("cats! I'm a kitty cat!"), letter_count % letter_count2, x, y)
        elif letter_count == letter_count2:
            for _ in range(3):
                for i in range(1, 11):
                    print(i)
        else:
            print(letter_count,'\n',letter_count2)
    @classmethod
    def CATS22(cls):
        words=content.split()
        word_counts_world={}
        for word in words:
           if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
exec(CATS123)

        