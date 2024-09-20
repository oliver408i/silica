from Cocoa import NSWindow, NSApplication, NSApp, NSMakeRect, NSBackingStoreBuffered, NSObject
from PyObjCTools import AppHelper
from .Widget import Widget

class WindowDelegate(NSObject):
    def windowWillClose_(self, notification):
        NSApp.terminate_(self)

class Window:
    def __init__(self, title="Window", width=400, height=300):
        frame = NSMakeRect(100.0, 100.0, width, height)
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
    
    def close(self):
        """Close window and quit the app"""
        self.window.close()
    