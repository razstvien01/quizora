import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:quizora/services/auth_service.dart';

final authServiceProvider = Provider((ref) => AuthService());

final authStateProvider = StateNotifierProvider<AuthController, bool>((ref) {
  final authService = ref.read(authServiceProvider);
  return AuthController(authService);
});

class AuthController extends StateNotifier<bool> {
  final AuthService _authService;

  AuthController(this._authService) : super(false) {
    _checkLogin();
  }

  void _checkLogin() async {
    final loggedIn = await _authService.isLoggedIn();
    state = loggedIn;
  }

  Future<bool> login() async {
    final creds = await _authService.login();
    final isSuccess = creds != null;
    state = isSuccess;
    return isSuccess;
  }

  Future<void> logout() async {
    await _authService.logout();
    state = false;
  }
}
