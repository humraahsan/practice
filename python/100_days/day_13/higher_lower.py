from art import logo, vs
import random
from game_data import data


def format_data(account):
    """Format the account data into printable format. """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_descr} from {account_country}"

def check_ans(guess, a_followers, b_followers):
    """ Use if statement to check if user is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display logo
print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    # Generate a random account from game_data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' :").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_ans(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are correct. Current score is {score}")
    else:
        should_continue = False
        print(f"Sorry, you are wrong. Final score is {score}")

