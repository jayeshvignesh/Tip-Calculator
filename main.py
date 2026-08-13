print("Welcome to tip calculator.")
(total_bill)=input("What is the total bill? ")
tip_percentage=input ("What percentage tip would like to give? ")
people_splitting_with=input("How many people are you splitting the bill with? ")
total_bill=float(total_bill)
tip_percentage=float(tip_percentage)
people_splitting_with=float(people_splitting_with)
tip_amount=total_bill*tip_percentage/100
payment=total_bill+tip_amount
payment_per_person=round (payment/people_splitting_with, 2)
payment_per_person="{:.2f}".format (payment_per_person)
print(f"Each person has to pay $ {payment_per_person}.")