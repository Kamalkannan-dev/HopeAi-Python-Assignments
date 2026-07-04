class multipleFunctions:
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def percentage():
        s1 = int(input("Subject1="))
        s2 = int(input("Subject2="))
        s3 = int(input("Subject3="))
        s4 = int(input("Subject4="))
        s5 = int(input("Subject5="))
        total = s1+s2+s3+s4+s5
        percentage = total/5
        return percentage

    def triangle():
        h = int(input("Height:"))
        b = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area = (h*b)/2
        print("Area of Triangle:",area)

        h1= int(input("Height1:"))
        h2= int(input("Height2:"))
        b1= int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = h1+h2+b1
        print("Perimeter of Triangle:",perimeter)

    def BMI():
        bmi = float(input("Enter Body mass index: "))
        if(bmi<18.5):
            print("Under Weight")
        elif(bmi>=18.5 and bmi<=24.9):
            print("Healthy Weight")
        elif(bmi>=25 and bmi<= 29.9):
            print("Over Weight")
        elif(bmi>=30 and bmi<=34.9):
            print("Obese class 1")
        elif(bmi>=35 and bmi<=39.9):
            print("Obese class 2")
        else:
            print("Obese class 3")

    def Elegible(gender, age):
        if(gender=="MALE"):
            if(age<=21):
                message = "NOT ELIGIBLE"
            else:
                message = "ELIGIBLE"
        if(gender == "FEMALE"):
            if(age<=18):
                message = "NOT ELIGIBLE"
            else:
                message = "ELIGIBLE"
        return message