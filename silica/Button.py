from Cocoa import NSButton, NSMakeRect, NSFont, NSMutableAttributedString, NSTrackingArea, NSTrackingMouseEnteredAndExited, NSTrackingActiveAlways, NSColor
from .Widget import Widget

class Button(Widget):
    def __init__(self, text="Button", width=100, height=30, command=None):
        super().__init__(width, height)
        frame = NSMakeRect(0, 0, width, height)
        self.widget = NSButton.alloc().initWithFrame_(frame)
        self.widget.setTitle_(text)

        if command:
            self.set_action(command)

        # Add a tracking area to detect mouse hover events on the button itself
        self.add_tracking_area()

        # Background color properties for hover and click effects
        self.default_background_color = NSColor.whiteColor()
        self.hover_background_color = NSColor.lightGrayColor()
        self.click_background_color = NSColor.darkGrayColor()

        # Set the initial background color
        self._update_background_color(self.default_background_color)

    def add_tracking_area(self):
        """Add a tracking area directly to the button to handle mouse hover events."""
        tracking_options = NSTrackingMouseEnteredAndExited | NSTrackingActiveAlways

        # The owner must be `self` so that the Button class handles the events
        self.tracking_area = NSTrackingArea.alloc().initWithRect_options_owner_userInfo_(
            self.widget.bounds(),  # Track the bounds of the button
            tracking_options,
            self,  # Ensure that the Button class is the owner of the tracking events
            None
        )
        self.widget.addTrackingArea_(self.tracking_area)
    def set_no_bezel(self):
        """Remove the default bezel from the button."""
        self.widget.setBordered_(False)  # Disables the border or bezel

    def set_corner_radius(self, radius):
        """Set the corner radius to give the button a rounded look."""
        self.widget.setWantsLayer_(True)  # Enable the use of layers for the button
        self.widget.layer().setCornerRadius_(radius)

    def set_action(self, command):
        """Set the action for the button."""
        self.widget.setTarget_(self)
        self.widget.setAction_("buttonClicked:")
        self._command = command

    def buttonClicked_(self, sender):
        """Handle button click."""
        if self._command:
            self._command()

    def set_font(self, font_name="Helvetica", font_size=14):
        """Set the font and font size for the button text."""
        font = NSFont.fontWithName_size_(font_name, font_size)
        self.widget.setFont_(font)

    def set_background_color(self, color):
        """Set the background color for the button."""
        self.default_background_color = color
        self._update_background_color(self.default_background_color)
    
    def _update_background_color(self, color):
        self.widget.setWantsLayer_(True)  # Enable layer to change background
        self.widget.layer().setBackgroundColor_(color.CGColor())


    def set_text_color(self, color):
        """Set the text color for the button."""
        # Get the button's current attributed title
        attributed_title = self.widget.attributedTitle()

        # Create a mutable copy of the attributed title
        mutable_title = NSMutableAttributedString.alloc().initWithAttributedString_(attributed_title)

        # Apply the color to the entire range of the title
        range_length = mutable_title.length()
        mutable_title.addAttribute_value_range_(
            "NSColor", color, (0, range_length)
        )

        # Set the modified title back to the button
        self.widget.setAttributedTitle_(mutable_title)

    def set_bezel_style(self, style):
        """Set the bezel style of the button."""
        self.widget.setBezelStyle_(style)
    
    def mouseEntered_(self, event):
        """Change the button appearance when the mouse hovers over it."""
        self._update_background_color(self.hover_background_color)

    def mouseExited_(self, event):
        """Revert to the default appearance when the mouse leaves the button."""
        self._update_background_color(self.default_background_color)

    def mouseDown_(self, event):
        """Handle mouse down event (button click)."""
        self._update_background_color(self.click_background_color)
        super(Button, self).mouseDown_(event)

    def mouseUp_(self, event):
        """Handle mouse up event (revert to hover or default state)."""
        self._update_background_color(self.hover_background_color if self.isMouseOver() else self.default_background_color)
        super(Button, self).mouseUp_(event)

    def isMouseOver(self):
        """Determine if the mouse is currently hovering over the button."""
        # Simple logic to detect whether mouse is over the button
        return self.widget.window().mouseLocationOutsideOfEventStream().x > self.widget.frame().origin.x and \
               self.widget.window().mouseLocationOutsideOfEventStream().y > self.widget.frame().origin.y