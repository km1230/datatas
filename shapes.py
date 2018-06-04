"""Code to work with shapes"""

#define a list of valid shapes
valid_shapes = [None, None, None, 'triangle', 'square','pentagon', 'hexagon']

#first function
def shape(sides):
	side = int(sides)
	return valid_shapes['side']

print('I know about the following shape')
for s in valid_shapes:
		if s is not None:
			print(s)