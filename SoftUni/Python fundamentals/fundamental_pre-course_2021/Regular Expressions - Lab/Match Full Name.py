import re
data = input()
command = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
sequence = re.findall(command, data)
print(' '.join(sequence))
