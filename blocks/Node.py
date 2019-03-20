from .Stack import Stack
from .Table import Table

import copy

class Node:
    def __init__(self, father=None, table_status=Table(),
                 stack_status=Stack(), name="Initial state", depth=0):
        self.father = father
        self.table_status = table_status
        self.stack_status = stack_status
        self.name = name
        self.depth = depth
        self.cost = 0

    def __str__(self):
        return "[{}]\nStack:\n{}\tTable: {}\n---------\n".format(self.name,
                                                               self.stack_status,
                                                               self.table_status)

    def __repr__(self):
        return str(self)

    def __eq__(self, node):
        if node == None:
            result = False
        else:
            result = self.stack_status == node.stack_status ## and self.table_status == node.table_status and
        return result

    def setCost(self):
        self.cost = self.depth * 10

    def expand(self):
        """
        Expand node and retur list of expanded nodes.
        :return: list of Nodes.
        """
        expanded = list()

        if len(self.stack_status) > 0:
            popped = self.stack_status.pop()
            self.table_status.put(popped)
            n = Node(
                father=self,
                table_status = copy.deepcopy(self.table_status),
                stack_status = copy.deepcopy(self.stack_status),
                name = "remove from stack {}".format(popped),
                depth=self.depth + 1
            )
            self.table_status.remove(popped)
            self.stack_status.push(popped)
            if n != self.father:
                expanded.append(n)

        for item in self.table_status.getElements():
            self.table_status.remove(item)
            self.stack_status.push(item)
            n = Node(father = self,
                     table_status = copy.deepcopy(self.table_status),
                     stack_status = copy.deepcopy(self.stack_status),
                     name = "move {} to stack".format(item),
                     depth=self.depth + 1
                     )
            self.stack_status.pop()
            self.table_status.put(item)
            if n != self.father:
                expanded.append(n)
        return expanded