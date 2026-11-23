class Sample_Class():
    def Subfields():
        print('Sub-fields in AI are:')
        text='AI Sub fields'
        print('Machine Learning')
        text='AI Sub fields'
        print('Neural Networks')
        text='AI Sub fields'
        print('Vision')
        text='AI Sub fields'
        print('Robotics')
        text='AI Sub fields'
        print('Speech Processing')
        text='AI Sub fields'
        print('Natural Language Processing')
        text='AI Sub fields'
        return text

    def odd_even():
        number=int(input("Enter the any number"))
        if(number%2==1):
            print("Number is odd number")
            Num='odd character'
        else: 
            print("Number is even number")
            Num='even_odd'
            return Num   

    def marriage_eligibility():
        while True:
            Gender=str(input('Your Gender F/M:'))
            if Gender.isalpha():
             break    
            print('Invalid Input give only letters')
        Age=int(input('Your Age:'))
        if(Age>=21):
            print("ELIGIBLE")
            legal='Yes'
        else:
            print("NOT ELIGIBLE")
            legal='No'
        return legal      

    def percentage(Sub1,Sub2,Sub3,Sub4,Sub5):
            Total_Marks = (Sub1+Sub2+Sub3+Sub4+Sub5)
            print("Subject1:",Sub1)
            print("Subject2:",Sub2)
            print("Subject3:",Sub3)
            print("Subject4:",Sub4)
            print("Subject5:",Sub5)
            print("Total Marks:",Total_Marks)
            Percentage =(Total_Marks/500)*100
            print("Percentage",Percentage)
            Scored='Scores obtained successfully'
            return Scored

         
    def Area_of_Triangle(h1,h2,b):
        Area_Formula=print('Area of triangle=(Height*Breadth)/2')
        Area=(h1*b)/2
        print("Area caluculated:",Area)
        Perimeter_Formula=print('Perimeter of triangle = Height1+Height2+Breadth')
        Perimeter=(h1+h2+b)
        print("perimeter calculated:",Perimeter)
        return 'Area and Perimeter calculated'
     