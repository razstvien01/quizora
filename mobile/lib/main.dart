import 'dart:async';

import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:quizora/config/app_theme.dart';
import 'package:quizora/router/router.dart';
import 'package:quizora/services/firebase_messaging_service.dart';
import 'package:sentry_flutter/sentry_flutter.dart';

Future<void> main() async {
  await dotenv.load(fileName: ".env");
  SentryWidgetsFlutterBinding.ensureInitialized();

  await SentryFlutter.init(
    (options) {
      options.dsn = dotenv.env['SENTRY_DSN'];
      options.tracesSampleRate = 1.0;
      options.environment = dotenv.env['ENVIRONMENT'] ?? 'development';
    },
    appRunner: () async {
      await Firebase.initializeApp();
      await initFCM();

      FlutterError.onError = (FlutterErrorDetails details) {
        FlutterError.presentError(details);
        Sentry.captureException(details.exception, stackTrace: details.stack);
      };

      // This is safe; Sentry sets this internally too for Flutter >=3.3
      PlatformDispatcher.instance.onError = (error, stack) {
        Sentry.captureException(error, stackTrace: stack);
        return true;
      };

      runApp(
        DefaultAssetBundle(
          bundle: SentryAssetBundle(),
          child: const ProviderScope(child: QuizoraApp()),
        ),
      );
    },
  );
}

class QuizoraApp extends ConsumerWidget {
  const QuizoraApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final router = ref.watch(routerProvider);

    return MaterialApp.router(
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light,
      darkTheme: AppTheme.dark,
      routerConfig: router,
    );
  }
}
