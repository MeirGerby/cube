
from game import *
import utils



def play_game() -> bool:
    """
    the main function that run the game
    """
    check = True
    pass_input = None
    updated_score_p1 = None
    updated_score_p2 = None
    player = player_turn("p1")
    if player == "p1":
        input_f = "p1"
        input_f = turn_decision(input_f)
        if input_f == 'r':
            start1 = roll_two_d6()
            sum_num = sum_cubes(start1)
            updated_score_p1 = utils.add_score_p1(sum_num)
        if input_f == "p" and pass_input == "p":
            tie_break_win = tie_breaker()
            check = False
        elif input_f == "p":
            pass_input = "p"
        else:
            pass_input = None



        check = utils.is_bust(updated_score_p1)




    if player == "p2":
        input_f2 = "p2"
        input_f2 = turn_decision(input_f2)
        if input_f2 == "r":
            start2 = roll_two_d6()
            sum_num2 = sum_cubes(start2)
            updated_score_p2 = utils.add_score_p2(sum_num2)


        if input_f2 == "p" and pass_input == "p":
            closer_win = utils.closer_to_target(updated_score_p1, updated_score_p2 )
            check = False
        elif input_f2 == "p":
            pass_input = "p"
        else:
            pass_input = None


        check = utils.is_bust(updated_score_p2)

    return check



if __name__ == "__main__":
    run_game = True
    while run_game:
        play_game()
















