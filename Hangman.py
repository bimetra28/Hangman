import random

phrases = ['Такой буквы нет, попробуйте еще.', 'Ты на один шаг ближе к провалу. УАХАХАХАХАХ!!!',
           'Тут не должно быть ошибки, но да ладно... Минус попытка',
           "Уже заготовлены веревка, стул и мыло...", "Ты не угадал. Ну хз... Попробуй \"Ж\"",
           'Не угадал. Закибербулен, получается...', 'Будет странно, если ты отгадаешь.', 'Ах какой молодец! Столько букв НЕ угадал.',
           'Ум это не главное. Зато ты очень красивый(ая)']

end_phrases = ['Такой буквы нет, осталась одна попытка!', 'Виселица ждет тебя, мой юный падаван.',
               'Ну эт самое... Тут наши полномочия всё. Окончены.', 'Ну и что, что одна попытка. Я в тебя и в самом начале не верил)',
               'Твой последний шанс затащить эту катку']


def addLetters(letter, cipher, word):
    for i in range(len(word)):
        if letter.upper() == word[i]:
            cipher = cipher[:i] + letter + cipher[i+1:]
    return cipher


def usedLetter(cur_att):
    cur_att += 1
    print('Такая буква уже была использована. Будьте внимательней. Минус 1 попытка Гриффиндору!!!')
    return cur_att


def hangman(cur_att):
    if cur_att > 0:
        print('   |')
    if cur_att > 1:
        print('   O')
    if cur_att == 3:
        print('   |')
    if cur_att == 4:
        print('  /|')
    if cur_att > 4:
        print('  /|\ ')
    if cur_att == 6:
        print('  /')
    if cur_att == 7:
        print('  / \ ')


def start():
    print("Приветствую в игре \"Виселица\"!\n"
          "По правилам игры у вас есть 7 попыток отгадать слово. За каждую неверную букву, количество попыток снижается.\n"
          "Если не угадаете, на вашей совести будет повешенный человечек.\n"
          "Нажимайте на буквы на вашей клавиатуре, я же буду говорить есть ли они и на каким местах стоят.\n"
          "May the odds be ever in your favor!")
    main()


def main():
    try:
        with open('list_of_words.txt', 'r') as low:
            allText = low.read()
            words = list(allText.split())
    except:
        print('Не удалось открыть файл')
    word = random.choice(words).upper()
    MAX_ATTEMPTS = 7
    CUR_ATTEMPT = 0
    cipher = '_' * len(word)
    used_letters = []
    print(f"Ваше слово состоит из {len(word)} букв.")

    while True:
        print(' '.join(cipher))
        print(f'Осталось попыток: {MAX_ATTEMPTS - CUR_ATTEMPT}')
        letter = input('Введите букву: ').upper()

        if letter in word and letter not in used_letters:
            used_letters.append(letter)
            letter_counter = word.count(letter)
            if letter_counter == 1:
                print(f'Угадал! Такая буква есть. Она находится на {word.find(letter) + 1} месте.')
                cipher = addLetters(letter, cipher, word)
            elif letter_counter > 1:
                nums = []
                for i in range(len(word)):
                    if letter.upper() == word[i]:
                        nums.append(i+1)
                nums = [", ".join([str(i) for i in nums][:-1]), str(nums[-1])]
                print(f'Так держать! Таких букв {letter_counter}. Они расположены на {nums[0]} и {nums[1]} местах')
                cipher = addLetters(letter, cipher, word)
        elif letter in word and letter in used_letters:
            CUR_ATTEMPT = usedLetter(CUR_ATTEMPT)
            if CUR_ATTEMPT != 7:
                hangman(CUR_ATTEMPT)
        elif letter not in word and letter not in used_letters:
            used_letters.append(letter)
            CUR_ATTEMPT += 1
            if CUR_ATTEMPT == 6:
                print(random.choice(end_phrases))
                hangman(CUR_ATTEMPT)
            elif CUR_ATTEMPT < 6:
                print(random.choice(phrases))
                hangman(CUR_ATTEMPT)
        elif letter not in word and letter in used_letters:
            CUR_ATTEMPT = usedLetter(CUR_ATTEMPT)
            if CUR_ATTEMPT != 7:
                hangman(CUR_ATTEMPT)

        if CUR_ATTEMPT == 7 and cipher != word:
            hangman(CUR_ATTEMPT)
            print(f'Увы, слово не угадано и жизнь загублена. Правильное слово: {word}')
            break
        elif cipher == word:
            print(f'Поздравляю! Вы угадали слово {word} и спасли человечка от петли, возьмите с полки пирожок ;)')
            break

    choise = input('Хотите попробовать снова? (введите да / нет)\n'
                   '> ')
    if choise.startswith('д') or choise.startswith('Д'):
        main()
    else:
        print('До скорой встречи!')


if __name__ == '__main__':
    start()