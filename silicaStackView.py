import silica

app = silica.App()
window = silica.Window(title="My App", width=400, height=300)

stackView = silica.StackView(width=400, height=300)

image = silica.Image(width=200, height=200, image_path="shapezio.jpg", useFrame=False)

stackView.add_widget(image)

checkbox_button = silica.Button(text="Checkbox", width=200, height=100)
checkbox_button.make_checkbox()

stackView.add_widget(checkbox_button)

window.add_widget(stackView)

window.add_constraints(stackView)

app.run()