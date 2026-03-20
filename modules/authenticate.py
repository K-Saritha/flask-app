def validate_user(username, password):
    if username=='admin' and password=='admin':
        return "valid user"
    else:
        return "invalid user"
