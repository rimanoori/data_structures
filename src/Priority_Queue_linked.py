"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Amirhossein Ahmadinoori
ID:      169042860
Email:   ahma2860@mylaurier.ca
__updated__ = "2023-06-27"
-------------------------------------------------------
"""
# Imports

# Constants

"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        if self._count==0:
            res=True
        else:
            res=False
        return res

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        i,p,c=self._linear_search(value)
        node=_PQ_Node(deepcopy(value),None)
        if i==-1:
            if p is None:
                if c is None:
                    self._front=node
                    self._rear=node
                    self._count+=1
                else:
                    node._next=self._front
                    self._front=node
                    self._count+=1
            else:
                if c is None:
                    self._rear._next=node
                    self._rear=node
                    self._count+=1
                else:
                    node._next=c
                    p._next=node
                    self._count+=1
        else:
            if c==self._rear:
                c._next=node
                self._count+=1
                self._rear=node
            else:
                node._next=c._next
                c._next=node
                self._count+=1
                
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"

        value=self._front._value
        current=self._front
        self._front=self._front._next
        current._next=None
        self._count-=1
        if self._count==0:
            self._rear=None
        # Your code here

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"
        value=deepcopy(self._front._value)

        # Your code here

        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """
        target1=Priority_Queue()
        target2=Priority_Queue()
        turn=True
        while self._front is not None:
            node=self._front
            self._front=self._front._next
            self._count-=1
            node._next=None
            if self._front is None:
                self._rear=None
            if turn:
                if target1._front is None:
                    target1._front=node
                    target1._rear=node
                    target1._count+=1
                else:
                    target1._rear._next=node
                    target1._rear=node
                    target1._count+=1
            else:
                if target2._front is None:
                    target2._front=node
                    target2._rear=node
                    target2._count+=1
                else:
                    target2._rear._next=node
                    target2._rear=node
                    target2._count+=1
            turn= not turn
            
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        target1=Priority_Queue()
        target2=Priority_Queue()
        i,p,c=self._linear_search(key)
        if c is not None:
            if p is not None:
                target1._front=self._front
                target1._rear=p
                target1._count+=i
                target2._front=c
                target2._rear=self._rear
                target2._count=len(self)-i
                p._next=None
                
            else:
                target2._front=c
                target2._rear=self._rear
                target2._count+=self._count
        else:
            target1._front=self._front
            target1._rear=self._rear
            target1._count+=self._count
            
        self._front=None
        self._rear=None
        self._count=0
        
        return target1,target2

    def _linear_search(self,key):
        prev=None
        curr=self._front
        i=0
        while curr and curr._value<key and curr._value!=key:
            prev=curr
            curr=curr._next
            i+=1
        if curr is None:
            i=-1
        else:
            if curr._value>key:
                i=-1
        
        return i,prev,curr

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while not (source1._front is None and source2._front is None):
            if source1._front is not None:
                node=source1._front
                source1._front=source1._front._next
                source1._count-=1
                node._next=None
                i,prev,curr=self._linear_search(node._value)
                if i==-1 and self._rear is None:
                    self._front=node
                    self._rear=node
                    self._count+=1
                elif i==-1 and curr==None:
                    self._rear._next=node
                    self._rear=node
                    self._count+=1
                elif i==-1:
                    node._next=curr
                    prev._next=node
                    self._count+=1
                else:
                    node._next=curr._next
                    curr._next=node
                    self._count+=1
                    if curr==self._rear:
                        self._rear=node
            if source2._front is not None:
                node=source2._front
                source2._front=source2._front._next
                source2._count-=1
                node._next=None
                i,prev,curr=self._linear_search(node._value)
                if i==-1 and self._rear is None:
                    self._front=node
                    self._rear=node
                    self._count+=1
                elif i==-1 and curr==None:
                    self._rear._next=node
                    self._rear=node
                    self._count+=1
                elif i==-1:
                    node._next=curr
                    prev._next=node
                    self._count+=1
                else:
                    node._next=curr._next
                    curr._next=node
                    self._count+=1
                    if curr==self._rear:
                        self._rear=node

        source1._rear=None
        source1._count=0
        source2._rear=None
        source2._count=0

        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"
        
        if self._rear is not None:
            self._rear._next=source._front
            self._rear=source._rear
            self._count+=source._count
        if self._front is None:
            self._front=source._front
            self._rear=source._rear
            self._count+=source._count
        
        source._front=None
        source._rear=None
        source._count=0
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"

        node=source._front
        source._front=node._next
        if source._front is None:
            source._rear=None
        source._count-=1
        if self._rear is not None:
            self._rear._next=node
            node._next=None
            self._rear=node
            self._count+=1
        else:
            node._next=None
            self._rear=node
            self._front=node
            self._count+=1

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

    # def prq(self):
    #     """
    #     ------------------------------------------------
    #     prints values of a queue
    #     Use: que.prq()
    #     ----------------
    #     returns:
    #         None
    #     ------------------------------------------------
    #     """
    #     curr=self._front
    #     while curr is not None:
    #         print(curr._value)
    #         curr=curr._next