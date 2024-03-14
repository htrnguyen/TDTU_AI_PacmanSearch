import util
from game import Actions, Agent, Directions

"""
# TODO 01: Problem formulation
Implement a class representing the problem
"""


class SearchProblem:
    def __init__(self, problem):
        self.problem = problem

    def getStartState(self):
        return self.problem.getStartState()

    def isGoalState(self, state):
        return self.problem.isGoalState(state)

    def getSuccessors(self, state):
        return self.problem.getSuccessors(state)


"""
# TODO 02: Search strategies
Implement a class with methods as search strategies
"""


class SearchStrategy(SearchProblem):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        return []


class uniformCostSearch(SearchStrategy):
    def __inti__(self, problem):
        super().__init__(problem)

    def search(self):
        start = self.getStartState()
        expanded = set()
        frontier = util.PriorityQueue()
        frontier.push((start, [], 0), 0)

        while not frontier.isEmpty():
            state, actions, totalCost = frontier.pop()

            if state not in expanded:
                if self.isGoalState(state):
                    return actions

                expanded.add(state)

                successors = self.getSuccessors(state)

                for nextState, action, cost in successors:
                    if nextState not in expanded:
                        newActions = actions + [action]
                        newCost = totalCost + cost
                        frontier.push((nextState, newActions, newCost), newCost)
        return []


class aStarSearch(SearchStrategy):
    def __init__(self, problem):
        super().__init__(problem)
        

    def search(self):
        start = self.getStartState()
        expanded = set()
        frontier = util.PriorityQueue()
        frontier.push((start, []), self.heuristic(start))

        g_cost = {start: 0}

        while not frontier.isEmpty():
            state, actions = frontier.pop()

            if state not in expanded:
                if self.isGoalState(state):
                    return actions

                expanded.add(state)

                successors = self.getSuccessors(state)

                for nextState, action, cost in successors:
                    newActions = actions + [action]
                    newCost = cost + self.heuristic(nextState) + g_cost[state]

                    if nextState not in g_cost or newCost < g_cost[nextState]:
                        g_cost[nextState] = newCost
                        frontier.push((nextState, newActions), newCost)
        return []
