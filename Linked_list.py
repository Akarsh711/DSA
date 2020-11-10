# #  Linked List in Python from Gayle Laakmann McDowell(Hacker Rank can easyly find on YouTube)
# # That's pretty easy DS
# class Node:
# 	next = None
#     def __init__(self, data):
#         self.data = data

#       # def append(self, data):
#       # 	current = self
#       # 	while(current.next != None):
#       # 		current = current.next # when we are not at end keep moving till reach

#       # 	current.next = Node(data)


# class LinkedList:
# 	head = None
#     def __init__(self, data):
#         self.data = data

#     def append(self, data):
#         if (head == None):
#         	self.head = Node(data)
#         	return
        
#         current = head
        
#         while current.next !=None:
#         	current = current.next

#         current.next = Node(data)

#     def prepend(self, data):
#     	pass 

    
        

# class Node: 

# 	# Function to initialise the node object 
# 	def __init__(self, data): 
# 		self.data = data # Assign data 
# 		self.next = None # Initialize next as null 


# # Linked List class contains a Node object 
# class LinkedList: 

# 	# Function to initialize head 
# 	def __init__(self): 
# 		self.head = None


# 	# Functio to insert a new node at the beginning 
# 	def push(self, new_data): 

# 		new_node = Node(new_data) 

# 		# 3. Make next of new Node as head 
# 		new_node.next = self.head 

# 		# 4. Move the head to point to new Node 
# 		self.head = new_node 


# 	# This function is in LinkedList class. Inserts a 
# 	# new node after the given prev_node. This method is 
# 	# defined inside LinkedList class shown above */ 
# 	def insertAfter(self, prev_node, new_data): 

# 		# 1. check if the given prev_node exists 
# 		if prev_node is None: 
# 			print "The given previous node must inLinkedList."
# 			return

# 		# 2. create new node & 
# 		#	 Put in the data 
# 		new_node = Node(new_data) 

# 		# 4. Make next of new Node as next of prev_node 
# 		new_node.next = prev_node.next

# 		# 5. make next of prev_node as new_node 
# 		prev_node.next = new_node 


# 	# This function is defined in Linked List class 
# 	# Appends a new node at the end. This method is 
# 	# defined inside LinkedList class shown above */ 
# 	def append(self, new_data): 

# 		# 1. Create a new node 
# 		# 2. Put in the data 
# 		# 3. Set next as None 
# 		new_node = Node(new_data) 

# 		# 4. If the Linked List is empty, then make the 
# 		# new node as head 
# 		if self.head is None: 
# 			self.head = new_node 
# 			return

# 		# 5. Else traverse till the last node 
# 		last = self.head 
# 		while (last.next): 
# 			last = last.next

# 		# 6. Change the next of last node 
# 		last.next = new_node 


# 	# Utility function to print the linked list 
# 	def printList(self): 
# 		temp = self.head 
# 		while (temp): 
# 			print temp.data, 
# 			temp = temp.next



# # Code execution starts here 
# if __name__=='__main__': 

# 	# Start with the empty list 
# 	llist = LinkedList() 

# 	# Insert 6. So linked list becomes 6->None 
# 	llist.append(6) 

# 	# Insert 7 at the beginning. So linked list becomes 7->6->None 
# 	llist.push(7); 

# 	# Insert 1 at the beginning. So linked list becomes 1->7->6->None 
# 	llist.push(1); 

# 	# Insert 4 at the end. So linked list becomes 1->7->6->4->None 
# 	llist.append(4) 

# 	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
# 	llist.insertAfter(llist.head.next, 8) 

# 	print 'Created linked list is:', 
# 	llist.printList() 


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None  # Try to put this without __init__

	def Prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head 
		self.head = new_node 
	
	def Append(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node
			return

		current = self.head
		while(current.next != None):
			current.next = new_node

	def AddAfterNode(self, data, NodeAfter):
		current = self.head

		while(current.data != NodeAfter):
			current = current.next
		new_node= Node(data)
		new_node.next= current.next
		current.next = new_node



	
	def PrintList(self):
		i = self.head
		while(i):
			print(i.data)
			i = i.next



if __name__ == "__main__":
	llist = LinkedList()
	llist.Append(23)
	llist.Append(24)
	llist.Append(25)
	llist.Prepend(22)
	llist.AddAfterNode(99, 24)
	llist.PrintList()


