import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:mobile/core/utils/env.dart';
import 'token_storage.dart';

class AuthService {
  final auth0 = Auth0(Env.auth0Domain, Env.auth0ClientId);

  Future<void> login() async {
    final credentials = await auth0.webAuthentication().login(
      redirectUrl: Env.auth0RedirectUri,
    );

    await TokenStorage.saveToken(credentials.accessToken);
  }

  Future<void> logout() async {
    await auth0.webAuthentication().logout();
    await TokenStorage.clear();
  }
}