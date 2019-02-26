# Cmput 496 sample code
# Alphabeta algorithm, depth-limited
# Written by Martin Mueller

#from search_basics import INFINITY
INFINITY = 1000000
from board_util import GoBoardUtil
# depth-limited alphabeta

current_color = None

def alphabetaDL(state, alpha, beta, depth, color):
    
    pt = None
    win = None
    
    check_end = state.check_game_end_gomoku()
    if check_end[0] or depth == 0 or len(state.get_empty_points())==0:
        ##print(">>>game end = {}, color = {}, winner = {}".format(check_end[0],color,check_end[1]))
        if not check_end[0]:
            return state.staticallyEvaluateForToPlay(color) ,pt , 0
        else: 
            #return state.staticallyEvaluateForToPlay(color) ,pt , check_end[1]
            if color == check_end[1]:
                return state.staticallyEvaluateForToPlay(color) ,pt , -1
            else: return -state.staticallyEvaluateForToPlay(color) ,pt , 1
        
    
    #check_end = state.check_game_end_gomoku()
    #print("game end = {}".format(check_end[0]))
    #if check_end[0] or depth == 0:
        #if check_end[1] == color: return 1000,0,1
        #elif check_end[1] == GoBoardUtil.opponent(color): return -1000,0,-1
        #else: return 1,0,0    

    ##print("\n-all empty points: {}".format(state.get_empty_points()))
    for m in state.get_empty_points():
        ##print("take move m = {}, evaluate value, m_1 and win_1".format(m))
        
        temp_state = state.copy()
        
        temp_state.play_move_gomoku(m,color)
        pt = m
        # alternate turn
        value, m_1, win_1 = alphabetaDL(temp_state, -beta, -alpha, depth - 1,GoBoardUtil.opponent(color))
        value = -int(value)
        win = win_1
        ##print("value = {}, m_1 = {}, win_1 = {}".format(value,m_1,win_1))
        if value > alpha:
            alpha = value
        temp_state.undoMove(m)
        ##print("value = {}, beta = {}, pt={}".format(value,beta,pt))
        if value > beta: 
            return beta, m_1, win_1  
        elif value == beta:
            return beta, m_1, win_1
    return alpha, pt, win

# initial call with full window
def callAlphabetaDL(rootState, depth, color):
    current_color = color
    value,move,winner = alphabetaDL(rootState, -INFINITY, INFINITY, depth, color)
    
    if winner!=0:
        if winner!=color: winner = -1
        else: winner = 1
    
    ##print(">>> result: move = {}, winner = {}".format(move,winner))
    
    return move,winner