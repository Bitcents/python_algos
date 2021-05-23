def gcd(a: int, b: int) -> int:
    if a < b:
        a,b = b,a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    
    return b

# tests
if __name__=='__main__':
    assert(gcd(5,3)) == 1
    assert(gcd(4,8)) == 4
    assert(gcd(14456, 15)) == 1
    