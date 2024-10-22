# Dictionary of Shapes
my_shape = input("What shape do you want to add?")
my_shape_height = int(input("How tall is your shape?"))

shapes = {
    "Triangle": 8,
    "Circle": 15,
    "Square": 10,
	"Rectangle" : 12,
}

shapes[my_shape] = my_shape_height

print(shapes)

# Arborist
name = input("Which tree do you want to remove?")
trees = {
	"aspen" : 75,
	"pine" : 82,
	"maple" : 60,
	"oak" : 65,
	"willow" : 80,
	"cottonwood" : 100,	
}

trees.pop(name)
print(trees)