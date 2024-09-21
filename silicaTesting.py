import silica

app = silica.App()

window = silica.Window(title="My App", width=400, height=1000)
winWidth, winHeight = window.get_size()

print(winWidth, winHeight)

label = silica.Label(text="Hello, World!", width=200, height=100)

label.set_center_at(200, 900)

window.add_widget(label)

image = silica.Image(width=200, height=200, image_path="shapezio.jpg")

image.set_center_at(200, 800)

window.add_widget(image)

webview = silica.WebView(width=winWidth-100, height=400, url="https://www.google.com")

webview.set_center_at(200, 200)

window.add_widget(webview)

app.run()