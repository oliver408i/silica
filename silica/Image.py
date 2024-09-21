from Cocoa import NSImageView, NSImage, NSMakeRect
from .Widget import Widget
import warnings

class Image(Widget):
    def __init__(self, width, height, image_path):
        """
        Initialize the Image widget with a specified width, height, and image path.
        """
        super().__init__(width, height)  # Call the parent class's initializer
        self.image_path = image_path

        # Create an NSImageView instance for displaying the image
        self.widget = NSImageView.alloc().initWithFrame_(NSMakeRect(0, 0, width, height))

        # Load the image from the file path
        image = NSImage.alloc().initWithContentsOfFile_(image_path)

        if image:
            # Set the image for the NSImageView
            self.widget.setImage_(image)
        else:
            warnings.warn(f"Error: Could not load image from {image_path}")