#Queue data structure in Python....
#Known as first in first out data structure.
#Enqueue- adding data to backend
#dequeue- removing data from front end.


class Queue:
	def __init__(self):
		self.queue=[]

	def enQueue(self, item):
		self.queue.append(item) #always add new elements at the end of the list.
		print(item," enQueued in the Queue...\n")

	def deQueue(self):
		if(self.queue==[]):
			print("Queue is Empty..")
		else:
			item=self.queue.pop(0)  #will always pop item at queue[0] position
			print(item," deQueued from the Queue..\n")

	def display(self):
		if(self.queue==[]):
			print("Queue is Empty..")
		else:
			print("Queue status is ...\n")
			print(self.queue)
q=Queue()
print("\n----------Operations on Queue-------")
print("\n1.EnQueue \t2.DeQueued\t3.Display \t4.exit\n")
ch=int(input("\n\nEnter ur choice : "))
while(ch>0 and ch<4):
	if(ch==1):
		num=int(input("\nEnter Element to add : "))
		q.enQueue(num)

	if(ch==2):
		q.deQueue()

	if(ch==3):
		q.display()

	print("\n--------Operations on Queue-------")
	print("\n1.EnQueue \t2.DeQueued\t3.Display \t4.exit\n")
	ch=int(input("\n\nEnter ur choice : "))
