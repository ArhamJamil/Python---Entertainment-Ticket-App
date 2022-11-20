var_ticketType = ['One Adult', 'One Child', 'One Senior', 'familyTicket', 'GroupsTicket']
var_CostForOneDay = [20.00, 12.00, 16.00, 60.00, 15.00]
var_CostForTwoDay = [30.00, 18.00, 24.00, 90.00, 22.50]
var_ExtraAtrractionChoice = ['lion feeding','penguin feeding', 'barbeque(only two day ticket)']
var_CostPerPerson = [2.50, 2.00, 5.00]
bookingID = 0
totalCostOneDay = 0
totalCostTwoDay = 0

Num_adults = 0
Num_childs = 0
Num_seniors = 0
Num_family = 0
Num_groups = 0

AttractionCost1 =0
AttractionCost2 = 0
AttractionCost3 = 0

totalCostWithAttraction1=0
totalCostWithAttraction2=0
totalCostWithAttraction3=0



# TASK 1 :
print("Welcome To Wild Life System !!!")
print("Options For Tickets Are below :")
for count in range(0,5):
    print("Ticket type :" ,var_ticketType[count],":", " Cost-OneDay is: $", var_CostForOneDay[count], " &", " Cost-TwoDay is: $", var_CostForTwoDay[count])
print("\n","Extraction Attraction available are :" )
for count in range(0,3):
    print(count+1, var_ExtraAtrractionChoice[count],": " "Cost For One Person is: $", var_CostPerPerson[count])
# TASK 2 :
print("\n","Do you want to Buy Ticket (1:Yes(Y), 2:No(N))")
var_inpYorN = int(input())
while var_inpYorN !=1:
    if var_inpYorN >2 or var_inpYorN <=0:
        print("Please press, '1':Yes , '2':No ")
        var_inpYorN = int(input())
    if var_inpYorN == 2:
        print("Thanks , Exiting . . . . .")
        break     
    
