

# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Pokemon Class)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it helps practice making a basic class object.
#
# U -- Understand
# 1) Do I only need to create one Pokemon object here? Yes.
# 2) Should the types value be stored as a list? Yes.
#
# P -- Plan
# I will define the Pokemon class and then create one object named my_pokemon
# with the name Pikachu and the type Electric.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define Pokemon class
# - create my_pokemon with "Pikachu" and ["Electric"]
#
# I -- Implement

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

# Test Cases
my_pokemon = Pokemon("Pikachu", ["Electric"])
print("V1 P1 Test 1:", my_pokemon.name, my_pokemon.types, my_pokemon.is_caught)

second_pokemon = Pokemon("Eevee", ["Normal"])
print("V1 P1 Test 2:", second_pokemon.name, second_pokemon.types, second_pokemon.is_caught)


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Create Squirtle)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices adding and using a class method.
#
# U -- Understand
# 1) Do I need to add print_pokemon() to the class? Yes.
# 2) Should I create a Squirtle object and call the method? Yes.
#
# P -- Plan
# I will redefine the Pokemon class with print_pokemon(), create squirtle,
# and then call the method.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define Pokemon class with print_pokemon
# - create squirtle
# - call print_pokemon
#
# I -- Implement

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

# Test Cases
squirtle = Pokemon("Squirtle", ["Water"])
print("V1 P2 Test 1:")
squirtle.print_pokemon()

bulbasaur = Pokemon("Bulbasaur", ["Grass", "Poison"])
print("V1 P2 Test 2:")
bulbasaur.print_pokemon()


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Is Caught)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it shows how to update an object's attribute.
#
# U -- Understand
# 1) Do I update squirtle.is_caught directly? Yes.
# 2) Should I verify the update with print_pokemon()? Yes.
#
# P -- Plan
# I will set squirtle.is_caught to True and print it before and after.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - print squirtle before update
# - set is_caught to True
# - print squirtle after update
#
# I -- Implement

# Test Cases
squirtle = Pokemon("Squirtle", ["Water"])
print("V1 P3 Test 1 - before:")
squirtle.print_pokemon()
squirtle.is_caught = True
print("V1 P3 Test 1 - after:")
squirtle.print_pokemon()

pikachu = Pokemon("Pikachu", ["Electric"])
pikachu.is_caught = True
print("V1 P3 Test 2:")
pikachu.print_pokemon()


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Catch Pokemon)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices writing a method that changes object data.
#
# U -- Understand
# 1) Should catch() take only self? Yes.
# 2) Should it return anything? No.
#
# P -- Plan
# I will add a catch() method that changes is_caught to True.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define catch method
# - set self.is_caught to True
#
# I -- Implement

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
        self.is_caught = True

# Test Cases
my_pokemon = Pokemon("rattata", ["Normal"])
print("V1 P4 Test 1 - before catch:")
my_pokemon.print_pokemon()
my_pokemon.catch()
print("V1 P4 Test 1 - after catch:")
my_pokemon.print_pokemon()

pidgey = Pokemon("Pidgey", ["Normal", "Flying"])
print("V1 P4 Test 2 - before catch:")
pidgey.print_pokemon()
pidgey.catch()
print("V1 P4 Test 2 - after catch:")
pidgey.print_pokemon()


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Choose Pokemon)
# Time Limit: 7 minutes
# Problem Importance:
# This matters because it practices conditionals inside a method.
#
# U -- Understand
# 1) What if the Pokemon is caught? Print "<name> I choose you!"
# 2) What if the Pokemon is not caught? Print "<name> is wild! Catch them if you can!"
#
# P -- Plan
# I will check is_caught and print the matching message.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - if is_caught is True, print chosen message
# - else, print wild message
#
# I -- Implement

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

# Test Cases
my_pokemon = Pokemon("rattata", ["Normal"])
print("V1 P5 Test 1:")
my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

psyduck = Pokemon("Psyduck", ["Water"])
print("V1 P5 Test 2:")
psyduck.choose()


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Add Pokemon Type)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices updating a list inside an object.
#
# U -- Understand
# 1) What does add_type() receive? A new string type.
# 2) What should happen? The new type should be added to the types list.
#
# P -- Plan
# I will use append() to add the new type.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define add_type
# - append new_type to self.types
#
# I -- Implement

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

# Test Cases
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
print("V1 P6 Test 1 - before:")
jigglypuff.print_pokemon()
jigglypuff.add_type("Fairy")
print("V1 P6 Test 1 - after:")
jigglypuff.print_pokemon()

charizard = Pokemon("Charizard", ["Fire"])
print("V1 P6 Test 2 - before:")
charizard.print_pokemon()
charizard.add_type("Flying")
print("V1 P6 Test 2 - after:")
charizard.print_pokemon()


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Get Pokemon)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices filtering objects from a list.
#
# U -- Understand
# 1) What should the function return? A list of Pokemon with the given type.
# 2) Should I check whether pokemon_type is inside each Pokemon's types list? Yes.
#
# P -- Plan
# I will loop through the list and keep the Pokemon that contain the target type.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - make empty result list
# - loop through all pokemon
# - if pokemon_type is in pokemon.types, add it
# - return result
#
# I -- Implement

def get_by_type(my_pokemon, pokemon_type):
    result = []
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            result.append(pokemon)
    return result

# Test Cases
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])
my_pokemon_list = [jigglypuff, diglett, meowth, pidgeot, blastoise]

normal_pokemon = get_by_type(my_pokemon_list, "Normal")
print("V1 P7 Test 1:", [pokemon.name for pokemon in normal_pokemon])

water_pokemon = get_by_type(my_pokemon_list, "Water")
print("V1 P7 Test 2:", [pokemon.name for pokemon in water_pokemon])


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Pokemon Evolution)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices following object links one step at a time.
#
# U -- Understand
# 1) What does evolution store? Another Pokemon object or None.
# 2) What should the function return? The full evolution line starting from the given Pokemon.
#
# P -- Plan
# I will start at starter_pokemon and keep following evolution until I reach None.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - make empty list
# - set current to starter_pokemon
# - while current is not None
#   - add current to list
#   - move to current.evolution
# - return list
#
# I -- Implement

