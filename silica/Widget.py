from Cocoa import NSMakeRect

class Widget:
    def __init__(self, width, height):
        """Initialize the widget with a specified width and height."""
        self.width = width
        self.height = height
        self.widget = None  # This will be set by child classes

    def set_center_at(self, x, y):
        """
        Set the position of the widget so that (x, y) is the center of the widget.
        """
        # Calculate the top-left corner coordinates to make (x, y) the center
        new_x = x - (self.width / 2)
        new_y = y - (self.height / 2)
        self.widget.setFrameOrigin_((new_x, new_y))

    def set_position(self, x, y):
        """Set the widget's position manually with the top-left corner at (x, y)."""
        self.widget.setFrameOrigin_((x, y))