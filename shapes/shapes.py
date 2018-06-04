#import the list from package named 'shapes' externally
from shapes import valid_shapes

#function
def shape(sides):
	side = int(sides)
	return valid_shapes['side']

def sides():
	for i in range(len(valid_shapes)):
		if valid_shapes[i] != None:
			print(('{0} has {1} sides').format(valid_shapes[i], i))

#main
print('enter the name of a shape')
sides()
