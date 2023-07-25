class Stack:
    def __init__(self, maxsize):
        """
        +createStack()
        This method makes an emtpy class that represents a Stack with the employees and is implemented with a list.
        """
        self.maxsize = maxsize
        self.array = [None] * maxsize

    def destroy(self):
        """
        +destroy()
        Destroys a stack
        """
        del self.array

    def isEmpty(self):
        """
        +isEmpty(): boolean     {query}
        This method returns True when the list is empty (no elements)
        :return: True --> when the lsit is empty
                 False --> when there is at least one element in the list
        """
        return self.array == [None] * self.maxsize

    def push(self, item):
        """
        +push(in item:integer, out success:boolean)
        This method puts a given item at the end of the list.
        :param item: This is an integer
        :return: This method returns the array with the new item.
        """
        if self.array == [None] * self.maxsize:
            self.array[self.maxsize - 1] = item
            return item, True
        elif self.array[0] is not None:
            return item, False
        else:
            i = 0
            while self.array[i + 1] is None:
                i += 1
            else:
                self.array[i] = item
                return item, True

    def pop(self):
        """
        +pop(out success:boolean)
        This method removes the top of the stack
        """
        i = 0
        while self.array[i] is None:
            i += 1
        else:
            giveback = self.array[i]
            self.array[i] = None
            return giveback, True

    def getTop(self):
        """
        +getTop(out stackTop:integer, out success:boolean)    {query}
        :return: This method returns the first item of the Stack.
        """
        i = 0
        while self.array[i] is not None:
            i += 1
        return self.array[i - 1], True

    def getSize(self):
        """
        +getSize(out size:integer)  {query}
        :return: This method returns the lenght of the Stack
        """
        i = 0
        while self.array[i] is None:
            i += 1
        return self.maxsize - i

    def retrieve(self, item):
        """
        +retrieve(in item:integer, out succes:boolean)  {query}
        :param item: This is the item that has to be found
        :return: True -> when item is found in the stack
                 False -> when item is not found in the stack
        """
        i = 0
        while self.array[i] != item:
            i += i
        return self.array[i], True

    def toDot(self, name):
        """
        +toDot()   {query}
        This method makes a .dot file
        """
        file = open(str(name) + ".dot", "w+")
        file.write("Graph G {" + "\n" + "bottom [shape=record]" + "\n")
        lengte = len(self.array) - 1
        while self.array[lengte] is not None:
            file.write(str(self.array[lengte]) + " " + "[shape=record]" + "\n")
            lengte -= 1
        file.write("rankdir=LR" + "\n}")
