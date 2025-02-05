new = []
available_parts = ['mouse','keyboard','cables','disk','monitor','speaker']
choice = "-"
while(choice!='0'):
      
      

      if choice in '123456':
            print("Adding choice {}".format(choice))
            if(choice == '1'):
                  new.append('mouse')
            elif(choice == '2'):
                  new.append('keyboard')
            elif(choice == '3'):
                  new.append('cables')
            elif(choice == '4'):
                  new.append('disk')
            elif(choice =='5'):
                  new.append('monitor')
            elif(choice == '6'):
                  new.append('speaker')  
      else:
            # print("Please add option from the list :")
            # for parts in available_parts:
            #         print("{0}:{1}".format(available_parts.index(parts)+1,parts))
            print("Please add option from the list :")
            for number,parts in enumerate(available_parts):
                    print("{0}:{1}".format(number+1,parts))
      choice = input("Select number between 0 to 6\n")  
    
    
    

print(new)
    
    
       
        
        
      
