import re 

#pattern=r'l.ve.'
#pattern=r'l\wvel\w'

#seq='level1'
#pattern=r'level: [1-9]'
#pattern=r'level: [^0]'
#seq='level: 1'

#pattern=r'levei?l1'
#seq='level1'

#pattern=r'\d{9,10}'
#seq='1258888889266654159'

pattern=r'[\w.-]+@[\w.]+'
seq='ibtissem_kadri@gmail.com'

match=re.search(pattern, seq)

if match:
	print ("found")
	print(match.group())
else:
	print("not found")


