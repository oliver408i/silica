from .App import App
from .Window import Window
from .Label import Label
from .Button import Button
from .Color import Color
from .NotificationManager import NotificationManager
from . import Constants
from .MessageBoxManager import MessageBoxManager
from .Input import Input
from .FloatingPanel import FloatingPanel
from .Image import Image
from .Webview import WebView
from .System import System
from .views import StackView
from .menubar.StatusBar import StatusBar
from .menubar.MenuItem import MenuItem

from objc import ObjCPointerWarning
import warnings

warnings.simplefilter("ignore", ObjCPointerWarning)

__doc__ = """Silica is a lightweight, MacOS native GUI library for Python."""

__all__ = [
    "App",
    "Window",
    "Label",
    "Button",
    "Color",
    "NotificationManager",
    "Constants",
    "MessageBoxManager",
    "Input",
    "FloatingPanel",
    "Image",
    "WebView",
    "System",
    "StackView",
    "StatusBar",
    "MenuItem",
]