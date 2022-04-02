print ("Now We will calculate your marketing:\n\nPrices:\nTomato=3 NIS\ncucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n ")
Tomatos=int(input("Enter how many tomatos?\n"))
Cucumber=int(input("Enter how many Cucumber?\n"))
Chicken= int(input("Enter how many Chicken?\n"))
Cola= int(input("Enter how many Cola?\n"))

print("\nSummary of Your Order:\n------\ntomato:" + str(Tomatos) + "\ncucumbers:" + str(Cucumber) + "\ncola:" + str(Cola)+ "\nChicken: " + str(Chicken) )

sum1= Tomatos*3
sum2=Cucumber*2
sum3=Cola*4
sum4=Chicken*10
summary=sum1+sum2+sum3+sum4
print("\nYou Have To Pay:" + str(summary) + "NIS Without tax")
print("\nYou Have To Pay:" + str(summary*1.17) + "NIS With tax")




