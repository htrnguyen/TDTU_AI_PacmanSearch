from queue import PriorityQueue


class SearchStrategy:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        return []


class UniformCostSearch(SearchStrategy):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        startState = self.problem.getStartState()
        expanded = set()
        frontier = PriorityQueue()
        frontier.put((0, startState, []))

        while not frontier.empty():
            currentCost, currentState, actions = frontier.get()

            if currentState not in expanded:

                if self.problem.isGoalState(currentState):
                    return actions

                expanded.add(currentState)

                successors = self.problem.getSuccessors(currentState)

                for nextState, action, cost in successors:
                    if nextState not in expanded:
                        newActions = actions + [action]
                        newCost = currentCost + cost

                        frontier.put((newCost, nextState, newActions))
        return []


class AStarSearch(SearchStrategy):
    def __init__(self, problem, heuristic):
        super().__init__(problem)
        if heuristic == "manhattan":
            self.heuristic = self.heuristicManhattan
        elif heuristic == "euclidean":
            self.heuristic = self.heuristicEuclidean
        else:
            self.heuristic = self.heuristicEuclidean

    def search(self):
        startState = self.problem.getStartState()
        expanded = set()

        frontier = PriorityQueue()
        frontier.put((self.heuristic(startState), startState, []))

        g_cost = {startState: 0}

        while not frontier.empty():
            _, currentState, actions = frontier.get()

            if currentState not in expanded:

                if self.problem.isGoalState(currentState):
                    return actions

                expanded.add(currentState)

                successors = self.problem.getSuccessors(currentState)

                for nextState, action, cost in successors:
                    if nextState not in expanded:
                        newActions = actions + [action]

                        newCost = (
                            g_cost[currentState] + cost + self.heuristic(nextState)
                        )

                        if nextState not in g_cost or newCost < g_cost[nextState]:
                            g_cost[nextState] = newCost
                            frontier.put((newCost, nextState, newActions))
        return []

    def manhattanDistance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)

    def euclideanDistance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def heuristicManhattan(self, state):
        position, listGoal = state

        if len(listGoal) == 0:
            return 0

        min_dist = float("inf")
        for goal in listGoal:
            dist = self.manhattanDistance(position, goal)
            min_dist = min(min_dist, dist)
        return min_dist

    def heuristicEuclidean(self, state):
        position, listGoal = state

        if len(listGoal) == 0:
            return 0

        min_dist = float("inf")
        for goal in listGoal:
            dist = self.euclideanDistance(position, goal)
            min_dist = min(min_dist, dist)
        return min_dist
