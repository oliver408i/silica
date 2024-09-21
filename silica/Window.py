from Cocoa import NSWindow, NSApplication, NSApp, NSMakeRect, NSBackingStoreBuffered, NSObject, NSWindowStyleMaskFullScreen
from PyObjCTools import AppHelper
from .Widget import Widget

class WindowDelegate(NSObject):
    def windowWillClose_(self, notification):
        NSApp.terminate_(self)

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
    
    def close(self):
        """Close window and quit the app"""
        self.window.close()
    