import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:quizora/constants/env.dart';

class AuthService {
  final auth0 = Auth0(Env.auth0Domain, Env.auth0ClientId);

  final storage = const FlutterSecureStorage();

  Future<Credentials?> login() async {
    final credentials = await auth0.webAuthentication().login(
      redirectUrl: Env.auth0RedirectUri,
    );
    await storage.write(key: 'access_token', value: credentials.accessToken);
    await storage.write(key: 'id_token', value: credentials.idToken);
    return credentials;
  }

  Future<void> logout() async {
    await auth0.webAuthentication().logout();
    await storage.deleteAll();
  }

  Future<bool> isLoggedIn() async {
    final token = await storage.read(key: 'access_token');
    return token != null;
  }

  Future<String?> getAccessToken() async {
    return await storage.read(key: 'access_token');
  }
}
