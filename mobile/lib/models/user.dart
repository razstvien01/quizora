class User {
  final String id;
  final String name;
  final String email;

  User({required this.id, required this.name, required this.email});

  @override
  String toString() {
    return 'User(id: $id, name: $name, email: $email)';
  }
}

User? parseUser(Map<String, dynamic> json) {
  if (json.isEmpty) return null;

  return User(
    id: json['id'] as String,
    name: json['name'] as String,
    email: json['email'] as String,
  );
}