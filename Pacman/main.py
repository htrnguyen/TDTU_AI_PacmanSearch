import sys

import search
import visualization

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <nameMap> <searchFunction>")
        sys.exit()

    if len(sys.argv) <= 3:
        _, nameMap, searchFunction = sys.argv
        visualization.Visualize(nameMap, searchFunction).visualize()
    else:
        _, nameMap, searchFunction, heuristic = sys.argv
        if heuristic == 'manhattan' or heuristic == 'euclidean':
            visualization.Visualize(nameMap, searchFunction, heuristic).visualize()
        else:
            print("Invalid heuristic")
            sys.exit()