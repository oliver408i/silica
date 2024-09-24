import silica

app = silica.App()
app.set_no_dock_icon()

messageBox = silica.MessageBoxManager()

def quit():
    app.quit()

menuBar = silica.StatusBar(image_path="shapezio.jpg") # If image_path is None, a text status bar will be used
# For example, menuBar = silica.StatusBar(text="My Cool App") will also work, creating a text status bar

menuBar.add_menu_item(silica.MenuItem("Quit", quit))
menuBar.add_menu_item(silica.MenuItem("Show Info", lambda: messageBox.show_info_message("Hello, World!")))

subMenu = silica.MenuItem("Submenu") # Create a submenu
subMenu.add_submenu_item(silica.MenuItem("Submenu Item 1", lambda: messageBox.show_info_message("Submenu Item 1")))
subMenu.add_submenu_item(silica.MenuItem("Submenu Item 2", lambda: messageBox.show_info_message("Submenu Item 2")))

menuBar.add_menu_item(subMenu)

app.run()