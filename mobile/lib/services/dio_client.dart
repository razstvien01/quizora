import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:quizora/constants/env.dart';

class DioClient {
  static final Dio _dio = Dio(BaseOptions(baseUrl: Env.apiUrl));
  static final _storage = FlutterSecureStorage();

  static Dio get client {
    _dio.interceptors.clear();
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await _storage.read(key: 'access_token');
          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          return handler.next(options);
        },
      ),
    );
    return _dio;
  }
}
