# Задание 1
# import random

# print("Игра: Угадайте число")

# b = random.randrange(10)
# i = 0

# while True:
#     a = int(input("Введите число: "))
#     if a < b:
#         print("Данное число меньше заданного числа")
#         i += 1
#     elif a > b:
#         print("Данное число больше заданного числа")
#         i += 1
#     elif a == b:
#         print("Вы угадали число, заданное число является: " + str(b))
#         print("Попытки: " + str(i))
#         break

# Задание 2


input_string = input("Введите строку без пробелов: ")

massive = []

index = 0
while index < len(input_string):
    char = input_string[index]
    if index + 1 < len(input_string) and input_string[index + 1] == char:
        massive.append([char, char])
        index += 2
    else:
        massive.append([char])
        index += 1


stroka = ' '.join(' '.join(psevdo_massive) for psevdo_massive in massive)
print(stroka)

# Задание 3
# import random

# def func_vidat_card(a):
#     return a.pop(random.randint(0, len(a) - 1))

# def see_card(card):
#     score = sum(card)
#     if 11 in card and score > 21:
#         score -= 10
#     return score

# def proverka_na_21(card):
#     if see_card(card) > 21:
#         print("Извиняйте, но вы проиграли :( ")
#         return True
#     return False

# def kto_vigral(card, card2):
#     if card2 > 21 or card > card2:
#         print("Ты выйграл, поздравляю")
#     elif card == 21:
#         print("Игрок взял карту: " + str(card) + " Сумма: " + str(see_card(card)))
#         print("Бот взял карту: " + str(card2) + " Сумма: " + str(see_card(card2)))
#         if card2 == 21:
#             print("Ничья")
#         else:
#             print("Ты выйграл, поздравляю")
#     elif card < card2:
#         print("Ты проиграл, я сочувствую тебе")
#     else:
#         print("Ничья")

# def igrai_v_igry():
#     print("Игра в Очко :)")

#     massive = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
#     random.shuffle(massive)

#     igrok = [func_vidat_card(massive), func_vidat_card(massive)]
#     bot = [func_vidat_card(massive), func_vidat_card(massive)]

#     player_lost = False

#     while True:
#         vibor = input("Берём карту? (y/n): ").strip().lower()
#         if vibor == 'y':
#             igrok.append(func_vidat_card(massive))
#             print("Игрок взял карту: " + str(igrok) + " Сумма: " + str(see_card(igrok)))
#             if proverka_na_21(igrok):
#                 player_lost = True
#                 break
#         else:
#             break

#     if not player_lost:
#         while see_card(bot) < 17:
#             bot.append(func_vidat_card(massive))
#             print("Бот взял карту: " + str(bot) + " Сумма: " + str(see_card(bot)))
#             if proverka_na_21(bot):
#                 break

#         card = see_card(igrok)
#         card2 = see_card(bot)
#         kto_vigral(card, card2)

# igrai_v_igry()


