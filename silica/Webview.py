from Cocoa import NSMakeRect
from WebKit import WKWebView, NSURLRequest, NSURL, WKWebViewConfiguration, WKPreferences
from .Widget import Widget
import warnings

class WebView(Widget):
    def __init__(self, width, height, url):
        """
        Initialize the WebView widget with a specified width, height, and URL.
        JavaScript is enabled by default.
        """
        super().__init__(width, height)  # Call the parent class's initializer

        # Configure the WKWebView to enable JavaScript
        webview_config = WKWebViewConfiguration.alloc().init()
        webview_prefs = WKPreferences.alloc().init()
        webview_prefs.setJavaScriptEnabled_(True)
        webview_config.setPreferences_(webview_prefs)

        # Create a WKWebView instance with JavaScript enabled
        self.widget = WKWebView.alloc().initWithFrame_configuration_(NSMakeRect(0, 0, width, height), webview_config)

        # Load the initial URL
        self.go_to_url(url)

    def go_to_url(self, url):
        """Navigate to a specific URL."""
        nsurl = NSURL.URLWithString_(url)
        if nsurl:
            request = NSURLRequest.requestWithURL_(nsurl)
            self.widget.loadRequest_(request)
        else:
            warnings.warn(f"Error: Invalid URL {url}")

    def reload(self):
        """Reload the current webpage."""
        self.widget.reload_(self)

    def go_back(self):
        """Navigate back to the previous page in history."""
        if self.widget.canGoBack():
            self.widget.goBack_(self)
    
    def can_go_back(self):
        """Check if the user can navigate back in history."""
        return self.widget.canGoBack()
    
    def can_go_forward(self):
        """Check if the user can navigate forward in history."""
        return self.widget.canGoForward()

    def go_forward(self):
        """Navigate forward to the next page in history."""
        if self.widget.canGoForward():
            self.widget.goForward_(self)

    def execute_javascript(self, script, callback=None):
        """
        Execute JavaScript code in the current webpage.
        
        Parameters:
        - script: A string containing the JavaScript code to be executed.
        - callback: An optional function to handle the result of the script execution.
        """
        def js_callback(result, error):
            if error:
                warnings.warn(f"JavaScript error: {error}")
            else:
                if callback:
                    callback(result)
        
        self.widget.evaluateJavaScript_completionHandler_(script, js_callback)