from Cocoa import NSImageView, NSImage, NSMakeRect
from .Widget import Widget
import warnings

class Image(Widget):
    def __init__(self, width: int, height: int, image_path: str, useFrame: bool=True):
        """
        Initialize the Image widget with a specified width, height, and image path.
        """
        super().__init__(width, height)  # Call the parent class's initializer
        self.image_path = image_path

        if (useFrame):
            # Create an NSImageView instance for displaying the image
            self.widget = NSImageView.alloc().initWithFrame_(NSMakeRect(0, 0, width, height))
        else:
            self.widget = NSImageView.alloc().init()
            self.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)

        # Load the image from the file path
        image = NSImage.alloc().initWithContentsOfFile_(image_path)

        if image:
            # Set the image for the NSImageView
            self.widget.setImage_(image)
        else:
            warnings.warn(f"Error: Could not load image from {image_path}")