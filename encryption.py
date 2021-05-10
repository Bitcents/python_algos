from secrets import token_bytes
from typing import Tuple

def get_random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(input_str: str) -> Tuple:
    input_bits: bytes = input_str.encode('utf-8')
    original = int.from_bytes(input_bits, "big")
    dummy_key = get_random_key(len(input_bits))
    original_key = original ^ dummy_key
    return original_key, dummy_key

def decrypt(key_1: int, key_2: int) -> str:
    decrypted: int = key_1 ^ key_2
    # adding 7 and dividing by 8 ensures that we round up to avoid an off-byte error
    temp: bytes = decrypted.to_bytes(decrypted.bit_length() + 7 // 8, "big")
    return temp.decode('utf-8')

