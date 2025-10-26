






# print(tie_breaker())

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
    p1_score = None
    p2_score = None
    if name == 'p1':
        score_num(score, "p1")
    elif name == 'p2':
        score_num(score, "p2")

def score_num(score, name) -> int| None:
    p1_score = None
    p2_score = None
    re_score = None
    if name == "p1":
        p1_score += score
        re_score =  p1_score
    elif name == "p2":
        p2_score += score
        re_score =  p2_score

    return re_score






