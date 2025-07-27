import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:quizora/constants/app_routes.dart';
import 'package:quizora/router/router_refresh_strream.dart';
import 'package:quizora/screens/dashboard_screen.dart';
import 'package:quizora/screens/landing_screen.dart';
import 'package:quizora/screens/splash_screen.dart';
import 'package:quizora/providers/auth_provider.dart';

final routerProvider = Provider<GoRouter>((ref) {
  final authNotifier = ref.read(authStateProvider.notifier);

  return GoRouter(
    initialLocation: AppRoutes.splash,
    debugLogDiagnostics: true,
    refreshListenable: GoRouterRefreshStream(authNotifier.stream),
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
      final user = ref.read(authStateProvider);
      final isSplash = state.uri.toString() == AppRoutes.splash;
      final isLanding = state.uri.toString() == AppRoutes.landing;

      if (user == null) {
        if (!isLanding) return AppRoutes.landing;
      } else {
        if (isLanding || isSplash) {
          return AppRoutes.dashboard;
        }
      }

      return null;
    },
  );
});
