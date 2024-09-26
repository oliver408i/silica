from PyObjCTools import AppHelper
from Cocoa import NSApplication, NSObject, NSApplicationActivationPolicyAccessory, NSApp, NSApplicationActivationPolicyProhibited
class App:
    def __init__(self):
        """Initialize the base application."""
        self.app = NSApplication.sharedApplication()

    def set_activation_policy(self, policy) -> None:
        """Set the activation policy for the app. Advanced uses, must pass in an objc NSApplicationActivationPolicyxxxx value"""
        self.app.setActivationPolicy_(policy)

    def run(self) -> None:
        """Run the application's event loop."""
        AppHelper.runEventLoop()
    
    def quit(self) -> None:
        """Stop the app"""
        NSApp.terminate_(self)
    
    def set_no_dock_icon(self) -> None:
        """Prevents the app from showing in the dock, but will still allow it to have windows, guis, etc"""
        self.app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    
    def focus(self) -> None:
        """Forces the app and all its visible windows to gain focus"""
        NSApp.activateIgnoringOtherApps_(True)