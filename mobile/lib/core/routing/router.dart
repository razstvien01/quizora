import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/presentation/screens/splash_screen.dart';

import 'package:mobile/features/dashbaord/presentation/screens/dashboard_screen.dart';
import 'package:mobile/features/auth/presentation/screens/login_screen.dart';

final authProvider = StateProvider<bool>((ref) => false);

final routerProvider = Provider<GoRouter>((ref) {
  final isLoggedIn = ref.watch(authProvider);

  return GoRouter(
    initialLocation: '/',
    debugLogDiagnostics: true,
    routes: [
      GoRoute(path: '/', builder: (context, state) => const SplashScreen()),
      GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
      GoRoute(
        path: '/dashboard',
        builder: (context, state) => const DashboardScreen(),
      ),
    ],
    redirect: (context, state) {
      final loggingIn = state.fullPath == '/login';

      if (!isLoggedIn) return loggingIn ? null : '/login';
      if (loggingIn) return '/dashboard';

      return null;
    },
  );
});
