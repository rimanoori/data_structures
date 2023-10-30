"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-03-13"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy



class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                print("node has no children")
                node=None
                # your code here

            elif node._left is None:
                # node has no left child.
                node=node._right
                # your code here
                print("node has no left child")

            elif node._right is None:
                # node has no right child.
                node=node._left
                # your code here
                print("node has no right child")
            else:
                # Node has two children
                
                if node._left._right is None:
                    repl_node=node._left
                else:
                    repl_node=self._delete_node_left(node._left)
                    repl_node._left=node._left
                
                repl_node._right=node._right
                node=repl_node
                # if repl_node._left is None:
                #
                #     repl_node=None
                #     print("repl node found")
                # else:
                #     repl_node._left=self._delete_node_left(repl_node._left)
                #     repl_node._right=node._right
                #     repl_node._left=node._left
                #     node=repl_node
                #     ####
                #     node._left=repl_node._left
                #     node=repl_node
                #     repl_node=repl_node._left
                #     print("general case")
                # # your code here

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        child=parent._right
        if child._right is None:
            repl_node=child
            parent._right=child._left
            
        else:
            repl_node=self._delete_node_left(child)
        parent._update_height()
        #
        # if parent._right is None:
        #     repl_node=parent
        # else:
        #     repl_node=self._delete_node_left(parent._right)
            
            
        
        

        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        if self._root is None:
            res=False
        else:
            res=self.contain_aux(key,self._root)
        return res
    
    
    def contain_aux(self,key,node):
        res=False
        if node:
            if node._value==key:
                res=True
            else:
                if node._left and res==False:
                    res=self.contain_aux(key,node._left)
                if node._right and res==False:
                    res=self.contain_aux(key,node._right)

        return res
    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """

        return self._root._height


    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals=True
        if self._count!=target._count:
            equals=False
        else:
            
            equals=self.eq_traverse(self._root, target._root)

        

        return equals
    def eq_traverse(self,current,target):
        res=True
        if current is not None and target is not None:
            if current._value==target._value:
                
                res=self.eq_traverse(current._left,target._left) and self.eq_traverse(current._right,target._right)
            else:
                res=False
        elif target!=current:
            res=False
            
            
                
        return res
    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"


        if self._root._height==1:
            value=None
        else:
            value=self._parent_aux(key,self._root)
        return value
    def _parent_aux(self,key,node):
        value=None
        if node:
            if not (node._left is None and node._right is None):
                if node._left:
                    if node._left._value==key:
                        value=node._value
                if node._right and value is None:
                    if node._right._value==key:
                        value=node._value
                if value is None:
                    value=self._parent_aux(key,node._left)
                if value is None:
                    value=self._parent_aux(key,node._right)
                    
        return value


    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # Find the node containing the key.
        node = self._root
        parent = None
        found = False

        while node is not None and found is False:

            if key < node._value:
                parent = node
                node = node._left
            elif key > node._value:
                parent = node
                node = node._right
            else:
                found = True

        if parent is None or not found:
            value = None
        else:
            value = deepcopy(parent._value)
        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        node=self._root
        value=self._root._value
        while node is not None:
            if node._right:
                value=node._right._value
            node=node._right
        return value


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"


        if self._root._height==1:
            value=self._root._value
        else:
            value=self._max_aux(self._root)
        return value

    def _max_aux(self,node):
        if node:
            value=node._value
            if node._right:
                value=self._max_aux(node._right)
        return value
            
    def min_r(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Recursive algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        if self._count==1:
            value=self._root._value

        else:
            value=self._min_aux(self._root)
        return value
        
    def _min_aux(self,root):
        if root._left is None:
            value=root._value
        else:
            value=self._min_aux(root._left)
        return value


    def min(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Iterative algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        value=None
        node=self._root
        prev=None
        while node is not None:
            prev=node
            node=node._left
        value=deepcopy(prev._value)
        return value


    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        if self._root is None:
            count=0
        if self._count==1:
            count=1
        else:
            count=self._leaf_count(self._root)
            
        return count

    def _leaf_count(self,root):
        count=0
        if root is not None:
            if root._height==1:
                count+=1
            else:
                count=self._leaf_count(root._left)+self._leaf_count(root._right)
        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        if self._root is None or self._count==1:
            count=0
        else:
            count=self._two_child_count(self._root)
            
            
        return count
        
    def _two_child_count(self,root):
        count=0
        if root is not None:
            
            if root._left is not None and root._right is not None:
                count+=1
                count=count+self._two_child_count(root._left)+self._two_child_count(root._right)
            if root._left is None:
                count=self._two_child_count(root._right)
            if root._right is  None:
                count=self._two_child_count(root._left)
                    
                    #count=self._two_child_count(root._left)+self._two_child_count(root._right)
            

        return count
    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        if self._root is None or self._count==1:
            count=0
        else:
            count=self._one_child_count(self._root)
        return count
        # your code here
    def _one_child_count(self,root):
        count=0
        if root is not None:
            if root._left is None and root._right is not None:
                count+=1
                count=count+self._one_child_count(root._right)
            elif root._left is not None and root._right is None:
                count+=1
                count=count+self._one_child_count(root._left)
            elif root._left is not None:
                count= self._one_child_count(root._right)+self._one_child_count(root._left)
            
            
            
            # if root._height==2:
            #     if root._left is None and root._right is not None:
            #         count+=1
            #     if root._left is not None and root._right is None:
            #         count+=1
            #     #if root._left is not None and root._right is not None:
            #         # if root._left._left is not None:
            #         #     count+=1
            # if root._height>=3:
            #     count=self._one_child_count(root._left)+self._one_child_count(root._right)
        return count
    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        # assert self._root is not None, "tree cannot be empty"

        zero, one, two = self._node_counts_aux(self._root)
        return zero, one, two

    def _node_counts_aux(self,node):
        zero=0
        one=0
        two=0
        if node:
            if node._left and node._right:
                two=two+1
            if node._left is None and node._right is not None:
                one=one+1
            if node._right is None and node._left is not None:
                one=one+1
            if node._left is None and node._right is None:
                zero=zero+1
            if node._left:
                a,b,c=self._node_counts_aux(node._left)
                zero+=a
                one+=b
                two+=c
            if node._right:
                a,b,c=self._node_counts_aux(node._right)
                zero+=a
                one+=b
                two+=c
        return zero,one,two
    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        
        res=True
        if self._count!=0:  
            if self._root._height>=3:
                res=self.leftright_height(self._root)
        else:
            res=True
        return res
    def leftright_height(self,root):
        res=True
        if root._height ==3:
            if root._left is None:
                res=False
            elif root._right is None:
                res=False
        else:
            if root._left is None:
                res=False     
            if root._right is None:
                res=False   
            # if root._left is not None and root._right is not None:
            #     t=root._left._height-root._right._height
            #     if t>=2 or t<=2:
            #         res=False
            # if root._left is None:
            #     t=root._right._height
            #     if t>=2:
            #         res=False
            # if root._right is None:
            #     t=root._left._height
            #     if t>=2:
            #         res=False
        
        if self._node_height(root)>=4: 
            t=self._node_height(root._left)-self._node_height(root._right)
            res= t>=-1 and t<=1
            if res==True: 
                res=root.leftright_height(root._left) and root.leftright_height(root._right)
        return res
            
    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """
        assert self._root is not None,"tree cannot be empty"
        
        value=self._retrieve_r_aux(key,self._root)
        return value

    def _retrieve_r_aux(self,key,node):
        value=None
        if node:
            if node._value==key:
                value=node._value
            if key>node._value:
                if node._right:
                    value=self._retrieve_r_aux(key,node._right)
            if key<node._value:
                if node._left:
                    value=self._retrieve_r_aux(key,node._left)
        return value

        


    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if self._count!=0:
            valid=self._is_valid(self._root)
        else:
            valid=True
        
        return valid

    def _is_valid(self,node):
        res=True
        if node:
            if node._left is None or node._right is None :
                if node._left:
                    # res=res and self._postorder_aux(node._left)
                    res= res and node._left._value<node._value
                    res= res and node._height==1+node._left._height
                if node._right:
                    # a=a+self._postorder_aux(node._right)
                    res=res and node._right._value>node._value
                    res= res and node._height==1+node._right._height
                else:
                    res=res and node._height==1
            
            elif node._left is not None and node._right is not None:
                res=res and node._left._value<node._value
                res=res and node._right._value>node._value
                res=res and node._height==max(node._left._height,node._right._height)+1
            
            res=res and self._is_valid(node._left)
            res=res and self._is_valid(node._right)
            
            # a=a+[node._value]
        return res
        
    def update(self, value, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Iterative algorithm.)
        --------------------------------------------------------- -
        """
        assert self._root is not None,"tree cannot be empty."
        found=False
        node=self._root
        while node and not found:
            if value>node._value:
                node=node._right
            if value<node._value:
                node=node._left
            if value==node._value:
                found=True
        if found:
            node._value = update(node._value)
            updated=True
        if node is None:
            n_val=value.update()
            self.insert(n_val)
            updated=False
        return updated
    def update_r(self, key, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Recursive algorithm.)
        --------------------------------------------------------- -
        """

        # your code here


    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        if self._count==0:
            a=[]
        else:
            a=self._inorder_aux(self._root)
        
        
        return a
    def _inorder_aux(self,node):
        a=[]
        if node :
            if node._left:
                a=a+self._inorder_aux(node._left)
            a=a+[node._value]
            if node._right:
                a=a+self._inorder_aux(node._right)
            
            # if node._left is not None:
            #     if node._left._left is None:
            #         a.append(node._left._value)
            #         a.append(node._value)
            #         node=node._right
            #     else:
            #         a=self._inorder_aux(node._left)
            
        return  a     
                
                
                    
                    
        
    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        if self._count==0:
            a=[]
        else:
            a=self._preorder_aux(self._root)
        return a
    
    def _preorder_aux(self,node):
        a=[]
        if node:
            a=a+[node._value]
            if node._left:
                a=a+self._preorder_aux(node._left)
            if node._right:
                a=a+self._preorder_aux(node._right)
        return a
            
        
        
        
        
    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        if self._count==0:
            a=[]
        else:
            a=self._postorder_aux(self._root)
        return a
        
    def _postorder_aux(self,node):
        
        a=[]
        if node:
            
            if node._left:
                a=a+self._postorder_aux(node._left)
            if node._right:
                a=a+self._postorder_aux(node._right)
            a=a+[node._value]
        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        if self._count==0:
            a=[]
        else:
            b=[]
            a=[]
            h=self._root._height
            for i in range(1,h+1):
                a=a+self._levelorder_aux(self._root,i)
            
                
        return a
       
    def _levelorder_aux(self,node,i):
        a=[]
        if node:
            if i==1:
                a=a+[node._value]
            elif i>1:
               
                a=a+self._levelorder_aux(node._left,i-1)
                a=a+self._levelorder_aux(node._right,i-1)
                
            
        
        
        return a
            

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        if self._root is None:
            number=0
        else:
            number=self._count_aux(self._root)
        return number
    def _count_aux(self,node):
        number=0
        if node:
            number=number+1
            if node._left:
                number=number+self._count_aux(node._left)
            if node._right:
                number=number+self._count_aux(node._right)
        return number


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
                    
