import game, main



def is_bust(score: int) -> bool:
    """
    get updated score and chack if one player pass the 100 after rolling
    """
    passed100 = False
    if score > 100:
        passed100 = True
    return passed100

def is_exact_100(score: int) -> bool:
    """
    checks if player won the game after rolling
    """
    exact100 = False
    if score == 100:
        exact100 = True
    return exact100



def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    """
    after twice pass check which number is bigger and return it
    if a = b return None
    """
    win = None
    if a > b:
        win = a
    elif a < b:
        win = b
    return win

def add_score(score: int, name: str):
    p1_score = 0
    p2_score = 0
    re_score = 0
    if name == 'p1':
        p1_score = score_num(score, "p1")
        re_score += p1_score
    elif name == 'p2':
        p2_score = score_num(score, "p2")
        re_score += p2_score
    return re_score



def score_num(score: int, name: str) -> int:
    p1_score = 0
    p2_score = 0
    re_score = 0
    if name == "p1":
        p1_score += score
        re_score =  p1_score
    elif name == "p2":
        p2_score += score
        re_score =  p2_score
    return re_score


def massage(player: str, score_p1, score_p2):

    if player == "p1":
        print(f"""
        it is the player 1 turn.
        your score is {score_p1} 
        player 2 score is {score_p2}
        """)







