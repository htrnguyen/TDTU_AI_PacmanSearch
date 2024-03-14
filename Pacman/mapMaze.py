class Map:
    def __init__(self, filePath):
        self.pacmanPosition, self.walls, self.foods, self.corners = self.readMapDetails(
            filePath
        )
        self.map = self.readMap(filePath)

    def readMap(self, filePath):
        with open(filePath, "r") as file:
            return [line.rstrip() for line in file]

    def readMapDetails(self, file_path):
        start = None
        walls = []
        foods = []
        corners = []
        heightWall, widthWall = 0, 0

        with open(file_path, "r") as file:
            lines = file.readlines()
            heightWall = len(lines)
            for y, line in enumerate(lines):
                widthWall = len(line.strip())
                for x, char in enumerate(line.strip()):  # remove \n
                    position = (x, y)
                    if char == "%":
                        walls.append(position)
                    elif char == ".":
                        foods.append(position)
                    elif char == "P":
                        start = position

        corners.append((1, 1))
        corners.append((1, heightWall - 2))
        corners.append((widthWall - 2, 1))
        corners.append((widthWall - 2, heightWall - 2))

        for x, y in corners:
            if (x, y) in walls:
                corners.remove((x, y))

        return start, walls, foods, corners

    def getMap(self):
        return self.map

    def getWalls(self):
        return self.walls

    def getFoods(self):
        return self.foods

    def getCorners(self):
        return self.corners

    def getPacmanPosition(self):
        return self.pacmanPosition


class ProcessMap:
    def printMap(map, position):
        for y, row in enumerate(map):
            line = ""
            for x, col in enumerate(row):
                if (x, y) == position:
                    line += "P"
                else:
                    line += col
            print(line)

    def getNewPosition(currentPosition, action):
        x, y = currentPosition

        if action == "North":
            return (x, y - 1)
        elif action == "South":
            return (x, y + 1)
        elif action == "East":
            return (x + 1, y)
        elif action == "West":
            return (x - 1, y)

    def update(map, position, element):
        x, y = position
        map[y] = map[y][:x] + element + map[y][x + 1 :]

    def updateMap(map, position, action):
        newPosition = ProcessMap.getNewPosition(position, action)

        ProcessMap.update(map, position, " ")
        ProcessMap.update(map, newPosition, "P")

        return newPosition
