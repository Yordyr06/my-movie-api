from jwt import encode

def create_token(data: dict):
  token = encode(payload = data, key = 'key', algorithm = 'HS256')
  return token

