import math

#function to print menu options
def menu():
    print('''
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average
                ''')

#function to get user input for menu option
def select():
    print("Enter Menu Selection: ", end='')
    choice = int(input())
    return choice

#function to get user input for both operands
def num_inputs(list):
    print("Enter first operand: ", end='')
    first_num = input()

    print("Enter second operand: ", end='')
    second_num = input()

    #compares input to string, if RESULT then replaces input with last result, else turns input to float
    if first_num.__eq__("RESULT"):
        first_num = list[-1]
    else:
        first_num = float(first_num)

    if second_num.__eq__("RESULT"):
        second_num = list[-1]
    else:
        second_num = float(second_num)

    return first_num, second_num #returns a tuple with the two user inputs


#main function
def main():

    #initialization
    result = 0.0
    all_results = [] #list with all results
    menu_selection = 0

    print("Current Result: ", result)
    print()

    menu()


    while menu_selection > -1:
        menu_selection = select()

        #invalid user selection for menu option
        if menu_selection < 0 or menu_selection > 7:
            print()
            print("Error: Invalid selection!")
            print()
            menu_selection = select()


        #end program
        if menu_selection == 0:

            print("Thanks for using this calculator. Goodbye!")
            break

        #addition
        if menu_selection == 1:
            output = num_inputs(all_results) #creates a tuple for the two user inputs returned by function

            #adds first and second index value of tuple
            result = output[0] + output[1]
            all_results.append(result) #appends result to list with all results
            print()
            print("Current Result: ", result)
            menu()

        #subtraction
        if menu_selection == 2:
            output = num_inputs(all_results)
            result = output[0] - output[1]
            all_results.append(result)
            print()
            print("Current Result: ", result)
            menu()

        #multiplication
        if menu_selection == 3:
            output = num_inputs(all_results)
            result = output[0] * output[1]
            all_results.append(result)
            print()
            print("Current Result: ", result)
            menu()

        #division
        if menu_selection == 4:
            output = num_inputs(all_results)
            result = output[0] / output[1]
            all_results.append(result)
            print()
            print("Current Result: ", result)
            menu()

        #expontentiation
        if menu_selection == 5:
            output = num_inputs(all_results)
            result = output[0] ** output[1]
            all_results.append(result)
            print()
            print("Current Result: ", result)
            menu()

        #logarithm
        if menu_selection == 6:

            output = num_inputs(all_results)
            result = math.log(output[1], (output[0])) #math.log(number, base)
            all_results.append(result)
            print()
            print("Current Result: ", result)
            menu()

        #average
        if menu_selection == 7:
            #if no results in list then error
            if len(all_results) == 0:
                print()
                print("Error: No calculations yet to average!")
                print()

            #if result in list then calculate sum, number of results, and average
            else:
                sum_result = 0.0
                num_result = 0
                #iterates through results list
                for i in all_results:
                    sum_result += i
                    num_result += 1
                print()
                print("Sum of calculations: ", sum_result,)
                print("Number of calculations: ", num_result)

                average = sum_result / num_result
                print("\nAverage of calculations: {:0.2f}\n".format(average))

                print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


