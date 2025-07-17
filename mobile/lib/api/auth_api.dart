import 'package:dio/dio.dart';
import 'package:quizora/constants/env.dart';

class AuthApi {
  static final Dio dio = Dio(
    BaseOptions(
      baseUrl: Env.apiUrl,
      connectTimeout: const Duration(seconds: 10),
      receiveTimeout: const Duration(seconds: 10),
      headers: {'Content-Type': 'application/json'},
    ),
  );
  
  static Future<Response> registerUser(Map<String, dynamic> data) async {
    final url = '${Env.apiUrl}/api/auth/';

    return await dio.post(
      url,
      data: data,
      options: Options(headers: {'Content-Type': 'application/json'}),
    );
  }
}
