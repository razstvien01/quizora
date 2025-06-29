import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/presentation/screens/splash_screen.dart';

import 'package:mobile/features/dashbaord/presentation/screens/dashboard_screen.dart';
import 'package:mobile/features/auth/presentation/screens/login_screen.dart';

import 'package:mobile/core/constants/app_routes.dart';
import 'package:mobile/features/landing/presentation/screens/landing_screen.dart';

final authProvider = StateProvider<bool>((ref) => false);

final routerProvider = Provider<GoRouter>((ref) {
  final isLoggedIn = ref.watch(authProvider);

  return GoRouter(
    initialLocation: '/',
    debugLogDiagnostics: true,
    routes: [
      GoRoute(
        path: AppRoutes.splash,
        builder: (context, state) => const SplashScreen(),
      ),
      GoRoute(
        path: AppRoutes.login,
        builder: (context, state) => const LoginScreen(),
      ),
      GoRoute(
        path: AppRoutes.dashboard,
        builder: (context, state) => const DashboardScreen(),
      ),
      GoRoute(
        path: AppRoutes.landing,
        builder: (context, state) => const LandingScreen(),
      ),
    ],
    redirect: (context, state) {
      final goingToLanding = state.fullPath == AppRoutes.landing;
      final goingToLogin = state.fullPath == AppRoutes.login;

      if (!isLoggedIn) {
        //* Allows landing and login for unauthenticated users
        if (goingToLanding || goingToLogin) return null;
        return AppRoutes.landing;
      }

      if (goingToLanding || goingToLogin) return AppRoutes.dashboard;

      return null;
    },
  );
});
