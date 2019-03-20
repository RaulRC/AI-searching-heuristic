class Stack:

    def __init__(self, elements=list()):
        self.elements = elements

    def __str__(self):
        res = ""

        for item in self.elements[::-1]:
            res += "|{}|\n".format(item)
        res += " * "

        return res

    def __eq__(self, stack):
        return self.elements == stack.elements

    def __len__(self):
        return len(self.elements)

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()