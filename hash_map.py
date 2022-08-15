# Author: Jacob Schiemenz

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
# Creates new node and inserts it at front of linked list. Args: key and value for node. 
    def add_front(self, key, value):
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

# Removes node from linked list. Args: key of node to remove
    def remove(self, key):
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False
# Searches linked list for node with a given key. Args: key of node. 
    def contains(self, key):
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out

def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash

def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

# Creates a new hash map with specified number of buckets
# Args: 
#       capacity: total number of buckets to be created in table 
#       function: which hash function (function 1 or 2) to use for hashing values.
class HashMap:
    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

# Empties buckets, appends new Linked List, and resets size.
    def clear(self):    
        self._buckets=[]
        for i in range(self.capacity):
            self._buckets.append(LinkedList())
        self.size=0
# Returns the value with a given key. Args: key, the value of the key to look for
    def get(self, key):
        hash_key = self._hash_function(key)%self.capacity
        x = self._buckets[hash_key].contains(key)
        try:
            return x.value
        except AttributeError:
            return None
# Resizes hash table to have a number of buckets equal to the give capacity
    def resize_table(self, capacity):
        #create new list
        new_data=[]
        temp=self._buckets
        self.capacity=capacity
        self.clear()
        #hash_key = self._hash_function(key) % self.capacity
        for i in range(capacity):
            new_data.append(LinkedList())
        for j in temp:
            if j.head!=None:
                while j.head is not None:
                    self.put(j.head.key,j.head.value)
                    #self._buckets[hash_key].add_front(j.head.key, j.head.value)
                    j.head=j.head.next

# Updates given key-value pair in the hash table. 
    def put(self, key, value):
        hash_key = self._hash_function(key)%self.capacity
        if self.contains_key(key)==True:
            while self._buckets[hash_key].head.key!=key:
                self._buckets[hash_key].head=self._buckets[hash_key].head.next
            self._buckets[hash_key].head.value=value
        else:
            (self._buckets[hash_key]).add_front(key,value)
            self.size+=1
        return

# Removes and freens the link with the given key from the table.
    def remove(self, key):
        if self.contains_key(key)==True:
            hash_key = self._hash_function(key)%self.capacity
            (self._buckets[hash_key]).remove(key)
            self.size=self.size-1
        else:
            return False

# Searches to see if a key exists within the hash table
    def contains_key(self, key):
        hash_key = self._hash_function(key)%self.capacity
        try:
            x = self._buckets[hash_key].contains(key)
            if x is not None:
                return True
            else:
                return False
        except IndexError:
            return False
# Returns number of empty buckets in the table
    def empty_buckets(self):
        
        count=0
        for i in self._buckets:
            if i.head==None:
                count=count+1
        return count
# Returns the ratio of number of links / number of buckets as a float
    def table_load(self):
        return float(self.size/self.capacity)

# Prints all the links in each of the buckets in the table
    def __str__(self):
        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out
