
from game import *
import utils



def play_game() -> bool:
    """
    the main function that run the game
    """
    check = True
    pass_input = None
    score_p1 = 0
    score_p2 = 0
    player = player_turn("p1")
    if player == "p1":
        input_f = "p1"
        input_f = turn_decision(input_f)
        if input_f == "p" and pass_input == "p":
            tie_break_win = tie_breaker()
            check = False
        elif input_f == "p":
            pass_input = "p"
        else:
            pass_input = None

        start1 = roll_two_d6()
        sum_num = sum_cubes(start1)
        if input_f == 'r':
            score_p1 += utils.add_score(sum_num, "p1")
            # updated_score_p1 = utils.score_num(score, "p1")
        check = utils.is_bust(score_p1)




    if player == "p2":
        input_f2 = "p2"
        input_f2 = turn_decision(input_f2)
        utils.massage("p2", score_p1, score_p2)
        if input_f2 == "p" and pass_input == "p":
            closer_win = utils.closer_to_target(score_p1, score_p2 )
            check = False
        elif input_f2 == "p":
            pass_input = "p"
        else:
            pass_input = None
        start2 = roll_two_d6()
        sum_num2 = sum_cubes(start2)
        if input_f2 == "r":
            score_p2 += utils.add_score(sum_num2, "p2")
            # updated_score_p2 = utils.score_num(score_p2, "p2")
        check = utils.is_bust(score_p2)

    return check



if __name__ == "__main__":
    run_game = True
    while run_game:
        play_game()
















