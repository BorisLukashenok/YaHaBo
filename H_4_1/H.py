def is_palindrome(obj):
    if isinstance(obj, int):
        obj = str(obj)
    return obj == obj[:: -1]
