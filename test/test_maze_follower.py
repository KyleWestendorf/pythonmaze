# 
from maze_follower import test, evaluateBoard

def test_test(): 
    result = test()
    assert(result == True)

def test_given_user_has_received_a_board_that_lacks_a_start_and_end_when_evaluating_the_board_then_an_error_is_thrown_missing_s_and_missing_e():
    maze = [""]
    try:
        evaluateBoard(maze)
        assert(False)
    except ValueError:
        return

def test_given_user_has_received_a_board_that_lacks_a_start_but_has_an_end_when_evaluating_the_board_then_an_error_is_thrown_missing_s():
    maze = ["E"]
    try:
        evaluateBoard(maze)
        assert(False)
    except ValueError:
        return

def test_given_user_has_received_a_board_that_lacks_an_end_but_has_a_start_when_evaluating_the_board_then_an_error_is_thrown_missing_s():
    maze = ["S"]
    try:
        evaluateBoard(maze)
        assert(False)
    except ValueError:
        return

        
