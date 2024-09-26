# 
# -- WARNING -- 
# THIS IS **NOT** A SILICA EXAMPLE FILE, NOR A SILICA SOURCE CODE FILE
#
# Do not reference off this file! See the files beginning with `silica` in the repo
#
# -- WARNING --
#

"""
!!
THIS IS **NOT** A SILICA EXAMPLE FILE, NOR A SILICA SOURCE CODE FILE
!!
"""

# These files are only for me to test basic objective-c features and are not part of the silica project


import objc
from Cocoa import NSApplication, NSPanel, NSTextField, NSButton, NSBackingStoreBuffered, NSView, NSWindowCollectionBehaviorCanJoinAllSpaces, NSScreenSaverWindowLevel, NSWindowCollectionBehaviorFullScreenAuxiliary, NSProcessInfo
from AppKit import NSApp, NSColor, NSWindowStyleMaskBorderless, NSNonactivatingPanelMask, NSFloatingWindowLevel, NSApplicationActivationPolicyAccessory
from WebKit import WKWebView, WKPreferences, WKWebViewConfiguration

from PyObjCTools.AppHelper import runEventLoop

class DraggableView(NSView):
    def mouseDown_(self, event):
        self.initialLocation = event.locationInWindow()

    def mouseDragged_(self, event):
        newLocation = event.locationInWindow()
        dx = newLocation.x - self.initialLocation.x
        dy = newLocation.y - self.initialLocation.y
        window_frame = self.window().frame()
        new_frame = ((window_frame.origin.x + dx, window_frame.origin.y + dy), window_frame.size)
        self.window().setFrame_display_(new_frame, True)


class CustomPanel(NSPanel):
    # Allow the panel to become the key window to capture input
    def canBecomeKeyWindow(self):
        return True

    # Optional: prevent it from becoming the main window, if desired
    def canBecomeMainWindow(self):
        return False


class WebViewWindow:
    def __init__(self):
        self.app = NSApplication.sharedApplication()
        self.app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

        # Create a custom panel that can become the key window
        self.panel = CustomPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            ((300, 300), (700, 800)),
            NSWindowStyleMaskBorderless | NSNonactivatingPanelMask,
            NSBackingStoreBuffered, False
        )

        self.panel.setBackgroundColor_(NSColor.clearColor())
        self.panel.setOpaque_(False)
        self.panel.setAlphaValue_(0.85)
        self.panel.setLevel_(NSScreenSaverWindowLevel)
        self.panel.setHidesOnDeactivate_(False)

        self.draggable_view = DraggableView.alloc().initWithFrame_(((0, 0), (700, 50)))
        self.draggable_view.setAutoresizingMask_(1)
        self.draggable_view.setWantsLayer_(True)
        self.draggable_view.layer().setBackgroundColor_(NSColor.grayColor().CGColor())
        self.panel.contentView().addSubview_(self.draggable_view)

        self.panel.setCollectionBehavior_(
            NSWindowCollectionBehaviorCanJoinAllSpaces | NSWindowCollectionBehaviorFullScreenAuxiliary
        )

        self.url_input = NSTextField.alloc().initWithFrame_(((10, 60), (480, 40)))
        self.url_input.setStringValue_("https://www.example.com")
        self.url_input.setEditable_(True)
        self.url_input.setSelectable_(True)
        self.url_input.setBezeled_(True)
        self.url_input.setBordered_(True)
        self.url_input.setFocusRingType_(1)
        self.panel.contentView().addSubview_(self.url_input)

        self.back_button = self.create_button("Back", (500, 60), self.go_back)
        self.forward_button = self.create_button("Forward", (550, 60), self.go_forward)
        self.reload_button = self.create_button("Reload", (600, 60), self.reload_page)
        self.go_button = self.create_button("Go", (650, 60), self.load_url)

        # Toggle Button to switch between capture mode and normal mode
        #self.toggle_button = self.create_button("Toggle Mode", (10, 110), self.toggle_capture_mode)

        self.close_button = self.create_button("Close", (650, 110), self.close_window)

        web_config = WKWebViewConfiguration.alloc().init()
        preferences = WKPreferences.alloc().init()
        preferences.setJavaScriptEnabled_(True)
        web_config.setPreferences_(preferences)

        self.web_view = WKWebView.alloc().initWithFrame_configuration_(((0, 150), (700, 550)), web_config)
        ns_url = objc.lookUpClass("NSURL").URLWithString_("https://www.desmos.com")
        request = objc.lookUpClass("NSURLRequest").requestWithURL_(ns_url)
        self.web_view.loadRequest_(request)

        self.panel.contentView().addSubview_positioned_relativeTo_(self.web_view, 1, None)

        # Initially, capture mode is off (keyboard input is ignored by the widget)
        self.is_capture_mode = False
    def create_button(self, title, position, action):
        button = NSButton.alloc().initWithFrame_(((position[0], position[1]), (100, 40)))
        button.setTitle_(title)
        button.setBezelStyle_(4)
        button.setTarget_(self)
        button.setAction_(objc.selector(action, signature=b"v@:"))
        button.setTransparent_(False)
        self.panel.contentView().addSubview_(button)
        return button

    def toggle_capture_mode(self):
        """Toggle between capture mode and normal mode."""
        self.is_capture_mode = not self.is_capture_mode
        if self.is_capture_mode:
            print("Capture mode ON: Widget will accept input.")

        else:
            print("Capture mode OFF: Widget will ignore input.")
            # Unfocus any input field and remove the panel as the key window
            self.panel.resignKeyWindow()

    def go_back(self):
        if self.web_view.canGoBack():
            self.web_view.goBack()

    def go_forward(self):
        if self.web_view.canGoForward():
            self.web_view.goForward()

    def reload_page(self):
        self.web_view.reload()

    def load_url(self):
        url = self.url_input.stringValue()
        if not url.startswith("http"):
            url = "http://" + url
        ns_url = objc.lookUpClass("NSURL").URLWithString_(url)
        request = objc.lookUpClass("NSURLRequest").requestWithURL_(ns_url)
        self.web_view.loadRequest_(request)
        # Optionally set the web view as the first responder to capture input there
        self.panel.makeFirstResponder_(self.web_view)

    def close_window(self):
        self.panel.close()
        NSApp().terminate_(None)

    def show(self):
        self.panel.orderFront_(None)
        # Default behavior when showing the window: No input should be accepted
        self.panel.makeFirstResponder_(None)


if __name__ == "__main__":
    window = WebViewWindow()
    window.show()
    runEventLoop()
