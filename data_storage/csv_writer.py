import csv
import pandas as pd

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])


# writer.writerows() 写入多行，传入二维列表
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', '20'],['10002', 'Bob', '22'], ['10003', 'Jordan', '21']])

# csv.DictWriter指定fieldnames, writeheader()后写入python dict
fieldnames = ['id', 'name', 'age']
with open('data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001', 'name':'Mike', 'age':20})
    writer.writerow({'id':'10002', 'name':'Bob', 'age':22})
    writer.writerow({'id':'10003', 'name':'Jordan', 'age':21})

with open('data.csv', 'a', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':'10004', 'name':'Durant', 'age':22})
    writer.writerow({'id':'10005', 'name':'王伟', 'age':22})

# csv.reader
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    for row in reader:
        print(row, type(row))

# pandas read_csv
df = pd.read_csv('data.csv')
print(df)
