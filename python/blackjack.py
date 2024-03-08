import gamble


# Check for face cards and reset value to 10
def check_face(card):
    if card.value.value > 10:
        return 10
    else:
        return card.value.value


deck = gamble.BlackJackDeck()

print(deck.cards_left)

# Player Sum of starting Hand
player_card_1 = deck.draw()
player_card_2 = deck.draw()
player_sum = check_face(player_card_1) + check_face(player_card_2)

# Dealer Sum of starting Hand
dealer_card_1 = deck.draw()
dealer_card_2 = deck.draw()
dealer_sum = check_face(dealer_card_1) + check_face(dealer_card_2)

print()
print(f"Players Hand: {player_card_1} & {player_card_2}")

print(f"Players Sum: {player_sum}")
print()
print(f"Dealers Hand: {dealer_card_1}")

while True:
    user = input("Hit, Stand, Double?\n\n").lower()

    match user:
        case "hit":
            print("You are hitting")
            player_sum += check_face(deck.draw())
            print(f"Player Total: {player_sum}")
        case "stand":
            print(f"Player Total: {player_sum}")
            break
        case "double":
            print("You are doubling")
            player_sum += check_face(deck.draw())
            # Adjust the logic for doubling down as needed
            print(f"Player Total: {player_sum}")
            break
        case _:
            print("Invalid input. Please enter 'Hit', 'Stand', or 'Double'.")

    if player_sum > 21:
        print("Get BUSTED, nerd.")
        break


print(f"Player Total: {player_sum}")

print("End of Game")


# Deal Cards
# Define what a "hand" is (2 cards dealt from the same deck)
# Do we inclue the cut off point to reshuffle? (How will we do that)
# How many decks do we want to use? Probably 8+ for ease


# Player Action

# Dealer Action
