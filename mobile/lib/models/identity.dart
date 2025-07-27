class Identity {
  final String provider;
  final String authId;

  Identity({required this.provider, required this.authId});

  factory Identity.fromJson(Map<String, dynamic> json) {
    return Identity(provider: json['provider'], authId: json['auth_id']);
  }

  Map<String, dynamic> toJson() {
    return {'provider': provider, 'auth_id': authId};
  }
}
