To send notifications and message boxes, you need to make managers for them first.
```py
notificationManager = silica.NotificationManager()
messageBoxManager = silica.MessageBoxManager()
```

You can notifcations using
```py
notificationManager.send_notification(title="Notification", subtitle="Test", informative_text="This is a notification", sound=True)
```
You can optionally clear notifications using `notificationManager.clear_delivered_notifications()`  

To send a message box (alert), do
```py
messageBoxManager.show_info_message(
    title="Info",
    message_text="This is a message.",
    informative_text="Something something"
)
```
There is also `show_warning_message` and `show_error_message` which follow the exact same format as `show_info_message`. Note that on recent MacOS versions, the warning box and info box look the exact same. The error box shows your app icon and a warning symbol.

For input message boxes (text field and/or buttons) you can do. Buttons can be `None`, which will make the default Ok and Cancel buttons. Icon path can be `None`, which will use your app's icon.
```py
response, button = messageBoxManager.show_input_message(
    title="Input",
    message_text="Some text",
    informative_text="Some more text",
    buttons=["option 0","option 1","option 2"],
    icon_path="someIcon.jpg"
)
print("user input", response)
print("button pressed", silica.Constants.MessageBoxButtons.convert_response_to_index(button))
```

If you perfer to do your own thing, you can use
```py
reponse, button = messageBoxManager.show_message(self, title="Message", message_text=None, informative_text=None, buttons=None, alert_style=None, icon_path=None, input_fields=None):
```
Obviously, all the options are customizable.