import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:quizora/constants/app_routes.dart';
import 'package:quizora/extensions/context_extensions.dart';
import 'package:quizora/providers/auth_provider.dart';

class DashboardScreen extends ConsumerStatefulWidget {
  const DashboardScreen({super.key});

  @override
  ConsumerState<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends ConsumerState<DashboardScreen> {
  Future<void> _handleLogout() async {
    try {
      await ref.read(authStateProvider.notifier).logout();

      if (!mounted) return;
      context.showSnack('Logged out successfully.');
    } catch (e) {
      debugPrint('Logout error: $e');
      if (mounted) {
        context.showSnack('Logout failed.');
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    Theme.of(context);
    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard'),
        actions: [
          IconButton(
            onPressed: _handleLogout,
            icon: const Icon(Icons.logout),
            tooltip: 'Logout',
          ),
        ],
      ),
      body: const Center(child: Text('Welcome to the Dashboard!')),
    );
  }
}
