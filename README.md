# Silica
Silica is a python GUI library for MacOS using Cocoa and PyObjC. It allows users to make native MacOS GUIs, Menubars, Notifcations, and more without having to deal with ObjectiveC. It is essentially a wrapper for PyObjC for Python programmers (like me) who don't know ObjectiveC and/or Cocoa/Quartz apis.
## Docs
See `windowReference.md` and `floatingPanelReference.md` for docs on `Window` and `FloatingPanel`. Other functions are yet to have docs, you can check out the examples below or look at the source code.
## Example
See `standardWindowTest.py` for a normal window usage example
See `testing.py` for a floating panel usage example
## API
Silica currently supports the following functions:
- Basic windows
- Buttons
- Colors and styles for buttons
- Labels (text fields, WIP styling for these)
- Message boxes (popup info boxes, with customizable buttons and input boxes)
- Notifications
- Menubar (WIP)