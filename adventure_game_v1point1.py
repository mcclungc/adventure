import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that there are monsters around here, "
                "and they have been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


def offer_choice(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = validate_choice("(Please enter 1 or 2.)\n")
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)


def offer_new_game():
    play_again = input("Would you like to play again? (y/n)\n").lower()
    if play_again != 'n' and play_again != 'y':
        print_pause("Enter y or n only, please.")
        offer_new_game()
    elif play_again == 'y':
        print_pause("Excellent! Restarting the game...")
        play_game()
    else:
        print_pause("Okay, goodbye!")


def validate_choice(choices_msg):
    choice = ""
    while choice != '1' and choice != '2':
        choice = input(choices_msg)
        if choice == '1':
            return choice
        elif choice == '2':
            return choice


def house(items):
    print_pause("You approach the door of the house.")
    monster = random.choice(["gorgon", "fairy", "dragon", "harpy", "werewolf",
                            "vampire"])
    print_pause(f"You are about to knock when the door opens and out "
                f"steps a {monster}.")
    # print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    attack_respond(items, monster)


def attack_respond(items, monster):
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, what "
                    "with only having a tiny dagger.")
    choice = validate_choice("Would you like to (1) fight or (2) run away?\n")
    if choice == '1':
        fight(items, monster)
    if choice == '2':
        run_away(items, monster)


def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "sword" not in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
        offer_choice(items)
    else:
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        offer_choice(items)


def fight(items, monster):
    if "sword" in items:
        print_pause(f"As the wicked {monster} moves to attack, you unsheath "
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as "
                    "you brace yourself for the attack.")
        outcome = random.randint(1, 11)
        if outcome <= 8:
            print_pause(f"But the wicked {monster} takes one look at your "
                        "shiny new toy and runs away!")
            print_pause(f"You have rid the town of the wicked {monster}. You "
                        " are victorious!")
        # occasionally having the sword isn't enough to let you win
        else:
            print_pause(f"You do your best...but today the Sword of Ogoroth "
                        f"is no match for the wicked {monster}.")
            print_pause("You have been defeated!")
    else:
        print_pause(f"You do your best...but your dagger is no match for the "
                    f"wicked {monster}.")
        print_pause("You have been defeated!")
    offer_new_game()


def run_away(items, monster):
    outcome = random.randint(1, 5)
    if outcome <= 3:
        print_pause("You run back into the field. Luckily, you don't seem "
                    "to have been followed.")
        offer_choice(items)
    # sometimes the monster pursues you when you run away
    else:
        print_pause(f"Oh no! The {monster} is following you!")
        attack_respond(items, monster)


def play_game():
    items = []
    intro()
    offer_choice(items)


play_game()
