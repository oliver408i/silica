import silica

app = silica.App()
panel = silica.FloatingPanel(width=500, height=1000, ignoreMouseEvents=False, canBeKeyWindow=True)

webview = silica.WebView(width=500, height=700, url="https://oliver408i.github.io/missilesim/")

webview.set_center_at(200, 300)

panel.add_widget(webview)

# add close button
close_button = silica.Button(
    text="Close",
    width=150,
    height=100,
    command=lambda: app.quit()
)
close_button.set_font("Helvetica-Bold", 16)
close_button.set_background_color(silica.Color.rgba(1, 0, 0, 0.5))
close_button.set_text_color(silica.Color.rgba(1, 1, 1, 1))
close_button.set_bezel_style(silica.Constants.BezelStyle.TexturedRounded)
close_button.set_center_at(200, 100)
close_button.set_corner_radius(30)
panel.add_widget(close_button)

panel.show()

app.set_float_policy()

app.run()