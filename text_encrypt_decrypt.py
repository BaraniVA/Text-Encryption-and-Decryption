import argparse

def encrypt_text(plaintext, key):
    """Encrypt text using a simple substitution cipher"""
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

def decrypt_text(ciphertext, key):
    """Decrypt text using a simple substitution cipher"""
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            index = key.index(char.lower())
            plaintext += chr(index + ord('a'))
        else:
            plaintext += char
    return plaintext

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Encrypt or decrypt text using a simple substitution cipher')
    parser.add_argument('input_file', type=str, help='Path to the input text file')
    parser.add_argument('--key', type=str, default='abcdefghijklmnopqrstuvwxyz', help='Encryption key')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the text')
    args = parser.parse_args()

    # Read the input file
    with open(args.input_file, 'r') as f:
        input_text = f.read()

    # Encrypt or decrypt the text
    if args.decrypt:
        output_text = decrypt_text(input_text, args.key)
        output_file = args.input_file[:-4] + '_decrypted.txt'
    else:
        output_text = encrypt_text(input_text, args.key)
        output_file = args.input_file[:-4] + '_encrypted.txt'

    # Write the output file
    with open(output_file, 'w') as f:
        f.write(output_text)

    print('Text {}ed successfully!'.format('decrypt' if args.decrypt else 'encrypt'))
