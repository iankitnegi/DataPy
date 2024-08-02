# Program to compress and decompress the string "hello world!hello world!hello world!hello world!"
# => import zlib

import zlib
str = "hello world!hello world!hello world!hello world!"

#compress the string
compressed_string = zlib.compress(str.encode())
print(compressed_string)

#decompres the sring
decompress_string = zlib.decompress(compressed_string).decode()
print(decompress_string)