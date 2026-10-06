def palindrome(s):
    rev=s[::-1]
    if s==rev:
        return "palindrome"
    else:
        return "not palindrome"
    
print(palindrome("harsh"))