#------------------------------------------------------------------------------------#
# Filename: nnsketcher.py
# Author: Urban Martin
# Description:
# NNsketcher is a simple tool for creating diagrams of fully
# connected neural networks using GraphViz.
#
#
# Modified from:
# https://github.com/martisak/dotnets/blob/master/dotnets.py
# Inspired by:
# https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/
#
# Thank you to Madhavun Candadai and Thiago G. Martins for these resources!
#------------------------------------------------------------------------------------#


#
# Finds index of central hidden layer
def get_middle_layer(num_hidden):
	if num_hidden == 1:
		return(1)
	elif (num_hidden % 2 == 0):
		return(int(round(num_hidden/2, 0)))  # even case
	else:
		return(int(round(num_hidden/2, 0) + 1))  # odd case


#
# Main function
def main():
	# Define layer properties
	input_layer = 5
	output_layer = 3
	hidden_layer = 8
	num_hidden = 10

	# Build list of layers
	layers = []
	layers.append(input_layer)
	layers.extend([hidden_layer] * num_hidden)
	layers.append(output_layer)


	# Define ranges and add labels appropriately
	num_leading = get_middle_layer(num_hidden) - 1
	num_following = num_hidden - get_middle_layer(num_hidden)
	layers_str = ["Input"] + ["none"] * num_leading + ["Hidden"] + ["none"] * num_following + ["Output"]
	layers_col = ["none"] + ["none"] * (len(layers) - 2) + ["none"]
	layers_fill = ["black"] + ["gray"] * (len(layers) - 2) + ["black"]

	# This section prints code to feed into GraphViz
	# Set style options
	penwidth = 15
	font = "Hilda 10"

	print("digraph G {")
	print("\tfontname = \"{}\"".format(font))
	print("\trankdir=LR")
	print("\tsplines=line")
	print("\tnodesep=.08;")
	print("\tranksep=1;")
	print("\tedge [color=black, arrowsize=.5];")  # original code
	print("\tnode [fixedsize=true,label=\"\",style=filled," + \
	    "color=none,fillcolor=gray,shape=circle]\n")

	# Define clusters
	for i in range(0, len(layers)):
	    print(("\tsubgraph cluster_{} {{".format(i)))
	    print(("\t\tcolor={};".format(layers_col[i])))
	    print(("\t\tnode [style=filled, color=white, penwidth={},"
	          "fillcolor={} shape=circle];".format(
	              penwidth,
	              layers_fill[i])))

	    print(("\t\t"), end=' ')

	    for a in range(layers[i]):
	        print("l{}{} ".format(i + 1, a), end=' ')

	    print(";")
	    if layers_str[i] != "none":
	    	print(("\t\tlabel = {};".format(layers_str[i])))

	    print("\t}\n")

	# Define nodes
	for i in range(1, len(layers)):
	    for a in range(layers[i - 1]):
	        for b in range(layers[i]):
	            print("\tl{}{} -> l{}{}".format(i, a, i + 1, b))

	print("}")


#
# Sentinel Function
if __name__ == '__main__':
	main()
