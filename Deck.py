class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} of {self.rank}"


class Deck:
    def __init__(self) -> None:
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            return None
        else:
            dealt_cards = self.cards[:num_cards]
            self.cards = self.cards[num_cards:]
            return dealt_cards

    def shuffle(self):
        import random

        random.shuffle(self.cards)
