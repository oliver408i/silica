from Cocoa import NSStatusBar, NSMenu, NSMenuItem, NSImage
from ..App import App
from .MenuItem import MenuItem
import objc, warnings
from typing import Optional

class StatusBar():

    def __init__(self, text: str="Silica App", image_path: Optional[str]=None):
        self.statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(-1)
        if image_path:
            image = NSImage.alloc().initByReferencingFile_(image_path)
            if not image or not image.isValid():
                warnings.warn(f"Error: Could not load image from {image_path}")
                return
            image.setSize_((22, 22))
            self.statusItem.setImage_(image)
        else:
            self.statusItem.setTitle_(text)

        self.menu = NSMenu.alloc().init()
        self.statusItem.setMenu_(self.menu)
    
    def add_menu_item(self, item: MenuItem) -> None:
        """Add a menu item to the status bar."""
        self.menu.addItem_(item.item)


