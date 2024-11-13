import time

name = input("What is your name? ")
print("Hi! " + name)
time.sleep(1)
print("Lets see how much carbon emmisions you put out!")
print(" ")
time.sleep(1.5)

#Now we will ask user about how much they drive
car_q = input("What vehicle do you drive? 1.) Truck 2.) Car 3.) Suv 4.) Electric? (Answer with #)")
print(" ")
car_q = int(car_q)
if car_q == 1:
  gasoline_q = input("How many miles do you drive per week? ")
  print(" ")
  gasoline_q = int(gasoline_q)
  gasoline_q = gasoline_q * 52
  gasoline_q = gasoline_q/18
  gasoline_a = gasoline_q * 1/42 * 431.87 * 1/1000
  gasoline_a = gasoline_a * 2204.63
  gasoline_a = round(gasoline_a, ndigits = 0)
  gasoline_a = str(gasoline_a)
  print("You are emitting " + gasoline_a + " pounds of carbon emmisions from your car use in a year.")
  print(" ")
  gasoline_a = float(gasoline_a)
elif car_q == 2:
  gasoline_q = input("How many miles do you drive per week? ")
  print(" ")
  gasoline_q = int(gasoline_q)
  gasoline_q = gasoline_q * 52
  gasoline_q = gasoline_q/24.2
  gasoline_a = gasoline_q * 1/42 * 431.87 * 1/1000
  gasoline_a = gasoline_a * 2204.63
  gasoline_a = round(gasoline_a, ndigits = 0)
  gasoline_a = str(gasoline_a)
  print("You are emitting out " + gasoline_a + " pounds of carbon emmisions from your car use in a year.")
  print(" ")
  gasoline_a = float(gasoline_a)
elif car_q == 3:
  gasoline_q = input("How many miles do you drive per week? ")
  print(" ")
  gasoline_q = int(gasoline_q)
  gasoline_q = gasoline_q * 52
  gasoline_q = gasoline_q/17
  gasoline_a = gasoline_q * 1/42 * 431.87 * 1/1000
  gasoline_a = gasoline_a * 2204.63
  gasoline_a = round(gasoline_a, ndigits = 0)
  gasoline_a = str(gasoline_a)
  print("You are emitting " + gasoline_a + " pounds of carbon emmisions from your car use in a year.")
  print(" ")
  gasoline_a = float(gasoline_a)
elif car_q == 4:
  gasoline_q = input("How many miles do you drive per week? ")
  print(" ")
  gasoline_q = int(gasoline_q)
  gasoline_q = gasoline_q * 52
  gasoline_q = gasoline_q/24.2
  gasoline_q = gasoline_q/31
  gasoline_a = gasoline_q * 1/42 * 431.87 * 1/1000
  gasoline_a = gasoline_a * 2204.63
  gasoline_a = round(gasoline_a, ndigits = 0)
  gasoline_a = str(gasoline_a)
  print("You are emitting " + gasoline_a + " pounds of carbon emmisions from your car use in a year.")
  print(" ")
time.sleep(2)
gasoline_a = float(gasoline_a)
time.sleep(4)


#Now we will ask user for about how much electricity they use
print("Now lets find out how many emmisions you put out by using electricity")
print(" ")
time.sleep(3.55)
eq1 = input("How much do you spend on your electricity bill every month? $")
print(" ")
eq1 = int(eq1)
eq1 = eq1*12
eq1 = eq1 / 9.37
eq1a = eq1 * 884.2 * (1/(1-0.073)) * 1/1000 * 1/2204.6
eq1a = eq1a * 2204.63
eq1a = round(eq1a, ndigits = 0)
eq1a = str(eq1a)
print("You are emitting " + eq1a + " pounds of carbon emmisions from your home's electricity usage in a year.")
print(" ")
eq1a = float(eq1a)
print("May seem small but this alone starts to add up over the course of a year")
print(" ")
time.sleep(2)



#Now we will ask the user for the natural gas 
print("Finally we will see how much carbon emmsion you put out based on your natural gas usage")
print(" ")
time.sleep(2.5)
ng = input("How many square feet is your house? ")
print(" ")
ng = int(ng)
ng1 = input("How high are your ceilings?(In feet) ")
print(" ")
ng1 = int(ng1)
ng2 = ng1 * ng
nga = ng2 * 0.0551 * 1/1000
nga = nga * 2204.63
nga = round(nga, ndigits = 0)
nga = str(nga)
print("From your natural gas usage in your house, you have emmitted " + nga + " pounds of carbon emmisions.")
nga = float(nga)
print(" ")

answer = gasoline_a + eq1a + ng1 
answer = str(answer)
print("Your total amount of carbon emmsions in pounds in one year is " + answer)
print(" ")
print(" ")
print(" ")

time.sleep(4)

#This is a transiton to the future
print("Since we now know how many pounds of carbon emmisions that you are emitting, we can start to look at how you can help it.")

#We now start talking about the future
time.sleep(3.5)
print(" ")
print("    ###    ")
print("  #######  ")
print("  #######  ")
print("  #######  ")
print("    ###    ")
print("    [|]    ")
print("    [|]    ")
print("    [|]    ")
print("   [|||]   ")
print("* Tree of Life *")
time.sleep(3.5)
print("")
print("")
print("")
print("")
print("Your total carbom emissions: " + answer)
print("")
x = 9977
answer = float(answer)
difference = x - answer
if difference < 0:
  difference = difference * -1
difference = str(difference)
if answer > x:
  print("You are emmiting " + difference + " lbs. more than the average person in the New Orleans area." )
elif answer < x:
  print("You are emitting " + difference + " lbs. less than the average person in the New Orleans area")
else:
  print("You are emmiting the same amount of carbon emmsions as the average person in the New Orleans area.")
x = str(x)

print("Avg. total carbon emmisions of one person in the New Orleans area is " + x)
print("")
print("")
print("This polluted air is not something that should be taken lightly. This is the air that you breathe every single day and can be cause of you and or your loved ones illness. Carbon dioxide is a green house gas and green house gases trap heat and lead to global warming. But you can very quickly start to reduce your emmsions.One big way can start to reduce your carbon emmisons is by recycling. ")

print("")