# Cmput 496 sample code
# Alphabeta algorithm, depth-limited
# Written by Martin Mueller

#from search_basics import INFINITY
INFINITY = 1000000
# depth-limited alphabeta
def alphabetaDL(state, alpha, beta, depth, color):
    if state.check_game_end_gomoku()[0] or depth == 0:
        return state.staticallyEvaluateForToPlay() ,0 , 0
    
    for m in state.get_empty_points():
        state.play_move_gomoku(m,color)
        value, m_1, win_1 = alphabetaDL(state, -beta, -alpha, depth - 1,color)
        value = -int(value)
        if value > alpha:
            alpha = value
        state.undoMove(m)
        if value > beta: 
            return beta, m, 1  
        elif value == beta:
            return beta, m, 0
    return alpha, m, -1

# initial call with full window
def callAlphabetaDL(rootState, depth, color):
    value,move,winner = alphabetaDL(rootState, -INFINITY, INFINITY, depth, color)
    return move,winner
