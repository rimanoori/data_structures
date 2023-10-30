"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Amirhossein Ahmadinoori
ID:      169042860
Email:   ahma2860@mylaurier.ca
__updated__ = "2023-07-20"
-------------------------------------------------------
"""
"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
# Use any appropriate data structure here.
from BST_linked import BST
from copy import deepcopy

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(BST())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        slot=self._table[hash(key)%self._capacity]
        
        return slot


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        slot=self._find_slot(key)
        
        return key in slot


    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        x=hash(value)%self._capacity
        
        
        if value in self._table[x]:
            if len(self._table[x])<self._LOAD_FACTOR:
                self._table[x].insert(deepcopy(value))
                self._count+=1
            else:
                self._rehash()
                x=hash(value)%self._capacity
                self._table[x].insert(deepcopy(value))
                self._count+=1
            inserted=True
        else:
            inserted=False
        return inserted


    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        value = None
        
        if key in self._table[hash(key)%self._capacity]:
            for _ in self._table[hash(key)%self._capacity]:
                if _==key:
                    value=deepcopy(_) 
        
        return value

        
    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        value=None
        
        slot=self._find_slot(key)
        if slot._linear_search(key)!=-1:
            value=slot.pop(slot._linear_search(key))
        return value

    def rehash(self):
        self._rehash()
        return
    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        temp_table=self._table
        self._table=[]
        for i in range (self._capacity*2+1):
            self._table.append(BST())
        self._capacity=self._capacity*2+1
        while len(temp_table)!=0:
            a=temp_table.pop(0)
            
            while not a.is_empty():
                
                if len(a)!=0:
                    val=a.remove(a._root)
                    k=hash(val)
                    n_slot=k%self._capacity
                    self._table[n_slot].insert(val)
                    
            


        # o_cap=self._capacity
        # n_cap=2*self._capacity+1
        # self._capacity=n_cap
        # n=self._capacity+1
        # for q in range(n):
        #     self._table.append(List())
        #
        #
        #
        #
        # s=0
        # m=0
        # while s<n_cap:
        #     while m<len(self._table[s]):
        #         h=hash(self._table[s][m])
        #         n_slot=h%n_cap
        #         self._table[n_slot].append(self._table[s][m])
        #         self._table[s].pop(m)
        #         if s!=n_slot:
        #             m+=1
        #
        #
        #     m=0   
        # s+=1
        
            
          
            
        return


    def __eq__(self, target):
        """
        ----------------
        Determines whether two Hash_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a hash set (Hash_Set)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        equals=True
        res=True
        if len(self._table)==len(self._table):
            for i in range(len(self._table)):
                if self._table[i]!=target._table[i]:
                    equals=False
                    res=False
        
                else:
                    equals=True
        
        else:
            equals=False

                                
        if res==False:
            equals=False   
        return equals


    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        print(f"""{self._capacity} slots 
        
        ========================================""")
        for i in range(self._capacity):
            print(f"Slot {i}")
            
            for i in self._table[i]:
                print(i)
        
        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item

