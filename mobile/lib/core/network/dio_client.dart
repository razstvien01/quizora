import 'package:dio/dio.dart';
import 'package:mobile/core/utils/env.dart';

class DioClient {
  final Dio dio;

  DioClient({String? token})
    : dio = Dio(
        BaseOptions(
          baseUrl: Env.apiUrl,
          headers: token != null ? {'Authorization': 'Bearer $token'} : {},
        ),
      ) {
    dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) {
          return handler.next(options);
        },
        onError: (e, handler) {
          return handler.next(e);
        },
      ),
    );
  }
}
