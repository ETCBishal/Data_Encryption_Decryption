import random

encryption_level = 128 // 8  # 1 byte = 8 bits

# 1. Key generator
def generate_key() -> str:
    key = ''
    char_pool = ''
    for byte in range(0x00, 0xFF):
        char_pool += chr(byte)

    for _ in range(encryption_level):
        key += random.choice(char_pool)
    return key

# 2. Encryptor
def encrypt(encryption_key,data) -> str:
    key_index = 0
    max_key_index = encryption_level-1
    encrypted_data = ''

    for char in data:
        xor_char = ord(char) ^ ord(encryption_key[key_index])
        encrypted_data += chr(xor_char)

    if key_index >= max_key_index:
        key_index = 0

    else:
        key_index += 1

    return encrypted_data

# 3. Decryptor
def decrypt(decryption_key, encrypted_data) -> str:
    key_index = 0
    max_key_index = encryption_level-1
    decrypted_data = ''

    for char in encrypted_data:
        xor_char = ord(char) ^ ord(decryption_key[key_index])
        decrypted_data += chr(xor_char)

    if key_index >= max_key_index:
        key_index = 0

    else:
        key_index += 1

    return decrypted_data


if __name__ == "__main__":
    key = generate_key()
    enc_data = encrypt(key,'myPass')
    dec_data = decrypt(key,enc_data)

    print(f"Key: {key}")
    print(f"Encrypted Data: {enc_data}")
    print(f"Decrypted Data: {dec_data}")
    
