"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(capacity)
        Use: target = Queue()  # uses default capacity
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert capacity > 0, "Queue size must be > 0"

        self._capacity = capacity
        self._values = [None] * self._capacity
        self._front = None   # queue has no data
        self._rear = 0       # first available index for insertion
        self._count = 0      # number of data items

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        res=True
        i=0
        while i<len(self._values) and self._values is None:
            i=(i+1)
        if i==len(self._values):
            res=True
        else:
            if self._values[i] is not None:
                res=False
            
            

        return res

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        res=True
        i=0
        while i<len(self._values) and self._values[i] is not None:
            i=(i+1)
        
        
        if i==len(self._values):
            res=True
            
        else:
            if self._values[i] is None:
                res=False
        return res

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """

        return self._count

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        """res=1
        eq=True
        i=self._front
        j=0
        while j<len(target) and target._values[j] is None :

            j+=1
        if j==len(target) and self._front==0:
            res=1
            eq=True
            
        while target._values[j-1] is not None:
                
                
            j-=1
            if j<0:
                j=len(target)+j
        t_front=j
           
        while target._values[t_front] is not None and res!=0:
            if target._values[t_front]!=self._values[i]:
                res=0
                eq=False
            i+=1
            if i>=len(self._values):
                i=i%len(self._values) 
            t_front+=1
            if t_front>=len(target):
                t_front=t_front%len(target)

        if self._values[i] is not None :
            res=0
            eq=False
        return eq
        """
        res=True
        
        i=self._front
        j=target._front
        a=0
        b=self._count
        if self._count==target._count:
            while res!=False and a<b:
                if i==self._capacity:
                    i=i%self._capacity
                if j==self._capacity:
                    j=j%target._capacity
                if self._values[i]!=target._values[j]:
                    
                    res=False
                i+=1
                j+=1
                a+=1
        else:
            res=False
            
        return res
    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot add to a full queue"
        self._values[self._rear]=deepcopy(value)
        if self._front is None:
            self._front=self._rear
        self._rear=(self._rear+1)%len(self._values)
        if self._rear==self._front:
            self._rear=None
        
        self._count+=1
        return
         

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        value=self._values[self._front]
        self._values[self._front]=None
        self._front+=1
        if self._front==len(self._values):
            self._front=self._front%len(self._values)
        if self._front==self._rear:
            self._front=None
        self._count-=1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"
        
        

        # your code here
        return self._values[self._front]

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._capacity

