def longest_palindromic_substring(s):
    if len(s) < 2:
        return ''
    result = ''
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if len(substring) > len(result):
                     result = substring
    return result
    """
    Given a string find the longest palindromic substring
    """