class Pokemon:
    def __init__(self, name, types, evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def __repr__(self):
        return self.name

def get_evolutionary_line(starter_pokemon):
    line = []
    current = starter_pokemon
    while current is not None:
        line.append(current)
        current = current.evolution
    return line

# Test Cases
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

print("V1 P8 Test 1:", get_evolutionary_line(charmander))
print("V1 P8 Test 2:", get_evolutionary_line(charmeleon))
print("V1 P8 Test 3:", get_evolutionary_line(charizard))


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (Node Class)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it introduces the basic part of a linked list.
#
# U -- Understand
# 1) Do I need two separate nodes? Yes.
# 2) Do they need to be connected yet? No.
#
# P -- Plan
# I will define Node and create node_one with "a" and node_two with "b".
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define Node class
# - create node_one
# - create node_two
#
# I -- Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Test Cases
node_one = Node("a")
node_two = Node("b")
print("V1 P9 Test 1:", node_one.value, node_one.next)
print("V1 P9 Test 2:", node_two.value, node_two.next)


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (Linking Nodes)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices connecting linked list nodes.
#
# U -- Understand
# 1) What should node_one.next point to? node_two.
# 2) Should node_two change? No.
#
# P -- Plan
# I will set node_one.next equal to node_two.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - update node_one.next to node_two
#
# I -- Implement

node_one.next = node_two

# Test Cases
print("V1 P10 Test 1:", node_one.value)
print("V1 P10 Test 2:", node_one.next.value)
print("V1 P10 Test 3:", node_two.value)


# ---------------------------------------------------------
# Session: 1
# Problem #: 11 (Mario Party)
# Time Limit: 7 minutes
# Problem Importance:
# This matters because it gives practice building a full linked list by hand.
#
# U -- Understand
# 1) What order should the nodes go in? Mario -> Luigi -> Wario -> Toad.
# 2) What does the last node point to? None.
#
# P -- Plan
# I will create the nodes from back to front and connect them.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create node_4 as Toad
# - create node_3 as Wario -> node_4
# - create node_2 as Luigi -> node_3
# - create node_1 as Mario -> node_2
#
# I -- Implement

node_4 = Node("Toad")
node_3 = Node("Wario", node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)

# Test Cases
print("V1 P11 Test 1:", node_1.value, "->", node_1.next.value)
print("V1 P11 Test 2:", node_2.value, "->", node_2.next.value)
print("V1 P11 Test 3:", node_3.value, "->", node_3.next.value)
print("V1 P11 Test 4:", node_4.value, "->", node_4.next)


# ---------------------------------------------------------
# Session: 1
# Problem #: 12 (Printing Linked List)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because linked list traversal is a main skill to learn.
#
# U -- Understand
# 1) What should separate the values? " -> "
# 2) Should the function print the whole linked list in order? Yes.
#
# P -- Plan
# I will move through the linked list and collect all values, then print them joined by " -> ".
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - make empty list of values
# - while current exists
#   - add current.value
#   - move to current.next
# - print joined values
#
# I -- Implement

def print_linked_list(head):
    values = []
    current = head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    print(" -> ".join(values))

# Test Cases
a = Node("a", Node("b", Node("c", Node("d", Node("e")))))
print("V1 P12 Test 1:")
print_linked_list(a)

mario_chain = Node("Mario", Node("Luigi", Node("Peach")))
print("V1 P12 Test 2:")
print_linked_list(mario_chain)


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Card Class)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices making an object with two attributes.
#
# U -- Understand
# 1) What card should be created? Spades and 8.
# 2) What variable name should store it? card.
#
# P -- Plan
# I will define the Card class and create one object named card.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define Card class
# - create card with "Spades" and "8"
#
# I -- Implement

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

# Test Cases
card = Card("Spades", "8")
print("V2 P1 Test 1:", card.suit, card.rank)

card_extra = Card("Hearts", "Ace")
print("V2 P1 Test 2:", card_extra.suit, card_extra.rank)


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Print Card)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices adding a method to a class.
#
# U -- Understand
# 1) What should print_card() print? "<rank> of <suit>"
# 2) What example card should I create? Ace of Clubs.
#
# P -- Plan
# I will add the method, create the object, and print it.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define print_card method
# - create Clubs Ace card
# - call print_card
#
# I -- Implement

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

# Test Cases
card = Card("Clubs", "Ace")
print("V2 P2 Test 1:")
card.print_card()

card_two = Card("Diamonds", "10")
print("V2 P2 Test 2:")
card_two.print_card()


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Verify Update)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it shows how to update object values.
#
# U -- Understand
# 1) What changes here? The card's suit.
# 2) What should it become? Hearts.
#
# P -- Plan
# I will print the card first, update the suit, and print it again.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - print card
# - change suit to Hearts
# - print card again
#
# I -- Implement

# Test Cases
card = Card("Clubs", "Ace")
print("V2 P3 Test 1 - before:")
card.print_card()
card.suit = "Hearts"
print("V2 P3 Test 1 - after:")
card.print_card()

card_two = Card("Spades", "7")
print("V2 P3 Test 2 - before:")
card_two.print_card()
card_two.suit = "Diamonds"
print("V2 P3 Test 2 - after:")
card_two.print_card()


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Valid Card)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices validating inputs inside a method.
#
# U -- Understand
# 1) When is a card valid? When both the suit and rank are allowed values.
# 2) What should happen if the card is invalid? Return False.
#
# P -- Plan
# I will store valid suits and ranks in sets and check membership.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - make set of valid suits
# - make set of valid ranks
# - return True only if suit and rank are both valid
#
# I -- Implement

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        valid_suits = {"Hearts", "Spades", "Clubs", "Diamonds"}
        valid_ranks = {
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"
        }
        return self.suit in valid_suits and self.rank in valid_ranks

# Test Cases
my_card = Card("Hearts", "7")
print("V2 P4 Test 1:", my_card.is_valid())

second_draw = Card("Spades", "Joker")
print("V2 P4 Test 2:", second_draw.is_valid())

third_draw = Card("Flowers", "3")
print("V2 P4 Test 3:", third_draw.is_valid())


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Get Value)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices converting card ranks into values.
#
# U -- Understand
# 1) What should Ace return? 1.
# 2) What should an invalid card return? None.
#
# P -- Plan
# I will first check if the card is valid, then return the matching value.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - if card is invalid, return None
# - if rank is a number, return int(rank)
# - else return special face-card value
#
# I -- Implement

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        valid_suits = {"Hearts", "Spades", "Clubs", "Diamonds"}
        valid_ranks = {
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"
        }
        return self.suit in valid_suits and self.rank in valid_ranks

    def get_value(self):
        if not self.is_valid():
            return None
        if self.rank.isdigit():
            return int(self.rank)
        if self.rank == "Ace":
            return 1
        if self.rank == "Jack":
            return 11
        if self.rank == "Queen":
            return 12
        if self.rank == "King":
            return 13
        return None

# Test Cases
card = Card("Hearts", "7")
print("V2 P5 Test 1:", card.get_value())

card_two = Card("Spades", "Jack")
print("V2 P5 Test 2:", card_two.get_value())

invalid_card = Card("Stars", "100")
print("V2 P5 Test 3:", invalid_card.get_value())


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Hand Class)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices storing objects inside another object.
#
# U -- Understand
# 1) What should a new hand start with? An empty list.
# 2) What should add_card() and remove_card() do? Add or remove Card objects.
#
# P -- Plan
# I will use a list to hold cards, append for adding, and remove for deleting.
# Time Complexity: O(1) for add_card, O(n) for remove_card
# Space Complexity: O(1)
#
# Pseudocode
# - create Hand class with cards list
# - add_card appends a card
# - remove_card removes a card
#
# I -- Implement

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

# Test Cases
card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")
player1_hand = Hand()
print("V2 P6 Test 1 - start:", [c.rank for c in player1_hand.cards])
player1_hand.add_card(card_one)
player1_hand.add_card(card_two)
print("V2 P6 Test 1 - after add:", [(c.suit, c.rank) for c in player1_hand.cards])
player1_hand.remove_card(card_one)
print("V2 P6 Test 1 - after remove:", [(c.suit, c.rank) for c in player1_hand.cards])

another_hand = Hand()
another_hand.add_card(Card("Diamonds", "King"))
print("V2 P6 Test 2:", [(c.suit, c.rank) for c in another_hand.cards])


