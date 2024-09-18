import os
import random

os.environ['TERM'] = 'xterm'

decks = input("Введите количество колод: ")

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 * int(decks)

wins = 0
losses = 0

def deal(deck_func):
    hand = []

    random.shuffle(deck_func)

    for i in range(2):
        card = deck_func.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Хотите сыграть еще раз? (Да/Нет) : ").lower()
    if again == "да":
        game()
    else:
        print("\033[0;35;40mКазино всегда выигрывает! До свидания!\033[0m")
        exit()

def total(hand):
    points = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            points += 10
        elif card == "A":
            if points >= 11: points += 1
            else: points += 11
        else: points += card
    return points

def hit(hand):
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
    return hand

def print_results(dealer_hand, player_hand):
    print("\n\033[0;35;40mРезультаты:\033[0m")
    print("Дилер: ", dealer_hand, " Всего: ", total(dealer_hand))
    print("Игрок: ", player_hand, " Всего: ", total(player_hand))
    
def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("\033[0;32;40mПоздравляю! Вы набрали 21!\033[0m")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("\033[0;31;40mК сожалению, дилер набрал 21.\033[0m")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
    global wins
    global losses
    
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("\033[0;32;40mПоздравляю! Вы набрали 21!\033[0m")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("\033[0;31;40mК сожалению, дилер набрал 21.\033[0m")
        losses += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("\033[0;31;40mК сожалению, вы проиграли.\033[0m")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("\033[0;32;40mПоздравляю! Вы выиграли!\033[0m")
        wins += 1
    elif total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("\033[0;33;40mНичья!\033[0m")

def game():
    global wins
    global losses

    print("\n Новая игра! \n")
    print("-" * 30 + "\n")
    print("\033[0;35;40mПобед: ", wins, "\033[0m")
    print("\033[0;35;40mПоражений: ", losses, "\033[0m")
    print("-" * 30 + "\n")

    dealer_hand = deal(deck)
    player_hand = deal(deck)

    print("Дилер: ", dealer_hand[0], " X")
    print("Игрок: ", player_hand, " Всего: ", total(player_hand))

    blackjack(dealer_hand, player_hand)

    while True:
        choice = input("Хотите добавить карту, остановиться или выйти? (д/о/в) : ").lower()
        if choice == 'д':
            hit(player_hand)
            print(player_hand)
            print("Всего: ", total(player_hand))
            if total(player_hand) > 21:
                print("\033[0;31;40mВы проиграли!\033[0m")
                losses += 1
                play_again()
        elif choice == 'о':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print("Дилер: ", dealer_hand)
                if total(dealer_hand) > 21:
                    print("\033[0;32;40mДилер проиграл! Вы выиграли!\033[0m")
                    wins += 1
                    play_again()
            else:
                score(dealer_hand, player_hand)
                play_again()
        elif choice == 'в':
            print("Казино все равно всегда выигрывает!")
            exit()
        else:
            print("Пожалуйста, введите 'д', 'о' или 'в'.")


if __name__ == "__main__":
    game()
            