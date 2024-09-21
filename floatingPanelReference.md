# Floating Panel Reference
Floating panels (NSPanel) are different from standard windows in that they aren't really a window. Silica's `FloatingPanel` do not have a title bar, aren't draggable, and have a transparent background.

### Making floating panels
Making a floating panel is a little bit more complicated than a normal window.
```py
app = silica.App()
window = silica.FloatingPanel(width=400, height=500, ignoreMouseEvents=False, canBeKeyWindow=False)
app.set_float_policy()

# Add widgets here

window.show()
```
Remember to set the float policy or else the panel will not float (keep itself above other windows).
Use `ignoreMouseEvents` only if you do not want the user to interact with your window (such as a notification window). Buttons will not work with this.
if `canBeKeyWindow` is false, the panel cannot be focused on and all inputs will be passed to the app/window behind it. Note that if this is false, keyboard inputs cannot be detected by the panel (input fields will not work) but buttons still work if mouse events are enabled (previous parameter). This also means that the panel cannot be in focus.
The `alpha` value will change the transparency of all widgets and elements of the panel (the background is transparent/passthrough still)
There is an additional `nonActivating` parameter (True or False). Setting this to false will make it behave more like a normal window. This should always be True anyways because if you need a normal window, just use the `silica.Window` class.
Like a normal window, `x=` and `y=` can also be used to set the starting position of the panel.
Remember to call the `show()` method or else the panel will not appear (`hide()` will make the panel disappear but will not close it).

### Considerations
Since floating panels do not have a title bar, they do not have a close button, and cannot be closed by the user unless you add a close button. For your close button, you should call `window.close()` then `app.quit()`.
Float panels are not draggable, but you can still use `move_to(x, y)` to move them.