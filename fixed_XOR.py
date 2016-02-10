from hex_to_64 import hex_to_binary

ORIGINAL = '1c0111001f010100061a024b53535009181c'
XOR = '686974207468652062756c6c277320657965'


def xor_2_strings(original_string, xor_string):
    length = len(original_string)
    num_of_bits = length * 4

    original_binary = hex_to_binary(original_string)
    xor_binary = hex_to_binary(xor_string)

    result_binary = ''
    for i in range(0, num_of_bits):
        result_char = int(original_binary[i]) ^ int(xor_binary[i])
        result_binary += str(result_char)
    hex_string = hex(int(result_binary, 2))[2:].rstrip('L')
    print(hex_string)

if __name__ == "__main__":
    xor_2_strings(ORIGINAL, XOR)