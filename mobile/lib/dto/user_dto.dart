import 'identity_dto.dart';

class UserDto {
  final String email;
  final String firstName;
  final String lastName;
  final String? picture;
  final String role;
  final IdentityDto identity;

  UserDto({
    required this.email,
    required this.firstName,
    required this.lastName,
    this.picture,
    required this.role,
    required this.identity,
  });

  Map<String, dynamic> toJson() => {
    'email': email,
    'first_name': firstName,
    'last_name': lastName,
    'picture': picture,
    'role': role,
    'auth_id': identity.authId,
    'identity': identity.toJson(),
    'provider': identity.provider,
  };
}
