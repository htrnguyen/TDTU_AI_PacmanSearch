import search


class PacmanProblem:
    def __init__(self, gameState):
        self.pacmanPosition = gameState.getPacmanPosition()
        self.food = tuple(gameState.getFoods())
        self.corner = tuple(gameState.getCorners())
        self.walls = gameState.getWalls()
        self.gameState = gameState
        self.foodAndCorners = set(self.food + self.corner)

        if self.pacmanPosition in self.foodAndCorners:
            self.foodAndCorners.remove(self.pacmanPosition)

        self.foodAndCorners = tuple(self.foodAndCorners)
        self.expanded = 0

    def getStartState(self):
        return (self.pacmanPosition, self.foodAndCorners)

    def isGoalState(self, state):
        return len(state[1]) == 0

    def getStartingGame(self):
        return self.gameState

    def getSuccessors(self, state):
        successors = []

        DIRECTIONS = ["North", "South", "East", "West"]

        x, y = state[0]
        currentFoodAndCorner = state[1]

        for direction in DIRECTIONS:
            nextx, nexty = self.getNextState(x, y, direction)
            nextPosition = (nextx, nexty)

            if nextPosition not in self.walls:
                nextCost = 1
                nextFoodAndCorner = list(currentFoodAndCorner)
                if nextPosition in nextFoodAndCorner:
                    nextFoodAndCorner.remove(nextPosition)
                successors.append(
                    ((nextPosition, tuple(nextFoodAndCorner)), direction, nextCost)
                )
        self.expanded += 1
        return successors

    def getNextState(self, x, y, action):
        if action == "North":
            return (x, y - 1)
        elif action == "South":
            return (x, y + 1)
        elif action == "East":
            return (x + 1, y)
        elif action == "West":
            return (x - 1, y)

    def getActions(self, searchFunction, heuristic=None):
        if searchFunction == "aStarSearch":
            func = search.AStarSearch(self, heuristic)
            return func.search()
        elif searchFunction == "uniformCostSearch" and heuristic is None:
            func = search.UniformCostSearch(self)
            return func.search()
        else:
            print("Invalid search function")
            return []
