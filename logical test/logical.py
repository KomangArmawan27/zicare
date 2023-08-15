def sequenceExists(list, seq):
    seq_length = len(seq)
    list_length = len(list)
    
    if seq_length > list_length:
        return False
    
    for i in range(list_length - seq_length + 1):
        if list[i:i + seq_length] == seq:
            return True
    
    return False

list = [20, 7, 8, 10, 2, 5, 6]
print(sequenceExists(list, [5, 6]))  
print(sequenceExists(list, [8, 7]))  
print(sequenceExists(list, [7, 10])) 