# ---------------------------------------------------------
# Session: 2
# Problem #: 7 (Sum of Cards)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it combines loops, classes, and helper methods.
#
# U -- Understand
# 1) What if one card is invalid? Return None.
# 2) What should be summed? The numeric values from get_value().
#
# P -- Plan
# I will loop through hand.cards, get each value, and add them.
# If I find None, I will return None.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - total = 0
# - loop through cards in hand
# - get each value
# - if value is None, return None
# - add value to total
# - return total
#
# I -- Implement

def sum_hand(hand):
    total = 0
    for card in hand.cards:
        value = card.get_value()
        if value is None:
            return None
        total += value
    return total

# Test Cases
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")
hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)
print("V2 P7 Test 1:", sum_hand(hand))

bad_hand = Hand()
bad_hand.add_card(Card("Hearts", "2"))
bad_hand.add_card(Card("Clouds", "9"))
print("V2 P7 Test 2:", sum_hand(bad_hand))


# ---------------------------------------------------------
# Session: 2
# Problem #: 8 (Print Hand)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices following links between objects.
#
# U -- Understand
# 1) What does next store here? The next card in the hand.
# 2) What should the function return? A list of cards from the starting card onward.
#
# P -- Plan
# I will move through the linked cards and add each one to a list.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - make empty result list
# - set current to starting_card
# - while current exists
#   - add current to result
#   - move to current.next
# - return result
#
# I -- Implement

class Card:
    def __init__(self, suit, rank, next=None):
        self.suit = suit
        self.rank = rank
        self.next = next

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

def print_hand(starting_card):
    result = []
    current = starting_card
    while current is not None:
        result.append(current)
        current = current.next
    return result

# Test Cases
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")
card_one.next = card_two
card_two.next = card_three
print("V2 P8 Test 1:", print_hand(card_one))
print("V2 P8 Test 2:", print_hand(card_two))


# ---------------------------------------------------------
# Session: 2
# Problem #: 9 (Head and Tail Nodes)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it reinforces a small linked list connection.
#
# U -- Understand
# 1) What values should the nodes store? 100 and 200.
# 2) Should head point to tail? Yes.
#
# P -- Plan
# I will create tail first and then create head pointing to tail.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create tail node
# - create head node with next=tail
#
# I -- Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tail = Node(200)
head = Node(100, tail)

# Test Cases
print("V2 P9 Test 1:", head.value)
print("V2 P9 Test 2:", head.next.value)
print("V2 P9 Test 3:", tail.value)
print("V2 P9 Test 4:", tail.next)


# ---------------------------------------------------------
# Session: 2
# Problem #: 10 (Middle Node)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices inserting into a linked list.
#
# U -- Understand
# 1) What value should middle have? 150.
# 2) Where should it go? Between head and tail.
#
# P -- Plan
# I will create middle pointing to tail, then make head point to middle.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create middle with next=tail
# - set head.next to middle
#
# I -- Implement

middle = Node(150, tail)
head.next = middle

# Test Cases
print("V2 P10 Test 1:", head.next.value)
print("V2 P10 Test 2:", middle.next.value)
print("V2 P10 Test 3:", tail.next)


# ---------------------------------------------------------
# Session: 2
# Problem #: 11 (Zodiac Signs)
# Time Limit: 7 minutes
# Problem Importance:
# This matters because it gives more practice building linked lists manually.
#
# U -- Understand
# 1) What order should the list follow? aries -> taurus -> gemini -> cancer.
# 2) What does the last node point to? None.
#
# P -- Plan
# I will create the nodes from the back to the front and connect them.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - node_4 cancer
# - node_3 gemini -> node_4
# - node_2 taurus -> node_3
# - node_1 aries -> node_2
#
# I -- Implement

node_4 = Node("cancer")
node_3 = Node("gemini", node_4)
node_2 = Node("taurus", node_3)
node_1 = Node("aries", node_2)

# Test Cases
print("V2 P11 Test 1:", node_1.value, "->", node_1.next.value)
print("V2 P11 Test 2:", node_2.value, "->", node_2.next.value)
print("V2 P11 Test 3:", node_3.value, "->", node_3.next.value)
print("V2 P11 Test 4:", node_4.value, "->", node_4.next)


# ---------------------------------------------------------
# Session: 2
# Problem #: 12 (Print Linked List)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices printing and returning linked list values.
#
# U -- Understand
# 1) Should the function both print and return the values? Yes.
# 2) In what order? The same order as the linked list.
#
# P -- Plan
# I will collect the values in a list, print the list, and return it.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - make empty values list
# - walk through the linked list
# - append each value
# - print values
# - return values
#
# I -- Implement

def print_linked_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    print(values)
    return values

# Test Cases
a = Node("a", Node("b", Node("c", Node("d", Node("e")))))
print("V2 P12 Test 1:")
returned_values = print_linked_list(a)
print("Returned:", returned_values)

nums = Node(1, Node(2, Node(3)))
print("V2 P12 Test 2:")
returned_nums = print_linked_list(nums)
print("Returned:", returned_nums)


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 3
# Problem #: 1 (Player Class)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices making a class with more than one attribute.
#
# U -- Understand
# 1) What should player_one store? Yoshi and Super Blooper.
# 2) Should items start empty? Yes.
#
# P -- Plan
# I will define Player and create player_one.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define Player class
# - create player_one
#
# I -- Implement

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

# Test Cases
player_one = Player("Yoshi", "Super Blooper")
print("V3 P1 Test 1:", player_one.character, player_one.kart, player_one.items)

player_extra = Player("Mario", "Standard Kart M")
print("V3 P1 Test 2:", player_extra.character, player_extra.kart, player_extra.items)


# ---------------------------------------------------------
# Session: 3
# Problem #: 2 (Get Player)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices returning a formatted string from a method.
#
# U -- Understand
# 1) What should get_player() return? "<character> driving the <kart>"
# 2) What should player_two store? Bowser and Pirahna Prowler.
#
# P -- Plan
# I will add get_player(), create player_two, and print both players in one line.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - add get_player method
# - create player_two
# - print match line
#
# I -- Implement

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

# Test Cases
player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")
print("V3 P2 Test 1:", player_one.get_player())
print("V3 P2 Test 2:", f"Match: {player_one.get_player()} vs {player_two.get_player()}")


# ---------------------------------------------------------
# Session: 3
# Problem #: 3 (Update Kart)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it shows how object values can change over time.
#
# U -- Understand
# 1) What should player_one's new kart be? Dolphin Dasher.
# 2) Should I show before and after? Yes.
#
# P -- Plan
# I will print player_one first, update the kart, then print again.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - print old player string
# - change kart
# - print new player string
#
# I -- Implement

# Test Cases
player_one = Player("Yoshi", "Super Blooper")
print("V3 P3 Test 1 - before:", player_one.get_player())
player_one.kart = "Dolphin Dasher"
print("V3 P3 Test 1 - after:", player_one.get_player())

player_two = Player("Luigi", "Mach Bike")
print("V3 P3 Test 2 - before:", player_two.get_player())
player_two.kart = "Flame Runner"
print("V3 P3 Test 2 - after:", player_two.get_player())


# ---------------------------------------------------------
# Session: 3
# Problem #: 4 (Set Character)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because setter methods help validate changes before updating data.
#
# U -- Understand
# 1) What if the name is valid? Update the character and print "Character updated".
# 2) What if the name is invalid? Print "Invalid character".
#
# P -- Plan
# I will keep a set of valid names and check if the input is allowed.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define valid character set
# - if name is valid, update and print success
# - else print invalid
#
# I -- Implement

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def set_player(self, name):
        valid_names = {
            "Mario", "Luigi", "Peach", "Yoshi",
            "Toad", "Wario", "Donkey Kong", "Bowser"
        }
        if name in valid_names:
            self.character = name
            print("Character updated")
        else:
            print("Invalid character")

