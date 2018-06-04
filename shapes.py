"""Code to work with shapes"""

#define a list of valid shapes
valid_shapes = [None, None, None, 'triangle', 'square','pentagon', 'hexagon']

#first function
def shape(sides):
	side = int(sides)
	return valid_shapes['side']

def sides():
	for i in range(len(valid_shapes)):
		if valid_shapes[i] != None:
			print(('{0} has {1} sides').format(valid_shapes[i], i))

print('enter the name of a shape')
sides()
