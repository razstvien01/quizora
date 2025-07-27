import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:quizora/mappers/user_mapper.dart';
import 'package:quizora/models/user.dart';
import 'package:quizora/services/auth_service.dart';

final authServiceProvider = Provider((ref) => AuthService());

final authStateProvider = StateNotifierProvider<AuthController, User?>((ref) {
  final authService = ref.read(authServiceProvider);
  return AuthController(authService);
});

class AuthController extends StateNotifier<User?> {
  final AuthService _authService;

  AuthController(this._authService) : super(null) {
    _checkLogin();
  }

  void _checkLogin() async {
    final userDto = await _authService.getCurrentUser();
    if (userDto != null) {
      state = UserMapper.fromDto(userDto);
    }
  }

  Future<bool> login() async {
    final userDto = await _authService.login();
    if (userDto != null) {
      state = UserMapper.fromDto(userDto);
      return true;
    }
    return false;
  }

  Future<void> logout() async {
    await _authService.logout();
    state = null;
  }
}
