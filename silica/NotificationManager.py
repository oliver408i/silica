from Cocoa import NSUserNotification, NSUserNotificationCenter, NSUserNotificationDefaultSoundName

class NotificationManager:
    def __init__(self):
        """Initialize the notification manager."""
        self.notification_center = NSUserNotificationCenter.defaultUserNotificationCenter()

    def send_notification(self, title="Notification", subtitle=None, informative_text=None, sound=True):
        """Create and send a macOS notification with optional sound."""
        # Create the notification
        notification = NSUserNotification.alloc().init()
        notification.setTitle_(title)

        if subtitle:
            notification.setSubtitle_(subtitle)

        if informative_text:
            notification.setInformativeText_(informative_text)

        if sound:
            notification.setSoundName_(NSUserNotificationDefaultSoundName)

        # Deliver the notification
        self.notification_center.deliverNotification_(notification)

    def clear_delivered_notifications(self):
        """Clear all delivered notifications from the Notification Center."""
        self.notification_center.removeAllDeliveredNotifications()