while var_inpYorN == 1 :
        
        print("\nEnter The Day for booking: 1-OneDay, 2-TwoDay ")
        var_InpBookingDay = int(input())
        bookingID = bookingID +1
    
        print("\nEnter Number of tickets for Type: ", var_ticketType[0])
        Num_adults = int(input())
        print("\nEnter Number of tickets for Type: ", var_ticketType[1])
        Num_childs = int(input())
        print("\nEnter Number of tickets for Type: ", var_ticketType[2])
        Num_seniors = int(input())
        print("\nEnter Number of tickets for Type: ", var_ticketType[3])
        Num_family = int(input())
        print("\nEnter Number of tickets for Type: ", var_ticketType[4])
        Num_groups = int(input())
        
        if var_InpBookingDay == 1:
            cost_adults = Num_adults*var_CostForOneDay[0]
            cost_childs = Num_childs*var_CostForOneDay[1]
            cost_seniors = Num_seniors*var_CostForOneDay[2]
            cost_family = Num_family*var_CostForOneDay[3]
            cost_groups = Num_groups*var_CostForOneDay[4]
            totalCostOneDay = (cost_adults+cost_childs+cost_seniors+cost_family+cost_groups)
            print("\nThe Total cost for all tickets without any extra attraction is", totalCostOneDay, "and your bookind Id is", bookingID)
        if var_InpBookingDay == 2:
            cost_adults = Num_adults*var_CostForTwoDay[0]
            cost_childs = Num_childs*var_CostForTwoDay[1]
            cost_seniors = Num_seniors*var_CostForTwoDay[2]
            cost_family = Num_family*var_CostForTwoDay[3]
            cost_groups = Num_groups*var_CostForTwoDay[4]
            totalCostTwoDay = (cost_adults+cost_childs+cost_seniors+cost_family+cost_groups)
            print("\nThe Total cost for all tickets without any extra attraction is", totalCostTwoDay, "and your bookind Id is", bookingID)
    
        if var_InpBookingDay > 2 or var_InpBookingDay < 0:
            print("Plz enter : 1 = Yes or 2 = No")
            print("Enter The Day for booking: 1-OneDay, 2-TwoDay ")
            var_InpBookingDay = int(input())
        
        print("Do You want any Extra Attraction: 1:(YES), 2:(NO) ")
        var_inpAttraction = int(input())
        
        while var_inpAttraction !=1:
            if var_inpAttraction >2 or var_inpAttraction <=0:
                print("Please press, '1':Yes , '2':No ")
                var_inpAttraction = int(input())
            if var_inpAttraction == 2:
                print("ok")
                break
        
        while var_inpAttraction == 1:
            var_personInp = int(input('Enter Number of person  '))
            print("Do you want attraction:", var_ExtraAtrractionChoice[0]," 1:(YES), 2:(NO) ")
            var_AttractionChoiceInp1 = int(input())
            while var_AttractionChoiceInp1 !=1:
                if var_AttractionChoiceInp1 >2 or var_AttractionChoiceInp1 <=0:
                    print("Please press, '1':Yes , '2':No ")
                    var_AttractionChoiceInp1 = int(input())
                if var_AttractionChoiceInp1 == 2:
                    print("ok")
                    break
            if var_AttractionChoiceInp1 == 1:
                AttractionCost1 = var_personInp*var_CostPerPerson[0]
                totalCostWithAttraction1 = AttractionCost1 + totalCostOneDay + totalCostTwoDay
                print("\nThe Total cost for all tickets with extra attraction",var_ExtraAtrractionChoice[1], "is", AttractionCost1, "bookingID:", bookingID)
            
            
            
            print("Do you want attraction:", var_ExtraAtrractionChoice[1]," 1:(YES), 2:(NO) ")
            var_AttractionChoiceInp2 = int(input())
            while var_AttractionChoiceInp2 !=1:
                if var_AttractionChoiceInp2 >2 or var_AttractionChoiceInp2 <=0:
                    print("Please press, '1':Yes , '2':No ")
                    var_AttractionChoiceInp2 = int(input())
                if var_AttractionChoiceInp2 == 2:
                    print("ok")   
                    break    
            if var_AttractionChoiceInp2 == 1:
                AttractionCost2 = var_personInp*var_CostPerPerson[1]
                totalCostWithAttraction2 = AttractionCost2 + totalCostOneDay + totalCostTwoDay
                print("\nThe Total cost for extra attraction",var_ExtraAtrractionChoice[1], "is", AttractionCost2, "bookingID:", bookingID)
              
            
            print("Do you want attraction:", var_ExtraAtrractionChoice[2]," 1:(YES), 2:(NO) ")
            var_AttractionChoiceInp3 = int(input())
            while var_AttractionChoiceInp3 !=1:
                if var_AttractionChoiceInp3 >2 or var_AttractionChoiceInp3 <=0:
                    print("Please press, '1':Yes , '2':No ")
                    var_AttractionChoiceInp3 = int(input())
                if var_AttractionChoiceInp3 == 2:
                    print("ok")   
                    break
            if var_AttractionChoiceInp3 == 1 and var_InpBookingDay == 1:
                    print("Sorry the attraction:", var_ExtraAtrractionChoice[2],"is a two day ticket" )
    
            if var_AttractionChoiceInp3 == 1 and var_InpBookingDay ==2:
                    AttractionCost3 = var_personInp*var_CostPerPerson[2]
                    totalCostWithAttraction3 = AttractionCost3 + totalCostTwoDay
                    print("The Total cost for extra attraction",var_ExtraAtrractionChoice[2], "is", AttractionCost3, "bookingID:", bookingID)
            
            
            if var_InpBookingDay == 1:
                totalCostWithAttraction = AttractionCost1 + AttractionCost2 + AttractionCost3 + totalCostOneDay
                print("\nThe Total cost for all tickets with $", totalCostWithAttraction, " and your bookind Id is", bookingID)
            if var_InpBookingDay == 2:
                totalCostWithAttraction = AttractionCost1 + AttractionCost2 + AttractionCost3 + totalCostTwoDay
                print("\nThe Total cost for all tickets with $", totalCostWithAttraction, " and your bookind Id is", bookingID)
            break
        print("\n","Do you want to Buy Ticket (1:Yes(Y), 2:No(N))")
        var_inpYorN = int(input())
        while var_inpYorN !=1:
            if var_inpYorN >2 or var_inpYorN <=0:
                print("Please press, '1':Yes , '2':No ")
                var_inpYorN = int(input())
            if var_inpYorN == 2:
                print("Thanks , Exiting . . . . .")
                break      
            
            

                    
            
                       
            
            
            
                  
                            
                            
                        
                
                
                
                
        