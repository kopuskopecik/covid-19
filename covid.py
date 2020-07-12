# Covid-19 risk
#Please answer below questions "Yes" or "No".
age = input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease? ")
immune = input("Is your immune system too weak?")

if age == "Yes" or chronic == "Yes" or immune == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")