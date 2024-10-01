import math


class MagicClass:
    """
    A class that defines a circle with methods to calculate area
    and circumference.
    """

    def __init__(self, radius=0):
        """
        Initialize the MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the circle. Default is 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
