from Cocoa import NSTextField, NSMakeRect, NSFont, NSColor, NSMutableAttributedString
from .Widget import Widget

class Label(Widget):
    def __init__(self, text="Label", width=200, height=20):
        """Initialize the Label widget."""
        super().__init__(width, height)
        frame = NSMakeRect(0, 0, width, height)
        self.widget = NSTextField.alloc().initWithFrame_(frame)
        self.widget.setStringValue_(text)
        self.widget.setEditable_(False)
        self.widget.setBezeled_(False)
        self.widget.setDrawsBackground_(False)

    def set_font(self, font_name="Helvetica", font_size=14):
        """Set the font and font size for the label."""
        font = NSFont.fontWithName_size_(font_name, font_size)
        self.widget.setFont_(font)

    def set_text_color(self, color):
        """Set the text color of the label."""
        self.widget.setTextColor_(color)

    def set_background_color(self, color):
        """Set the background color for the label."""
        self.widget.setDrawsBackground_(True)
        self.widget.setBackgroundColor_(color)

    def set_text(self, text):
        """Set the text of the label."""
        self.widget.setStringValue_(text)