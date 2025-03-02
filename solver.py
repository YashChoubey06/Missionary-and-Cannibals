from collections import deque
from state import State


def bfs_solve():

    initial_state = State(3, 3, 1)
    queue = deque([initial_state])
    visited = set()

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return trace_solution_path(current_state)

        visited.add((current_state.missionaries, current_state.cannibals, current_state.boat))

        for next_state in current_state.get_possible_moves():
            if (next_state.missionaries, next_state.cannibals, next_state.boat) not in visited:
                queue.append(next_state)

    return None


def trace_solution_path(state):

    path = []
    while state:
        path.append(state)
        state = state.parent
    return list(reversed(path))