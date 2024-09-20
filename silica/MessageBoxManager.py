from Cocoa import NSAlert, NSAlertStyleInformational, NSAlertStyleWarning, NSAlertStyleCritical, NSImage, NSTextField, NSAlertFirstButtonReturn, NSView
import warnings

class MessageBoxManager:
    def __init__(self):
        """Initialize the MessageBoxManager."""
        pass

    def show_message(self, title="Message", message_text=None, informative_text=None, buttons=None, alert_style=None, icon_path=None, input_fields=None):
        """
        Display a message box with a custom title, message, informative text, buttons, icon, and optional input fields.
        
        - title: The title of the message box.
        - message_text: The main message to display.
        - informative_text: Additional details (informative text).
        - buttons: List of button titles (e.g., ["OK", "Cancel"]).
        - alert_style: The style of the alert (e.g., NSAlertStyleInformational, NSAlertStyleWarning).
        - icon_path: Path to the custom icon.
        - input_fields: A list of NSTextField objects to be used as input fields.
        
        Returns a tuple containing the user input (if any) and the button pressed (response).
        """
        # Create the alert
        alert = NSAlert.alloc().init()
        alert.setMessageText_(title)

        if message_text:
            alert.setMessageText_(message_text)

        if informative_text:
            alert.setInformativeText_(informative_text)

        # Set the style of the alert (optional)
        if alert_style:
            alert.setAlertStyle_(alert_style)

        # Add custom icon (if provided)
        if icon_path:
            icon = NSImage.alloc().initWithContentsOfFile_(icon_path)
            if icon:
                alert.setIcon_(icon)

        # Add buttons (e.g., "OK", "Cancel")
        if buttons:
            for button in buttons:
                alert.addButtonWithTitle_(button)
        else:
            # Default to "OK" and "Cancel"
            alert.addButtonWithTitle_("OK")
            alert.addButtonWithTitle_("Cancel")

        # Add input fields (if provided)
        if input_fields:
            # Create an accessory view to contain all input fields
            accessory_view = NSView.alloc().initWithFrame_(((0, 0), (200, 24 * len(input_fields))))
            y_position = len(input_fields) * 24  # Y position to stack input fields
            for field in input_fields:
                field.setFrame_(((0, y_position - 24), (200, 24)))  # Set position for each field
                accessory_view.addSubview_(field)
                y_position -= 24
            alert.setAccessoryView_(accessory_view)

        # Show the alert and wait for the response (modal)
        response = alert.runModal()

        # If input fields exist, return the input values and the button pressed
        if input_fields:
            input_values = [field.stringValue() for field in input_fields]
            return input_values, response
        else:
            return None, response  # Return None for input if canceled or no input fields
        
    def show_input_message(self, title="Input Required", message_text=None, informative_text=None, buttons=None, icon_path=None):
        """Convenience method for showing a message box with a single input field."""
        # Create a single input field for user input
        input_field = NSTextField.alloc().initWithFrame_(((0, 0), (200, 24)))
        return self.show_message(
            title=title,
            message_text=message_text,
            informative_text=informative_text,
            buttons=buttons,
            icon_path=icon_path,
            input_fields=[input_field]  # Add the input field
        )

    def show_info_message(self, title="Information", message_text=None, informative_text=None, buttons=None):
        """Show an informational message box."""
        _, button = self.show_message(
            title=title,
            message_text=message_text,
            informative_text=informative_text,
            buttons=buttons,
            alert_style=NSAlertStyleInformational
        )
        return button

    def show_warning_message(self, title="Warning", message_text=None, informative_text=None, buttons=None):
        """Show a warning message box."""
        _, button = self.show_message(
            title=title,
            message_text=message_text,
            informative_text=informative_text,
            buttons=buttons,
            alert_style=NSAlertStyleWarning
        )
        return button

    def show_error_message(self, title="Error", message_text=None, informative_text=None, buttons=None):
        """Show an error/critical message box."""
        _, button = self.show_message(
            title=title,
            message_text=message_text,
            informative_text=informative_text,
            buttons=buttons,
            alert_style=NSAlertStyleCritical
        )
        return button