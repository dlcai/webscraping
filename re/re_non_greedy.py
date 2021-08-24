import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^He.*(\d+).*Demo', content)
print(result)
print(result.group(1))

# .*? non-greedy match
result = re.match(r'^He.*?(\d+).*Demo', content)
print(result)
print(result.group(1))

# use .* at the end of string
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match(r'http.*?comment/(.*?)', content)
result2 = re.match(r'http.*?comment/(.*)', content)
print('result1:', result1.group(1))
print('result2:', result2.group(1))


