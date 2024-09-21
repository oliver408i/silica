from Cocoa import NSWindow, NSApplication, NSApp, NSMakeRect, NSBackingStoreBuffered, NSObject, NSWindowStyleMaskFullScreen
from PyObjCTools import AppHelper
import objc
from .Widget import Widget

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
    def __init__(self, title="Window", width=400, height=300, x=100, y=100):
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

    def add_widget(self, widget: Widget):
        """Add a widget (Button, Label, etc.) to the window."""
        self.window.contentView().addSubview_(widget.widget)
    
    def move_to(self, x, y):
        """Move the window to a new position."""
        self.window.setFrameOrigin_((x, y))
    
    def set_size(self, width, height):
        """Set the size of the window."""
        self.window.setContentSize_((width, height))
    
    def minimize(self):
        """Minimize the window."""
        self.window.miniaturize_(None)
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        self.window.toggleFullScreen_(None)
    
    def get_location(self):
        """Return the current location (x, y) of the window."""
        return self.window.frame().origin.x, self.window.frame().origin.y
    
    def get_size(self):
        """Return the current size (width, height) of the window."""
        return self.window.frame().size.width, self.window.frame().size.height

    def is_fullscreen(self):
        """Return True if the window is in fullscreen mode, False otherwise."""
        return (self.window.styleMask() & NSWindowStyleMaskFullScreen) != 0
    
    def get_screen(self):
        """Return the screen that the window is on."""
        return self.window.screen()
    
    def close(self):
        """Close window and quit the app"""
        self.window.close()
    
    def on_resize(self, handler):
        """Set a handler to be called when the window is resized."""
        self.delegate.on_resize_handler = handler

    def on_move(self, handler):
        """Set a handler to be called when the window is moved."""
        self.delegate.on_move_handler = handler