class Identity {
  final String provider;
  final String providerUserId;

  Identity({required this.provider, required this.providerUserId});

  factory Identity.fromJson(Map<String, dynamic> json) {
    return Identity(
      provider: json['provider'],
      providerUserId: json['provider_user_id'],
    );
  }

  Map<String, dynamic> toJson() {
    return {'provider': provider, 'provider_user_id': providerUserId};
  }
}
