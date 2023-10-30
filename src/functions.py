"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Amirhossein Ahmadinoori
ID:      169042860
Email:   ahma2860@mylaurier.ca
__updated__ = "2023-07-10"
-------------------------------------------------------
"""
# Imports

from Word import Word
from Food import Food
# Constants

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- -------------------")
    for _ in range(len(values)):
        z=hash(values[_])
        x=hash(values[_])%slots
        y=values[_].key()
        print(f"{z} {x:4d} {y}")
    return

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    line=fv.readline()
    lis=line.split(" ")
    for i in lis:
        i=i.lower()
        if i.isalpha() and i.islower():
            w=Word(i)
            hash_set.insert(w)
    while line!="":
        line=fv.readline()
        lis=line.split(" ")
        for i in lis:
            i=i.lower()
            if i.isalpha():
                w=Word(i)
                hash_set.insert(w)
    
    return

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """ 
    for _ in hash_set._table:
        total=0
        max_word=Word("of")
        max=max_word.comparisons
        for x in _:
            total=total+x.comparisons
            if x.comparisons>max:
                max_word=x
                max=x.comparisons
    return total, max_word
            
