from PyObjCTools import AppHelper
from Cocoa import NSApplication, NSObject, NSApplicationActivationPolicyAccessory, NSApp
class App:
    def __init__(self):
        """Initialize the base application."""
        self.app = NSApplication.sharedApplication()

    def set_activation_policy(self, policy) -> None:
        """Set the activation policy for the app (e.g., show/hide in dock)."""
        self.app.setActivationPolicy_(policy)

    def set_float_policy(self) -> None:
        self.app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)

    def run(self) -> None:
        """Run the application's event loop."""
        AppHelper.runEventLoop()
    
    def quit(self) -> None:
        """Stop the app"""
        NSApp.terminate_(self)