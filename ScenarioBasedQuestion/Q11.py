"""Please write a program to compress and decompress the string
"hello world!hello world!hello world!hello world!"."""

s = "hello world!hello world!hello world!hello world!"
word = "hello world!"
c = s.count(word)
compressed = str(c) + "*" + word
print(compressed)
print(s)
