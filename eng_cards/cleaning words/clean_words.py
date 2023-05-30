
new_word = ''
with open('words.txt', 'r') as words:
    with open('clean_words.txt', 'w', encoding='utf-8') as clean_words:
        for word in words:
            if word.endswith('\n'):
                print(word, end='')
            else:
                print(word)
            for letter in word:
                if letter != ' ':
                    new_word += letter
                    print(new_word)

                else:
                    clean_words.write(new_word)
                    clean_words.write('\n')
                    new_word = ''
                    break



