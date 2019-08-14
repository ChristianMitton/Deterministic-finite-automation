graph = {}

states = input().split()
states.remove('states:')
symbols = input().split()
symbols.remove('symbols:')

for state in states:
	graph[state] = []

#User types 'begin rules'
flag = input()
while(True):
	flag = input().split()
	if(flag[0] == 'end_rules'):
		break;
	#handle rules
	currentNode = flag[0] #ex1: q0
	destination = flag[2] #ex1: q1
	edge = flag[4] #ex1: a

	edgePair = (edge, destination)
	array = graph.get(currentNode)
	array.append(edgePair)
	graph[currentNode] = array	

#end rules has been inputed	

#start
start = input().split()
start.remove("start:")
#final
final = input().split()
final.remove("final:")

'''
for key,value in graph.items():
	print("{}, {}".format(key,value))
'''

def checkIfNodeEdgePointsToNodeEdge(e1, e2):	
	for key,array in graph.items():
		for pair in array:
			edge1, dest = pair
			
			if edge1 == e1:				
				array2 = graph.get(dest)				
				for pair2 in array2:
					edge2,dest2 = pair2
					if edge2 == e2:					
						return True

	return False

stack = []

while(True):
	#For each input check if path is possible
	userInput = input()
	userInput = list(userInput)	
	validPath = True

	# Checking input begins at start node
	atStart = False

	for state in start:		
		currentNodeArray = graph.get(state)

		for pair in currentNodeArray:
			e,d = pair
			if e == userInput[0]:
				atStart = True
				break
		
	if atStart == True:		
		pass
	else:
		print("rejected")
		continue

	# Checking input begins at start node
	atFinal = False	

	for state in final:
		for node, nodeArray in graph.items():
			for pair in nodeArray:
				e,d = pair				
				if d == state:					
					if userInput[len(userInput)-1] == e:
						atFinal = True
						break


	if atFinal == True:		
		pass
	else:
		print("rejected")
		continue


	count = 1	

	for letter in userInput:		

		if count % 2 != 0 and len(stack) != 1:
			stack.append(letter)			
			count += 1
			continue
		
		stack.append(letter)
		
		letter2 = stack.pop()				
		letter1 = stack.pop()

		if checkIfNodeEdgePointsToNodeEdge(letter1, letter2) == True:
			stack.append(letter2)
		else:
			validPath = False
			break

		count += 1

	if validPath == False:
		print("rejected")
		stack = []
	else:
		print("accepted")
		stack = []



