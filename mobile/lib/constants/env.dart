import 'package:flutter_dotenv/flutter_dotenv.dart';

class Env {
  static String get apiUrl => dotenv.env['API_BASE_URL']!;
  static String get auth0Domain => dotenv.env['AUTH0_DOMAIN']!;
  static String get auth0ClientId => dotenv.env['AUTH0_CLIENT_ID']!;
  static String get auth0ApiIdentifier => dotenv.env['AUTH0_API_IDENTIFIER']!;
  static String get auth0RedirectUri => dotenv.env['AUTH0_REDIRECT_URI']!;
}
