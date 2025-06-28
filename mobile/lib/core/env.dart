import 'package:flutter_dotenv/flutter_dotenv.dart';

class Env {
  static String get apiUrl => dotenv.env['API_BASE_URL']!;
  static String get auth0Domain => dotenv.env['AUTH_DOMAIN']!;
}
