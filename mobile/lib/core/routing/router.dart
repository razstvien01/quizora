import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/constants/app_routes.dart';
import 'package:mobile/domain/providers/auth_provider.dart';
import 'package:mobile/presentation/screens/dashboard_screen.dart';
import 'package:mobile/presentation/screens/landing_screen.dart';
import 'package:mobile/presentation/screens/splash_screen.dart';

final routerProvider = Provider<GoRouter>((ref) {
  final authState = ref.watch(authProvider);
  final isLoggedIn = authState.isLoggedIn;

  return GoRouter(
    initialLocation: '/',
    debugLogDiagnostics: true,
    routes: [
      GoRoute(
        path: AppRoutes.splash,
        builder: (context, state) => const SplashScreen(),
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
