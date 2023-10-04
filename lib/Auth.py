import jwt

def verify_token(token, secret_key):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded.get('userId')
    except jwt.ExpiredSignatureError:
        # Handle expired token error here
        return None
    except jwt.InvalidTokenError:
        # Handle invalid token error here
        return None

# Example usage:
# user_id = verify_token(your_token, your_secret_key)
# if user_id:
#     print(f'Token is valid. User ID: {user_id}')
# else:
#     print('Token is invalid.')
