print('Hello, Django girls!')
if 3>2:
    print('It works!')	
if 5>2:
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')
name='Sonja'
if name=='Ola':
	print('Hey Ola!')
elif name=='Sonja':
	print('Hey Sonja!')
else: 
	print('Hey anonymous!')
def hi():
	print('Hi there!')
	print ('How are you?')
hi()
def hi(name):
	if name=='Ola':
		print('Hi Ola!')
	elif name=='Sonja':
		print('Hi Sonja!')
	else:
		print('Hi anonymous!')
hi("Ola")
def hi(name):
	print('Hi ' +  name + '!')
girls=['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
	hi(name)
	print('Next girl')
for i in range(1, 6):
	print (i)