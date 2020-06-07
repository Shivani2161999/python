class stack:
	def __init__(self):
		self.stk=[]
	def push(self,item):
		self.stk.append(item)
	def pop(self):
		if self.stk==[]:
			return -1
		else:
			return self.stk.pop()
	def peep(self):
		n=len(self.stk)
		return self.stk[n-1]
	def display(self):
		return self.stk

st=stack()
print("\n--------Operations on stack-------")
print("1.push\t2.pop\t3.peep\t4.display\n5.exit")
ch=int(input("\nEnter ur choice : "))
while(ch>0 and ch<5):
	if(ch==1):
		num=int(input("\nEnter Element to Push : "))
		st.push(num)
		print(num, " is pushed on the stack.\n")

	if(ch==2):
		num=st.pop()
		print(num," is popped from the stack.\n")

	if(ch==3):
		num=st.peep()
		print(num, " is top of the stack.\n")

	if(ch==4):
		print("Current Stack state is :\n")
		print(st.display())

	print("\n--------Operations on stack-------")
	print("1.push\t2.pop\t3.peep\t4.display\n5.exit")
	ch=int(input("\nEnter ur choice : "))
