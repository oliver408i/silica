from Cocoa import NSTextField, NSMakeRect, NSFont, NSColor
from .Widget import Widget

class Input(Widget):
    """A widget for text input."""
    def __init__(self, width: int=200, height: int=24, placeholder: str="", useFrame: bool=True):
        super().__init__(width, height)
        if (useFrame):
            self.widget = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 0, width, height))
        else:
            self.widget = NSTextField.alloc().init()
            self.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)
        self.widget.setPlaceholderString_(placeholder)

    def get_text(self) -> str:
        """Get the current text from the input field."""
        return self.widget.stringValue()

    def set_text(self, text) -> None:
        """Set the text in the input field."""
        self.widget.setStringValue_(text)

    def set_font(self, font_name: str="Helvetica", font_size: int=14) -> None:
        """Set the font and font size for the input field."""
        font = NSFont.fontWithName_size_(font_name, font_size)
        self.widget.setFont_(font)

    def set_text_color(self, color: NSColor) -> None:
        """Set the text color of the input field."""
        self.widget.setTextColor_(color)

    def set_background_color(self, color: NSColor) -> None:
        """Set the background color of the input field."""
        self.widget.setDrawsBackground_(True)
        self.widget.setBackgroundColor_(color)

    def set_placeholder(self, placeholder: str) -> None:
        """Set the placeholder text for the input field."""
        self.widget.setPlaceholderString_(placeholder)