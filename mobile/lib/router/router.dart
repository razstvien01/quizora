import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:quizora/constants/app_routes.dart';
import 'package:quizora/router/router_refresh_strream.dart';
import 'package:quizora/screens/dashboard_screen.dart';
import 'package:quizora/screens/landing_screen.dart';
import 'package:quizora/screens/splash_screen.dart';
import 'package:quizora/providers/auth_provider.dart';

final routerProvider = Provider<GoRouter>((ref) {
  return GoRouter(
    initialLocation: AppRoutes.splash,
    debugLogDiagnostics: true,
    refreshListenable: GoRouterRefreshStream(
      ref.watch(authStateProvider.notifier).stream,
    ),
    routes: [
      GoRoute(
        path: AppRoutes.splash,
        builder: (context, state) => const SplashScreen(),
      ),
      GoRoute(
        path: AppRoutes.landing,
        builder: (context, state) => const LandingScreen(),
      ),
      GoRoute(
        path: AppRoutes.dashboard,
        builder: (context, state) => const DashboardScreen(),
      ),
    ],
    redirect: (context, state) {
      final isLoggedIn = ref.read(authStateProvider);
      final goingTo = state.uri.toString();

      if (!isLoggedIn && goingTo != AppRoutes.landing) {
        return AppRoutes.landing;
      }

      if (isLoggedIn && goingTo == AppRoutes.landing) {
        return AppRoutes.dashboard;
      }

      return null;
    },
  );
});
