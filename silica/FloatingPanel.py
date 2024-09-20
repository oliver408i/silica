from Cocoa import NSPanel, NSWindowStyleMaskBorderless, NSNonactivatingPanelMask, NSBackingStoreBuffered, NSFloatingWindowLevel, NSColor, NSApp
from .Widget import Widget

class CustomPanel(NSPanel):
    # Allow the panel to become the key window to capture input
    def canBecomeKeyWindow(self):
        return False

    # Optional: prevent it from becoming the main window, if desired
    def canBecomeMainWindow(self):
        return False


class FloatingPanel:
    def __init__(self, width=400, height=100, ignoreMouseEvents=True, alpha=0.8, nonActivating=True):
        self.panel = CustomPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            ((300, 300), (width, height)),  # Window position and size
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

    def show(self):
        """Show the panel. (bring it to the front)"""
        self.panel.orderFront_(None)
    
    def close(self):
        """Close the panel"""
        self.panel.close()