# Test Cases
player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")
print("V3 P4 Test 1 - before:", player_one.get_player())
player_one.set_player("Peach")
print("V3 P4 Test 1 - after:", player_one.get_player())

print("V3 P4 Test 2 - before:", player_two.get_player())
player_two.set_player("Kermit")
print("V3 P4 Test 2 - after:", player_two.get_player())


# ---------------------------------------------------------
# Session: 3
# Problem #: 5 (Add Special Item)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices validating values before adding them.
#
# U -- Understand
# 1) What happens if an item is valid? Add it to items.
# 2) What happens if an item is invalid? Ignore it.
#
# P -- Plan
# I will check if item_name is in the valid items set before appending.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - define valid items set
# - if item_name is valid, append to items
#
# I -- Implement

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def set_player(self, name):
        valid_names = {
            "Mario", "Luigi", "Peach", "Yoshi",
            "Toad", "Wario", "Donkey Kong", "Bowser"
        }
        if name in valid_names:
            self.character = name
            print("Character updated")
        else:
            print("Invalid character")

    def add_item(self, item_name):
        valid_items = {
            "banana", "green shell", "red shell", "bob-omb",
            "super star", "lightning", "bullet bill"
        }
        if item_name in valid_items:
            self.items.append(item_name)

# Test Cases
player_one = Player("Yoshi", "Dolphin Dasher")
player_one.add_item("red shell")
player_one.add_item("super star")
player_one.add_item("super smash")
print("V3 P5 Test 1:", player_one.items)

player_two = Player("Mario", "Standard Kart M")
player_two.add_item("banana")
player_two.add_item("lightning")
print("V3 P5 Test 2:", player_two.items)


# ---------------------------------------------------------
# Session: 3
# Problem #: 6 (Print Inventory)
# Time Limit: 12 minutes
# Problem Importance:
# This matters because it practices counting repeated values in a list.
#
# U -- Understand
# 1) What if the player has no items? Print "Inventory empty".
# 2) What should be shown if there are items? Item names and counts.
#
# P -- Plan
# I will count each item with a dictionary and print the results in one line.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if items is empty, print Inventory empty
# - count all items in a dictionary
# - build output text
# - print it
#
# I -- Implement

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def set_player(self, name):
        valid_names = {
            "Mario", "Luigi", "Peach", "Yoshi",
            "Toad", "Wario", "Donkey Kong", "Bowser"
        }
        if name in valid_names:
            self.character = name
            print("Character updated")
        else:
            print("Invalid character")

    def add_item(self, item_name):
        valid_items = {
            "banana", "green shell", "red shell", "bob-omb",
            "super star", "lightning", "bullet bill"
        }
        if item_name in valid_items:
            self.items.append(item_name)

    def print_inventory(self):
        if not self.items:
            print("Inventory empty")
            return

        counts = {}
        for item in self.items:
            counts[item] = counts.get(item, 0) + 1

        parts = []
        for item, count in counts.items():
            parts.append(f"{item}: {count}")

        print("Inventory: " + ", ".join(parts))

# Test Cases
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

print("V3 P6 Test 1:")
player_one.print_inventory()

print("V3 P6 Test 2:")
player_two.print_inventory()


# ---------------------------------------------------------
# Session: 3
# Problem #: 7 (Race Results)
# Time Limit: 7 minutes
# Problem Importance:
# This matters because it practices looping through objects with positions.
#
# U -- Understand
# 1) What does the first player in the list represent? First place.
# 2) What should the function print? Numbered places and player names.
#
# P -- Plan
# I will use enumerate starting at 1 and print each player's character.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - loop through race_results with enumerate starting at 1
# - print place and player.character
#
# I -- Implement

def print_results(race_results):
    for place, player in enumerate(race_results, start=1):
        print(f"{place}. {player.character}")

# Test Cases
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print("V3 P7 Test 1:")
print_results(race_one)

race_two = [luigi, peach]
print("V3 P7 Test 2:")
print_results(race_two)


# ---------------------------------------------------------
# Session: 3
# Problem #: 8 (Get Rank)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices following a chain of references.
#
# U -- Understand
# 1) What does ahead mean? The player directly ahead in the race.
# 2) How do I find place? Count how many players are ahead, then add 1.
#
# P -- Plan
# I will move through the ahead chain until there is nobody ahead.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - start place at 1
# - while current.ahead exists
#   - move current to ahead
#   - add 1 to place
# - return place
#
# I -- Implement

class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

def get_place(my_player):
    place = 1
    current = my_player
    while current.ahead is not None:
        place += 1
        current = current.ahead
    return place

# Test Cases
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print("V3 P8 Test 1:", get_place(luigi))
print("V3 P8 Test 2:", get_place(peach))
print("V3 P8 Test 3:", get_place(mario))


# ---------------------------------------------------------
# Session: 3
# Problem #: 9 (Tom and Jerry)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it reinforces basic linked list creation.
#
# U -- Understand
# 1) What should the chain be? cat -> mouse.
# 2) What values should the nodes hold? Tom and Jerry.
#
# P -- Plan
# I will create mouse first and then cat pointing to mouse.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create mouse
# - create cat pointing to mouse
#
# I -- Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)

# Test Cases
print("V3 P9 Test 1:", cat.value)
print("V3 P9 Test 2:", cat.next.value)
print("V3 P9 Test 3:", mouse.value)
print("V3 P9 Test 4:", mouse.next)


# ---------------------------------------------------------
# Session: 3
# Problem #: 10 (Chase List)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it practices adding a node to the front of a list.
#
# U -- Understand
# 1) What new node should be added? dog with value Spike.
# 2) Where should dog point? To cat.
#
# P -- Plan
# I will create dog and set its next to cat.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create dog with next=cat
#
# I -- Implement

dog = Node("Spike", cat)

# Test Cases
print("V3 P10 Test 1:", dog.value)
print("V3 P10 Test 2:", dog.next is cat)
print("V3 P10 Test 3:", dog.next.value)
print("V3 P10 Test 4:", cat.next is mouse)
print("V3 P10 Test 5:", cat.next.value)
print("V3 P10 Test 6:", mouse.next)


# ---------------------------------------------------------
# Session: 3
# Problem #: 11 (Update Chase)
# Time Limit: 7 minutes
# Problem Importance:
# This matters because it practices changing linked list pointers.
#
# U -- Understand
# 1) What should the final chain be? cat -> mouse -> cheese.
# 2) What happens to dog? It gets removed from the chain.
#
# P -- Plan
# I will create cheese and attach it after mouse. Then I will use cat as the new head.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create cheese node
# - set mouse.next to cheese
# - use cat as the start of the new chain
#
# I -- Implement

cheese = Node("Gouda")
mouse.next = cheese

# Test Cases
print("V3 P11 Test 1:", cat.value)
print("V3 P11 Test 2:", cat.next.value)
print("V3 P11 Test 3:", cat.next.next.value)
print("V3 P11 Test 4:", cheese.next)

new_head = cat
print("V3 P11 Test 5:", new_head.value, "->", new_head.next.value, "->", new_head.next.next.value)


