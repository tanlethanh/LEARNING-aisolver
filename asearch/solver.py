from aisolver.blind.solver import *


class ASearch:
    def __init__(self, initial_state) -> None:
        # self.init_state = ASearchState(initial_state.cState[:])
        self.init_state = initial_state
        # self.frontier = PriorityQueueFrontier()
        # self.frontier.append(self.init_state)

    def solve(self, frontier):
        frontier.append(self.init_state)
        while not frontier.is_empty():
            current_state = frontier.pop()
            if current_state.is_goal():
                return Solver.solution(current_state)
            neighbours = current_state.neighbours()
            for next_state in neighbours:
                frontier.append(next_state)
        return None
