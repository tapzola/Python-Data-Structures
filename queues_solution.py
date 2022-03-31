# Implement Queue using List(Functions)

q = []
size = int(input("Enter the size of Queue:"))
def Enqueue():
    if len(q) == size: # check wether the stack is full or not
        print("Queue is Full!!!!")
    else:
        element=input("Enter the element:")   # if not ask the user to enter the element the want to enter in the queue
        q.append(element)     # add the element to the list 
        print(element,"is added to the Queue!")   # print out the element you just added to the queue
def dequeue():
    if not q:        # check if the length of list is empty
        print("Queue is Empty!!!")
    else:
        e = q.pop(0)   # if list not empty the remove the first item in the list and print that element you just removed
        print("element removed!!:",e)
def display():
    print(q)
    while True:
        print("Select the Operation:1.Add 2.Delete 3. Display 4. Quit")
        choice = int(input())
        if choice == 1:
            Enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Invalid Option!!!")

print(display())

# Test code
# if you make the size to be 3 and select operation 1, which means to add
# you can only add a maximum of 3 elements more than that it is not going to work
# Let's say you add 1, 2 and 3 to the list the q = [1, 2, 3]. if you select delete after adding
#  those elements you should remain with this list q = [2, 3] it should follow the FIFO(First in fist out) rule
# 