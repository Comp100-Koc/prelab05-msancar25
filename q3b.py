def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    if a[:2] == '0b':
        a = a[2:]
        
    if b[:2] == '0b':
        b = b[2:]
        
    while len(a) < len(b):
        a = '0' + a
        
    while len(b) < len(a):
        b = '0' + b
        
    result = ''
    carry = 0
    
    for i in range(len(a) - 1, -1, -1):
        val_a = 0
        
        if a[i] == '1':
            val_a = 1
            
        val_b = 0
        if b[i] == '1':
            val_b = 1
            
        total = val_a + val_b + carry
        if total == 0:
            result += '0'
            carry = 0
            
        elif total == 1:
            result += '1'
            carry = 0
            
        elif total == 2:
            result += '0'
            carry = 1
            
        elif total == 3:
            result += '1'
            carry = 1
            
    if carry > 0:
        result += '1'
    
    final_str = result[::-1]
    final_str = final_str.lstrip('0')
    if final_str == '':
        final_str = '0'
        
    return '0b' + final_str