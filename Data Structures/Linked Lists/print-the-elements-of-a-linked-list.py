#!/bin/python3
# Complete the printLinkedList function below.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def printLinkedList(head):
    node = head
    while node != None:
        print(node.data)
        node = node.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
