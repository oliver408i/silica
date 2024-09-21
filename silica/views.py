from Cocoa import NSStackView, NSMakeRect, NSUserInterfaceLayoutOrientationHorizontal, NSUserInterfaceLayoutOrientationVertical, NSStackViewGravityTop, NSStackViewGravityBottom, NSStackViewGravityLeading, NSStackViewGravityTrailing, NSStackViewGravityCenter
from .Widget import Widget
import warnings

class View(Widget):
    # Parent class for all views
    pass

class StackView(View):
    def __init__(self, width: float, height: float, x: float=0, y: float=0, orientation: str="vertical", useAutoLayout: bool=True):
        super().__init__(width, height)
        self.widget = NSStackView.alloc().initWithFrame_(NSMakeRect(x, y, width, height))

        if (not orientation in ["vertical", "horizontal"]):
            warnings.warn(f"Invalid orientation: {orientation}. Defaulting to vertical.")
            orientation = "vertical"

        if (orientation == "vertical"):
            self.widget.setOrientation_(NSUserInterfaceLayoutOrientationVertical)
        else:
            self.widget.setOrientation_(NSUserInterfaceLayoutOrientationHorizontal)
        
        if (useAutoLayout):
            self.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)


    def add_widget(self, widget: Widget, gravity="top") -> None:
        """Add a widget (Button, Label, etc.) to the stack view. Gravity can be top, bottom, left, right, or center."""
        if (not gravity in ["top", "bottom", "left", "right", "center"]):
            warnings.warn(f"Invalid gravity: {gravity}. Defaulting to top.")
            gravity = "top"

        if (gravity == "top"):
            self.widget.addView_inGravity_(widget.widget, NSStackViewGravityTop)
        elif (gravity == "bottom"):
            self.widget.addView_inGravity_(widget.widget, NSStackViewGravityBottom)
        elif (gravity == "left"):
            self.widget.addView_inGravity_(widget.widget, NSStackViewGravityLeading)
        elif (gravity == "right"):
            self.widget.addView_inGravity_(widget.widget, NSStackViewGravityTrailing)
        else:
            self.widget.addView_inGravity_(widget.widget, NSStackViewGravityCenter)
    
    def set_spacing(self, spacing: float) -> None:
        """Set the spacing between the widgets in the stack view."""
        self.widget.setSpacing_(spacing)


