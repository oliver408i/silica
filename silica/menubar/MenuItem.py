from Cocoa import NSMenu, NSMenuItem, NSImage
import objc, warnings
from typing import Callable, Optional

class MenuItem:
    def __init__(self, text: str, action: Optional[Callable] = None):
        self.item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(text, None, "")
        self.enabled = True
        
        if action:
            self.item.setTarget_(self)
            self.item.setAction_("trigger_")
        else:
            self.enabled = False
            warnings.warn("No action specified for menu item.")

        self.submenu = None
        self._command = action
    
    def add_submenu_item(self, item: 'MenuItem') -> None: # Must be quoted because it isn't defined *yet*. It's a forward declaration
        """Add a submenu item to the menu item."""
        if not self.submenu:
            self.submenu = NSMenu.alloc().init()
            self.item.setSubmenu_(self.submenu)

        # Add the passed MenuItem instance to this item's submenu
        self.submenu.addItem_(item.item)
    
    def trigger_(self):
        if (self._command):
            self._command()
    
    def set_action(self, action: Callable) -> None:
        """Set the action for the menu item."""
        self._command = action
        if not self.enabled:
            self.item.setTarget_(self)
            self.item.setAction_("trigger_")
            self.enabled = True
