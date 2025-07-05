import 'package:dio/dio.dart';
import 'dio_client.dart';

class UserService {
  Future<Map<String, dynamic>> getCurrentUser() async {
    try {
      final res = await DioClient.dio.get('/uers/me/');
      return res.data;
    } on DioException catch (e) {
      throw e.response?.data['details'] ?? 'Unknown error occurred';
    }
  }
}
