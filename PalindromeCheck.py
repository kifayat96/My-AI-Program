def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

print(is_palindrome("madam"))
print(is_palindrome("hello"))
