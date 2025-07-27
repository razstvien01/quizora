import 'package:quizora/dto/user_dto.dart';
import 'package:quizora/models/identity.dart';
import 'package:quizora/models/user.dart';

class UserMapper {
  static User fromDto(UserDto dto) {
    return User(
      email: dto.email,
      firstName: dto.firstName,
      lastName: dto.lastName,
      role: dto.role,
      identity: Identity.fromJson(dto.identity.toJson()),
    );
  }
}
