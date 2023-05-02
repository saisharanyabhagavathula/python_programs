import turtle

# this procedure captures user inputs and returns a height,weight
def ask_user_inputs():
    height = float(input("Enter height in inches: "))
    weight = float(input("Enter weight in pounds: "))
    return height,weight

#BMI is calculated based on height & weight and returns bmi value
def calculate_bmi(height,weight):
    bmi = round((weight/(height * height)) * 703,2)
    #print(bmi)
    return bmi

# this procedure is most important aspect of the program where the logic is implemented
# BMI is calculated
# BMI category is identified using linear search of name value pairs
# Graph is display with corresponding color coding
def calculate_display_bmi(height,weight,t):
    bmi=calculate_bmi(height,weight)

    # storing bmi category name and max value in the category
    # used python dictionary as collection type
    bmi_name_values = {
    "Very severely underweight":15,
    "Severely underweight":16,
    "Underweight":18.5,
    "Normal":25,
    "Overweight":30,
    "Obese Class I":35,
    "Obese Class II":40,
    "Obese Class III":50
    }
    #identify bmi category using bmi_name_values
    bmi_category=""
    for key in bmi_name_values:
        if bmi > bmi_name_values[key]:
            #continue to search for next bmi range
            continue
        else:
            bmi_category=key
            break
    #print(bmi_category)
    # these steps display the bar graph
    #the bmi category is color coded
    #the category name and range is also displayed
    #max height of the graph set to 50
    maxheight = 50

    #total number of bmi categories are 8
    numbars = 8
    border = 10

    t.reset()
    t.clear()
    screen = turtle.Screen()
    #move to screen to bottom left
    screen.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)

    #set the background color to cyan
    screen.bgcolor("cyan")

    prev=0

    # all the bars are filled with white except the one that falls under the bmi category
    t.fillcolor("white")
    t.pensize(3)

    for key in bmi_name_values:
        t.fillcolor("white")
        value=bmi_name_values[key]
        #color coding based on the bmi value
        if bmi_category == key :
            if bmi > 25:
                t.fillcolor("red")
            elif bmi<18.5:
                t.fillcolor("yellow")
            else:
                t.fillcolor("blue")
        t.begin_fill()
        t.left(90)
        t.forward(value)
        list_of_strings=key.split()
        display_text=""
        for i in list_of_strings:
            display_text=display_text+i+"\n"
        #write the range and content in clear fashion
        t.write(str(prev)+"-"+str(value)+"\n"+display_text,font=("Comic Sans", 10,"bold"))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(value)
        t.left(90)
        t.end_fill()
        prev=bmi_name_values[key]

    t.penup()
    t.goto(15,40)
    #displays the BMI value on top of the screen
    t.write("\t\t\t         BMI value is "+str(bmi)+" -  Category is "+bmi_category, align="center", font=("Impact", 20))


# main procedure to loop under users press "n"
# call user input procedure
# calls calculate_display_bmi procedure with values of height and weight
def main():
    print("Hello!! this program calculates & displays BMI based on height and weight ")
    proceed = "y"
    #launch turtle screen
    t = turtle.Turtle()
    while proceed == "y":
        height,weight=ask_user_inputs()
        ###this is where the bmi calculation, display, and procedure is being called
        calculate_display_bmi(height,weight,t)
        proceed=input("Do you want to enter another person details (y/n)? ")

    print("Goodbye!")
    #close turtle screen
    turtle.bye()

if __name__ == "__main__":
    main()
