from Cocoa import NSScreen
from typing import Tuple

class System:
    @staticmethod
    def get_screen_dimensions(screen: NSScreen=None) -> Tuple[float, float]:
        """
        Returns the width and height of the user's main screen in points.
        """
        if screen is None:
            screen = NSScreen.mainScreen()
        
        # Get the main screen's frame (in points, not pixels)
        screen_frame = screen.frame()
        
        # The frame returns an NSRect, where:
        # - origin.x and origin.y are the bottom-left corner of the screen
        # - size.width and size.height are the screen's dimensions
        screen_width = screen_frame.size.width
        screen_height = screen_frame.size.height
        
        return screen_width, screen_height

    @staticmethod
    def get_screen_dimensions_in_pixels(screen: NSScreen=None) -> Tuple[float, float]:
        """
        Returns the width and height of the user's main screen in pixels. (For Retina displays)
        """
        if screen is None:
            screen = NSScreen.mainScreen()
        
        screen_frame = screen.frame()
        scale_factor = screen.backingScaleFactor()  # Get the scale factor for Retina displays

        # Multiply the frame's width and height by the scale factor to get the pixel dimensions
        screen_width_in_pixels = screen_frame.size.width * scale_factor
        screen_height_in_pixels = screen_frame.size.height * scale_factor
        
        return screen_width_in_pixels, screen_height_in_pixels