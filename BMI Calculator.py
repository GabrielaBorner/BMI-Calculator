
print("Welcome to this handy dandy BMI calculator, the perfect tool to determine if you are fat or not! \n\n"
      "We will conveniently let you know if you are not eating enough, eating too much, way too much or just right! \n\n"
      "So please, before you pick your poison, how would you like to be told you are too fat:\n"
      )


def BMIcalcIMP():
    weightImp = int(input('Enter your weight in lbs: '))
    feet = int(input('Enter your height in feet:'))
    inches = int(input('Enter the remaining inches: '))
    heightImp = (feet * 12) + inches
    BMI = (weightImp * 703) / (heightImp * heightImp)

    if BMI < 18:
        print('Your BMI is ', "{:.1f}".format(BMI), ' which makes you underweight')
    elif BMI < 25:
        print('Your BMI is ', "{:.1f}".format(BMI), 'which makes you a rare breed of normal weight - Congratulations!')
    elif BMI < 30:
        print('Your BMI is ', "{:.1f}".format(BMI),
              ' which makes you overweight/fat - either lose weight or become obese')
    elif BMI < 35:
        print('Your BMI is ', "{:.1f}".format(BMI),
              ' which makes you Obese/Super fat - You better join the fat acceptance "movement"...')
    else:
        print('Danm you are so fat you fall off the BMI scale... No BMI for you!')


def BMIcalcMTR():
    weightMtc = int(input('Enter your weight in kg: '))
    heightMrc = int(input('Enter your height in cm: '))
    BMI = ((weightMtc / heightMrc) / (heightMrc)) * 10000

    if BMI < 18:
        print('Your BMI is ', "{:.1f}".format(BMI), ' which makes you underweight')
    elif BMI < 25:
        print('Your BMI is ', "{:.1f}".format(BMI), 'which makes you a rare breed of normal weight - Congratulations!')
    elif BMI < 30:
        print('Your BMI is ', "{:.1f}".format(BMI),
              ' which makes you overweight/fat - either lose weight or become obese')
    elif BMI < 35:
        print('Your BMI is ', "{:.1f}".format(BMI),
              ' which makes you Obese/Super fat - You better join the fat acceptance "movement"...')
    else:
        print('Danm you are so fat you fall off the BMI scale... No BMI for you!')


system = input('Type m for the metric scale, i for the imperial scale: ')



if system == "m":
    print(BMIcalcMTR())
elif system == "i":
    print(BMIcalcIMP())
else:
    input("To continue, type m for metric or i for imperial: ")
    print(system)