# ---------------------------------------------------------
# Session: 3
# Problem #: 12 (Chase String)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it combines traversal and string building.
#
# U -- Understand
# 1) What should connect the values? The word "chases".
# 2) What should the function return? One string showing the full chain.
#
# P -- Plan
# I will walk through the linked list, collect the values, and join them with " chases ".
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - make empty values list
# - walk through linked list
# - add each value
# - return joined string
#
# I -- Implement

def chase_list(head):
    values = []
    current = head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    return " chases ".join(values)

# Test Cases
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")
dog.next = cat
cat.next = mouse
mouse.next = cheese
print("V3 P12 Test 1:", chase_list(dog))

cat2 = Node("Tom", Node("Jerry"))
print("V3 P12 Test 2:", chase_list(cat2))


# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# WEEK 5: SESSION  2
# Each problem includes:
# 1) Why this problem was chosen
# 2) UMPIRE
# 3) Python solution with comments
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================
# =========================================================


def sll_to_string(head):
    parts = []
    current = head
    while current:
        parts.append(str(current.value))
        current = current.next
    return " -> ".join(parts) if parts else "EMPTY"

def dll_forward_to_string(head):
    parts = []
    current = head
    while current:
        parts.append(str(current.value))
        current = current.next
    return " <-> ".join(parts) if parts else "EMPTY"


# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Battle Pokemon)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices updating another object's data using a method.
#
# U -- Understand
# 1) What should happen if opponent hp goes below 0? Set it to 0.
# 2) What should be printed when the opponent faints? "<Opponent name> fainted".
#
# P -- Plan
# I will subtract self.damage from opponent.hp. If opponent.hp becomes 0 or less,
# I will set it to 0 and print the fainted message. Otherwise, I will print the
# normal attack message.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - subtract self.damage from opponent.hp
# - if opponent.hp <= 0
#   - set opponent.hp to 0
#   - print fainted message
# - else
#   - print damage message
#
# I -- Implement

class Pokemon:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            opponent.hp = 0
            print(f"{opponent.name} fainted")
        else:
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

# Test Cases
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30)
print("V1 P1 Test 1:")
pikachu.attack(bulbasaur)
print("Bulbasaur HP:", bulbasaur.hp)

charmander = Pokemon("Charmander", 39, 50)
squirtle = Pokemon("Squirtle", 44, 10)
print("V1 P1 Test 2:")
charmander.attack(squirtle)
print("Squirtle HP:", squirtle.hp)


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Convert to Linked List)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it introduces how to build a linked list by hand.
#
# U -- Understand
# 1) How many nodes do I need? Two nodes.
# 2) What should the second node point to? None.
#
# P -- Plan
# I will create node_2 first, then create node_1 pointing to node_2.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create node_2 with Wigglytuff
# - create node_1 with Jigglypuff pointing to node_2
#
# I -- Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)

# Test Cases
print("V1 P2 Test 1:", node_1.value, "->", node_1.next.value)
print("V1 P2 Test 2:", node_2.value, "->", node_2.next)


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Add First)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because adding to the front is a common linked list operation.
#
# U -- Understand
# 1) What should the function return? The new head.
# 2) What should happen to new_node.next? It should point to the old head.
#
# P -- Plan
# I will point new_node.next to head and return new_node.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - set new_node.next = head
# - return new_node
#
# I -- Implement

def add_first(head, new_node):
    new_node.next = head
    return new_node

# Test Cases
head = node_1
print("V1 P3 Test 1 - before:", sll_to_string(head))
new_node = Node("Ditto")
head = add_first(head, new_node)
print("V1 P3 Test 1 - after:", sll_to_string(head))

