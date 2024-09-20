from Cocoa import NSBezelStyleRounded, NSBezelStyleRegularSquare, NSBezelStyleTexturedRounded, NSBezelStyleTexturedSquare, NSBezelStyleDisclosure, NSBezelStyleShadowlessSquare, NSBezelStyleCircular, NSAlertFirstButtonReturn

"""
	•	NSBezelStyleRounded: Standard rounded button.
	•	NSBezelStyleRegularSquare: Square button.
	•	NSBezelStyleTexturedRounded: A more textured and rounded button.
	•	NSBezelStyleTexturedSquare: Textured square button.
	•	NSBezelStyleDisclosure: A small triangle, used for disclosure.
	•	NSBezelStyleShadowlessSquare: Square button with no shadow.
	•	NSBezelStyleCircular: Circular button.
"""

class BezelStyle:
    Rounded = NSBezelStyleRounded
    RegularSquare = NSBezelStyleRegularSquare
    TexturedRounded = NSBezelStyleTexturedRounded
    TexturedSquare = NSBezelStyleTexturedSquare
    Disclosure = NSBezelStyleDisclosure
    ShadowlessSquare = NSBezelStyleShadowlessSquare
    Circular = NSBezelStyleCircular

class MessageBoxButtons:
	First = NSAlertFirstButtonReturn
	Second = NSAlertFirstButtonReturn + 1
	Third = NSAlertFirstButtonReturn + 2
	Fourth = NSAlertFirstButtonReturn + 3

	@staticmethod
	def convert_response_to_index(response):
		"""
		Convert the NSAlert button response into an index based on the number of buttons.
		
		- response: The response from the alert.
		
		Returns an integer index (0-any) corresponding to the button clicked.
		"""
		return response - NSAlertFirstButtonReturn