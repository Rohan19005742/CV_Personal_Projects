

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, values):
        self.values = values
        self.root = self._createTree(0, len(values))
    
    def _createTree(self, i, n):
        root = None
        if i < n:
            root = Node(self.values[i])
            
            root.left = self._createTree(i*2 + 1, n)
            root.right = self._createTree(i*2 + 2, n)

        
        return root

    def printTree(self):
        def _printTree(node):
            if node is not None:
                _printTree(node.left)
                print(node.value, end=' ')
                _printTree(node.right)
        
        _printTree(self.root)
        print()

    def inOrder(self):
        result = []
        
        def _inOrder(node):
            if node is not None:
                _inOrder(node.left)
                result.append(node.value)
                _inOrder(node.right)
        
        _inOrder(self.root)
        return result

    def preOrder(self):
        result = []
        
        def _preOrder(node):
            if node is not None:
                result.append(node.value)
                _preOrder(node.left)
                _preOrder(node.right)
        
        _preOrder(self.root)
        return result
    
    def postOrder(self):
        result = []
        
        def _postOrder(node):
            if node is not None:
                _postOrder(node.left)
                _postOrder(node.right)
                result.append(node.value)
        
        _postOrder(self.root)
        return result
    

if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]
    tree = BinaryTree(values)
    print(tree.inOrder())
    print(tree.preOrder())
    print(tree.postOrder())
