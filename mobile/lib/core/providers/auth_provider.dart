import 'package:flutter_riverpod/flutter_riverpod.dart';

final authProvider = StateNotifierProvider<AuthController, AuthState>((ref) {
  return AuthController();
});

class AuthState {
  final bool isLoggedIn;
  final String? token;

  AuthState({required this.isLoggedIn, this.token});
}

class AuthController extends StateNotifier<AuthState> {
  AuthController() : super(AuthState(isLoggedIn: false));

  void login(String token) {
    state = AuthState(isLoggedIn: true, token: token);
  }

  void logout() {
    state = AuthState(isLoggedIn: false, token: null);
  }
}
