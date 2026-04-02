def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    result = ''
    for char in s:
        result += char
        if len(result) >= 2 and result[-1] == result[-2]:
            result = result[:-2]
    return result
                
    pass
""" lenght = len(s)
 for i in range(lenght):
     for j in range(i+2,lenght+1):
         substring = s[i:j]
         if substring == substring[-1]:
             s = s[:s.find(substring)]+ s[s.find(substring)+len(substring):]
 return s"""