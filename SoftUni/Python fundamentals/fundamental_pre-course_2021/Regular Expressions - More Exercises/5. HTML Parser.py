import re

data = input()

title = re.finditer(r"(?<=<title>).+(?=</title>)", data)
for s in title:
    title = s.group()
print(f"Title: {title}")

body_regex = r'<body>.*<\/body>' # Само body
body = re.findall(body_regex, data)
body = ''.join(body)

content_regex = r">([^><]*)<"# Прави го на лист, но с \\n

content = re.findall(content_regex, body)

content = ''.join(content)
content = content.replace('\\n', '') # за да махнем n

print(f"Content: {content}")
