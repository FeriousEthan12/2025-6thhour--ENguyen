#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and trying it to
#the right classification

#Code Here:

W = int(input("type in your weight kg : "))
H = int(input("type in your Height meters  : "))

BMI = W / (H**2)
if BMI >= 18.5:
    if BMI >= 24.9:

        if BMI >= 25:
            if BMI >= 30:
                print(BMI, "is Obese")
            else:
                print(BMI, "is Overweight")

    else:
        print(BMI, "is Normal weight")

else:
    print(BMI, "is Underweight")

