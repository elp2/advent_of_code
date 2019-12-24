class Deck:
    def __init__(self, num_cards):
        self.cards = [0] * num_cards
        for i in range(0, num_cards):
            self.cards[i] = i

    def deal_new_stack(self):
        self.cards.reverse()

    def cut_cards(self, cut):
        if cut == 0:
            return
        if cut > 0:
            n = cut
        else:
            n = len(self.cards) + cut

        a = self.cards[0:n]
        b = self.cards[n:]
        self.cards = b + a

    def deal_with_increment(self, increment):
        pos = 0
        new_cards = self.cards[:]
        for i in range(0, len(self.cards)):
            new_cards[pos] = self.cards[i]
            pos += increment
            pos = pos % len(self.cards)
        self.cards = new_cards

def test():
    deck = Deck(10)
    print(deck.cards)
    deck.deal_new_stack()
    print(deck.cards)

    deck = Deck(10)
    deck.cut_cards(3)
    print(deck.cards)

    deck = Deck(10)
    deck.cut_cards(-4)
    print(deck.cards)

    deck = Deck(10)
    deck.deal_with_increment(3)
    print(deck.cards)

test()


def part1():
    deck = Deck(10007)
    lines = open('input').readlines()
    for line in lines:
        words = line.split(' ')
        if words[0] == 'cut':
            deck.cut_cards(int(words[1]))
        elif words[1] == 'into':
            deck.deal_new_stack()
        else:
            deck.deal_with_increment(int(words[3]))
    
    print(deck.cards.index(2019))

part1() # 8502