head2 = Node("A", Node("B"))
new_head2 = add_first(head2, Node("Start"))
print("V1 P3 Test 2:", sll_to_string(new_head2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Get Tail)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices traversing to the end of a linked list.
#
# U -- Understand
# 1) What if the list is empty? Return None.
# 2) What should I return for a non-empty list? The tail node's value.
#
# P -- Plan
# I will walk through the list until current.next is None, then return current.value.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if head is None, return None
# - set current = head
# - while current.next exists
#   - move current forward
# - return current.value
#
# I -- Implement

def get_tail(head):
    if head is None:
        return None
    current = head
    while current.next:
        current = current.next
    return current.value

# Test Cases
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3
print("V1 P4 Test 1:", get_tail(num1))
print("V1 P4 Test 2:", get_tail(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Replace Node)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices updating node values while traversing a list.
#
# U -- Understand
# 1) Should the function make a new list? No, it updates in place.
# 2) What should happen if multiple nodes match? Replace all of them.
#
# P -- Plan
# I will loop through the list and change every matching value.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - set current = head
# - while current exists
#   - if current.value == original
#     - set current.value = replacement
#   - move current forward
#
# I -- Implement

def ll_replace(head, original, replacement):
    current = head
    while current:
        if current.value == original:
            current.value = replacement
        current = current.next

# Test Cases
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
print("V1 P5 Test 1 - before:", sll_to_string(num1))
ll_replace(num1, 5, "banana")
print("V1 P5 Test 1 - after:", sll_to_string(num1))

letters = Node("x", Node("y", Node("x")))
print("V1 P5 Test 2 - before:", sll_to_string(letters))
ll_replace(letters, "x", "z")
print("V1 P5 Test 2 - after:", sll_to_string(letters))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (List Nodes)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it connects linked list traversal with regular Python lists.
#
# U -- Understand
# 1) What if n is bigger than the list length? Return all values.
# 2) What if n is 0? Return an empty list.
#
# P -- Plan
# I will traverse up to n nodes or until the list ends, collecting values.
# Time Complexity: O(min(n, length))
# Space Complexity: O(min(n, length))
#
# Pseudocode
# - create empty result list
# - set current = head and count = 0
# - while current exists and count < n
#   - add current.value
#   - move current
#   - increment count
# - return result
#
# I -- Implement

def listify_first_n(head, n):
    result = []
    current = head
    count = 0
    while current and count < n:
        result.append(current.value)
        current = current.next
        count += 1
    return result

# Test Cases
a = Node("a", Node("b", Node("c")))
print("V1 P6 Test 1:", listify_first_n(a, 2))

j = Node("j", Node("k", Node("l")))
print("V1 P6 Test 2:", listify_first_n(j, 5))
print("V1 P6 Test 3:", listify_first_n(j, 0))


# ---------------------------------------------------------
# Session: 2
# Problem #: 7 (Insert Value)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because inserting at any position is a key linked list skill.
#
# U -- Understand
# 1) What if i is 0? Insert at the front and return the new head.
# 2) What if i is past the end? Insert at the end.
#
# P -- Plan
# I will handle index 0 first. Otherwise, I will move to the node right before
# the target index and insert there. If I reach the end early, I will attach
# the new node at the end.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - create new node
# - if i == 0, point new node to head and return it
# - move to node before index i
# - insert new node there
# - if index too large, attach at end
# - return head
#
# I -- Implement

def ll_insert(head, val, i):
    new_node = Node(val)

    if i <= 0 or head is None:
        new_node.next = head
        return new_node

    current = head
    index = 0

    while current.next and index < i - 1:
        current = current.next
        index += 1

    new_node.next = current.next
    current.next = new_node
    return head

# Test Cases
head = Node(3, Node(8, Node(12, Node(9))))
print("V1 P7 Test 1 - before:", sll_to_string(head))
head = ll_insert(head, 20, 2)
print("V1 P7 Test 1 - after:", sll_to_string(head))

head2 = Node(1, Node(2))
print("V1 P7 Test 2 - before:", sll_to_string(head2))
head2 = ll_insert(head2, 99, 10)
print("V1 P7 Test 2 - after:", sll_to_string(head2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 8 (Linked Listify)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it converts a regular list into a linked list structure.
#
# U -- Understand
# 1) What should happen if the list is empty? Return None.
# 2) What should the function return? The head of the new linked list.
#
# P -- Plan
# I will create the head from the first item, then keep attaching new nodes.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if lst is empty, return None
# - create head from first item
# - loop through remaining items
#   - create node and attach it
# - return head
#
# I -- Implement

def list_to_linked_list(lst):
    if not lst:
        return None

    head = Node(lst[0])
    current = head

    for value in lst[1:]:
        current.next = Node(value)
        current = current.next

    return head

# Test Cases
normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print("V1 P8 Test 1:", linked_list.value)
print("V1 P8 Test 2:", sll_to_string(linked_list))
print("V1 P8 Test 3:", list_to_linked_list([]))


# ---------------------------------------------------------
# Session: 2
# Problem #: 9 (Doubly Linked List)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it introduces forward and backward connections in a list.
#
# U -- Understand
# 1) What extra link does each node need? A prev pointer.
# 2) What should the middle node connect to? Both its previous and next nodes.
#
# P -- Plan
# I will create three nodes and set both next and prev references correctly.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create poliwag, poliwhirl, poliwrath
# - connect next pointers
# - connect prev pointers
#
# I -- Implement

class DNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

poliwag = DNode("Poliwag")
poliwhirl = DNode("Poliwhirl")
poliwrath = DNode("Poliwrath")

poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

# Test Cases
print("V1 P9 Test 1:", poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
print("V1 P9 Test 2:", dll_forward_to_string(poliwag))


# ---------------------------------------------------------
# Session: 2
# Problem #: 10 (Print Backwards)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it shows how doubly linked lists support reverse traversal.
#
# U -- Understand
# 1) What parameter is given? The tail node.
# 2) What direction do I move? Backward using prev.
#
# P -- Plan
# I will start at the tail and keep moving with prev, collecting values to print.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - create empty list
# - set current = tail
# - while current exists
#   - add current.value
#   - move current to prev
# - print joined values
#
# I -- Implement

def print_reverse(tail):
    values = []
    current = tail
    while current:
        values.append(str(current.value))
        current = current.prev
    print(" ".join(values))

# Test Cases
print("V1 P10 Test 1:")
print_reverse(poliwrath)

single_dll = DNode("Solo")
print("V1 P10 Test 2:")
print_reverse(single_dll)


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Poker Two-Pair Hand)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it practices counting repeated values in objects.
#
# U -- Understand
# 1) What makes a two-pair hand? Two cards of one rank and two cards of another rank.
# 2) Does the fifth card matter? No, it is unused for this check.
#
# P -- Plan
# I will count how many times each rank appears. If the sorted counts are
# [1, 2, 2], then the hand is two-pair.
# Time Complexity: O(1) because the hand always has 5 cards
# Space Complexity: O(1)
#
# Pseudocode
# - count each rank
# - sort the counts
# - return True if counts are [1, 2, 2]
#
# I -- Implement

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def is_two_pair(player_hand):
    counts = {}
    for card in player_hand:
        counts[card.rank] = counts.get(card.rank, 0) + 1
    return sorted(counts.values()) == [1, 2, 2]

# Test Cases
card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print("V2 P1 Test 1:", is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print("V2 P1 Test 2:", is_two_pair(player_two_hand))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Barbie Linked List)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it reinforces how to build a longer linked list manually.
#
# U -- Understand
# 1) How many nodes are needed? Four.
# 2) What should the last node point to? None.
#
# P -- Plan
# I will create the last node first and connect backward to the head.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create node_4 Ken
# - create node_3 Weird Barbie -> node_4
# - create node_2 President Barbie -> node_3
# - create node_1 Barbie -> node_2
#
# I -- Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_4 = Node("Ken")
node_3 = Node("Weird Barbie", node_4)
node_2 = Node("President Barbie", node_3)
node_1 = Node("Barbie", node_2)

# Test Cases
print("V2 P2 Test 1:", node_1.value, "->", node_1.next.value)
print("V2 P2 Test 2:", node_2.value, "->", node_2.next.value)
print("V2 P2 Test 3:", node_3.value, "->", node_3.next.value)
print("V2 P2 Test 4:", node_4.value, "->", node_4.next)


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Insert Value First)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices creating and inserting a new head node.
#
# U -- Understand
# 1) What is passed in here? A head node and a raw value.
# 2) What should the function return? The new head node.
#
# P -- Plan
# I will create a new node from val, point it to head, and return it.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create new node with val
# - set new_node.next = head
# - return new_node
#
# I -- Implement

def add_first_value(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

# Test Cases
node_c = Node("C")
node_b = Node("B", node_c)
node_a = Node("A", node_b)
new_list = add_first_value(node_a, 0)
print("V2 P3 Test 1:", sll_to_string(new_list))

nums = Node(2, Node(3))
nums = add_first_value(nums, 1)
print("V2 P3 Test 2:", sll_to_string(nums))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Linked List Length)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because counting nodes is a basic linked list traversal skill.
#
# U -- Understand
# 1) What should an empty list return? 0.
# 2) What counts as length? The number of nodes in the list.
#
# P -- Plan
# I will walk through the list and count each node.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - set count = 0
# - while current exists
#   - add 1 to count
#   - move current
# - return count
#
# I -- Implement

def ll_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

# Test Cases
head = Node("num1", Node("num2", Node("num3")))
print("V2 P4 Test 1:", ll_length(head))
print("V2 P4 Test 2:", ll_length(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Delete Tail)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because removing the last node is a common pointer update problem.
#
# U -- Understand
# 1) Should this modify the list in place? Yes.
# 2) What if there is only one node? The list effectively becomes a single node unchanged
#    from the outside because only head is passed in, so I will handle multi-node cases cleanly.
#
# P -- Plan
# I will stop at the second-to-last node and set its next to None.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if head is None or head.next is None, do nothing
# - move until current.next.next is None
# - set current.next = None
#
# I -- Implement

def delete_tail(head):
    if head is None or head.next is None:
        return
    current = head
    while current.next and current.next.next:
        current = current.next
    current.next = None

# Test Cases
nums = Node("num1", Node("num2", Node("num3")))
print("V2 P5 Test 1 - before:", sll_to_string(nums))
delete_tail(nums)
print("V2 P5 Test 1 - after:", sll_to_string(nums))

nums2 = Node("only")
print("V2 P5 Test 2 - before:", sll_to_string(nums2))
delete_tail(nums2)
print("V2 P5 Test 2 - after:", sll_to_string(nums2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Greatest Node)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices scanning a list to find an extreme value.
#
# U -- Understand
# 1) What type of values are stored? Integers.
# 2) What should the function return? The maximum value in the linked list.
#
# P -- Plan
# I will keep track of the biggest value seen so far while traversing.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - set max_value to head.value
# - move through list
# - update max_value when a bigger value is found
# - return max_value
#
# I -- Implement

def find_max(head):
    if head is None:
        return None
    max_value = head.value
    current = head.next
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next
    return max_value

# Test Cases
num1 = Node(20, Node(15, Node(30, Node(10))))
print("V2 P6 Test 1:", find_max(num1))

num2 = Node(-5, Node(-2, Node(-10)))
print("V2 P6 Test 2:", find_max(num2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 7 (Pop Node)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because removing by index is an important linked list operation.
#
# U -- Understand
# 1) What if i is 0? Remove the head and return the next node.
# 2) What if i is too large? Leave the list unchanged.
#
# P -- Plan
# I will handle index 0 first. Otherwise, I will move to the node before index i
# and skip over the target node if it exists.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if head is None, return None
# - if i == 0, return head.next
# - move to node before index i
# - if target exists, skip it
# - return head
#
# I -- Implement

def ll_pop(head, i):
    if head is None:
        return None
    if i == 0:
        return head.next

    current = head
    index = 0

    while current.next and index < i - 1:
        current = current.next
        index += 1

    if current.next:
        current.next = current.next.next

    return head

# Test Cases
nums = Node("num1", Node("num2", Node("num3")))
print("V2 P7 Test 1 - before:", sll_to_string(nums))
nums = ll_pop(nums, 1)
print("V2 P7 Test 1 - after:", sll_to_string(nums))

nums2 = Node(1, Node(2, Node(3)))
print("V2 P7 Test 2 - before:", sll_to_string(nums2))
nums2 = ll_pop(nums2, 10)
print("V2 P7 Test 2 - after:", sll_to_string(nums2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 8 (Find Middle Node)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it practices solving linked list problems with two pointers.
#
# U -- Understand
# 1) What should happen for even-length lists? Return the first middle node.
# 2) How can I force that? Move the fast pointer two steps ahead from fast.next.
#
# P -- Plan
# I will use slow and fast pointers. By starting fast one step ahead, slow will
# stop at the first middle for even-length lists.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if head is None, return None
# - slow = head, fast = head.next
# - while fast and fast.next
#   - move slow one step
#   - move fast two steps
# - return slow
#
# I -- Implement

def find_middle_node(head):
    if head is None:
        return None

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Test Cases
nums = Node(1, Node(2, Node(3, Node(4))))
mid = find_middle_node(nums)
print("V2 P8 Test 1:", mid.value)

nums2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
mid2 = find_middle_node(nums2)
print("V2 P8 Test 2:", mid2.value)


# ---------------------------------------------------------
# Session: 2
# Problem #: 9 (Create Double Links)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it shows how to update a class to support doubly linked lists.
#
# U -- Understand
# 1) What new attribute does the node need? prev.
# 2) What should tail.prev point to? head.
#
# P -- Plan
# I will add prev to the constructor and then connect head and tail both ways.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - update Node class to include prev
# - create head and tail
# - set head.next = tail and tail.prev = head
#
# I -- Implement

class DoubleNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = DoubleNode("First")
tail = DoubleNode("Last")
head.next = tail
tail.prev = head

# Test Cases
print("V2 P9 Test 1:", head.value, "<->", head.next.value)
print("V2 P9 Test 2:", tail.prev.value, "<->", tail.value)


# ---------------------------------------------------------
# Session: 2
# Problem #: 10 (Double to Single)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it practices rebuilding one linked structure into another.
#
# U -- Understand
# 1) What should the new list type be? Singly linked list.
# 2) Should the new list reuse old nodes? No, create new singly linked nodes.
#
# P -- Plan
# I will traverse the doubly linked list and create matching singly linked nodes.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if dll_head is None, return None
# - create sll head from dll_head value
# - move through dll nodes
#   - create new sll node for each dll node
#   - attach it
# - return sll head
#
# I -- Implement

class SLLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class DLLNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def dll_to_sll(dll_head):
    if dll_head is None:
        return None

    sll_head = SLLNode(dll_head.value)
    sll_current = sll_head
    dll_current = dll_head.next

    while dll_current:
        sll_current.next = SLLNode(dll_current.value)
        sll_current = sll_current.next
        dll_current = dll_current.next

    return sll_head

# Test Cases
ice = DLLNode("Ice")
water = DLLNode("Water")
steam = DLLNode("Steam")
ice.next = water
water.prev = ice
water.next = steam
steam.prev = water

sll_head = dll_to_sll(ice)
print("V2 P10 Test 1:", sll_to_string(sll_head))
print("V2 P10 Test 2:", dll_to_sll(None))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Calculate Tournament Placement)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it combines averages, comparisons, and object methods.
#
# U -- Understand
# 1) What tournament place is best? 1st place, meaning the lowest average.
# 2) How do I find the current player's rank? Count how many opponents have a lower average.
#
# P -- Plan
# I will compute this player's average and compare it to each opponent's average.
# Each opponent with a lower average moves this player down by one place.
# Time Complexity: O(n * m), where n is number of opponents and m is races
# Space Complexity: O(1)
#
# Pseudocode
# - find self average
# - set place = 1
# - for each opponent
#   - find opponent average
#   - if opponent average < self average
#     - increase place
# - return place
#
# I -- Implement

class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        my_avg = sum(self.race_outcomes) / len(self.race_outcomes)
        place = 1

        for opponent in opponents:
            opp_avg = sum(opponent.race_outcomes) / len(opponent.race_outcomes)
            if opp_avg < my_avg:
                place += 1

        return place

# Test Cases
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])
print("V3 P1 Test 1:", f"{player1.character} was number {player1.get_tournament_place([player2, player3])}")

player4 = Player("Toad", "Standard", [4, 4, 4])
player5 = Player("Yoshi", "Standard", [1, 1, 1])
print("V3 P1 Test 2:", f"{player4.character} was number {player4.get_tournament_place([player5])}")


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Update Linked List Sequence)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices inserting nodes into exact positions in a list.
#
# U -- Understand
# 1) What is the starting list? red -> yellow -> blue.
# 2) What should the final list be? red -> orange -> yellow -> green -> blue.
#
# P -- Plan
# I will create orange and green, then reconnect the pointers so they appear
# in the correct positions.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create red, yellow, blue
# - connect them
# - create orange and green
# - insert orange after red
# - insert green after yellow
#
# I -- Implement

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

red = Node("red")
yellow = Node("yellow")
blue = Node("blue")
red.next = yellow
yellow.next = blue

orange = Node("orange")
green = Node("green")

red.next = orange
orange.next = yellow
yellow.next = green
green.next = blue

# Test Cases
print("V3 P2 Test 1:", sll_to_string(red))
print("V3 P2 Test 2:", red.value, "->", red.next.value, "->", red.next.next.value)


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Insert Node as Second Element)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices pointer updates near the front of a list.
#
# U -- Understand
# 1) Where should the new node go? Right after the head.
# 2) Should I assume head exists? Yes.
#
# P -- Plan
# I will create a new node, point it to the old second node, and then make
# head point to the new node.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create new node with val
# - point new node to head.next
# - set head.next to new node
# - return head
#
# I -- Implement

def add_second(head, val):
    new_node = Node(val)
    new_node.next = head.next
    head.next = new_node
    return head

# Test Cases
head = Node(1, Node(3, Node(4)))
print("V3 P3 Test 1 - before:", sll_to_string(head))
head = add_second(head, 2)
print("V3 P3 Test 1 - after:", sll_to_string(head))

head2 = Node("A", Node("C"))
head2 = add_second(head2, "B")
print("V3 P3 Test 2:", sll_to_string(head2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Increment Linked List Node Values)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices updating every node in a numeric list.
#
# U -- Understand
# 1) Should the same list be returned? Yes.
# 2) What happens to each value? It increases by 1.
#
# P -- Plan
# I will traverse the list and add 1 to each node value, then return head.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - set current = head
# - while current exists
#   - add 1 to current.value
#   - move current
# - return head
#
# I -- Implement

def increment_ll(head):
    current = head
    while current:
        current.value += 1
        current = current.next
    return head

# Test Cases
my_list = Node(5, Node(6, Node(7)))
print("V3 P4 Test 1 - start:", sll_to_string(my_list))
my_list = increment_ll(my_list)
print("V3 P4 Test 1 - after 1:", sll_to_string(my_list))
my_list = increment_ll(my_list)
print("V3 P4 Test 1 - after 2:", sll_to_string(my_list))

single = Node(10)
increment_ll(single)
print("V3 P4 Test 2:", sll_to_string(single))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Copy Linked List)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because deep copying prevents accidental changes from affecting both lists.
#
# U -- Understand
# 1) Should the copy reuse original nodes? No.
# 2) What should happen if the original changes later? The copy should stay the same.
#
# P -- Plan
# I will create a brand new linked list with the same values as the old one.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if head is None, return None
# - create new head from old head value
# - move through original list
#   - create new node for each value
#   - attach it to copy
# - return copy head
#
# I -- Implement

def copy_ll(head):
    if head is None:
        return None

    new_head = Node(head.value)
    current_old = head.next
    current_new = new_head

    while current_old:
        current_new.next = Node(current_old.value)
        current_new = current_new.next
        current_old = current_old.next

    return new_head

# Test Cases
head = Node(5, Node(6, Node(7)))
copy_head = copy_ll(head)
print("V3 P5 Test 1 - original:", sll_to_string(head))
print("V3 P5 Test 1 - copy:", sll_to_string(copy_head))
head.value = 10
print("V3 P5 Test 1 - original changed:", sll_to_string(head))
print("V3 P5 Test 1 - copy unchanged:", sll_to_string(copy_head))

print("V3 P5 Test 2:", copy_ll(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Find Minimum in Linked List)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices scanning a list to find the smallest value.
#
# U -- Understand
# 1) What type of values are in the list? Numeric values.
# 2) What should the function return? The minimum value.
#
# P -- Plan
# I will traverse the list and keep track of the smallest value seen.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - set min_value to head.value
# - move through list
# - if current.value is smaller, update min_value
# - return min_value
#
# I -- Implement

def find_min(head):
    if head is None:
        return None

    min_value = head.value
    current = head.next

    while current:
        if current.value < min_value:
            min_value = current.value
        current = current.next

    return min_value

# Test Cases
head = Node(5, Node(6, Node(7, Node(8))))
print("V3 P6 Test 1:", find_min(head))

head2 = Node(8, Node(5, Node(6, Node(7))))
print("V3 P6 Test 2:", find_min(head2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 7 (Remove Node by Value from Linked List)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because removing by value is a common linked list operation.
#
# U -- Understand
# 1) Should every matching node be removed? No, only the first one.
# 2) What if no node matches? Return the original list unchanged.
#
# P -- Plan
# I will handle the head match first. Otherwise, I will search for the first node
# whose next node matches the value and skip it.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if head is None, return None
# - if head.value == val, return head.next
# - move through list
# - if current.next.value == val
#   - skip current.next
#   - stop
# - return head
#
# I -- Implement

def ll_remove(head, val):
    if head is None:
        return None

    if head.value == val:
        return head.next

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next
            return head
        current = current.next

    return head

# Test Cases
head = Node(5, Node(6, Node(7, Node(8))))
print("V3 P7 Test 1 - before:", sll_to_string(head))
head = ll_remove(head, 6)
print("V3 P7 Test 1 - after:", sll_to_string(head))

head2 = Node(1, Node(2, Node(3)))
print("V3 P7 Test 2 - before:", sll_to_string(head2))
head2 = ll_remove(head2, 9)
print("V3 P7 Test 2 - after:", sll_to_string(head2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 8 (Move Tail to Front of Linked List)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it practices both finding and repositioning nodes.
#
# U -- Understand
# 1) What if the list has 0 or 1 node? Return it unchanged.
# 2) What should happen to the old tail? It becomes the new head.
#
# P -- Plan
# I will stop at the second-to-last node, detach the tail, and move it to the front.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if list too short, return head
# - move to second-to-last node
# - store tail
# - detach tail
# - point tail.next to old head
# - return tail
#
# I -- Implement

def tail_to_head(head):
    if head is None or head.next is None:
        return head

    current = head
    while current.next.next:
        current = current.next

    tail = current.next
    current.next = None
    tail.next = head
    return tail

# Test Cases
head = Node(1, Node(2, Node(3, Node(4))))
print("V3 P8 Test 1 - before:", sll_to_string(head))
head = tail_to_head(head)
print("V3 P8 Test 1 - after:", sll_to_string(head))

head2 = Node("A")
print("V3 P8 Test 2 - before:", sll_to_string(head2))
head2 = tail_to_head(head2)
print("V3 P8 Test 2 - after:", sll_to_string(head2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 9 (Convert Singly Linked List to Doubly Linked List)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it adds backward links to an existing forward-only list.
#
# U -- Understand
# 1) What is already connected? The next pointers.
# 2) What do I need to add? The prev pointers.
#
# P -- Plan
# I will walk through the list and set each next node's prev pointer to the
# current node.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - create nodes and next links
# - set current = head
# - while current.next exists
#   - set current.next.prev = current
#   - move current
#
# I -- Implement

class MusicNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

crazy_in_love = MusicNode("Crazy in Love")
formation = MusicNode("Formation")
texas_hold_em = MusicNode("Texas Hold 'Em")
crazy_in_love.next = formation
formation.next = texas_hold_em

current = crazy_in_love
while current.next:
    current.next.prev = current
    current = current.next

# Test Cases
print("V3 P9 Test 1:", crazy_in_love.value, "<->", crazy_in_love.next.value)
print("V3 P9 Test 2:", formation.prev.value, "<->", formation.value, "<->", formation.next.value)
print("V3 P9 Test 3:", texas_hold_em.prev.value, "<->", texas_hold_em.value)


# ---------------------------------------------------------
# Session: 2
# Problem #: 10 (Find Length of Doubly Linked List from Any Node)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it shows how to explore both directions in a doubly linked list.
#
# U -- Understand
# 1) Is the given node always the head? No, it can be anywhere.
# 2) How do I get the full length? Go left to the head, then count forward.
#
# P -- Plan
# I will first move backward until I reach the head, then count all nodes moving
# forward.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if node is None, return 0
# - move backward to head using prev
# - count nodes going forward using next
# - return count
#
# I -- Implement

class AnyDNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def get_length(node):
    if node is None:
        return 0

    current = node
    while current.prev:
        current = current.prev

    count = 0
    while current:
        count += 1
        current = current.next

    return count

# Test Cases
n1 = AnyDNode(3)
n2 = AnyDNode(5)
n3 = AnyDNode(6)
n4 = AnyDNode(7)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3

print("V3 P10 Test 1:", get_length(n3))
print("V3 P10 Test 2:", get_length(n1))
print("V3 P10 Test 3:", get_length(None))