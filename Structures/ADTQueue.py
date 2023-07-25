class Aqueue:
    def __init__(self, maxsize):
        """
        +createQueue()
        This method makes an empty array with length of maxsize values. The queue is implemented as an array, so every array
        that is used in this function refers to the queue.
        """
        self.maxsize = maxsize
        self.array = [None] * maxsize

    def destroy(self):
        """
        +destroy()
        Destroys a queue
        """
        del self.array

    def printQueue(self):
        """
        +printQueue():           {query}
        This method prints the elements of the array
        """
        print(self.array)

    def retrieve(self, item):
        return item in self.array

    def isEmpty(self):
        """
        +isEmpty(): boolean {query}
        This method returns True when the whole array of length maxsize is empty (empty = maxsize * None)
        :return: True --> when the array is empty
                 False --> when there is at least one element in the array
        """
        return self.array == [None] * self.maxsize

    def getSize(self):
        i = 0
        while self.array[i] is not None:
            i += 1
        return i

    def enqueue(self, item):
        """
        +enqueue(in item:integer, out success:boolean)
        This method puts a given item at the end of the array. The end of the array is the first None in the array.
        there can not be more than the maxsize items in the array.
        :param item: This is an integer
        :return: This method returns the array with the new item.
        """
        if self.array[len(self.array)-1] is not None:
            return item, False
        else:
            self.array[self.getSize()] = item
            return item, True

    def dequeue(self):
        """
        +dequeue(out queueFront:integer, out success:boolean)
        This method deletes the last item (that is not None) in the array and returns the array. This method only needs
        the array.
        :return: This method returns the array without the last element.
        """
        giveback = self.array[0]
        self.array[0] = None
        item = self.array[1]
        i = 1
        while self.array[i] is not None:
            self.array[i-1] = self.array[i]
            i += 1
        self.array[i-1] = self.array[i]
        if item != self.array[0]:
            return False
        return giveback, True

    def getFront(self):
        """
        +getFront(out queueFront: integer, out success:boolean)   {query}
        This method gives the front of the given array.
        :return: This method returns the first item of the array or the front of the array. If the method returns None
        that means that the array is emtpy and has no front.
        """
        return self.array[0], True

    def toDot(self, name):
        """
        +toDot()   {query}
        This method makes a .dot file
        """
        file = open(str(name) + ".dot", "w+")
        file.write("Digraph G {" + "\n" + "front [style=invis]" + "\n")
        element = 0
        while self.array[element] is not None:
            file.write(str(self.array[element]) + " " + "[shape=record]" + "\n")
            element += 1
        file.write("back [style=invis]" + "\n" + "front ->")
        element = 0
        while self.array[element] is not None:
            file.write(str(self.array[element]) + "->")
            element += 1
        file.write("back" + "\n" "rankdir=LR" + "\n}")
