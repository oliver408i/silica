from PyObjCTools import AppHelper
from Cocoa import NSApplication, NSObject

class App:
    def __init__(self):
        """Initialize the base application."""
        self.app = NSApplication.sharedApplication()

    def set_activation_policy(self, policy):
        """Set the activation policy for the app (e.g., show/hide in dock)."""
        self.app.setActivationPolicy_(policy)

    def run(self):
        """Run the application's event loop."""
        AppHelper.runEventLoop()