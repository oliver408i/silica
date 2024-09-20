from Cocoa import NSColor

class Color:
    @staticmethod
    def rgba(red: float, green: float, blue: float, alpha:float=1.0):
        """
        Create an NSColor with custom RGB and alpha values.
        - red, green, blue: Values between 0.0 and 1.0
        - alpha: Optional, default is 1.0 (opaque), values between 0.0 and 1.0
        """
        return NSColor.colorWithCalibratedRed_green_blue_alpha_(red, green, blue, alpha)