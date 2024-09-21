To get the user's screen size for your application (i.e. scale the window correctly) you can use `silica.System`
```py
# Get the main screen's size
w, h = silica.System.get_screen_dimensions()

# Or if you need it in pixels (for Retina displays)
wp, hp = silica.System.get_screen_dimensions_in_pixels()

# If you want to find the dimensions of the screen that a window is on
w, h = silica.System.get_screen_dimensions(window.get_screen())

```
Both get screen dimensions functions take an optional `screen: NSScreen` arguement (such as the output of `window.get_screen()`)