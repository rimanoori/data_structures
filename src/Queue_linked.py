"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Amirhossein Ahmadinoori
ID:      169042860
Email:   ahma2860@mylaurier.ca
__updated__ = "2023-06-26"
-------------------------------------------------------
"""

"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        if self._count==0:
            res=True
        else:
            res=False
        return res

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        if self._rear is None and self._count!=0:
            res=True
        else:
            res=False
        return res

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """


            
            
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        new_node=_Queue_Node(deepcopy(value),None)
        if self._front is None:
            self._front=new_node
            self._rear=new_node
            self._count+=1
        else:
            self._rear._next=new_node
            self._rear=new_node
            self._count+=1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"
        value=self._front._value
        self._front=self._front._next
        self._count-=1
        if self._front is None:
            self._rear=None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        value=deepcopy(self._front._value)
        return value

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
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
        assert source._front is not None, "Cannot append an empty queue"
        if self._rear is not None:
            self._rear._next=source._front
        else:
            self._front=source._front
        self._rear=source._rear
        self._count=self._count+source._count
        source._front=None
        source._rear=None
        source._count=0
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while not (source1._front is None and source2._front is None):
            if source1._front is not None:
                if self._rear is not None:
                    self._rear._next=source1._front
                self._rear=source1._front
                if self._front is None:
                    self._front=self._rear
                source1._front=source1._front._next
                self._rear._next=None
                self._count+=1
                source1._count-=1
            if source2._front is not None:
                if self._rear is not None:
                    self._rear._next=source2._front
                self._rear=source2._front
                if self._front is None:
                    self._front=self._rear
                source2._front=source2._front._next
                self._rear._next=None
                self._count+=1
                source2._count-=1
        source1._rear=None
        source2._rear=None
        
        return
    
    def rotate(self,k):
        ind=k
        if ind>0:
            prev=None
            curr=self._front
            for i in range(len(self)-ind):
                prev=curr
                curr=curr._next
            
            prev._next=None
            
           
            self._rear._next=self._front
            self._front=curr
            self._rear=prev
            
        if ind<0:
            ind=-1*ind
            prev=None
            curr=self._front
            for i in range(ind):
                prev=curr
                curr=curr._next
            prev._next=None
            self._rear._next=self._front
            self._front=curr
            self._rear=prev
                    
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1=Queue()
        target2=Queue()
        while self._front is not None:
            if target1._rear is not None:
                target1._rear._next=self._front
            target1._rear=self._front
            if target1._front is None:
                target1._front=target1._rear
            self._front=self._front._next
            target1._rear._next=None
            target1._count+=1
            self._count-=1
            
            if self._front is not None:
                if target2._rear is not None:
                    target2._rear._next=self._front
                    """always first check for the relation between nodes then change the nodes"""               
                target2._rear=self._front
                if target2._front is None:
                    target2._front=target2._rear
                self._front=self._front._next
                target2._rear._next=None
                target2._count+=1
                self._count-=1
                
                
        self._rear=None
            
        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
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
        -------------------------------------------------------
        """
        equals=True
        if self._count==target._count:
            curr_self=self._front
            curr_target=target._front
            while curr_self is not None:
                if curr_self._value!=curr_target._value:
                    equals=False
                curr_self=curr_self._next
                curr_target=curr_target._next
        else:
            equals=False
        return equals

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
    def prq(self):
        """
        ------------------------------------------------
        prints values of a queue
        Use: que.prq()
        ----------------
        returns:
            None
        ------------------------------------------------
        """
        curr=self._front
        while curr is not None:
            print(curr._value)
            curr=curr._next