import objc
from Cocoa import NSApplication, NSPanel, NSWindow, NSTextField, NSBackingStoreBuffered, NSNonactivatingPanelMask
from AppKit import NSApp, NSColor, NSWindowStyleMaskBorderless, NSFloatingWindowLevel, NSApplicationActivationPolicyAccessory
import sys
import time
from PyObjCTools.AppHelper import runEventLoop

class TransparentWindow:
    def __init__(self):
        # Create the application
        self.app = NSApplication.sharedApplication()

        # Set the application to stay active without showing in the dock or menu bar
        self.app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

        # Create the panel (floating window)
        self.panel = NSPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            ((300, 300), (400, 100)),  # Window position and size
            NSWindowStyleMaskBorderless | NSNonactivatingPanelMask,  # Non-activating, borderless
            NSBackingStoreBuffered, False
        )

        # Set the panel properties
        self.panel.setBackgroundColor_(NSColor.clearColor())  # Transparent background
        self.panel.setOpaque_(False)  # Make it non-opaque (i.e., transparent)
        self.panel.setLevel_(NSFloatingWindowLevel)  # Always on top
        self.panel.setIgnoresMouseEvents_(True)  # Don't allow interaction
        self.panel.setAlphaValue_(0.8)  # Semi-transparent

        # Add a label to display the message
        self.content_view = self.panel.contentView()
        self.label = NSTextField.alloc().initWithFrame_(((50, 30), (300, 40)))
        self.label.setStringValue_("Hello, this is a notification!")  # Set your message here
        self.label.setBezeled_(False)
        self.label.setDrawsBackground_(False)
        self.label.setEditable_(False)
        self.label.setSelectable_(False)
        self.label.setTextColor_(NSColor.whiteColor())  # White text
        self.content_view.addSubview_(self.label)

    def show(self):
        # Show the panel without activating the app or affecting window focus
        self.panel.orderFront_(None)

    def close_after(self, seconds):
        time.sleep(seconds)
        self.panel.close()

if __name__ == "__main__":
    window = TransparentWindow()
    window.show()

    # Close the window after 5 seconds
    import threading
    threading.Thread(target=window.close_after, args=(5,)).start()

    # Start the event loop
    runEventLoop()
