#Author Brenden Wade

import random

cards = {
        "Ace":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "Jack":10,
        "Queen":10,
        "King":10,
    }

def deal():
    
    global cards
    firstcard = random.choice(list(cards))
    secondcard = random.choice(list(cards))
    

    print("***** Your hand *****")
    print(cards.get(firstcard))
    print(cards.get(secondcard))
    
    
    total = cards.get(firstcard)+ cards.get(secondcard)
    
    print(f"Total:{total}")
    print("")
    

    print("***** Computer's hand *****")
    compfirstcard = random.choice(list(cards))
    compsecondcard = random.choice(list(cards))
    print(cards.get(compfirstcard))
    print(cards.get(compsecondcard))
    
    comptotal = cards.get(compfirstcard)+ cards.get(compsecondcard)
    print(f"Total:{comptotal}")
    return total,comptotal

   

def player_extra_deal(total):
    
    while True:
        global cards
        print("***** Your Turn *****")
        if total < 21:
            command = input("Do you want another card? (Y)es or (N)o: ").lower().strip()
        if command == "y":
            card = random.choice(list(cards))
            print(card)
            print(f"Your total:{card}+{total}")
        elif command == "n":
            break
        

def computer_extra_deal(comptotal):
    
    global cards
    while comptotal < 14:
        compcard = random.choice(list(cards))
        print(compcard)
        print(f"Your total:{compcard}+{comptotal}")


def who_wins(total,comptotal):
    if total == comptotal:
        print("Push")
    elif total > 21:
        print("You lose")
    elif total <= 21 and total > comptotal:
        print("You win!")
    elif total == 21:
        print("Blackjack!")
    elif total < 21 and total < comptotal:
        print("You lose!")



def blackjack():
    deal()
    player_extra_deal()
    computer_extra_deal()
    who_wins()
    
    
    

blackjack()

        


        

    
    
    
    




