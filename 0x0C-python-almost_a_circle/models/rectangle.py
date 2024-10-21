#!/usr/bin/python3
# models/rectangle.py

"""Module for the Rectangle class.

This module defines the Rectangle class, which inherits from the Base class
and encapsulates the properties of a rectangle, including width, height,
and position (x, y).
"""

from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                Defaults to 0.
            id (int, optional): The id of the rectangle. If None, it is
                assigned automatically.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Getter for height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """Getter for x.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x.

        Args:
            value (int): The new x-coordinate of the rectangle's position.

        Raises:
            ValueError: If value is not a non-negative integer.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("x must be a non-negative integer")
        self.__x = value

    @property
    def y(self):
        """Getter for y.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y.

        Args:
            value (int): The new y-coordinate of the rectangle's position.

        Raises:
            ValueError: If value is not a non-negative integer.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("y must be a non-negative integer")
        self.__y = value
