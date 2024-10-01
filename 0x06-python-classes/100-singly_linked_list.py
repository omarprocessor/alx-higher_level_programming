#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class.
"""


class Node:
    """
    A class that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node with given data and next_node.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the linked list.
            Default is None.

        Raises:
            TypeError: If data is not an integer or if next_node
            is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node with validation.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node.

        Returns:
            Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node with validation.

        Args:
            value (Node): The next node value to set.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        String representation of the singly linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value for the new Node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
