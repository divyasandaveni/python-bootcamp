#how many fruits r there in my data not in memebership
data=[1,8,'apple','carrot','mango']
fruits=['apple','mango','orange','watermelon']
veggies=['tomato','beans','carrot','onions']

for i in data: 
  if i not in fruits:

    print(i)   

   #how many obj r there in veggies but nou in fruits:

for i in data:
  if i in veggies and i not in fruits:
    print(i) 