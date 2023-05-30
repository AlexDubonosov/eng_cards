import random


def choice_random_word(text):
    # выбор случайного слова
    word = random.choice(text)
    text.remove(word)
    print(word[0])
    return word


def main_program(text):
    word = choice_random_word(text)
    command = input('> ')
    while command != 'a' and command != 'd' and command != 'end' and command != 'c':
        command = input('> ')
    if command == 'a':
        # когда не знаем слово
        print(word[0], '-', word[1], '\n')
        with open('forgetting_words.txt', 'a', encoding='utf-8') as forgetting_words:
            forgetting_words.write(f'{word[0]} {word[1]}\n')
        main_program(text)
    elif command == 'd':
        # когда знаем слово
        print(word[0], '-', word[1], '\n')
        with open('known_words.txt', 'a', encoding='utf-8') as known_words:
            known_words.write(f'{word[0]} {word[1]}\n')
        main_program(text)
    elif command == 'end':
        # удаляем слова, которые прошли в этой сессии, из основного списка + завершаем выполнение
        print(word[0], '-', word[1], '\n')
        with open('A1.txt', 'w', encoding='utf-8') as rewrite_words:
            for word in text:
                word = ' '.join(word)
                rewrite_words.write(f'{word}\n')
        return False
    elif command == 'c':
        # проверить перевод
        print('Check the word: ', word[1])
        main_program(text)


with open('A1.txt', 'r', encoding='utf-8') as words:
    # with open('A2.txt', 'r', encoding='utf-8') as words:
    # with open('B1.txt', 'r', encoding='utf-8') as words:
    # with open('B2.txt', 'r', encoding='utf-8') as words:

    # превращаем пары слов в список и объединяем в единый список для обработки
    all_words = words.read()
    all_words = all_words.split('\n')
    all_words = [word.split() for word in all_words]

is_end = True
while is_end:
    is_end = main_program(all_words)
