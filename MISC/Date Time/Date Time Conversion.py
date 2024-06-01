from datetime import datetime

value = '21 March 1991'
newdt = datetime.strptime(value, '%d %B %Y')
dateStr = datetime.strftime(newdt, '%Y-%m-%d')

print(newdt)
print(dateStr)


