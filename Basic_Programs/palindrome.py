def isPalindrome(s):
    return s == s[::-1]


s = input("Enter A String\n")
ans = isPalindrome(s)
 
if ans:
    print(s + " Is A Palindrome")
else:
    print(s + " Is Not A Palindrome")