import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dio/dio.dart';
import 'package:mobile/core/utils/env.dart';
import '../../auth/token_storage.dart';

class AuthService {
  final auth0 = Auth0(Env.auth0Domain, Env.auth0ClientId);

  Future<Map<String, dynamic>> login() async {
    final credentials = await auth0.webAuthentication().login(
      redirectUrl: Env.auth0RedirectUri,
    );

    final accessToken = credentials.accessToken;

    final dio = Dio();
    final response = await dio.post(
      '${Env.apiUrl}/auth/',
      options: Options( 
        headers: {
          'Authorization': 'Bearer $accessToken',
          'Content-Type': 'application/json',
        },
      ),
    );

    await TokenStorage.saveToken(accessToken);

    final user = response.data;

    print("Authenticated user: $user");

    return user;
  }

  Future<void> logout() async {
    await auth0.webAuthentication().logout();
    await TokenStorage.clear();
  }
}
