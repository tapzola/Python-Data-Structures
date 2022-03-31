# Implement Queue using List(using Functions)
# First analyze what each function is supposed to do then you can start solving the problems

q = []
size = int(input("Enter the size of Queue:"))
def Enqueue():

    # check wether the stack is full or not

    # if not ask the user to enter the element the want to enter in the queue

    # add the element to the list 
    
    # print out the element you just added to the queue

    pass

def dequeue():
    # check if length of list is empty
       
    # if list not empty the remove the first item in the list and print that element you just removed

    pass

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