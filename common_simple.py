def is_win(game_state):
    return game_state[0] == game_state[1] == 0


def boat_is_at_a(game_state):
    return game_state[2] == 'a'


def boat_is_at_b(game_state):
    return game_state[2] == 'b'


def get_boat_at_a_new_states(game_state):
    new_states = []
    for missionary in range(game_state[0] + 1):
        for cannibal in range(game_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (game_state[0] - missionary,
                         game_state[1] - cannibal,
                         'b')
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states


def get_boat_at_b_new_states(game_state):
    new_states = []
    for missionary in range(3 - game_state[0] + 1):
        for cannibal in range(3 - game_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (game_state[0] + missionary,
                         game_state[1] + cannibal,
                         'a')
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states


def find_best_frontier(frontier_states, side, compute_fn):
    min_value = 100000
    min_state = -1
    for state in frontier_states:
        if state[2] != side:
            continue
        fn = compute_fn(state)
        if fn < min_value:
            min_value = fn
            min_state = state
    return min_state, min_value