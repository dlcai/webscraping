import re

content = '''Hello 1234567 World_This
is a Regex Demo'''

result = re.match(r'^He.*?(\d+).*?Demo$', content) # failed to match \n
print(result) # return None
#print(result.group(1))


result = re.match(r'^He.*?(\d+).*?Demo$', content, re.S) 
print(result)
print(result.group(1))
