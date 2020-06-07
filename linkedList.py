#linked list in python....
class node:
	def __init__(self, data=None):
		self.data=data
		self.next=None

class linkedlist:
	def __init__(self):
		self.head=None

	def insertAtFirst(self,value):
		newNode=node(value)
		if(self.head==None):
			self.head=newNode
		else:
			newNode.next=self.head
			self.head=newNode
		print("Added at first..")

	def insertAtEnd(self,value):
		newNode=node(value)
		if(self.head==None):
			self.head=newNode
		else:
			temp=self.head
			while(temp.next!=None):
				temp=temp.next
			temp.next=newNode
		print("Added at last..")

	def deleteAtFirst(self):
		if(self.head==None):
			print("List is Empty...")
		else:
			tmp=self.head.data
			self.head=self.head.next #first node automatically deleted by the python.
			print(tmp, " first data deleted from the list")

	def deleteAtEnd(self):
		if(self.head==None):
			print("List is Empty...")
		else:
			tmp=self.head
			while(tmp.next!=None):
				t1=tmp
				tmp=tmp.next
			t1.next=None
			print(tmp.data, " last data deleted from the list")
     
	def display(self):
		if(self.head==None):
			print("List is Empty..")
		else:
			print("\nLinked list is : \n")
			temp=self.head
			while(temp!=None):
				print(temp.data)
				temp=temp.next

myList=linkedlist()
print("\n--------Operations on LinkedList-------")
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
