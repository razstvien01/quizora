import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:mobile/core/services/auth_service.dart';

final authProvider = StateNotifierProvider<AuthController, AuthState>((ref) {
  return AuthController(AuthService());
});

class AuthState {
  final bool isLoggedIn;
  final String? token;
  final String? email;
  final String? name;
  final String? role;

  AuthState({
    required this.isLoggedIn,
    this.token,
    this.email,
    this.name,
    this.role,
  });
}

class AuthController extends StateNotifier<AuthState> {
  final AuthService _authService;

  AuthController(this._authService) : super(AuthState(isLoggedIn: false));

  Future<void> login() async {
    final user = await _authService.login();
    state = AuthState(isLoggedIn: true, token: user['token']);
  }

  Future<void> logout() async {
    await _authService.logout();
    state = AuthState(isLoggedIn: false, token: null);
  }
}
