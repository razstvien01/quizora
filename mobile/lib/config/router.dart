import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:quizora/constants/app_routes.dart';
import 'package:quizora/screens/dashboard_screen.dart';
import 'package:quizora/screens/landing_screen.dart';
import 'package:quizora/screens/splash_screen.dart';
import 'package:quizora/providers/auth_provider.dart';

final routerProvider = Provider<GoRouter>((ref) {
  final isLoggedIn = ref.watch(authStateProvider);

  return GoRouter(
    initialLocation: AppRoutes.splash,
    debugLogDiagnostics: true,
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
      if (isLoggedIn) return AppRoutes.dashboard;
      if (!isLoggedIn) return AppRoutes.landing;

      return null;
    },
  );
});
