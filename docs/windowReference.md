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

### On resize and move
You can add listeners for on move and on resize, which will trigger when the user moves the window or resizes it.
```py
window.on_move(lambda x, y: print(x, y))
window.on_resize(lambda w, h: print(w, h))
```

### Window actions
- `minimize()` - Minimizes the window (it will not be brought up again until the user manually do it)
- `move_to(x, y)` - Move the window
- `set_size(width, height)` - Resizes the window
- `toggle_fullscreen()` - Toggles fullscreen
- `get_size()` - Gets the size (as a tuple) of the window
- `get_location()` - Gets the location (as a tuple) of the window
- `is_fullscreen()` - Get if the window is in fullscreen
- `get_screen()` - Returns the NSScreen object that this window is on. See the screen size reference
- `add_constraints(widget, marginTop=0, marginRight=0, marginBottom=0, marginLeft=0)` - Add constraints to the window. Only used for auto layout. Use this to add margins, for example.
- `set_window_level(level)` - Set the level of this window, basically how much in front or in the back the window should be relative to other windows. The `Constants` module has a `WindowLevels` class that contains the basic levels.