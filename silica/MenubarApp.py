from Cocoa import NSStatusBar, NSStatusItem, NSVariableStatusItemLength, NSMenu, NSMenuItem, NSImage, NSApp
from .App import App

# Major WIP, not working yet

class MenubarApp(App):
    def __init__(self):
        """Initialize the Menubar app, inheriting from the base App class."""
        super().__init__()  # Initialize the base App class
        
        # Setup the menubar
        self.setup_menubar()

    def setup_menubar(self):
        """Setup the menubar with a custom icon and menu items."""
        # Create a status item in the menubar
        self.status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)

        # Set the status item icon
        icon_path = "/path/to/icon.png"  # Replace with the path to your icon image
        icon_image = NSImage.alloc().initWithContentsOfFile_(icon_path)
        if icon_image:
            icon_image.setSize_((18, 18))  # Resize the icon to fit the menubar
            self.status_item.button().setImage_(icon_image)

        # Create the menu
        self.menu = NSMenu.alloc().init()

        # Add menu items
        info_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Show Info", "showInfo:", "")
        quit_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Quit", "quitApp:", "")

        self.menu.addItem_(info_item)
        self.menu.addItem_(NSMenuItem.separatorItem())  # Add a separator
        self.menu.addItem_(quit_item)

        # Assign the menu to the status item
        self.status_item.setMenu_(self.menu)

    def showInfo_(self, sender):
        """Handle the 'Show Info' menu item click."""
        print("Info menu clicked!")

    def quitApp_(self, sender):
        """Handle the 'Quit' menu item click and terminate the app."""
        NSApp.terminate_(self)