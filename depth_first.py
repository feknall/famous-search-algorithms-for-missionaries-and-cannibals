from common import *
from treelib import Tree

depth = 13
win = False
tree = Tree()
visited_states = set()


def dfs():
    initial_state = (3, 3, 'a')
    visited_states.add(initial_state)
    states = [initial_state]
    root_node = "0" + str(initial_state) + "0"
    tree.create_node(get_node_label(initial_state, 0, 0), root_node)

    new_states = get_boat_at_a_new_states(initial_state)
    go_deeper(new_states, 1, states, root_node)

    tree.show()
    print("Finished! Solution found? " + str(win))


def handle_win(game_state, state_stack):
    global win
    state_stack.append(game_state)
    print("Win! Last state: " + str(game_state))
    print("Steps: " + str(state_stack))
    win = True


def get_new_states(game_state):
    new_states = []
    if boat_is_at_a(game_state):
        new_states = get_boat_at_a_new_states(game_state)
    elif boat_is_at_b(game_state):
        new_states = get_boat_at_b_new_states(game_state)
    return new_states


def handle_not_win(game_state, state_stack, current_depth, parent_node_id):
    state_stack.append(game_state)
    new_states = get_new_states(game_state)
    not_duplicate_states = []
    for new_state in new_states:
        if new_state not in visited_states:
            visited_states.add(new_state)
            not_duplicate_states.append(new_state)
    go_deeper(not_duplicate_states, current_depth + 1, state_stack, parent_node_id)
    state_stack.pop()


def go_deeper(same_level_states, current_depth, state_stack, parent_node_id):
    global win
    for index, game_state in enumerate(same_level_states):
        if not win:
            visited_states.add(game_state)
            current_node_id = add_to_tree(game_state, current_depth, index, parent_node_id)
            if is_win(game_state):
                handle_win(game_state, state_stack)
            elif current_depth < depth:
                handle_not_win(game_state, state_stack, current_depth, current_node_id)


def add_to_tree(game_state, current_depth, index, parent_node_id):
    current_node_label = get_node_label(game_state, current_depth, index)
    current_node_id = parent_node_id + str(current_depth) + str(game_state) + str(index)
    tree.create_node(current_node_label, current_node_id, parent_node_id)
    return current_node_id


def get_node_label(game_state, current_depth, index):
    if is_win(game_state):
        return "***** " \
               + get_simple_node_label(game_state, current_depth, index) \
               + " *****"
    else:
        return get_simple_node_label(game_state, current_depth, index)


def get_simple_node_label(game_state, current_depth, index):
    return "depth: " \
           + str(current_depth) \
           + ", index: " \
           + str(index) + ", state: " \
           + str(game_state)


if __name__ == "__main__":
    dfs()
