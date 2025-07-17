import 'dart:convert';

import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:quizora/api/auth_api.dart';
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

    try {
      final idTokenParts = credentials.idToken.split('.');

      if (idTokenParts.length == 3) {
        final decoded = utf8.decode(
          base64Url.decode(base64Url.normalize(idTokenParts[1])),
        );
        final payload = json.decode(decoded);

        final email = payload['email'];
        final username = payload['name'];
        final authId = payload['sub'];

        await registeringUserToBackend(email, username, authId);
      }
    } catch (error) {
      print(error);
    }

    return credentials;
  }

  Future<void> logout() async {
    await auth0.webAuthentication(scheme: Env.auth0Scheme).logout();

    await storage.deleteAll();
  }

  Future<bool> isLoggedIn() async {
    final token = await storage.read(key: 'access_token');
    return token != null;
  }

  Future<String?> getAccessToken() async {
    return await storage.read(key: 'access_token');
  }

  Future<void> registeringUserToBackend(
    String email,
    String username,
    String authId,
  ) async {
    final response = await AuthApi.registerUser({
      'email': email,
      'username': username,
      'role': 'student',
      'auth_id': authId,
    });

    if (response.statusCode != 200) {
      print("Registration failed: ${response.statusMessage}");
    } else {
      print("User registered: ${response.data}");
    }
  }
}
