# Write a recursive function called isPalindrome.  
# The function should take one input, S, which is assumed a string.  
# It should produce a Boolean output depending 
# - True if the string is a palindrome 
# - False if not.

def isPalindrome(S):
  """Takes a string S. Returns True if S is a palindrome, False otherwise"""
  if len(S) == 0:
    return True
  
  if S[0] != S[-1]:
    return False
  
  return isPalindrome(S[1:len(S) - 1])
  
print(isPalindrome("a"))
