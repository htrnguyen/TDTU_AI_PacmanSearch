import random
import time

import search
import util
from game import Actions, Agent, Directions


class RandomAgent(Agent):
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        if len(legalActions) > 0:
            return random.choice(legalActions)
        else:
            return Directions.STOP


"""
# TODO 03: SearchAgent
Implement a subclass of Agent class.
For each game step, getAction() method is invoked and 
the returned action is performed.
"""


class SearchAgent(Agent):
    def __init__(self, searchFunction=None, searchType="CornerAndAllFoodSearchAgent"):
        if searchFunction == "uniformCostSearch":
            func = search.uniformCostSearch.search
        else:
            func = search.aStarSearch.search

        self.searchFunction = func
        self.searchType = globals()[searchType]

    def registerInitialState(self, state):
        problem = self.searchType(state)
        self.actionIndex = 0
        starttime = time.time()
        self.actions = self.searchFunction(problem)
        endtime = time.time()

        print("Time:", endtime - starttime)
        print("List of actions:", self.actions)
        print("Total cost:", len(self.actions))

    def getAction(self, state):
        i = self.actionIndex
        self.actionIndex += 1
        if i < len(self.actions):
            return self.actions[i]


class ucsSearchAgent(SearchAgent):
    def __init__(self, functionSearch="uniformCostSearch"):
        super().__init__(functionSearch)


class aStarSearchAgent(SearchAgent):
    def __init__(self, functionSearch="aStarSearch"):
        super().__init__(functionSearch)


class CornerAndAllFoodSearchAgent(SearchAgent):
    def __init__(self, gameState):
        self.pacmanPosition = gameState.getPacmanPosition()
        self.walls = gameState.getWalls()
        self.food = gameState.getFood()
        self.corners = (
            (1, 1),
            (1, self.walls.height - 2),
            (self.walls.width - 2, 1),
            (self.walls.width - 2, self.walls.height - 2),
        )
        self.cornersVisited = [False, False, False, False]

        if self.pacmanPosition in self.corners:
            cornerIndex = self.corners.index(self.pacmanPosition)
            self.cornersVisited[cornerIndex] = True

        self.cornersVisited = tuple(self.cornersVisited)

        self.expanded = 0

    def getStartState(self):
        return (self.pacmanPosition, self.food, self.cornersVisited)

    def isGoalState(self, state):
        if state[0] not in self.visitedList:
            self.visitedList.append(state[0])
            import __main__

            if "_display" in dir(__main__):
                if "drawExpandedCells" in dir(__main__._display):
                    __main__._display.drawExpandedCells(self.visitedList)
                    
        return state[1].count() == 0 and all(state[2])

    def getSuccessors(self, state):
        successors = []

        for action in [
            Directions.NORTH,
            Directions.SOUTH,
            Directions.EAST,
            Directions.WEST,
        ]:
            x, y = state[0]
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            nextPosition = (nextx, nexty)

            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False

                cornersVisited = list(state[2])

                if nextPosition in self.corners:
                    cornerIndex = self.corners.index(nextPosition)
                    cornersVisited[cornerIndex] = True

                successors.append(
                    ((nextPosition, nextFood, tuple(cornersVisited)), action, 1)
                )

        self.expanded += 1
        return successors

    def heuristic(self, state):
        position, foodGrid, cornersVisited = state
        foodList = foodGrid.asList()

        if len(foodList) == 0 and all(cornersVisited):
            return 0

        minDistance = float("inf")

        for food in foodList:
            distance = util.manhattanDistance(position, food)
            minDistance = min(minDistance, distance)

        for corner in self.corners:
            if not cornersVisited[self.corners.index(corner)]:
                distance = util.manhattanDistance(position, corner)
                minDistance = min(minDistance, distance)

        return minDistance
