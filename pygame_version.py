import pygame
import random
import pygame_widgets
from pygame_widgets.button import Button
pygame.init()

W = 1184
H = 734

sf = pygame.display.set_mode((W, H))
pygame.display.set_caption('Hangman')
pygame.display.set_icon(pygame.image.load('icons/hangman.png'))
background = pygame.image.load('icons/background.jpg')
att_background = pygame.image.load('icons/att_background.jpg')
word_background = pygame.image.load('icons/word_background.jpg')
but_sound = pygame.mixer.Sound('sounds/button_sound1.wav')
pygame.mixer.music.load('sounds/bg_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
bg_rect = background.get_rect(topleft=(0, 0))
att_rect = att_background.get_rect(topright=(W, 0))
word_rect = word_background.get_rect(topright=(W, 330))


counter = 0
pause = False
clock = pygame.time.Clock()
FPS = 60

phrases = ['Такой буквы нет, попробуйте еще.', 'Ты на один шаг ближе к провалу. УАХАХАХАХАХ!!!',
           'Тут не должно быть ошибки, но да ладно... Минус попытка',
           "Уже заготовлены веревка, стул и мыло...", "Ты не угадал. Ну хз... Попробуй \"Ж\"",
           'Не угадал. Закибербулен, получается...', 'Будет странно, если ты отгадаешь.', 'Ах какой молодец! Столько букв НЕ угадал.',
           'Ум это не главное. Зато ты очень красивый(ая)']

end_phrases = ['Такой буквы нет, осталась одна попытка!', 'Виселица ждет тебя, мой юный падаван.',
               'Ну эт самое... Тут наши полномочия всё. Окончены.', 'Ну и что, что одна попытка. Я в тебя и в самом начале не верил)',
               'Твой последний шанс затащить эту катку']


def addletters(letter, cipher, word):
    for i in range(len(word)):
        if letter == word[i]:
            cipher = cipher[:i] + letter + cipher[i+1:]
    return cipher


def main():
    #
    sf.blit(background, bg_rect)
    music()
    letters = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
    used_letter = pygame.image.load('icons/used_letter.png')
    used_letter = pygame.transform.scale(used_letter, (55, 55))
    num = 55
    y_cord = 480
    l_sys = pygame.font.SysFont('comicsansms', 55)
    for i in letters[0]:
        text = l_sys.render(i, True, (255, 255, 255))
        if i == 'М':
            num = 55
            y_cord = 570
        elif i == 'Ш':
            num = 251
            y_cord = 660
        pos = text.get_rect(center=(num, y_cord))
        sf.blit(text, pos)
        num += 98


    with open('list_of_words.txt', 'r') as low:
        alltext = low.read()
        words = list(alltext.split())
    word = random.choice(words).upper()
    CUR_ATTEMPT = 0
    used_letters = []

    cipher = '_' * len(word)
    cipherP = '  '.join(cipher)
    cipher_font = pygame.font.SysFont('comicsansms', 65)
    text = cipher_font.render(cipherP, True, (255, 255, 255))
    pos = text.get_rect(center=(W//2, 385))
    sf.blit(text, pos)
    flag = False
    button_back = Button(
        sf, 20, 670, 130, 45,
        text='назад',  # Text to display
        font=pygame.font.SysFont('comicsansms', 30),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=3,
        shadowColour=(140, 140, 140),
        radius=15,  # Radius of border corners (leave empty for not curved)
    )

    f = None
    while f == None:
        events = pygame.event.get()
        att_count = CUR_ATTEMPT
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(event.pos)
                if 20 <= event.pos[0] <= 150 and 670 <= event.pos[1] <= 715:
                    but_sound.play()
                    f = start
                elif 70 <= event.pos[0] <= 100 and 15 <= event.pos[1] <= 45:
                    music(1)
                elif 20 <= event.pos[0] <= 60 and 10 <= event.pos[1] <= 50:
                    music(switch=True)
                elif 38 <= event.pos[0] <= 70 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(54, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'А', CUR_ATTEMPT, used_letters)
                elif 139 <= event.pos[0] <= 168 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(152, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Б', CUR_ATTEMPT, used_letters)
                elif 237 <= event.pos[0] <= 266 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(250, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'В', CUR_ATTEMPT, used_letters)
                elif 335 <= event.pos[0] <= 364 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(348, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Г', CUR_ATTEMPT, used_letters)
                elif 426 <= event.pos[0] <= 466 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(448, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Д', CUR_ATTEMPT, used_letters)
                elif 529 <= event.pos[0] <= 558 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(544, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Е', CUR_ATTEMPT, used_letters)
                elif 619 <= event.pos[0] <= 667 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(642, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ж', CUR_ATTEMPT, used_letters)
                elif 726 <= event.pos[0] <= 755 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(740, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'З', CUR_ATTEMPT, used_letters)
                elif 820 <= event.pos[0] <= 855 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(838, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'И', CUR_ATTEMPT, used_letters)
                elif 919 <= event.pos[0] <= 955 and 447 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(936, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Й', CUR_ATTEMPT, used_letters)
                elif 1019 <= event.pos[0] <= 1051 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(1034, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'К', CUR_ATTEMPT, used_letters)
                elif 1112 <= event.pos[0] <= 1149 and 462 <= event.pos[1] <= 504:
                    flag, letter_pos = True, used_letter.get_rect(center=(1132, 482))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Л', CUR_ATTEMPT, used_letters)
                elif 31 <= event.pos[0] <= 78 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(54, 574))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'М', CUR_ATTEMPT, used_letters)
                elif 133 <= event.pos[0] <= 170 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(152, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Н', CUR_ATTEMPT, used_letters)
                elif 230 <= event.pos[0] <= 270 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(250, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'О', CUR_ATTEMPT, used_letters)
                elif 325 <= event.pos[0] <= 370 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(348, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'П', CUR_ATTEMPT, used_letters)
                elif 434 <= event.pos[0] <= 460 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(446, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Р', CUR_ATTEMPT, used_letters)
                elif 529 <= event.pos[0] <= 561 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(546, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'С', CUR_ATTEMPT, used_letters)
                elif 624 <= event.pos[0] <= 661 and 559 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(643, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Т', CUR_ATTEMPT, used_letters)
                elif 723 <= event.pos[0] <= 758 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(740, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'У', CUR_ATTEMPT, used_letters)
                elif 823 <= event.pos[0] <= 857 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(838, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ф', CUR_ATTEMPT, used_letters)
                elif 916 <= event.pos[0] <= 955 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(936, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Х', CUR_ATTEMPT, used_letters)
                elif 1015 <= event.pos[0] <= 1056 and 549 <= event.pos[1] <= 602:
                    flag, letter_pos = True, used_letter.get_rect(center=(1034, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ц', CUR_ATTEMPT, used_letters)
                elif 1117 <= event.pos[0] <= 1148 and 549 <= event.pos[1] <= 598:
                    flag, letter_pos = True, used_letter.get_rect(center=(1132, 572))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ч', CUR_ATTEMPT, used_letters)
                elif 226 <= event.pos[0] <= 273 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(250, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ш', CUR_ATTEMPT, used_letters)
                elif 323 <= event.pos[0] <= 374 and 639 <= event.pos[1] <= 692:
                    flag, letter_pos = True, used_letter.get_rect(center=(347, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Щ', CUR_ATTEMPT, used_letters)
                elif 425 <= event.pos[0] <= 465 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(448, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ъ', CUR_ATTEMPT, used_letters)
                elif 518 <= event.pos[0] <= 572 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(545, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ы', CUR_ATTEMPT, used_letters)
                elif 630 <= event.pos[0] <= 658 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(642, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ь', CUR_ATTEMPT, used_letters)
                elif 723 <= event.pos[0] <= 756 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(740, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Э', CUR_ATTEMPT, used_letters)
                elif 807 <= event.pos[0] <= 868 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(838, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Ю', CUR_ATTEMPT, used_letters)
                elif 919 <= event.pos[0] <= 951 and 639 <= event.pos[1] <= 685:
                    flag, letter_pos = True, used_letter.get_rect(center=(936, 662))
                    CUR_ATTEMPT, cipher = playing(word, cipher, 'Я', CUR_ATTEMPT, used_letters)
        if CUR_ATTEMPT == 0 or CUR_ATTEMPT != att_count:
            sf.blit(att_background, att_rect)
            attempts_font = pygame.font.SysFont('comicsansms', 30)
            attempts = attempts_font.render(f'Сделано {CUR_ATTEMPT} ошибок из 7', True, 'white')
            sf.blit(attempts, (825, 1))
        if flag:
            sf.blit(used_letter, letter_pos)
            flag = False
        if CUR_ATTEMPT == 7 and cipher != word:
            status = 'dead'
            f = endgame(status, word)
        elif cipher == word:
            status = 'alive'
            f = endgame(status, word)
        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(FPS)
    button_back.hide()
    f()


def music(num=0, switch=False):
    global counter
    global pause
    sound_bg = pygame.image.load('icons/sound_background.jpg')
    sound_bg_rect = sound_bg.get_rect(topleft=(0, 0))
    arrow = pygame.image.load('icons/arrow.png')
    arrow_rect = arrow.get_rect(topleft=(70, 15))
    sf.blit(arrow, arrow_rect)
    without_sound_icon = pygame.image.load('icons/without_sound.png')
    wsi_rect = without_sound_icon.get_rect(topleft=(20, 10))
    sound_icon = pygame.image.load('icons/sound.png')
    si_rect = sound_icon.get_rect(topleft=(20, 10))
    list_of_tracks = ['sounds/bg_music.mp3', 'sounds/bg_music1.mp3', 'sounds/bg_music2.mp3']

    if pause:
        if switch:
            pause = False
            pygame.mixer.music.unpause()
            sf.blit(sound_bg, sound_bg_rect)
            sf.blit(sound_icon, si_rect)
            return False
        sf.blit(without_sound_icon, wsi_rect)
    else:
        if switch:
            pause = True
            pygame.mixer.music.pause()
            sf.blit(sound_bg, sound_bg_rect)
            sf.blit(without_sound_icon, wsi_rect)
            return False
        sf.blit(sound_icon, si_rect)


    if num == 1:
        counter += num
        if counter == len(list_of_tracks):
            counter = 0
        pygame.mixer.music.load(list_of_tracks[counter])
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        pause = False
        sf.blit(sound_bg, sound_bg_rect)
        sf.blit(sound_icon, si_rect)


def rules():
    sf.blit(background, bg_rect)
    music()
    title = pygame.font.SysFont('comicsansms', 30)
    another_text = pygame.font.SysFont('comicsansms', 20)
    text1 = title.render("Приветствую в игре \"Виселица\"!", True, 'white')
    text2 = another_text.render(
        "По правилам игры, у вас есть 7 попыток отгадать слово. За каждую неверную букву количество попыток снижается.",
        True, (255, 255, 255))
    text3 = another_text.render("Если не отгадаете, на вашей совести будет повешенный человечек.", True, 'white')
    text4 = another_text.render(
        "Вы выбираете букву на вашем экране, я же оставляю за собой право глумиться над вами, если она окажется неверной.", True, 'white')
    text5 = title.render("May the odds be ever in your favor!", True, 'white')
    pos1 = text1.get_rect(center=(W//2, 60))
    pos2 = text2.get_rect(topleft=(20, 100))
    pos3 = text3.get_rect(topleft=(20, 140))
    pos4 = text4.get_rect(topleft=(20, 180))
    pos5 = text5.get_rect(center=(W//2, 240))
    sf.blit(text1, pos1)
    sf.blit(text2, pos2)
    sf.blit(text3, pos3)
    sf.blit(text4, pos4)
    sf.blit(text5, pos5)
    button_back = Button(
        sf, 20, 670, 130, 45,
        text='назад',  # Text to display
        font=pygame.font.SysFont('comicsansms', 30),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=3,
        shadowColour=(140, 140, 140),
        radius=15,  # Radius of border corners (leave empty for not curved)
    )
    counter = 1
    f = None
    while f == None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 20 <= event.pos[0] <= 150 and 670 <= event.pos[1] <= 715:
                    but_sound.play()
                    f = start
                elif 70 <= event.pos[0] <= 100 and 15 <= event.pos[1] <= 45:
                    music(1)
                elif 20 <= event.pos[0] <= 60 and 10 <= event.pos[1] <= 50:
                    music(switch=True)
        if counter == 46:
            counter = 1
        f_t = pygame.image.load(f'icons/gifs/first time/first_time{counter}.jpeg')
        f_t_rect = f_t.get_rect(center=(W//2, 440))
        sf.blit(f_t, f_t_rect)
        counter += 1
        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(18)
    button_back.hide()
    f()


def playing(word, cipher, letter, CUR_ATTEMPT, used_letters):
    if letter in word and letter not in used_letters:
        used_letters.append(letter)
        letter_counter = word.count(letter)
        if letter_counter == 1:
            print(f'Угадал! Такая буква есть. Она находится на {word.find(letter) + 1} месте.')
            cipher = addletters(letter, cipher, word)
        elif letter_counter > 1:
            nums = []
            for i in range(len(word)):
                if letter.upper() == word[i]:
                    nums.append(i + 1)
            nums = [", ".join([str(i) for i in nums][:-1]), str(nums[-1])]
            print(f'Так держать! Таких букв {letter_counter}. Они расположены на {nums[0]} и {nums[1]} местах')
            cipher = addletters(letter, cipher, word)
    elif letter in word and letter in used_letters:
        CUR_ATTEMPT += 1
        print('Такая буква уже была использована. Будьте внимательней. Минус 1 попытка Гриффиндору!!!')
    elif letter not in word and letter not in used_letters:
        used_letters.append(letter)
        CUR_ATTEMPT += 1
        if CUR_ATTEMPT == 6:
            print(random.choice(end_phrases))
        elif CUR_ATTEMPT < 6:
            print(random.choice(phrases))
    elif letter not in word and letter in used_letters:
        CUR_ATTEMPT += 1
        print('Такая буква уже была использована. Будьте внимательней. Минус 1 попытка Гриффиндору!!!')
    cipherP = '  '.join(cipher)
    cipherP_font = pygame.font.SysFont('comicsansms', 65)
    text = cipherP_font.render(cipherP, True, 'white')
    pos = text.get_rect(center=(W//2, 385))
    sf.blit(word_background, word_rect)
    sf.blit(text, pos)
    return CUR_ATTEMPT, cipher


def start():
    sf.blit(background, bg_rect)
    music()
    l_sys = pygame.font.SysFont('comicsansms', 70)
    text = l_sys.render('Виселица', True, (230, 230, 230))
    pos = text.get_rect(center=(W//2, 110))
    sf.blit(text, pos)
    button_start = Button(
        sf, 440, 200, 300, 100,
        text='Начать игру',  # Text to display
        font=pygame.font.SysFont('comicsansms', 40),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=4,
        shadowColour=(140, 140, 140),
        radius=20,  # Radius of border corners (leave empty for not curved)
    )
    button_rules = Button(
        sf, 440, 350, 300, 100,
        text='Правила игры',  # Text to display
        font=pygame.font.SysFont('comicsansms', 38),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=4,
        shadowColour=(140, 140, 140),
        radius=20,  # Radius of border corners (leave empty for not curved)
    )
    button_exit = Button(
        sf, 440, 500, 300, 100,
        text='Выход',  # Text to display
        font=pygame.font.SysFont('comicsansms', 40),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=4,
        shadowColour=(140, 140, 140),
        radius=20,  # Radius of border corners (leave empty for not curved)
    )
    counter = 1
    f = None
    while f == None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(event.pos)
                if 440 <= event.pos[0] <= 740 and 200 <= event.pos[1] <= 300:
                    but_sound.play()
                    f = main
                elif 440 <= event.pos[0] <= 740 and 350 <= event.pos[1] <= 450:
                    but_sound.play()
                    f = rules
                elif 440 <= event.pos[0] <= 740 and 500 <= event.pos[1] <= 600:
                    but_sound.play()
                    exit()
                elif 70 <= event.pos[0] <= 100 and 15 <= event.pos[1] <= 45:
                    music(1)
                elif 20 <= event.pos[0] <= 60 and 10 <= event.pos[1] <= 50:
                    music(switch=True)
        if counter == 27:
            counter = 1
        s_a = pygame.image.load(f'icons/gifs/start animation/start_animation{counter}.gif')
        s_a = pygame.transform.scale(s_a, (50, 70))
        s_a_rect = s_a.get_rect(topleft=(355, 77))
        sf.blit(s_a, s_a_rect)
        counter += 1
        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(15)
    button_start.hide()
    button_exit.hide()
    button_rules.hide()
    f()


def endgame(status, word):
    endgame_background = pygame.image.load('icons/endgame_background.png')
    eg_rect = endgame_background.get_rect(center=(W//2, H//2))
    sf.blit(endgame_background, eg_rect)
    backbuttonbackground = pygame.image.load('icons/backbuttonbackground.jpg')
    bbb_rect = backbuttonbackground.get_rect(bottomleft=(0, H))
    sf.blit(backbuttonbackground, bbb_rect)
    button_again = Button(
        sf, 237, 540, 310, 90,
        text='Играть снова',  # Text to display
        font=pygame.font.SysFont('comicsansms', 40),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=4,
        shadowColour=(140, 140, 140),
        radius=20,  # Radius of border corners (leave empty for not curved)
    )
    button_menu = Button(
        sf, 637, 540, 310, 90,
        text='Главное меню',  # Text to display
        font=pygame.font.SysFont('comicsansms', 40),
        fontSize=50,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(210, 210, 210),  # Colour of button when not being interacted with
        hoverColour=(169, 169, 169),  # Colour of button when being hovered over
        shadowDistance=4,
        shadowColour=(140, 140, 140),
        radius=20,  # Radius of border corners (leave empty for not curved)
    )

    if status == 'dead':
        obituary_font = pygame.font.SysFont('comicsansms', 35)
        obituary = obituary_font.render('Увы, слово не угадано и жизнь загублена.', True,
                                        'white')
        obituary2 = obituary_font.render(f'Правильное слово: {word}', True,
                                        'white')
        pos = obituary.get_rect(center=(W//2, 450))
        pos2 = obituary2.get_rect(center=(W//2, 500))
        sf.blit(obituary, pos)
        sf.blit(obituary2, pos2)
    elif status == 'alive':
        amnesty_font = pygame.font.SysFont('comicsansms', 28)
        amnesty = amnesty_font.render('Поздравляю!', True, 'white')
        amnesty2 = amnesty_font.render(f'Вы угадали слово {word} и спасли человечка от петли.', True, 'white')
        amnesty3 = amnesty_font.render( 'Возьмите с полки пирожок ;)', True, 'white')
        pos = amnesty.get_rect(center=(W//2, 400))
        pos2 = amnesty2.get_rect(center=(W//2, 450))
        pos3 = amnesty3.get_rect(center=(W//2, 500))
        sf.blit(amnesty, pos)
        sf.blit(amnesty2, pos2)
        sf.blit(amnesty3, pos3)
    f = None
    while f == None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(event.pos)
                if 70 <= event.pos[0] <= 100 and 15 <= event.pos[1] <= 45:
                    music(1)
                elif 20 <= event.pos[0] <= 60 and 10 <= event.pos[1] <= 50:
                    music(switch=True)
                elif 237 <= event.pos[0] <= 547 and 540 <= event.pos[1] <= 630:
                    f = main
                    but_sound.play()
                elif 637 <= event.pos[0] <= 947 and 540 <= event.pos[1] <= 630:
                    f = start
                    but_sound.play()
        pygame_widgets.update(events)
        pygame.display.update()
    button_menu.hide()
    button_again.hide()
    f()


if __name__ == '__main__':
    start()
