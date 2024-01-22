class RBT:
    class Node:
        def __init__(self, rideNumber, rideCost, tripDuration, color):
            self.rideNumber = rideNumber
            self.rideCost = rideCost
            self.tripDuration = tripDuration
            self.left = None
            self.right = None
            self.parent = None
            self.color = color
    
    def __init__(self):
        self.root = None
    
    # Insert a node into the Red-Black Tree
    def insert(self, rideNumber, rideCost, tripDuration):        
        node = self.Node(rideNumber, rideCost, tripDuration, 'RED')
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if node.rideNumber < current.rideNumber:
                current = current.left
            elif node.rideNumber > current.rideNumber:
                current = current.right
            else:
                # Error: node with the same rideNumber already exists
                return
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.rideNumber < parent.rideNumber:
            parent.left = node
        else:
            parent.right = node
        self.insert_fixup(node)
    
    # Restore the Red-Black Tree properties after insertion
    def insert_fixup(self, node):
        while node.parent is not None and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left: #case LYz
                y = node.parent.parent.right 
                if y is not None and y.color == 'RED': #case LYr
                    node.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else: #case LYb
                    if node == node.parent.right: #case LRb
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'#case LLb
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:#case RYz
                y = node.parent.parent.left
                if y is not None and y.color == 'RED': #case RYr
                    node.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else: #case RYb
                    if node == node.parent.left: #case RLb
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK' #case RRb
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'BLACK'
    
    # Left rotate a node in the Red-Black Tree
    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        
        if y.left is not None:
            y.left.parent = node
        
        y.parent = node.parent
        
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        
        y.left = node
        node.parent = y
    
    # Right rotate a node in the Red-Black Tree
    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        
        if y.right is not None:
            y.right.parent = node
        
        y.parent = node.parent
        
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        
        y.right = node
        node.parent = y
    
    # Find the minimum node in the Red-Black
    def find_minimum(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    # Find the maximum node in the Red-Black Tree
    def find_maximum(self, node):
        while node.right is not None:
            node = node.right
        return node
    
    # Find the successor of a node in the Red-Black Tree
    def find_successor(self, node):
        if node.right is not None:
            return self.find_minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent
    
    # Delete a node from the Red-Black Tree
    def delete(self, node):
        if node.left is None or node.right is None:
            y = node
        else:
            y = self.find_successor(node)
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != node:
            node.rideNumber = y.rideNumber
            node.rideCost = y.rideCost
            node.tripDuration = y.tripDuration
        if y.color == 'BLACK': #restore property of red-black tree only if black tree is deleted
            self.delete_fixup(x, y.parent)
    # function to restore red_black tree property after deletion of a black node
    def delete_fixup(self, node, parent):
        while node is None or node.color == 'BLACK':
            if self.root is None or node == self.root:
                break
            if node == parent.left:
                w = parent.right
                if w is not None and w.color == 'RED':
                    w.color = 'BLACK'
                    parent.color = 'RED'
                    self.left_rotate(parent)
                    w = parent.right
                if (w is None or w.left is None or w.left.color == 'BLACK') and (w is None or w.right is None or w.right.color == 'BLACK'):
                    if w is not None:
                        w.color = 'RED'
                    node = parent
                    parent = node.parent
                else:
                    if w.right is None or w.right.color == 'BLACK':
                        if w.left is not None:
                            w.left.color = 'BLACK'
                        if w is not None:
                            w.color = 'RED'
                        self.right_rotate(w)
                        w = parent.right
                    if w is not None:
                        w.color = parent.color
                    parent.color = 'BLACK'
                    if w.right is not None:
                        w.right.color = 'BLACK'
                    self.left_rotate(parent)
                    node = self.root
            else:
                w = parent.left
                if w is not None and w.color == 'RED':
                    w.color = 'BLACK'
                    parent.color = 'RED'
                    self.right_rotate(parent)
                    w = parent.left
                if (w is None or w.right is None or w.right.color == 'BLACK') and (w is None or w.left is None or w.left.color == 'BLACK'):
                    if w is not None:
                        w.color = 'RED'
                    node = parent
                    parent = node.parent
                else:
                    if w.left is None or w.left.color == 'BLACK':
                        if w.right is not None:
                            w.right.color = 'BLACK'
                        if w is not None:
                            w.color = 'RED'
                        self.left_rotate(w)
                        w = parent.left
                    if w is not None:
                        w.color = parent.color
                    parent.color = 'BLACK'
                    if w.left is not None:
                        w.left.color = 'BLACK'
                    self.right_rotate(parent)
                    node = self.root
        if node is not None:
            node.color = 'BLACK'

    # Search for a node in the Red-Black Tree by ride number
    def search(self, rideNumber):
        current = self.root
        while current is not None:
            if rideNumber < current.rideNumber:
                current = current.left
            elif rideNumber > current.rideNumber:
                current = current.right
            else:
                return current
        return None
    def search_range(self, x, y):
        nodes = []
        self._search_range_helper(x, y, self.root, nodes)
        return nodes
    
    def _search_range_helper(self, x, y, node, nodes):
        if node is None:
            return
        if node.rideNumber > x:
            self._search_range_helper(x, y, node.left, nodes)
        if x <= node.rideNumber <= y:
            nodes.append(node)
        if node.rideNumber < y:
            self._search_range_helper(x, y, node.right, nodes)
        
    

