import gamble


# Check for face cards and reset value to 10
def check_face(card):
    if card.value.value > 10:
        return 10
    else:
        return card.value.value


deck = gamble.BlackJackDeck()

print(deck.cards_left)

# Player Hand
player_hand = [deck.draw(), deck.draw()]
player_sum = sum(check_face(card) for card in player_hand)
print(player_hand[0].value.value == player_hand[1].value.value)

# Dealer Hand
dealer_hand = [deck.draw(), deck.draw()]
dealer_sum = sum(check_face(card) for card in dealer_hand)

print()
print(f"Player's Hand: {[str(card) for card in player_hand]}")
print(f"Player's Sum: {player_sum}")
print()
print(f"Dealer's Hand: {[str(card) for card in dealer_hand[:1]]}")

while True:
    user = input("Hit, Stand, Double?\n\n").lower()

    match user:
        case "hit":
            print("You are hitting")
            player_hand.append(deck.draw())
            player_sum = sum(check_face(card) for card in player_hand)
            print(f"Player's Hand: {[str(card) for card in player_hand]}")
            print(f"Player's Sum: {player_sum}")
        case "stand":
            print(f"Player's Hand: {[str(card) for card in player_hand]}")
            print(f"Player's Sum: {player_sum}")
            break
        case "double":
            print("You are doubling")
            player_hand.append(deck.draw())
            player_sum = sum(check_face(card) for card in player_hand)
            # Adjust the logic for doubling down as needed
            print(f"Player's Hand: {[str(card) for card in player_hand]}")
            print(f"Player's Sum: {player_sum}")
            break
        case _:
            print("Invalid input. Please enter 'Hit', 'Stand', or 'Double'.")

    if player_sum > 21:
        print("Get BUSTED, nerd.")
        break


print("End of Player's Turn")

# Dealer's Turn
while dealer_sum < 17:
    dealer_hand.append(deck.draw())
    dealer_sum = sum(check_face(card) for card in dealer_hand)

print()
print(f"Dealer's Hand: {[str(card) for card in dealer_hand]}")
print(f"Dealer's Sum: {dealer_sum}")

if dealer_sum or player_sum > 21:
    print("Dealer Bust.")
elif player_sum > dealer_sum:
    print("Player wins!")
elif player_sum == dealer_sum:
    print("Push")
else:
    print("Dealer wins")

print("End of Game")


# TODO:
# Include splits
# Other
