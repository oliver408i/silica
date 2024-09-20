from Cocoa import NSTextField, NSMakeRect
from .Widget import Widget

class Label(Widget):
    def __init__(self, text="Label", width=200, height=20):
        # Initialize the parent Widget with the specified width and height
        super().__init__(width, height)
        # Create the label widget
        frame = NSMakeRect(0, 0, width, height)  # Initially set to (0, 0)
        self.widget = NSTextField.alloc().initWithFrame_(frame)
        self.widget.setStringValue_(text)
        self.widget.setEditable_(False)
        self.widget.setBezeled_(False)
        self.widget.setDrawsBackground_(False)