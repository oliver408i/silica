# Silica
Silica is a python GUI library for MacOS using Cocoa and PyObjC. It allows users to make native MacOS GUIs, Menubars, Notifcations, and more without having to deal with ObjectiveC. It is essentially a wrapper for PyObjC for Python programmers (like me) who don't know ObjectiveC and/or Cocoa/Quartz apis.
## Docs
See the `docs` folder for docs on Silica and how to use it.
## Example
See `standardWindowTest.py` for a normal window usage example  
See `silicaFloatingWindow.py` for a floating panel usage example  
See `silicaTesting.py` for how to use the `Image` and `Webview` classes  
## API
Silica currently supports the following functions:
- Basic windows
- Floating windows (panels)
- Buttons
- Colors and styles for buttons
- Labels (text fields, WIP styling for these)
- Message boxes (popup info boxes, with customizable buttons and input boxes)
- Notifications
- Webviews (using WebKit)
- Menubar (WIP)