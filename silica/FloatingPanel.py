from Cocoa import NSPanel, NSWindowStyleMaskBorderless, NSNonactivatingPanelMask, NSBackingStoreBuffered, NSFloatingWindowLevel, NSColor, NSLayoutConstraint
from .Widget import Widget
from typing import Tuple

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
    def __init__(self, width: float=400, height: float=100, x: float=300, y: float=300,ignoreMouseEvents: bool=True, alpha: float=0.8, nonActivating: bool=True, canBeKeyWindow: bool=True):
        """Initialize a floating panel window with a specified title, width, height, and position. The panel will be transparent and non-activating by default.
        
        For a detailed explanation of the parameters, see the floatingPanel reference.
        """
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
    
    def add_widget(self, widget: Widget) -> None:
        """Add a widget (Button, Label, etc.) to the window."""
        self.content_view.addSubview_(widget.widget)
    
    def move_to(self, x: float, y: float) -> None:
        """Move the panel to a new position."""
        self.panel.setFrameOrigin_((x, y))

    def set_size(self, width: float, height: float) -> None:
        """Set the size of the panel."""
        self.panel.setContentSize_((width, height))

    def show(self) -> None:
        """Show the panel. (bring it to the front)"""
        self.panel.orderFront_(None)
    
    def hide(self) -> None:
        """Hide the panel."""
        self.panel.orderOut_(None)
    
    def get_position(self) -> Tuple[float, float]:
        """Return the current position (x, y) of the panel."""
        return self.panel.frame().origin.x, self.panel.frame().origin.y

    def get_size(self) -> Tuple[float, float]:
        """Return the current size (width, height) of the panel."""
        return self.panel.frame().size.width, self.panel.frame().size.height

    def get_screen(self):
        """Return the objc NSScreen object representing the screen that the panel is on."""
        return self.panel.screen()
    
    def close(self) -> None:
        """Close the panel"""
        self.panel.close()
    
    def set_window_level(self, level) -> None:
        """Set the window level to a specific value."""
        self.panel.setLevel_(level)
    
    def add_constraints(self, widget: Widget, marginTop=0, marginRight=0, marginBottom=0, marginLeft=0) -> None:
        """Add a constraints to the panel. Only used for auto layout. Use this to add margins, for example."""
        widget.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)
        NSLayoutConstraint.activateConstraints_([
            widget.widget.topAnchor().constraintEqualToAnchor_constant_(self.content_view.topAnchor(), marginTop),
            widget.widget.trailingAnchor().constraintEqualToAnchor_constant_(self.content_view.trailingAnchor(), marginRight),
            widget.widget.bottomAnchor().constraintEqualToAnchor_constant_(self.content_view.bottomAnchor(), marginBottom),
            widget.widget.leadingAnchor().constraintEqualToAnchor_constant_(self.content_view.leadingAnchor(), marginLeft)
        ])