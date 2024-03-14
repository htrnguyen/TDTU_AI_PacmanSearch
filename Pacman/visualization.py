import os
import time

import mapMaze
import pacman


class Visualize:
    def __init__(self, nameMap, searchFunction, heuristic=None):
        self.searchFunction = searchFunction
        self.map = mapMaze.Map("./pacman_layouts/" + nameMap + ".lay")
        self.problem = pacman.PacmanProblem(self.map)
        self.heuristic = heuristic

    def clearScreen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def visualize(self):
        timeStart = time.time()
        if self.heuristic is None:
            actions = self.problem.getActions(self.searchFunction)
        elif self.searchFunction != "uniformCostSearch":
            actions = self.problem.getActions(self.searchFunction, self.heuristic)
        else:
            print("Invalid heuristic for uniformCostSearch")
            actions = []
        timeEnd = time.time()

        if len(actions) == 0:
            print("No solution found")
            return

        map = self.map.getMap()
        pacmanPos = self.map.getPacmanPosition()

        for action in actions:
            pacmanPos = mapMaze.ProcessMap.updateMap(map, pacmanPos, action)
            mapMaze.ProcessMap.printMap(map, pacmanPos)
            time.sleep(0.2)
            self.clearScreen()

        print("List of actions:")
        print(actions)
        print("Total Cost:", len(actions))
        # print("Expanded Nodes:", self.problem.expanded)
        # print("Time:", (timeEnd - timeStart))
