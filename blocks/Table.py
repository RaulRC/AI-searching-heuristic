class Table:

    def __init__(self, elements=set()):
        self.elements = elements

    def __str__(self):
        return str(self.elements)

    def __eq__(self, table):
        return self.elements == table.elements

    def put(self, element):
        self.elements.update({element})

    def remove(self, element):
        self.elements.remove(element)

    def getElements(self):
        return self.elements
