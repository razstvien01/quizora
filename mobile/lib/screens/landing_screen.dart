import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:quizora/constants/app_routes.dart';
import 'package:quizora/extensions/context_extensions.dart';
import 'package:quizora/providers/auth_provider.dart';
import 'package:quizora/widgets/landing/features_page.dart';
import 'package:quizora/widgets/landing/hero_page.dart';
import 'package:quizora/widgets/landing/kickstart_page.dart';

class LandingScreen extends ConsumerStatefulWidget {
  const LandingScreen({super.key});

  @override
  ConsumerState<LandingScreen> createState() => _LandingScreenState();
}

class _LandingScreenState extends ConsumerState<LandingScreen> {
  final PageController _controller = PageController();
  int _currentIndex = 0;
  bool _isLoading = false;

  Future<void> _handleLogin() async {
    setState(() {
      _isLoading = true;
    });

    try {
      final success = await ref.read(authStateProvider.notifier).login();

      if (!mounted) return;

      if (success) {
        context.go(AppRoutes.dashboard);
      } else {
        context.showSnack('Login failed.');
      }
    } catch (e, stack) {
      debugPrint('Login error: $e');
      debugPrint('Stack: $stack');

      if (!mounted) return;
      context.showSnack('Login failed. Please try again.');
    } finally {
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  Future<void> _nextPage() async {
    if (_currentIndex < 2) {
      _controller.nextPage(
        duration: const Duration(milliseconds: 400),
        curve: Curves.easeInOut,
      );
    } else {
      await _handleLogin();
    }
  }

  Widget _buildDot(int index) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      margin: const EdgeInsets.symmetric(horizontal: 4),
      width: _currentIndex == index ? 12 : 8,
      height: _currentIndex == index ? 12 : 8,
      decoration: BoxDecoration(
        color:
            _currentIndex == index
                ? Theme.of(context).colorScheme.primary
                : Colors.grey[400],
        shape: BoxShape.circle,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      backgroundColor: theme.scaffoldBackgroundColor,
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: PageView(
                controller: _controller,
                onPageChanged: (index) {
                  setState(() {
                    _currentIndex = index;
                  });
                },
                children: const [HeroPage(), FeaturesPage(), KickstartPage()],
              ),
            ),
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: List.generate(3, _buildDot),
            ),
            const SizedBox(height: 12),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
              child:
                  _isLoading
                      ? const CircularProgressIndicator()
                      : ElevatedButton(
                        onPressed: _nextPage,
                        style: ElevatedButton.styleFrom(
                          minimumSize: const Size.fromHeight(48),
                          textStyle: const TextStyle(fontSize: 16),
                        ),
                        child: Text(_currentIndex < 2 ? 'Next' : 'Get Started'),
                      ),
            ),
          ],
        ),
      ),
    );
  }
}
