import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;
final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
    FlutterLocalNotificationsPlugin();

Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await _showLocalNotification(message);
}

Future<void> initFCM() async {
  await _firebaseMessaging.requestPermission();

  const androidSettings = AndroidInitializationSettings('@mipmap/ic_launcher');
  const initSettings = InitializationSettings(android: androidSettings);

  await flutterLocalNotificationsPlugin.initialize(initSettings);

  FirebaseMessaging.onMessage.listen(_showLocalNotification);

  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
}

Future<void> _showLocalNotification(RemoteMessage message) async {
  const androidDetails = AndroidNotificationDetails(
    'default_channel',
    'Default',
    importance: Importance.max,
    priority: Priority.high,
    showWhen: true,
  );

  const notificationDetails = NotificationDetails(android: androidDetails);

  await flutterLocalNotificationsPlugin.show(
    message.hashCode,
    message.notification?.title ?? "No title",
    message.notification?.body ?? "No body",
    notificationDetails,
  );
}
