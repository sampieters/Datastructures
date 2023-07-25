from Structures import ADTStack, Heap, CircularDoublyLinkedChain, ADTQueue, BinarySearchTree, TwoThreeTree, TwoThreeFourTree


class stackwrapper:
    def __init__(self):
        self.stack = None

    def createTable(self):
        self.stack = ADTStack.Stack(100)
        return self.stack

    def destroyTable(self):
        return self.stack.destroy()

    def tableIsEmpty(self):
        return self.stack.isEmpty()

    def tableLentgh(self):
        return self.stack.getSize()

    def tableInsert(self, item):
        return self.stack.push(item)

    def tableDelete(self):
        return self.stack.pop()

    def tableRetrieve(self, item):
        return self.stack.retrieve(item)

    def tablePrint(self, name):
        return self.stack.toDot(name)


class queuewrapper:
    def __init__(self):
        self.Aqueue = None

    def createTable(self):
        self.Aqueue = ADTQueue.Aqueue(100)
        return self.Aqueue

    def destroyTable(self):
        return self.Aqueue.destroy()

    def tableIsEmpty(self):
        return self.Aqueue.isEmpty()

    def tableLentgh(self):
        return self.Aqueue.getSize()

    def tableInsert(self, item):
        return self.Aqueue.enqueue(item)

    def tableDelete(self):
        return self.Aqueue.dequeue()

    def tableRetrieve(self, item):
        return self.Aqueue.retrieve(item)

    def tablePrint(self, name):
        return self.Aqueue.toDot(name)


class chainwrapper:
    def __init__(self):
        self.chain = None

    def createTable(self):
        self.chain = CircularDoublyLinkedChain.Double_circ_chain()
        return self.chain

    def destroyTable(self):
        return self.chain.destroy()

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def tablegetLentgh(self):
        return self.chain.getLenght()

    def tableInsert(self, item, index=None):
        return self.chain.insert(item, index)

    def tableDelete(self, index):
        return self.chain.remove(index)

    def tableRetrieve(self, index):
        return self.chain.retrieve(index)

    def tablePrint(self, name):
        return self.chain.toDot(name)

    def tablePrintSorted(self):
        return self.chain.selectionSort()


class BSTwrapper:
    def __init__(self):
        self.BST = None

    def createTable(self):
        self.BST = BinarySearchTree.BinarySearchTree()
        return self.BST

    def destroyTable(self):
        return self.BST.destroy()

    def tableIsEmpty(self):
        return self.BST.isEmpty()

    def tableInsert(self, item):
        return self.BST.insert(item)

    def tableDelete(self, item):
        return self.BST.delete(item)

    def tableRetrieve(self, item):
        return self.BST.retrieve(item)

    def tablePrint(self, name):
        return self.BST.toDot(name)

    def tablePrintSorted(self):
        return self.BST.inorderTraversal()


class TwoThreewrapper:
    def __init__(self):
        self.TwoThreeTree = None

    def createTable(self):
        self.TwoThreeTree = TwoThreeTree.TwoThreeTree()
        return self.TwoThreeTree

    def destroyTable(self):
        return self.TwoThreeTree.destroy()

    def tableIsEmpty(self):
        return self.TwoThreeTree.isEmpty()

    def tableInsert(self, item):
        return self.TwoThreeTree.insert(item)

    def tableDelete(self, item):
        return self.TwoThreeTree.delete(item)

    def tableRetrieve(self, item):
        return self.TwoThreeTree.retrieveItem(item)

    def tablePrint(self, name):
        return self.TwoThreeTree.toDot(name)

    def tablePrintSorted(self):
        return self.TwoThreeTree.inorder()


class Heapwrapper:
    def __init__(self):
        self.Heap = None

    def createTable(self):
        self.Heap = Heap.Heap()
        return self.Heap

    def destroyTable(self):
        return self.Heap.destroyHeap()

    def tableIsEmpty(self):
        return self.Heap.heapisEmpty()

    def tableInsert(self, item):
        return self.Heap.heapInsert(item)

    def tableDelete(self):
        return self.Heap.heapDelete()

    def tableRetrieve(self, item):
        return self.Heap.heapRetrieve(item)

    def tablePrint(self, name):
        return self.Heap.toDot(name)

    def tablePrintSorted(self):
        return self.Heap.Printsorted()

class TwoThreeFourwrapper:
    def __init__(self):
        self.TwoThreeFourTree = None

    def createTable(self):
        self.TwoThreeFourTree = TwoThreeFourTree.TwoThreeFourTree()
        return self.TwoThreeFourTree

    def destroyTable(self):
        return self.TwoThreeFourTree.destroy()

    def tableIsEmpty(self):
        return self.TwoThreeFourTree.isEmpty()

    def tableInsert(self, item):
        return self.TwoThreeFourTree.insert(item)

    def tableDelete(self, item):
        return self.TwoThreeFourTree.delete(item)

    def tableRetrieve(self, item):
        return self.TwoThreeFourTree.retrieve(item)

    def tablePrint(self, name):
        return self.TwoThreeFourTree.toDot(name)

    def tablePrintSorted(self):
        return self.TwoThreeFourTree.inorderTraversal()
