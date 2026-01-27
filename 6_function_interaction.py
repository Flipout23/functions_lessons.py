# Interactions Between Functions Practice #1
# Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).

# Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:

# If the sum is less than or equal to 6:

# "The sum of your dice is {sum_dice}. Unfortunate"

# If the sum is greater than 6 and less than 10:

# "The sum of your dice is {sum_dice}. You have a good chance"

# If the sum is greater than or equal to 10:

# "The sum of your dice is {sum_dice}. It looks like a winning roll"

# Hint: use the random library's choice or randint method to choose a random value between 1 and 6.


import random
def throw_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2
def roll_result(die1, die2):
    sum_dice = die1 + die2
    if sum_dice <= 6:
        return f"The sum of your dice is {sum_dice}. Unfortunate"
    elif 6 < sum_dice < 10:
        return f"The sum of your dice is {sum_dice}. You have a good chance"
    else:
        return f"The sum of your dice is {sum_dice}. It looks like a winning roll"
die1, die2 = throw_dice()
result_message = roll_result(die1, die2)
print(result_message)


# Interactions Between Functions Practice #2
# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the elements can be changed.

# For example, if given the list [1,2,15,7,2] it should return [1,2,7].

# Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values. It should return the result (a float), without printing it.

# \
# Interactions Between Functions Practice #3
# You must create a list with values and call it secret_codes.

# Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.

# Create a second function called luck, that takes two arguments: the first must be the result of the coin toss. The second argument will be any list (the secret_codes variable that was created at the beginning).

# If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ].

# If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.

# Hint: Use the random library's choice method to choose an element at random from a sequence.



secret_codes = [42, 7, 13, 99, 7, 42]
import random
def toss_coin():
    return random.choice(["Heads", "Tails"])
def luck(coin_result, codes_list):
    if coin_result == "Tails":
        print("List will self-destruct")
        return []
    else:
        print("List was saved")
        return codes_list
coin_result = toss_coin()
final_list = luck(coin_result, secret_codes)
print(final_list)

