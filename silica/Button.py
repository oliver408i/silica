from Cocoa import NSButton, NSMakeRect, NSFont, NSMutableAttributedString, NSTrackingArea, NSTrackingMouseEnteredAndExited, NSTrackingActiveAlways, NSColor, NSButtonTypeSwitch, NSButtonTypeRadio, NSControlStateValueOn, NSControlStateValueOff
from .Widget import Widget

class Button(Widget):
    def __init__(self, text: str="Button", width: int=100, height: int=30, command: callable=None, useFrame: bool=True, noTracking: bool=False):
        super().__init__(width, height)
        if (useFrame):
            frame = NSMakeRect(0, 0, width, height)
            self.widget = NSButton.alloc().initWithFrame_(frame)
        else:
            self.widget = NSButton.alloc().init()
            self.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)
        self.widget.setTitle_(text)

        if command:
            self.set_action(command)
        
        if not noTracking:

            # Add a tracking area to detect mouse hover events on the button itself
            self.add_tracking_area()

        # Background color properties for hover and click effects
        self.default_background_color = NSColor.whiteColor()
        self.hover_background_color = NSColor.lightGrayColor()
        self.click_background_color = NSColor.darkGrayColor()

        # Set the initial background color
        self.__update_background_color(self.default_background_color)
    
    def make_checkbox(self) -> None:
        """Make the button a checkbox."""
        self.widget.setButtonType_(NSButtonTypeSwitch)
    
    def make_radio_button(self) -> None:
        """Make the button a radio button."""
        self.widget.setButtonType_(NSButtonTypeRadio)
    
    def get_button_checked(self) -> bool:
        """Get the checked state of the button. Only for checkbox and radio buttons."""
        return self.widget.state() == NSControlStateValueOn
    
    def update_text(self, text: str) -> None:
        """Update the text of the button."""
        self.widget.setTitle_(text)

    def add_tracking_area(self) -> None:
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
    def set_no_bezel(self) -> None:
        """Remove the default bezel from the button."""
        self.widget.setBordered_(False)  # Disables the border or bezel

    def set_corner_radius(self, radius: float) -> None:
        """Set the corner radius to give the button a rounded look."""
        self.widget.setWantsLayer_(True)  # Enable the use of layers for the button
        self.widget.layer().setCornerRadius_(radius)

    def set_action(self, command: callable) -> None:
        """Set the action for the button."""
        self.widget.setTarget_(self)
        self.widget.setAction_("buttonClicked:")
        self._command = command

    def buttonClicked_(self, sender):
        """Handle button click. Internal only"""
        if self._command:
            self._command()

    def set_font(self, font_name: str="Helvetica", font_size: int=14) -> None:
        """Set the font and font size for the button text."""
        font = NSFont.fontWithName_size_(font_name, font_size)
        self.widget.setFont_(font)

    def set_background_color(self, color: NSColor) -> None:
        """Set the background color for the button."""
        self.default_background_color = color
        self.__update_background_color(self.default_background_color)
    
    def __update_background_color(self, color: NSColor) -> None:
        self.widget.setWantsLayer_(True)  # Enable layer to change background
        self.widget.layer().setBackgroundColor_(color.CGColor())


    def set_text_color(self, color : NSColor) -> None:
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

    def set_bezel_style(self, style) -> None:
        """Set the bezel style of the button."""
        self.widget.setBezelStyle_(style)
    
    def mouseEntered_(self, event):
        """Change the button appearance when the mouse hovers over it. Internal only."""
        self._update_background_color(self.hover_background_color)

    def mouseExited_(self, event):
        """Revert to the default appearance when the mouse leaves the button. Internal only."""
        self._update_background_color(self.default_background_color)

    def mouseDown_(self, event):
        """Handle mouse down event (button click). Internal only."""
        self._update_background_color(self.click_background_color)
        super(Button, self).mouseDown_(event)

    def mouseUp_(self, event):
        """Handle mouse up event (revert to hover or default state). Internal only."""
        self._update_background_color(self.hover_background_color if self.isMouseOver() else self.default_background_color)
        super(Button, self).mouseUp_(event)

    def isMouseOver(self):
        """Determine if the mouse is currently hovering over the button."""
        # Simple logic to detect whether mouse is over the button
        return self.widget.window().mouseLocationOutsideOfEventStream().x > self.widget.frame().origin.x and \
               self.widget.window().mouseLocationOutsideOfEventStream().y > self.widget.frame().origin.y