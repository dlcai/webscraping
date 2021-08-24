import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match(r'^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group()) # the same as group(0) 
print(result.span())


content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group(0))
print(result.group(1))
print(result.span())
