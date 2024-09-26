import objc

# Enable verbose logging to catch more errors
objc.setVerbose(True)
import silica

app = silica.App()
app.set_no_dock_icon()

messageBox = silica.MessageBoxManager()

def quit():
    app.quit()

window = None # YOU MUST KEEP A GLOBAL REFERENCE TO THE WINDOW! Else it will cause a segmentation fault when it is closed.

def showWindow():
    global window

    window = silica.Window(title="My Cool App", width=400, height=300, x=100, y=100, shouldQuitOnClose=False) # shouldQuitOnClose=False to prevent the window from quitting the app on close

    label = silica.Label(text="Hello, World!", width=200, height=20)
    window.add_widget(label)
    window.show() # bring the window to the top of the app layer
    app.focus() # bring the app to the top of the system window layer

menuBar = silica.StatusBar(image_path="shapezio.jpg") # If image_path is None, a text status bar will be used
# For example, menuBar = silica.StatusBar(text="My Cool App") will also work, creating a text status bar

menuBar.add_menu_item(silica.MenuItem("Quit", quit))
menuBar.add_menu_item(silica.MenuItem("Show Info", lambda: messageBox.show_info_message("Hello, World!")))

subMenu = silica.MenuItem("Submenu", lambda: messageBox.show_info_message("Submenu")) # The action can be None here, in which case the child items still work, but you cannot click on "Submenu" (this item) anymore
subMenu.add_submenu_item(silica.MenuItem("Submenu Item 1", lambda: messageBox.show_info_message("Submenu Item 1")))
subMenu.add_submenu_item(silica.MenuItem("Open window", showWindow))

menuBar.add_menu_item(subMenu)

app.run()