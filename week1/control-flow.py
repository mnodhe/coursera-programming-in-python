bill_total = 210

discount1 = 10

if bill_total > 100 and bill_total<200:
    print("bill is greater than 100!")
    bill_total = bill_total-discount1
elif bill_total>200:
    print("bill is greater than 200")
    bill_total = bill_total-discount1
else:
    print("bill is less than 100")



print("Total bill: "+ str(bill_total))
