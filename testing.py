from silica import App, Window, Label, Button
import silica

# Example usage
app = App()

notifcationManager = silica.NotificationManager()
messageBoxManager = silica.MessageBoxManager()

def on_button_click():
    response, button = messageBoxManager.show_input_message(
        title="Information",
        message_text="something something",
        informative_text="yes or no.",
        buttons=["very much", "defintally", "100%"],
        icon_path="./shapezio.jpg"
    )
    print("user input", response)
    print("button pressed", silica.Constants.MessageBoxButtons.convert_response_to_index(button))
    
# Create a window
window = Window(title="My Centered App", width=400, height=300)

# Create a label and center it at a specific coordinate
label = Label(text="Welcome to the centered app!", width=200, height=20)
label.set_center_at(200, 150)  # Center the label at (200, 150) in the window
window.add_widget(label)

# Create a button and apply styles
button = Button(text="Styled Button", width=150, height=100, command=on_button_click)
button.set_font("Helvetica-Bold", 16)
button.set_background_color(silica.Color.rgba(0, 1, 0, 0.5))
button.set_text_color(silica.Color.rgba(1, 1, 1, 1))
button.hover_background_color = silica.Color.rgba(0, 1, 0, 1)
button.set_bezel_style(silica.Constants.BezelStyle.TexturedRounded)
button.set_center_at(200, 100)  # Center the button at (200, 150)
button.set_no_bezel()
button.set_corner_radius(30)
window.add_widget(button)

def on_error_button_click():
    messageBoxManager.show_error_message(
        title="Error",
        message_text="This is an error message.",
        informative_text="Something went wrong."
    )

error_button = Button(
    text="Error Message",
    width=150,
    height=100,
    command=on_error_button_click
)
error_button.set_font("Helvetica-Bold", 16)
error_button.set_background_color(silica.Color.rgba(1, 0, 0, 0.5))
error_button.set_text_color(silica.Color.rgba(1, 1, 1, 1))
error_button.set_bezel_style(silica.Constants.BezelStyle.TexturedRounded)
error_button.set_center_at(200, 250)  # Center the button at (200, 250)
error_button.set_no_bezel()
error_button.set_corner_radius(30)
window.add_widget(error_button)

def on_warning_button_click():
    messageBoxManager.show_warning_message(
        title="Warning",
        message_text="This is a warning message.",
        informative_text="Be careful."
    )

warning_button = Button(
    text="Warning Message",
    width=150,
    height=100,
    command=on_warning_button_click
)
warning_button.set_font("Helvetica-Bold", 16)
warning_button.set_background_color(silica.Color.rgba(1, 0, 0, 0.5))
warning_button.set_text_color(silica.Color.rgba(1, 1, 1, 1))
warning_button.set_bezel_style(silica.Constants.BezelStyle.TexturedRounded)
warning_button.set_center_at(200, 200)  # Center the button at (200, 250)
warning_button.set_no_bezel()
warning_button.set_corner_radius(30)
window.add_widget(warning_button)

# Add an input box
inputBox = silica.Input(width=200, height=24, placeholder="Enter something")
inputBox.set_center_at(200, 50)
window.add_widget(inputBox)

# Run the application
app.run()