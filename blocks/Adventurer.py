from .Node import Node
from .Stack import Stack
from .Table import Table

import logging
import time

class Adventurer:
    def __init__(self, initial_node=Node(), goal=Node()):
        self.initial_node = initial_node
        self.initial_node.cost = 0
        self.current_node = self.initial_node
        self.goal = goal
        self.solution = list()
        self.open = [self.initial_node]
        self.solution_node = None
        self.visited = list()

    def solve(self, solver='i'):
        """
        Search for solution using specified solver (Default width search)
        :param solver: Solver used to find solution. [w]idth, [d]epth, [a]*, [i]terative A*
        :return: Solution node and instance of adventurer
        """
        start = time.time()
        if solver=='w':
            self.solver = 'Width'
            self.solveWidth()
        elif solver=='d':
            self.solver = 'Depth'
            self.solveDepth()
        elif solver=='a':
            self.solver = "A*"
            self.solveAStar()
        elif solver=='i':
            self.solver = "A* Iterative"
            self.solveAStarIterative()
        end = time.time()

        result = " -> ".join(self.constructSolution(compact=True))
        print(result)
        print("Solution reached with solver [{}] in [{}] levels ({} seconds)".format(
            self.solver,
            self.solution_node.depth,
            round(end - start, 2)))
        return result, self

    def solveWidth(self):
        """
        Solve problem using width search
        :return: Solution node. Updates state of Adventurer
        """
        if len(self.open) > 0:
            if self.goal in self.open:
                candidate = None
                for item in self.open:
                    if item == self.goal:
                        candidate = item
                logging.info("Final state: {}".format(candidate))
                self.solution_node = candidate
                print("Done! Depth: {}".format(self.solution_node.depth))
            else:
                logging.info("Expand... lvl {}".format(self.open[0].depth))
                expanded = self.open[0].expand()
                for item in expanded:
                    if (item not in self.visited) and (item not in self.open):
                        self.open.append(item)
                self.visited.append(self.open.pop(0))
                #logging.info(str(expanded))
                self.solveWidth()
        else:
            self.solution_node = self.initial_node
            print("Done! with no solution.")
        return self.solution_node

    def solveDepth(self):
        """
        Solve problem using depth search
        :return: Solution node. Updates state of Adventurer
        """
        if len(self.open) > 0:
            if self.goal in self.open:
                candidate = None
                for item in self.open:
                    if item == self.goal:
                        candidate = item
                logging.info("Final state: {}".format(candidate))
                self.solution_node = candidate
                print("Done! Depth: {}".format(self.solution_node.depth))
            else:
                logging.info("Expand... lvl {}".format(self.open[0].depth))
                expanded = self.open[0].expand()
                self.visited.append(self.open.pop(0))
                for item in expanded:
                    if (item not in self.visited) and (item not in self.open):
                        self.open.insert(0, item)
                #logging.info(str(expanded))
                self.solveDepth()
        else:
            self.solution_node = self.initial_node
            print("Done! with no solution.")
        return self.solution_node


    # Recursive
    def solveAStar(self):
        """
        Solve problem using A* algorithm (recursive)
        :return: Update state of Adventurer
        """
        if len(self.open) == 0:
            self.solution_node = self.initial_node
            print("Done! with no solution.")

        item = list(filter(lambda x: x == self.goal, self.open))
        if item:
            item.sort(key=lambda x: x.cost)
            self.solution_node = item.pop(0)
            logging.info("Final state: {}".format(self.solution_node))
            print("Done! Depth: {}".format(self.solution_node.depth))

        else:
            logging.info("Expand... lvl {}".format(self.open[0].depth))
            expanded = self.open[0].expand()
            self.open[0].setCost()
            self.visited.append(self.open.pop(0))
            self.open += list(map(lambda x: self.setCost(x), expanded))
            self.open.sort(key=lambda x: x.cost, reverse=False)
            #logging.info(str(expanded))
            self.solveAStar()

    # Iterative
    def solveAStarIterative(self):
        """
        Solve problem using A* algorithm (iterative)
        :return: Solution node. Updates state of Adventurer
        """
        result = self.initial_node
        self.open = [self.initial_node]
        while self.goal != self.solution_node:
            node = self.open.pop(0)
            node.setCost()
            if self.goal == node:
                self.solution_node = node
                logging.info("Final state: {}".format(self.solution_node))
                print("Done! Depth: {}".format(self.solution_node.depth))
            else:
                logging.info("Expand... lvl {}".format(node.depth))
                expanded = node.expand()
                self.open += list(map(lambda x: self.setCost(x), expanded))
                self.open.sort(key=lambda x: x.cost, reverse=False)
        return self.solution_node

    def constructSolution(self, compact=False):
        aux_node = self.solution_node
        self.solution.append(aux_node)
        while aux_node.father != None:
            aux_node = aux_node.father
            self.solution.append(aux_node)
        self.solution.reverse()

        if compact:
            self.solution = list(map(lambda x: x.name, self.solution))
        return self.solution

    def setCost(self, node):
        """
        Set to a node a cost.
        :param node: Node to ponderate
        :return: Node with the cost associated
        """
        if node.stack_status.elements == self.goal.stack_status.elements[:len(node.stack_status)]:
            node.cost += len(self.goal.stack_status.elements) - len(node.stack_status.elements)
        else:
            node.cost += node.depth + (len(node.stack_status.elements)+1) * 10
        return node