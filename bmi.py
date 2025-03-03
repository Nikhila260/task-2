height=float(input("Enter your height in meters : "))
weight=float(input("Enter your weight in kg : "))
bmi=weight/(height **2)
def BMI(bmi):
    if bmi<=18:
        return 'underweight'
    elif (bmi>=18 and bmi<25):
        return'normal weight'
    elif bmi>25:
        return'overweight'
    else:
        return 'obese'
category=BMI(bmi)    
print(f"BMI:{bmi}({category})")
