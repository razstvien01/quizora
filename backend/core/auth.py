import requests
from jose import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

#* Auth0 Config
AUTH0_DOMAIN = settings.AUTH0_DOMAIN
API_IDENTIFIER = settings.AUTH0_API_IDENTIFIER
ALGORITHMS = ["RS256"]

def fetch_user_info(token):
  response = requests.get(
        f"https://{AUTH0_DOMAIN}/userinfo",
        headers={"Authorization": f"Bearer {token}"}
  )
  
  if response.status_code != 200:
    raise AuthenticationFailed("Failed to fetch useer info from Auth0")
  return response.json()

def get_token_auth_header(request):
  """
  * Extracts the JWT token from the Authorization header.
  * Must be in the format: "Authorization: Bearer <token>"
  * Returns just the token part
  """
  auth = request.headers.get("Authorization", None)
  if not auth:
    raise AuthenticationFailed("Authorization header is expected.")
  
  parts = auth.split()
  
  if parts[0].lower() != "bearer":
    raise AuthenticationFailed("Authorization header must start with Bearer")
  elif len(parts) == 1:
    raise AuthenticationFailed("Token not found.")
  elif len(parts) > 2:
    raise AuthenticationFailed("Authorization header must be Bearer token.")
  
  return parts[1]

def decode_jwt(token):
  """
  * Validate and decodes the JWT token using Auth0's public key.
  * - Fetches Auth0's JWKS (JSON Web Key Set)
  * - Matches the key ID (kid) in the token header
  * - Verifie the token's signature using the matched key
  * - Returns the payload if valid
  """
  jsonurl = requests.get(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
  jwks = jsonurl.json()
  unverified_header = jwt.get_unverified_header(token)
  
  rsa_key = []
  for key in jwks["keys"]:
    if key["kid"] == unverified_header["kid"]:
      rsa_key = {
        "kty": key["kty"],
        "kid": key["kid"],
        "use": key["use"],
        "n": key["n"],
        "e": key["e"]
      }
      
  if rsa_key:
    try:
      payload = jwt.decode(
        token,
        rsa_key,
        algorithms=ALGORITHMS,
        audience=API_IDENTIFIER,
        issuer=f"https://{AUTH0_DOMAIN}/"
      )
      return payload
    except Exception as e:
      print("JWT Decode Error:", str(e))
      raise AuthenticationFailed(f"Token decade error: {str(e)}")
  
  raise AuthenticationFailed("Unable to find appropraite key.")