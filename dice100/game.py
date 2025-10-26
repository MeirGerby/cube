from random import randint

def roll_two_d6() -> tuple[int, int]:
    """
    return two roll numbers
    """
    roll_dice_one = randint(1, 6)
    roll_dice_two = randint(1, 6)
    roll_num = (roll_dice_one, roll_dice_two)
    return roll_num




def turn_decision(input_p: str) -> str:
    """
    when invalid characters pressed it will ask again the input
    until the user will press p/r
    """
    while input_p != "p" or input_p != "r":
        input_p = input("choose again (p/r)")
        if input_p == "p" or input_p == "r":
            break
    return input_p

def tie_breaker() -> int:
    """
    executed when two player score are same and twice pass was executed
    """
    player1 = roll_two_d6()
    player2 = roll_two_d6()
    p1_num = sum_cubes(player1)
    p2_num = sum_cubes(player2)
    check = check_num(p2_num, p1_num)
    while player1 == player2:
        player1 = roll_two_d6()
        player2 = roll_two_d6()
        p1_num = sum_cubes(player1)
        p2_num = sum_cubes(player2)
        check = check_num(p1_num, p2_num)
    return check
def sum_cubes(num: tuple[int, int]) -> int:
    """calculate the sum of two cubes"""
    num = sum(num)
    return num


def check_num(num1: int, num2: int) -> int:
    """check which is the bigger number"""
    bigger = num1
    if num2 > num1:
        bigger = num2
    return bigger

def player_turn(name: str = "p2"):
    name_p = name
    if name == "p1":
        name_p = "p2"
    elif name == "p2":
        name_p = "p1"
    return name_p


