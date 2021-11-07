from common import *

depth = 150
win = False
side = 'a'


def best_first():
    initial_state = (3, 3, 'a')
    frontier_states = list()
    frontier_states.append(initial_state)
    iterate_over_states(frontier_states, 0)
    print("Finished! Win: " + str(win))


def iterate_over_states(frontier_states, current_depth):
    global win
    while not win:
        best_frontier_state, best_frontier_fn = find_best_frontier(frontier_states, side, compute_fn)
        toggle_side()

        print("Frontiers: " + str(frontier_states))
        print("Best State: " + str(best_frontier_state))
        print("Best Value: " + str(best_frontier_fn))
        print("")
        frontier_states.remove(best_frontier_state)

        if is_win(best_frontier_state):
            print("Win! Last state: " + str(best_frontier_state))
            win = True
        elif boat_is_at_a(best_frontier_state):
            add_new_states_to_frontier(frontier_states, get_boat_at_a_new_states(best_frontier_state))
        elif boat_is_at_b(best_frontier_state):
            add_new_states_to_frontier(frontier_states, get_boat_at_b_new_states(best_frontier_state))

        iterate_over_states(frontier_states, current_depth + 1)


def add_new_states_to_frontier(frontier_states, new_states):
    frontier_states += new_states


def toggle_side():
    global side
    if side == 'a':
        side = 'b'
    else:
        side = 'a'


def compute_fn(game_state):
    return compute_hn(game_state)


def compute_hn(game_state):
    return game_state[0] + game_state[1]


if __name__ == "__main__":
    best_first()
