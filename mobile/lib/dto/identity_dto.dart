class IdentityDto {
  final String provider;
  final String providerUserId;
  final String authId;

  IdentityDto({
    required this.provider,
    required this.providerUserId,
    required this.authId,
  });

  factory IdentityDto.fromSub(String sub) {
    final parts = sub.split('|');
    return IdentityDto(
      provider: parts[0],
      providerUserId: parts[1],
      authId: sub,
    );
  }

  Map<String, dynamic> toJson() => {
    'provider': provider,
    'auth_id': authId,
    'provider_user_id': providerUserId,
  };
}
