############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
################################################################

from art import logo
import random
print(logo)
def Play():
  if input("Do you wanna play a game of BlackJack? Press 'y' to deal otherwise Press 'n'.") == 'y':
    Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    Special_Cards = {
      "J": 10,
      "Q": 10,
      "K": 10,
      "A": [1,11]
    }
    Your_Cards = [random.choice(Cards),random.choice(Cards)]
    Computer_Cards = [random.choice(Cards), random.choice(Cards)]
    c_score = 0
    for i in Your_Cards:
      if i == "J" or i == "Q" or i == "K":
        i = Special_Cards[i]
        c_score = c_score + i
      elif i == "A":
        c_score = c_score + Special_Cards[i][1]
        if c_score > 21:
          c_score = c_score - Special_Cards[i][1] + Special_Cards[i][0]
      else:
        c_score = c_score + i
    print(f"\tYour Cards: {Your_Cards}, current score: {c_score}")
    print(f"\tComputer's First Card: {Computer_Cards[0]}")
    if input("Press 'y' to hit or 'n' to stand.")  == 'y':
      Your_Cards.append(random.choice(Cards))
      if Your_Cards[2] == "J" or Your_Cards[2] == "Q" or Your_Cards[2] == "K":
        Your_Cards[2] = Special_Cards[Your_Cards[2]]
        c_score = c_score + Your_Cards[2]
      elif Your_Cards[2] == "A":
        c_score = c_score + Special_Cards[Your_Cards[2]][1]
        if c_score > 21:
          c_score = c_score - Special_Cards[Your_Cards[2]][1] + Special_Cards[Your_Cards[2]][0]
      else:
        c_score = c_score + Your_Cards[2]
      print(f"\tYour Cards: {Your_Cards}, current score: {c_score}")
      print(f"\tComputer's First Card: {Computer_Cards[0]}")
      print(f"\tYour Final Hand: {Your_Cards}, current score: {c_score}")
      comp_score = 0
      for i in Computer_Cards:
        if i == "J" or i == "Q" or i == "K":
          i = Special_Cards[i]
          comp_score = comp_score + i
        elif i == "A":
          comp_score = comp_score + Special_Cards[i][1]
          if comp_score > 21:
            comp_score = comp_score - Special_Cards[i][1] + Special_Cards[i][0]
        else:
          comp_score = comp_score + i
      print(f"\tComputer's Final Hand: {Computer_Cards}, final score {comp_score}")
      if c_score > 21:
        print(f"Its a Bust! You Loose.🤯")
        Play()
      elif c_score > comp_score:
        print(f"You Win.😎")
        Play()
      elif c_score < comp_score:
        print(f"You Loose.😭")
        Play()
      else:
        print(f"Draw.🤔")
        Play()
    else:
      print(f"\tYour Cards: {Your_Cards}, current score: {c_score}")
      print(f"\tComputer's First Card: {Computer_Cards[0]}")
      print(f"\tYour Final Hand: {Your_Cards}, current score: {c_score}")
      comp_score = 0
      for i in Computer_Cards:
        if i == "J" or i == "Q" or i == "K":
          i = Special_Cards[i]
          comp_score = comp_score + i
        elif i == "A":
          comp_score = comp_score + Special_Cards[i][1]
          if comp_score > 21:
            comp_score = comp_score - Special_Cards[i][1] + Special_Cards[i][0]
        else:
          comp_score = comp_score + i
      print(f"\tComputer's Final Hand: {Computer_Cards}, final score {comp_score}")
      if c_score > 21:
        print(f"Its a Bust! You Loose.🤯")
        Play()
      elif c_score > comp_score:
        print(f"You Win.😎")
        Play()
      elif c_score < comp_score:
        print(f"You Loose.😭")
        Play()
      else:
        print(f"Draw.🤔")
        Play()


Play()
