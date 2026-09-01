Taxable_Income = float(input("Enter your taxable income: "))
if Taxable_Income <= 20000:
    Tax_Rate = .02
    Tax_Amount = Taxable_Income * Tax_Rate
elif Taxable_Income <= 50000:
    Tax_Rate = 0.025
    Tax_Amount = 400 + (Taxable_Income - 20000) * Tax_Rate  
else:
    Tax_Rate = 0.035
    Tax_Amount = 1150 + (Taxable_Income - 50000) * Tax_Rate
print(f"Your tax amount is ${Tax_Amount}.")
