# Cmput 496 sample code
# Alphabeta algorithm, depth-limited
# Written by Martin Mueller

#from search_basics import INFINITY
INFINITY = 1000000
from board_util import GoBoardUtil
# depth-limited alphabeta



def alphabetaDL(state, alpha, beta, depth, color):
    
    
    
    pt = None
    win = None
    
    check_end = state.check_game_end_gomoku()
    if check_end[0] or depth == 0 or len(state.get_empty_points())==0:
        ##print(">>>game end = {}, color = {}, winner = {}".format(check_end[0],state.current_player,check_end[1]))
        if not check_end[0]:
            return state.staticallyEvaluateForToPlay(state.current_player) ,pt , 0
        else: 
            #return state.staticallyEvaluateForToPlay(color) ,pt , check_end[1]
            if state.current_player == check_end[1]:
                return state.staticallyEvaluateForToPlay(state.current_player) ,pt , -1
            else: return state.staticallyEvaluateForToPlay(state.current_player) ,pt , 1
        
    
    #check_end = state.check_game_end_gomoku()
    #print("game end = {}".format(check_end[0]))
    #if check_end[0] or depth == 0:
        #if check_end[1] == color: return 1000,0,1
        #elif check_end[1] == GoBoardUtil.opponent(color): return -1000,0,-1
        #else: return 1,0,0    

    ##print("\n-all empty points: {}".format(state.get_empty_points()))
    for m in state.get_empty_points():
        
        ##print("{} take move m = {}, evaluate value, m_1 and win_1".format(state.current_player,m))
        
        #temp_state = state.copy()
        
        state.play_move_gomoku(m,color)
        ##print(str(GoBoardUtil.get_twoD_board(state)))
        ##print("alpha = {}, beta = {}".format(alpha, beta))
        pt = m
        # alternate turn
        value, m_1, win_1 = alphabetaDL(state, -beta, -alpha, depth - 1,state.current_player)
        value = -int(value)
        win = win_1
        ##print("-value = {}, m = {}, m_1 = {}, win_1 = {}".format(value,m, m_1,win_1))
        ##print("alpha = {}, beta = {}".format(alpha, beta))
        if value > alpha:
            alpha = value
        ##    print("alpha = value = {}".format(alpha))
        state.undoMove(m)
        ##print("value = {}, beta = {}, pt={}".format(value,beta,pt))
        if value >= beta: 
        ##    print(">>>return beta = {}, m = {}, win = {}".format(beta,m,win))
            return beta, m, win 
        ##print("after move({}), alpha = {}, beta = {}".format(m,alpha, beta))
    ##print(">>>after all, alpha = {}, beta = {}".format(alpha, beta))
    ##print(">>>return alpha = {}, pt = {}, win = {}".format(alpha,m,win))    
    return alpha, m, win

# initial call with full window
def callAlphabetaDL(rootState, depth, color):
    value,move,winner = alphabetaDL(rootState, -INFINITY, INFINITY, depth, color)
    
    if winner!=0:
        if winner!=color: winner = -1
        else: winner = 1
    
    ##print(">>> result: move = {}, winner = {}".format(move,winner))
    
    return move,winner