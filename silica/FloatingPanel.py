from Cocoa import NSPanel, NSWindowStyleMaskBorderless, NSNonactivatingPanelMask, NSBackingStoreBuffered, NSFloatingWindowLevel, NSColor, NSApp
from .Widget import Widget

class NoKeyNoMain(NSPanel):
    def canBecomeKeyWindow(self):
        return False
    
    def canBecomeMainWindow(self):
        return False

class NoMainOnly(NSPanel):
    def canBecomeKeyWindow(self):
        return True

    def canBecomeMainWindow(self):
        return False

class FloatingPanel:
    def __init__(self, width=400, height=100, x=300, y=300,ignoreMouseEvents=True, alpha=0.8, nonActivating=True, canBeKeyWindow=True):
        if canBeKeyWindow:
            CustomPanel = NoMainOnly
        else:
            CustomPanel = NoKeyNoMain
        self.panel = CustomPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            ((x, y), (width, height)),  # Window position and size
            NSWindowStyleMaskBorderless | (NSNonactivatingPanelMask if nonActivating else 0),  # Non-activating, borderless
            NSBackingStoreBuffered, False
        )

        # Set the panel properties
        self.panel.setBackgroundColor_(NSColor.clearColor())  # Transparent background
        self.panel.setOpaque_(False)  # Make it non-opaque (i.e., transparent)
        self.panel.setLevel_(NSFloatingWindowLevel)  # Always on top
        if ignoreMouseEvents:
            self.panel.setIgnoresMouseEvents_(True)  # Don't allow interaction
        self.panel.setAlphaValue_(alpha)  # Semi-transparent
        self.panel.setHidesOnDeactivate_(False)

        self.content_view = self.panel.contentView()
    
    def add_widget(self, widget: Widget):
        """Add a widget (Button, Label, etc.) to the window."""
        self.content_view.addSubview_(widget.widget)
    
    def move_to(self, x, y):
        """Move the panel to a new position."""
        self.panel.setFrameOrigin_((x, y))

    def set_size(self, width, height):
        """Set the size of the panel."""
        self.panel.setContentSize_((width, height))

    def show(self):
        """Show the panel. (bring it to the front)"""
        self.panel.orderFront_(None)
    
    def hide(self):
        """Hide the panel."""
        self.panel.orderOut_(None)
    
    def get_position(self):
        """Return the current position (x, y) of the panel."""
        return self.panel.frame().origin.x, self.panel.frame().origin.y

    def get_size(self):
        """Return the current size (width, height) of the panel."""
        return self.panel.frame().size.width, self.panel.frame().size.height
    
    def close(self):
        """Close the panel"""
        self.panel.close()