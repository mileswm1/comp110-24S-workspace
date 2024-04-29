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