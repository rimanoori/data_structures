"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Amirhossein Ahmadinoori
ID:      169042860
Email:   ahma2860@mylaurier.ca
__updated__ = "2023-05-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
import random
# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
 
    while len(source)!=0:
        a=source.pop()
        stack.push(a)
    
    
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    target_p=[]
    while not(stack.is_empty()):
        a1=stack.pop()
        target_p.append(a1)
    while not(len(target_p)==0):
        a1=target_p.pop()
        target.append(a1)
    return 

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    ss=Stack()
    for i in source:
        ss.push(i)
        
    
    no=len(source)
    if no==0:
        if ss.is_empty():
            print ("is_empty works right")
        else:
            print ("is_empty ERROR")
    else:
        if ss.is_empty():
            print ("is_empty ERROR")
        else:
            print ("is_empty works right")   
    n=random.randint(1,999)
    ss.push(n)
    t=0
    for i in ss:
        t+=1
    if t==no+1:
        m=ss.pop()
        if m==n:
            print("push works right")
        else:
            print("push ERROR")
    ss.push(n)
    l=ss.pop()
    if l==n:
        print("pop works right")
    else:
        print("pop ERROR")
    ss.push(n)
    p=ss.peek()
    if p==n:
        print("peek works right")
    else:
        print("peek ERROR")
    
    
    
    
    ##############check
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        a=source.pop(0)
        queue.insert(a)
        
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        a=queue.remove()
        target.append(a)
        
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    n=len(a)
    if len(a)==0:
        if a.is_empty():
            print("is_empty ok")
        else:
            print("is_empty ERROR")
    else:
        if len(a)==0:
            print("is_empty ERROR")
        else:
            print("is_empty ok")
    a.insert(0)
    if a[len(a)]==0:
        print("insert ok")
    else:
        print("insert ERROR")
    a.remove(0)
    if len(a==0):
        print("queue is empty cannot remove")
    else:
        var=a.remove()
        if var==a[0]:
            print("remove ok")
        else:
            print("remove ERROR")
    a.append(var)
    r=a.peek()
    if r==a[0]:
        print("peek ok")
    else:
        print("peek ERROR")
        
    if len(a)==n:
        print("len ok")
    else:
        print(" len ERROR")
        
        
        
    
    q = Queue()

    

    return
     
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while source!=[] :
        value=source[0]
        source.remove(source[0])
        pq.insert(value)
        
    return
        

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        value=pq.remove()
        target.append(value)

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    for i in a:
        pq.insert(i)    
    
    # tests for the priority queue methods go here
    ##is_empty test
    if len(a)==0:
        if pq.is_empty():
            emp=1
        else:
            emp=0
    else:
        if pq.is_empty():
            emp=0
        else:
            emp=1        
    if len(a)==0:
        print("cannot test insert and peek and remove method with an empty input list")
        
    else:
        ## insert check
        pq.insert(a[0])
        
        if emp==1:
            if pq.is_empty():
                ins=0
            else:
                ins=1
        else:
            print("cannot test insert method while is_empty has ERROR")
    ##test remove method
    if ins==0:
        print("cannot test remove method while insert has ERROR")
    else:
        s=pq.remove()
        if s==a[0]:
            rem=1
        else:
            rem=0
    ##peek test
    if ins==1:
        if len(a)>=1:
            pq.insert(a[0])
            pq.insert(a[1])
            p=pq.peek()
            if a[1]<=a[0]:
                if p==a[1]:
                    pee=1
                else:
                    pee=0
            else:
                if p==a[0]:
                    pee=1
                else:
                    pee=0               
                
        else:
            print("cannot test peek with a list having less that 2 elements")
    else:
        print("cannot test peek while insert has ERROR")
        
          
        
        
        
        
    
    
    # print the results of the method calls and verify by hand
    if emp==1:
        print("is_empty ok")
    else:
        print("is_empty ERROR")
    if ins==1:
        print("insert ok")
    else:
        print("insert ERROR")
    if rem==1:
        print("remove ok")
    else:
        print("remove ERROR")
    if pee==1:
        print("peek ok")
    else:
        print("peek ERROR")
    
    
    
    return
