# Silica
Silica is a python GUI library for MacOS using Cocoa and PyObjC. It allows users to make native MacOS GUIs, Menubars, Notifcations, and more without having to deal with ObjectiveC. It is essentially a wrapper for PyObjC for Python programmers (like me) who don't know ObjectiveC and/or Cocoa/Quartz apis.
## Using
Silica is not on PyPI. Instead, a wheel is provided in the repo's releases. Download it and use `pip install ./silica-x.x.x-py3-none-macosx_10_9_universal2.whl` (change it depending on the actual file name). Optionally you can also just copy the source code (`silica` folder) into your project.
## Docs
See the `docs` folder for docs on Silica and how to use it. All functions and methods (should) be well typed and documented in the code and docstrings itself.
## Example
See `standardWindowTest.py` for a normal window usage example  
See `silicaFloatingWindow.py` for a floating panel usage example  
See `silicaTesting.py` for how to use the `Image` and `Webview` classes  
See `silicaStackView.py` for how to use the `StackView` class (and also checkbox buttons)
See `silicaWebview.py` for how to use the `Webview` class
See `silicaMenubar.py` for how to make a menubar (status bar icon)
## API
Silica currently supports the following functions:
- Basic windows
- Floating windows (panels)
- Views: StackView (auto layout)
- Buttons (checkbox, radio buttons, and normal buttons)
- Colors and styles for buttons
- Labels (text fields, WIP styling for these)
- Message boxes (popup info boxes, with customizable buttons and input boxes)
- Notifications
- Webviews (using WebKit)
- Menubar (WIP)