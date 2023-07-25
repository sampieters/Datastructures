from Structures import wrappers


def changetype(line, self):
    if line.startswith("type=bst"):
        print("\nBinary Search Tree:")
        self = wrappers.BSTwrapper()
    elif line.startswith("type=stack"):
        print("\nstack:")
        self = wrappers.stackwrapper()
    elif line.startswith("type=queue"):
        print("\nqueue:")
        self = wrappers.queuewrapper()
    elif line.startswith("type=chain"):
        print("\nDouble circular chain:")
        self = wrappers.chainwrapper()
    elif line.startswith("type=heap"):
        print("\nHeap:")
        self = wrappers.Heapwrapper()
    elif line.startswith("type=23"):
        print("\n2-3 Tree:")
        self = wrappers.TwoThreewrapper()
    elif line.startswith("type=234"):
        print("\n2-3-4 Tree:")
        self = wrappers.TwoThreeFourwrapper()
    self.createTable()
    return self


def readfile(filename):
    wrappertype = None
    printcount = 0
    typeprint = "None"
    with open(filename, "r") as read:
        for line in read:
            if line.startswith("insert"):
                lijst = line.split(" ")[1]
                print(wrappertype.tableInsert(int(lijst)))
            elif line.startswith("delete"):
                lijst = line.split(" ")
                if len(lijst) == 2:
                    lijst = line.split(" ")[1]
                    print(wrappertype.tableDelete(int(lijst)))
                else:
                    print(wrappertype.tableDelete())
            elif line.startswith("printsorted"):
                print(wrappertype.tablePrintSorted())
            elif line.startswith("print"):
                printcount += 1
                if isinstance(wrappertype, wrappers.Heapwrapper):
                    typeprint = "Heap"
                elif isinstance(wrappertype, wrappers.BSTwrapper):
                    typeprint = "BinarySearchTree"
                elif isinstance(wrappertype, wrappers.chainwrapper):
                    typeprint = "DoucleCircularChain"
                elif isinstance(wrappertype, wrappers.queuewrapper):
                    typeprint = "Queue"
                elif isinstance(wrappertype, wrappers.stackwrapper):
                    typeprint = "Stack"
                elif isinstance(wrappertype, wrappers.TwoThreewrapper):
                    typeprint = "TwoThreeTree"
                elif isinstance(wrappertype, wrappers.TwoThreeFourwrapper):
                    typeprint = "TwoThreeFourTree"
                wrappertype.tablePrint("Output/" + str(typeprint) + "-" + str(printcount))
            elif line.startswith("type="):
                wrappertype = changetype(line, wrappertype)
                printcount = 0


readfile("input.txt")
