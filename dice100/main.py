from game import *
import utils



def play_game():
    """
    the main function that run the game
    """
    pass_input = None
    updated_score_p1 = 0
    updated_score_p2 = 0
    player = player_turn()
    if player == "p1":
        input_f = input("choose p/r")
        input_f = turn_decision(input_f)
        if input_f == "p" and pass_input == "p":
            tie_break_win = tie_breaker()
        elif input_f == "p":
            pass_input = "p"
        else:
            pass_input = None

        start = roll_two_d6()
        sum_num = sum_cubes(start)
        score = utils.add_score(sum_num, "p1")
        updated_score_p1 = utils.score_num(score, "p1")
        check = utils.is_bust(updated_score_p1)




    elif player == "p2":
        input_f2 = input("choose p/r")
        input_f2 = turn_decision(input_f2)
        if input_f2 == "p" and pass_input == "p":
            closer_win = utils.closer_to_target(updated_score_p1, updated_score_p2 )
        elif input_f2 == "p":
            pass_input = "p"
        else:
            pass_input = None
        start = roll_two_d6()
        sum_num = sum_cubes(start)
        utils.add_score(sum_num, "p2")
        score = utils.add_score(sum_num, "p2")
        updated_score = utils.score_num(score, "p2")
        check = utils.is_bust(updated_score)













