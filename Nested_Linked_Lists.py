# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 10:12:07 2021

@author: manik
"""

class Node:
    def __init__(self,value):
        self.value= value
        self.next= None
        
    def __repr__(self):
        return str(self.value)

class LinkedList:
    
    def __init__(self,head):
        self.head= head
    
    def append(self, value):
        if self.head is None:
            self.head= Node(value)
            return self.head
        node= self.head
        while node.next:
            node= node.next
        node.next= Node(value)
        
    
    def to_list(self):
        output_list=[]
        if self.head == None:
            return []
        node= self.head
        while node:
            output_list.append(int(node.value))
            node= node.next
        return output_list
        

def merge(list1, list2):
    
    if list1 is None:
        return list2
    if list2 is None:
        return list1 
    node_1= list1.head
    node_2= list2.head
    new_list= LinkedList(None)
    
    while node_1 is not None or node_2 is not None:
        if node_1 is None:
            new_list.append(node_2.value)
            node_2= node_2.next
        elif node_2 is None:
            new_list.append(node_1.value)
            node_1= node_1.next
        elif node_1.value < node_2.value:
            new_list.append(node_1.value)
            node_1= node_1.next
        else:
            new_list.append(node_2.value)
            node_2= node_2.next
    
    new_node= new_list.head
    while new_node:
        #print(new_node.value)
        new_node= new_node.next
    return new_list
    
        
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head) 

    '''  A recursive function ''' 
    def _flatten(self, node):
        
        # A termination condition
        if node.next is None:
            return merge(node.value, None) 
        
        return merge(node.value, self._flatten(node.next))
  
        
        
    
linked_list= LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list= LinkedList(Node(2))
second_linked_list.append(4)

merged_list= merge(linked_list,second_linked_list)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    print(node.value)
    node = node.next