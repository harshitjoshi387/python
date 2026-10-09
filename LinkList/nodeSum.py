class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(5)
b=Node(10)
c=Node(15)
d=Node(20)

a.next=b
b.next=c
c.next=d

head=a
total=0
curr=head
while curr is not None:
    total=total+curr.data
    curr=curr.next

print('sum =',total)