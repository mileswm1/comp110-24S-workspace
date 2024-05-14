"""Utility functions for working with Linked Lists."""
 
from __future__ import annotations
 
__author__ = "730323164"
 
 
class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
 
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        return self.next
    
    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        while self.next is not None:
            self = self.next
        return self.data
    

def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node stored at the given index, or raise an IndexError if the index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.data
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum data value in the linked list. If the linked list is empty, raise a ValueError."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.data
    tail_max = max(head.next)
    return head.data if head.data > tail_max else tail_max


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values, in the same order, as the input list."""
    if not items:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    if head is None:
        return None
    return Node(head.data * factor, scale(head.next, factor))