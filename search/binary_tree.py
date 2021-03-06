class BinaryTree:
    def __init__(self):
        self.bt = None

    def add_to_parent_recurrent(self, parent, value):
        print "PARENT:" + str(parent.data) + " VALUE:" + str(value)
        from structs import btnode
        if value < parent.data:
            if parent.left is None:
                parent.left = btnode.BinaryTreeNode(value, None, None, parent)
                print "to left " + str(parent.left.data)
            else:
                self.add_to_parent_recurrent(parent.left, value)
        elif value >= parent.data:
            if parent.right is None:
                parent.right = btnode.BinaryTreeNode(value, None, None, parent)
                print "to right " + str(parent.right.data)
            else:
                self.add_to_parent_recurrent(parent.right, value)
        
    def find_node(self, parent, value, result):
        result = result
        if value < parent.data:
            if parent.left is not None:
                result = self.find_node(parent.left, value, result)
        elif value >= parent.data:
            if parent.right is not None:
                if parent.data == value:
                    result += str(parent.data) + " "
                    result = self.find_node(parent.right, value, result)
                else:
                    result = self.find_node(parent.right, value, result)
            else:
                if parent.data == value:
                    result += str(parent.data) + " "
        if len(result) == 10:
            result += "not found"
        return result

    def search(self, value):
        res = self.find_node(self.bt, value, "RESULT:\t\t\t")
        return res

    def add(self, value):
        from structs import btnode
        if self.bt is None:
            self.bt = btnode.BinaryTreeNode(value, None, None, None)
            print self.bt.data
        else:
            self.add_to_parent_recurrent(self.bt, value)
