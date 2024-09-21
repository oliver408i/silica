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

### Adjust window size
You and move and resize the window using
```py
window.move_to(100,100)
window.set_size(300,400)
```

### Running the app
To run the app, you must use the event loop from the App object, not the Window object.
```py
app.run()
```