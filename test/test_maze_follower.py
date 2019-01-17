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

def test_given_current_location_is_unknown_and_the_board_has_not_been_navigated_when_evaluating_the_board_for_s_then_the_location_of_the_s_is_returned():
    maze = ["WWSWWE"]
    x, y = evaluateBoard(maze)
    assert(x == 2)
    assert(y == 0)
    
        
def test_given_current_location_is_known_when_evaluating_adjacent_spaces_then_coordinates_of_empty_space_is_returned():
    maze = ["WWS WWE"]
    x, y = evaluateBoard(maze, 2, 0)
    assert(x == 3)
    assert(y == 0)

def test_given_current_location_is_known_and_there_are_no_adjacent_empty_spaces_when_evaluating_adjacent_spaces_then_an_error_is_thrown():
    maze = ["WWSWWE"]
    try:
         evaluateBoard(maze, 2, 0)
         assert(False)
    except ValueError:
        return