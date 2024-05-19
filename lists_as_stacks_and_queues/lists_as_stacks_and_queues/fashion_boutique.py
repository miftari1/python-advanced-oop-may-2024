#Creating a variable of type list(stack)to store the sequence of integers(the box of clothes)
clothes_stack = input().split()
#Creating a variable of type integer to store the number representing the capacity of one rack
rack_capacity = int(input())
#Creating a variable of type integer which stores the number of racks used
racks_counter = 1
#Creating a varible of type integer to store the sum\
#of the values of clothes at the current rack
sum_clothes = 0
#Starting a while loop through the stack which iterates\
#until there is elements(clothes) in iterate
while clothes_stack:
    #Initializing a variable of type integer which representates the current clothes
    current_clothing = int(clothes_stack[-1])
    #Creating an If Else statement to check if the sum of clothes\
    #is more or even to the capacity of the rack
    if sum_clothes + current_clothing > rack_capacity:
        #Increasing the racks counter with one and updating the\
        #sum counter to zero if the sum is higher than the capacity but the current clothing stays in the stack
        racks_counter += 1
        sum_clothes = 0
    elif sum_clothes + current_clothing == rack_capacity:
        #Increasing the racks counter with one and updating the\
        #sum counter to zero if the sum is equal to the capacity and we delete the current clothing from the stack
        sum_clothes = 0
        clothes_stack.pop()
        if clothes_stack:
            racks_counter += 1
    elif sum_clothes + current_clothing < rack_capacity:
        sum_clothes += int(clothes_stack.pop())

#Outputing the number of racks used
print(racks_counter)