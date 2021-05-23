def compress(raw: str) -> bytes:
    """
    Compress the raw string to bytes using RLE.
    """
    string_bytes = raw.encode('utf8')
    count = 1
    n = len(string_bytes)
    result = bytes(0)
    
    if n == 1:
    	temp = count.to_bytes(1, 'big')
    	return temp + string_bytes
    	
    for i in range(n):
    		c = string_bytes[i]
    		if (i+1<n) and (c == string_bytes[i+1]):
    			count += 1
    		else:
    			result += count.to_bytes(1, 'big')
    			result += c.to_bytes(1, 'big')
    			count = 1
    
    return result
    