class Node:
    def __init__(self, value, prev_pointer=None, next_pointer=None):
        """
        +createNode()
        This method creates a node for the double circ. chain.
        :param value: This is the class "Werknemer".
        :param prev_pointer: This is the pointer to the previous Node, if there is none than there is no pointer.
        :param next_pointer: This is the pointer to the next Node, if there is none than there is no pointer.
        """
        self.value = value
        self.prev_pointer = prev_pointer
        self.next_pointer = next_pointer


class Double_circ_chain:
    def __init__(self, front=None):
        """
        +createDoublecircularchain()
        This method creates an empty Double_circ_chain
        :param front: This is the front of the chain
        """
        self.front = front

    def destroy(self):
        """
        +destroy()
        This function destroys a double circular chain.
        """
        del self.front

    def isEmpty(self):
        """
        +isEmpty(): boolean     {query}
        This method returns True when the double circular chain is empty
        :return: True --> when the double circular chain is empty
                 False --> when there is at least one element in the double circular
        """
        return self.front is None

    def getLenght(self):
        """
        +getLenght(out lenght: integer)    {query}
        This function returns the lenght of the double circular chain
        :return: The lenght ofhte double circular chain
        """
        if self.front is None:
            return 0
        else:
            huidige = self.front
            i = 0
            while huidige.value != self.front.prev_pointer.value:
                i += 1
                huidige = huidige.next_pointer
            return i+1

    def retrieve(self, index):
        """
        +retrieve(in index:integer, out dataItem: class, out success: boolean)    {query}
        :param index: This is the index of the Node that has to be retrieved. This is an integer.
        :return: This method returns a class.
        """
        current = self.front
        for i in range(index):
            current = current.next_pointer
        return current, True

    def insert(self, value, index=None):
        """
        +insert(in index:integer, in newItem: class, out success: boolean)
        :param value: This is what you want to insert in the chain, this is of the type class.
        :param index: This is the index or on which location the new item is stored.
        :return: This method returns the new Node.
        """
        nieuwe_node = Node(value)
        if self.front is None:
            nieuwe_node.next_pointer = nieuwe_node
            nieuwe_node.prev_pointer = nieuwe_node
            self.front = nieuwe_node

        elif index is None:
            nieuwe_node.prev_pointer = self.front.prev_pointer
            nieuwe_node.next_pointer = self.front
            self.front.prev_pointer.next_pointer = nieuwe_node
            self.front.prev_pointer = nieuwe_node
        elif index == 0:
            nieuwe_node.prev_pointer = self.front.prev_pointer
            nieuwe_node.next_pointer = self.front
            self.front.prev_pointer.next_pointer = nieuwe_node
            self.front.prev_pointer = nieuwe_node
            self.front = nieuwe_node
        elif index > 0:
            bestaande = self.retrieve(index)
            nieuwe_node.prev_pointer = bestaande.prev_pointer
            nieuwe_node.next_pointer = bestaande
            bestaande.prev_pointer.next_pointer = nieuwe_node
            bestaande.prev_pointer = nieuwe_node
        if index is not None:
            if self.retrieve(index) is not value:
                return value, False
        else:
            return value, True

    def remove(self, index):
        """
        +remove(in index: integer, out index: integer, out succes: boolean)
        This function removes an item on a specific index.
        :param index: The place where the item has to be deleted
        :return: The index where item is deleted and a boolean: True if item of the index is succesfully deleted
                                                                False if item of the index is not succesfully deleted
        """
        if self.front is None:
            return index, False
        else:
            current = self.retrieve(index)[0]
            if current == self.front:
                self.front = current.next_pointer

            current.next_pointer.prev_pointer = current.prev_pointer
            current.prev_pointer.next_pointer = current.next_pointer
            return index, True

    def selectionSort(self):
        """
        +selectionSort(out Double_circ_chain: class)
        This function sorts the elements in the Double Circular Chain.
        :return: Returns a list k with the sorted elements
        """
        lijst = []
        sortlijst = []
        huidige = self.front
        while huidige != self.front.prev_pointer:
            lijst[len(lijst):len(lijst)] = [huidige.value]
            huidige = huidige.next_pointer
        lijst[len(lijst):len(lijst)] = [huidige.value]

        i = 0
        lenght = len(lijst)
        while i < lenght:
            grootste = max(lijst)
            lijst.remove(grootste)
            sortlijst.append(grootste)
            i += 1
        sortlijst.sort()
        return sortlijst

    def toDot(self, name):
        file = open(str(name) + ".dot", "w+")
        file.write("Digraph G {")
        if self.front is None or self is None:
            file.write("}")
        else:
            file.write("\nhead->" + str(self.front.value) + "[label=head color=red] \n")
            current = self.front

            if self.front == self.front.next_pointer:
                file.write("\nhead->" + str(self.front.value) + "[label=head color=red] \n")
            elif self.front.next_pointer == self.front.prev_pointer:
                file.write(str(current.value) + "->" + str(current.prev_pointer.value)+"[label=previous color=blue]\n")
                file.write(str(current.value) + "->" + str(current.next_pointer.value) + "[label=next color=green]\n")
            else:
                while current.next_pointer.value != self.front.value:
                    file.write(str(current.value) + "->" + str(current.prev_pointer.value)+"[label=previous color=blue]\n")
                    file.write(str(current.value) + "->" + str(current.next_pointer.value) + "[label=next color=green]\n")
                    current = current.next_pointer
                else:
                    file.write(str(current.value) + "->" + str(current.prev_pointer.value) + "[label=previous color=blue]"
                                + "\n" + str(current.value) + "->" + str(current.next_pointer.value)
                                + "[label=next color=green]")
            file.write("\nrankdir=LR\n}")
