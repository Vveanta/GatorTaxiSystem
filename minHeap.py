# Define the node class for the min heap
class Ride:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration
        

# Define the min heap class
class MinHeap:
    def __init__(self):
        self.heap=[]
        # self.root = None
        self.size = 0
#functions to find the index for parent or child nodes
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    
    def root(self):
        return(self.heap[0])
    
    
    
    # Insert a node into the min heap
    def insert(self, rideNumber, rideCost, tripDuration):
        node = Ride(rideNumber, rideCost, tripDuration)
        self.heap.append(node)
        self.size += 1    
        self.heapify_up(self.size-1)
    
    # Remove the root node from the min heap
    def remove_min(self):
        if self.size == 0 :
            return None
        
        min_node = self.heap[0]
        
        if self.size == 1:
            self.heap.pop(0) 
            self.size -= 1
            # return self.heap(min_node)
            return min_node
               
        last_node = self.heap[self.size-1]
        self.heap[0]=last_node
        self.heap.pop(self.size-1)
        self.size -= 1
        self.heapify_down(0)        
        return min_node
    
    # Heapify up after insertion
    def heapify_up(self, index):
        if self.parent(index) < 0:
            return
        
        if self.heap[index].rideCost < self.heap[self.parent(index)].rideCost or (self.heap[index].rideCost == self.heap[self.parent(index)].rideCost and self.heap[index].tripDuration < self.heap[self.parent(index)].tripDuration):
            self.swap_nodes(self.heap[index], self.heap[self.parent(index)])
            self.heapify_up(self.parent(index))
    
    # Heapify down after removal
    def heapify_down(self, index):
        if index>self.size-1 or index<0 :
            return
        
        min_node = index
        
        if self.left(index) < self.size and (self.heap[self.left(index)].rideCost < self.heap[min_node].rideCost or (self.heap[self.left(index)].rideCost == self.heap[min_node].rideCost and self.heap[self.left(index)].tripDuration < self.heap[min_node].tripDuration)):
            min_node = self.left(index)
        
        if self.right(index) < self.size and (self.heap[self.right(index)].rideCost < self.heap[min_node].rideCost or (self.heap[self.right(index)].rideCost == self.heap[min_node].rideCost and self.heap[self.right(index)].tripDuration < self.heap[min_node].tripDuration)):
            min_node = self.right(index)
        
        if min_node != index:

            self.swap_nodes(self.heap[index], self.heap[min_node])
            self.heapify_down(min_node)
    
    # Swap two nodes in the min heap
    def swap_nodes(self, node1, node2):
        node1.rideNumber, node2.rideNumber = node2.rideNumber, node1.rideNumber
        node1.rideCost, node2.rideCost = node2.rideCost, node1.rideCost
        node1.tripDuration, node2.tripDuration = node2.tripDuration, node1.tripDuration
    
    # Find the last node in the min heap
    def find_last_node(self, size):
        return self.size-1
    
    # Get the minimum ride from the min heap
    def get_min_ride(self):
        if self.size ==0:
            return None
        else:
            return (self.heap[self.root()].rideNumber, self.heap[self.root()].rideCost, self.heap[self.root()].tripDuration)
    
    # Check if the min heap is empty
    def is_empty(self):
        return self.size == 0
    
    #find the index of a node in the heap using given its ride Number
    def find_index(self, ridenumber):
        for i, ride in enumerate(self.heap):
            if ride.rideNumber == ridenumber:
                return i
        return -1
    
    #delete a node given its ride number
    def delete(self, rideNumber):
        index = self.find_index(rideNumber)
        if index == -1:
            return None
        
        node = self.heap[index]
        self.heap[index] = self.heap[self.size-1]
        self.heap.pop()
        self.size -= 1
        
        if index < self.size:
            parent_index = self.parent(index)
            # if index > 0 and self.heap[index].rideCost < self.heap[parent_index].rideCost:
            if index > 0 and (self.heap[index].rideCost < self.heap[parent_index].rideCost or (self.heap[index].rideCost == self.heap[parent_index].rideCost and self.heap[index].tripDuration < self.heap[parent_index].tripDuration)):
                self.heapify_up(index)
            else:
                self.heapify_down(index)
        return node
    
    #function to update the ride if destination changed
    def update(self, rideNumber, rideCost, tripDuration):
        index = self.find_index(rideNumber)
        if index == -1:
            return False
        
        self.heap[index].rideCost = rideCost
        self.heap[index].tripDuration = tripDuration
        
        parent_index = self.parent(index)
        if index > 0 and (self.heap[index].rideCost < self.heap[parent_index].rideCost or (self.heap[index].rideCost == self.heap[parent_index].rideCost and self.heap[index].tripDuration < self.heap[parent_index].tripDuration)):
            self.heapify_up(index)
        else:
            self.heapify_down(index)
        
        return True


