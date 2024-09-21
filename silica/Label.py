from Cocoa import NSTextField, NSMakeRect, NSFont, NSColor, NSMutableAttributedString
from .Widget import Widget

class Label(Widget):
    def __init__(self, text: str="Label", width: int=200, height: int=20, useFrame: bool=True):
        """Initialize the Label widget."""
        super().__init__(width, height)
        if (useFrame):
            frame = NSMakeRect(0, 0, width, height)
            self.widget = NSTextField.alloc().initWithFrame_(frame)
        else:
            self.widget = NSTextField.alloc().init()
            self.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)
        
        self.widget.setStringValue_(text)
        self.widget.setEditable_(False)
        self.widget.setBezeled_(False)
        self.widget.setDrawsBackground_(False)

    def set_font(self, font_name: str="Helvetica", font_size: int=14) -> None:
        """Set the font and font size for the label."""
        font = NSFont.fontWithName_size_(font_name, font_size)
        self.widget.setFont_(font)

    def set_text_color(self, color: NSColor) -> None:
        """Set the text color of the label."""
        self.widget.setTextColor_(color)

    def set_background_color(self, color: NSColor) -> None:
        """Set the background color for the label."""
        self.widget.setDrawsBackground_(True)
        self.widget.setBackgroundColor_(color)

    def set_text(self, text: str) -> None:
        """Set the text of the label."""
        self.widget.setStringValue_(text)