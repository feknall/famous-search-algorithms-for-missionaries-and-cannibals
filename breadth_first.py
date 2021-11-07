from common import *


def get_future_states(game_state):
    if boat_is_at_a(game_state):
        return get_boat_at_a_new_states(game_state)
    else:
        return get_boat_at_b_new_states(game_state)


def bfs():
    state_stack = list()
    visited_states = set()
    initial_state = (3, 3, 'a')
    visited_states.add(initial_state)
    states = [initial_state]
    all_states = [states]

    win = False
    while not win:
        print("States: " + str(states))
        new_states = []
        for game_state in states:
            print("Current State: " + str(game_state))
            state_stack.append(game_state)
            if is_win(game_state):
                print("Win! Last state: " + str(game_state))
                win = True
                break
            future_states = get_future_states(game_state)
            for future_state in future_states:
                if future_state not in visited_states:
                    new_states.append(future_state)
                    visited_states.add(future_state)
                    print("Future State: " + str(future_state))
            print()
        if not win:
            states = new_states
            all_states.append(states)
    print()
    print()
    print("State Stack:")
    for i in state_stack:
        print(i)
    print()
    print("All States:")
    for p_state in all_states:
        print(p_state)
    print("Finished!")


if __name__ == "__main__":
    bfs()
