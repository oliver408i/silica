from Cocoa import NSWindow, NSApplication, NSApp, NSMakeRect, NSBackingStoreBuffered, NSObject, NSWindowStyleMaskFullScreen, NSLayoutConstraint
from PyObjCTools import AppHelper
import objc
from .Widget import Widget
from .views import View
from typing import Tuple, Callable

class WindowDelegate(NSObject):
    def init(self):
        """Proper Objective-C style init method."""
        self = objc.super(WindowDelegate, self).init()  # Correct way to initialize in PyObjC
        if self is None:
            return None
        
        self.on_resize_handler = None
        self.on_move_handler = None
        return self

    def windowWillClose_(self, notification):
        NSApp.terminate_(self)
    
    def set_window_level(self, level) -> None:
        """Set the window level to a specific value."""
        self.window.setLevel_(level)

    def windowDidResize_(self, notification):
        """Called when the window is resized."""
        if self.on_resize_handler:
            window = notification.object()
            new_size = window.frame().size
            self.on_resize_handler(new_size.width, new_size.height)

    def windowDidMove_(self, notification):
        """Called when the window is moved."""
        if self.on_move_handler:
            window = notification.object()
            new_origin = window.frame().origin
            self.on_move_handler(new_origin.x, new_origin.y)


class Window:
    def __init__(self, title: str="Window", width: float=400, height: float=300, x: float=100, y: float=100):
        """Initialize a standard window with a specified title, width, height, and position."""
        frame = NSMakeRect(x, y, width, height)
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame,
            15,  # Window style (closable, resizable, titled)
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_(title)
        self.window.makeKeyAndOrderFront_(None)
        self.delegate = WindowDelegate.alloc().init()
        self.window.setDelegate_(self.delegate)

    def add_widget(self, widget: Widget) -> None:
        """Add a widget (Button, Label, etc.) to the window."""
        self.window.contentView().addSubview_(widget.widget)
    
    def move_to(self, x: float, y: float) -> None:
        """Move the window to a new position."""
        self.window.setFrameOrigin_((x, y))
    
    def set_size(self, width: float, height: float) -> None:
        """Set the size of the window."""
        self.window.setContentSize_((width, height))
    
    def minimize(self) -> None:
        """Minimize the window."""
        self.window.miniaturize_(None)
    
    def toggle_fullscreen(self) -> None:
        """Toggle fullscreen mode."""
        self.window.toggleFullScreen_(None)
    
    def get_location(self) -> Tuple[float, float]:
        """Return the current location (x, y) of the window."""
        return self.window.frame().origin.x, self.window.frame().origin.y
    
    def get_size(self) -> Tuple[float, float]:
        """Return the current size (width, height) of the window."""
        return self.window.frame().size.width, self.window.frame().size.height

    def is_fullscreen(self) -> bool:
        """Return True if the window is in fullscreen mode, False otherwise."""
        return (self.window.styleMask() & NSWindowStyleMaskFullScreen) != 0
    
    def get_screen(self):
        """Return the objc NSScreen object representing the screen that the window is on."""
        return self.window.screen()
    
    def close(self) -> None:
        """Close window and quit the app"""
        self.window.close()
    
    def on_resize(self, handler: Callable[[float, float], None]) -> None:
        """Set a handler to be called when the window is resized."""
        self.delegate.on_resize_handler = handler
    
    def add_constraints(self, widget: Widget, marginTop=0, marginRight=0, marginBottom=0, marginLeft=0) -> None:
        """Add a constraints to the window. Only used for auto layout. Use this to add margins, for example."""
        widget.widget.setTranslatesAutoresizingMaskIntoConstraints_(False)
        NSLayoutConstraint.activateConstraints_([
            widget.widget.topAnchor().constraintEqualToAnchor_constant_(self.window.contentView().topAnchor(), marginTop),
            widget.widget.trailingAnchor().constraintEqualToAnchor_constant_(self.window.contentView().trailingAnchor(), marginRight),
            widget.widget.bottomAnchor().constraintEqualToAnchor_constant_(self.window.contentView().bottomAnchor(), marginBottom),
            widget.widget.leadingAnchor().constraintEqualToAnchor_constant_(self.window.contentView().leadingAnchor(), marginLeft)
        ])

    def on_move(self, handler: Callable[[float, float], None]) -> None:
        """Set a handler to be called when the window is moved."""
        self.delegate.on_move_handler = handler