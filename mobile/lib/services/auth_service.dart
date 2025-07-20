import 'dart:convert';
import 'dart:developer' as developer;
import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:quizora/api/auth_api.dart';
import 'package:quizora/constants/env.dart';
import 'package:quizora/dto/identity_dto.dart';
import 'package:quizora/dto/user_dto.dart';

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
        final sub = payload['sub'];
        final firstName = payload['given_name'];
        final lastName = payload['family_name'];
        final picture = payload['picture'];

        final identity = IdentityDto.fromSub(sub);
        final userDto = UserDto(
          email: email,
          firstName: firstName,
          lastName: lastName,
          role: "student",
          identity: identity,
          picture: picture
        );

        await registeringUserToBackend(userDto);
      }
    } catch (error) {
      developer.log(error.toString());
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

  Future<void> registeringUserToBackend(UserDto userDto) async {
    final response = await AuthApi.registerUser(userDto.toJson());

    if (response.statusCode != 200) {
      developer.log(
        "Registration failed: ${response.statusMessage}",
        name: 'AuthService',
      );
    } else {
      developer.log("User registered: ${response.data}", name: 'AuthService');
    }
  }
}
