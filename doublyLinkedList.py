#Doubly linked List....
class node:
	def __init__(self, data):
		self.data = data
		self.left=None
		self.right=None
class DoublylinkedList:
	def __init__(self):
		self.head=None
		self.temp=None
	def insertAtFirst(self,value):
		newNode=node(value)
		if(self.head==None):
			self.head=newNode
			self.temp=self.head
		else:
			self.head.left=newNode
			newNode.right=self.head
			self.head=newNode
		print("Data inserted at the first..\n")

	def insertAtEnd(self,value):
		newNode=node(value)
		if(self.head==None):
			self.head=newNode
			self.temp=self.head
		else:
			self.temp.right=newNode
			newNode.left=self.temp
			self.temp=newNode
		print("Data inserted at end..\n")       
		
	def deleteAtFirst(self):
		if(self.head==None):
			print("List is Empty..")
		else:
			tmp=self.head.data
			self.head=self.head.right
			self.head.left=None
			print(tmp," Eliminated from first position..\n")

	def deleteAtEnd(self):
		if(self.head==None):
			print("List is Empty..")
		else:
			tmp=self.temp.data
			self.temp=self.temp.left
			self.temp.right=None
			print(tmp," Eliminated from last position..\n")

	def display(self):
		if(self.head==None):
			print("List is Empty..")
		else:
			print("Status of Doubly Linked List..\n")
			tmp=self.head
			while(tmp!=None):
				print(tmp.data)
				tmp=tmp.right


myList=DoublylinkedList()
print("\n----------Operations on Doubly Linked List-------")
print("\n1.InsertAtFirst \t2.InsertAtEnd\t3.deleteAtFirst \t4.deleteAtEnd \t5.display \t6.exit")
ch=int(input("\nEnter ur choice : "))
while(ch>0 and ch<6):
	if(ch==1):
		num=int(input("\nEnter Element to add : "))
		myList.insertAtFirst(num)
		print(num, " is inserted At First of the list.\n")

	if(ch==2):
		num=int(input("\nEnter Element to add : "))
		myList.insertAtEnd(num)
		print(num, " is inserted At End of the list.\n")

	if(ch==3):
		num=myList.deleteAtFirst()

	if(ch==4):
		num=myList.deleteAtEnd()

	if(ch==5):
		myList.display()

	print("\n--------Operations on LinkedList-------")
	print("\n1.InsertAtFirst \t2.InsertAtEnd\t3.deleteAtFirst \t4.deleteAtEnd \t5.display \t6.exit")
	ch=int(input("\nEnter ur choice : "))
