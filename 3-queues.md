# Queues

Queue is a linear data structure that stores items in a First-In/First Out(FIFO) manner. In queue, the data element that is inserted first will be removed first.

![Representation of a Queue](https://www.guru99.com/images/1/020820_0702_PythonQueue1.png)

Operations that can be performed on the queue are:

Enqueue: It adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.

Dequeue: It removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.

Front: It gives the front item from the queue.

Rear: It gives the last item from the queue.

In the above image item 1 was the first one to be inserted in the queue, and while removing it is the first one to come out. Hence the queue is called FIRST IN FIRST OUT (FIFO)

![How an item is removed from a Queue](https://www.guru99.com/images/1/020820_0702_PythonQueue2.png)

## Applications
The queue data structure is used when we want to organize the group of objects in a particular order. The second person or the thing cannot use the resources until the first person or thing releases that resource.

* It serves the request on a single shared resource. For example, Printer, CPU, etc.
One request has to process and finish first before another is completed. the first one is completed 1st.

* If we relate it with the real-world example then, the call center is one of the powerful examples of a queue.
In a call center he who call first is answered first whilst the other one is put on hold. When the first person finishes calling then the other person is attended to. 

* If any issue occurs, it can be resolved in the FIFO order i.e. the issue which occurs first will be resolved first.

## Big O Notation

Common Queue Operation | Description | Python code | Perfomance
-------- | -------- | -------- | --------
enqueue(value) | Adds "value" to the back of the queue | my_queue.append(value) | O(1)
dequeue() | Two approaches: Remove and return the item from the front of the queue; or pop off index 0 | value = my_queue[0]
del my_queue[0]
or
value = my_queue.pop(0) | O(n) 
size() | Return the size of the queue | length = len(my_queue) | O(1) 
empty() | Returns true if the length of the queue is zero. | if len(my_queue) == 0: | O(1) 

## Simple Queues Example using Lists


``` python
""" Initialize an empty list """
q=[]
# add the following numbers to the queue and print them out basically this is called enqueing them 
q.append(10)
q.append(100)
q.append(1000)
q.append(10000)
print("Initial Queue is:",q)
#Remove the first number that you added to the queue and this is called dequeue. Print the numbers remaining in the queue
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print("After Removing elements:",q)
```
When you run this code this is what the results will be:

``` python
Initial Queue is: [10, 100, 1000, 10000]
10
100
1000
After Removing elements: [10000]
```
Now after understanding much about queues let's apply queues using functions.
Here is a problem
[Problem](https://github.com/tapzola/cse212-final-project/blob/main/queues_problem.py)
After you have finished solving the problem, compare it with your answer below.
[Solution]()



