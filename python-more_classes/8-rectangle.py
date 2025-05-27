class Rectangle:
    """
    Defines a rectangle with width and height.
    Tracks number of instances and allows custom print symbol.
    """

    # Public class attributes
    number_of_instances = 0  # Tracks number of Rectangle instances
    print_symbol = "#"       # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        Increments the instance counter.
        """
        self.width = width    # Set width via property setter 
        self.height = height  # Set height via property setter 
        Rectangle.number_of_instances += 1  # Increment class counter

    # Private instance attributes
    # We use __width and __height to make them private

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        Raises TypeError if not int, ValueError if < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Raises TypeError if not int, ValueError if < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the string representation for print().
        Uses print_symbol for drawing.
        Returns empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        # Use str(self.print_symbol) to support any type
        row = str(self.print_symbol) * self.width
        return "\n".join([row for _ in range(self.height)])

    def __repr__(self):
        """
        Return a string that can recreate the Rectangle using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called when instance is deleted.
        Decrements instance counter and prints message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.
        If equal, return rect_1.
        Raises TypeError if inputs are not Rectangle instances.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
