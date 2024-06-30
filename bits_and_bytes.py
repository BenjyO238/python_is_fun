# bytes and strings
def string_to_bytes(text):
    byte_array = text.encode('utf-8')
    print(f"'{text}' as bytes: {byte_array}")
    print("Individual byte values:")
    for byte in byte_array:
        print(f"{byte:08b}", end=" ")

word = 'a'
# Example usage
string_to_bytes(word)
# string_to_bytes("Hello, World!")