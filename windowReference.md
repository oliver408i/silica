## Standard Window reference
This reference shows how to use the normal Window class of Silica.

### Making a window
```py
app = silica.App()
window = Window(title="My App", width=400, height=300)
```
Optionally, you can set the x and y of the window by passing in `x=` and `y=` into the constructor

### Adding stuff to a window
To add buttons, labels, and inputs to a window:
```py
window.add_widget(someWidget)
```

### Running the app
To run the app, you must use the event loop from the App object, not the Window object.
```py
app.run()
```

### Window actions
- `minimize()` - Minimizes the window (it will not be brought up again until the user manually do it)
- `move_to(x, y)` - Move the window
- `set_size(width, height)` - Resizes the window
- `toggle_fullscreen()` - Toggles fullscreen
- `get_size()` - Gets the size (as a tuple) of the window
- `get_location()` - Gets the location (as a tuple) of the window
- `is_fullscreen()` - Get if the window is in fullscreen