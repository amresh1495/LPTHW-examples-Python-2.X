# Function to show that variables in a function are not connected to the variables in script.
# We can pass any variable as an arguement of the function just by using "=" sign.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses." % cheese_count
	print "You have %d boxes of crackers." % boxes_of_crackers
	print "Man that's enough for party !"
	print "Get a blanket \n"

print "We can just give the input directly."
cheese_and_crackers(20, 30)     #------ numbers as arguments

print "Or we can use variables from our script."
amount_of_cheese = 40;
amount_of_crackers = 50;

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  #------ new variables from the script passed as arguments

print "We can even do math inside !"
cheese_and_crackers(10 + 20, 10 + 30)     #------ math operation while passing the arguments

print "Or we can combine the variables with numbers."
cheese_and_crackers(amount_of_cheese + 32, amount_of_crackers + 34)   #------ variables and math combination in the function

