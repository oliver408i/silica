Instead of manually positioning widgets, you can add them to the `StackView` using the `add_widget` method. `StackView` will automatically position the widgets in the order they are added to it (or in reverse order, if you set the gravity).  
To make a stack view,
```py
stackView = silica.StackView(width=100, height=100)

# Or you can make a horizontal stack view
stackView = silica.StackView(width=100, height=100, orientation="horizontal")

# If you wish to disable automatic layout, set useAutoLayout=False
stackView = silica.StackView(width=100, height=100, useAutoLayout=False)
```
You can add any `Widget`s to the stack view using the `add_widget` method, like a window, but you also have the optional gravity parameter to set where the widget will be added
```py
stackView.add_widget(someWidget, gravity="top") # Gravity can be top, bottom, left, right, or center
```
Note that to use auto layout, widgets cannot have a frame. To make widgets without a frame, you can do
```py
label = silica.Label(text="Hello World", width=100, height=100, useFrame=False)
```
The `useFrame` option is available for all widgets. Note that if `useFrame` is false, the x and y parameters are ignored, and positioning is handle by the view. Thus you don't need to and shouldn't use the `set_center_at` method.

The `set_spacing` method can be used to set the spacing between the widgets in the stack view.
```py
stackView.set_spacing(10)
```

You can simply add the stack view to a `Window` like any other widget
```py
window.add_widget(stackView)
```

Before you can use auto layout, you need to add constraints to the window
```py
window.add_constraints(stackView)

# Or define custom margins
window.add_constraints(stackView, marginTop=10, marginRight=10, marginBottom=10, marginLeft=10)
```

You can also use a `FloatingPanel`. Simpley replace the `window` in the above examples a `FloatingPanel` object.