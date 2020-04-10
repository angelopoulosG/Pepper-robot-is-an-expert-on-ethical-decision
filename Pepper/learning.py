import matplotlib.pyplot as plt


cases = [
        'In this case, the self-driving car, with sudden brake failure, will continue ahead and crash into a concrete barrier  and it will result in the death of the 3 passengers (3 men) or the self-driving car will drive through a pedestrian crossing in the other lane and this  will result in the killing of the 3 pedestrians (3 women)',
        'In this case, the self-driving car, with sudden brake failure, will continue ahead and drive through pedestrians (2 women) crossing ahead or will swerve and drive through a pedestrian (1 man) crossing in the other lane.',
        'In this case, the self-driving car, with sudden brake failure, will swerve and drive through pedestrians (1 boy and 1 man) crossing in the other lane (Note that the affected pedestrians are flouting the law by crossing on the red signal.) or will continue ahead and crash into a concrete barrier and it will result in the death of the 2 elderly passengers.',
        'The self-driving car, with sudden brake failure, will continue ahead and drive through a pedestrian (1 woman) illegally crossing ahead or will swerve and drive through a pedestrian (1 man) crossing legally in the other lane.',
        'The self-driving car, with sudden brake failure, will continue ahead and drive through a pedestrian (1 child) crossing ahead or will swerve and crash into a concrete barrier and it will result in the death of the passenger (1 woman ).',
        'In this case, the self-driving car, with sudden brake failure, will swerve and drive through pedestrians (1 woman and 2 children) crossing in the other lane. or will continue ahead and crash into a concrete barrier and it will result in the death of the 2 passengers (1 woman and 1 child).'
        ]




           #.swerve.male.female.child.elder.followinglaw


a=[['','pas.0.3.0.0.0','ped.1.0.3.0.0.FL'],
   ['','ped.0.0.2.0.0.FL','ped.1.1.0.0.0.FL'],
   ['','ped.1.1.0.1.0.NL','pas.0.0.0.0.2'],
   ['','ped.0.0.1.0.0.NL','ped.1.1.0.0.0.FL'],
   ['','ped.0.0.0.1.0.FL','pas.1.0.1.0.0'],
   ['','ped.1.0.1.2.0.FL','pas.0.0.1.1.0']]



i,sumpas,passenger,sumlaw,law,sumsaving,saving,gender,sumgender,sumchild,sumelder,swerve,sumswerve=0,0,0,0,0,0,0,0,0,0,0,0,0

print("Hello, I am going to learn from your decisions. I am going to ask you some questions. Let's Start!")

for i in range(len(cases)):
    print(cases[i])
    
    
#getting user's answer
##########################################
    while True:
        try:
            data = int(raw_input('Enter your decision 1 or 2 : '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
    
        if data != 1 and data != 2:
            print("Sorry, your response must not be negative.")
            continue
        else:
            #we're ready to exit the loop.
            break    
##########################################    



#getting information about the case
##########################################        
    b=a[i]
    c=a[i]
    
    if data==1:        
        b=b[1]
        answer1 = b.split('.')
        c=c[2]
        answer2 = c.split('.')
    if data==2:  
        b=b[2]
        answer1 = b.split('.')
        c=c[1]
        answer2 = c.split('.')
    
    male1=int(answer1[2])
    female1=int(answer1[3])
    child1=int(answer1[4])
    elder1=int(answer1[5])
    sumpeople1 = male1+female1+child1+elder1 
    male2=int(answer2[2])
    female2=int(answer2[3])
    child2=int(answer2[4])
    elder2=int(answer2[5])
    sumpeople2 = male2+female2+child2+elder2 
    summale=male1+male2
    sumfemale=female1+female2
    sumchild=child1+child2
    sumelder=elder1+elder2
##########################################






##########################################
    if answer1[0] == 'ped' and answer2[0] == 'pas':
        sumpas=sumpas+1
        passenger=passenger+1
        if answer1[5] == 'FL':
            sumlaw=sumlaw-1
            law=law+1
        else:
            sumlaw=sumlaw+1
            law=law+1      

        if answer1[1] == '0':
            sumswerve=sumswerve+1
            swerve=swerve+1
        else:	
            sumswerve=sumswerve-1
            swerve=swerve+1              


        if sumpeople1 > sumpeople2:
            sumsaving =sumsaving -1
            saving=saving+1
            if ((male1 and female2) or (male2 and female1)):
                if male1>female1:
                    sum1=1
                elif male1<female1:
                    sum1=-1
                else:
                    sum1=0
                if male2>female2:
                    sum2=1
                elif male2<female2:
                    sum2=-1
                else:
                    sum2=0
                if sum1>sum2:
                    sumgender =sumgender-1
                    
                    gender=gender+1 
                elif sum1<sum2:
                    
                    sumgender =sumgender+1
                    
                    gender=gender+1
                else:
                    
                    sumgender =sumgender
                    gender=gender+1   


            
        elif sumpeople1 < sumpeople2:
            sumsaving =sumsaving +1
            saving =saving+1
        else:
            if ((male1 and female2) or (male2 and female1)):
                if male1>female1:
                    sum1=1
                elif male1<female1:
                    sum1=-1
                else:
                    sum1=0
                if male2>female2:
                    sum2=1
                elif male2<female2:
                    sum2=-1
                else:
                    sum2=0
                if sum1>sum2:
                    sumgender =sumgender-1
                    
                    gender=gender+1 
                elif sum1<sum2:
                    
                    sumgender =sumgender+1
                    
                    gender=gender+1
                else:
                    
                    sumgender =sumgender
                    gender=gender+1            
            
                       
                          
            
     
            
    elif answer1[0] == 'pas' and answer2[0] == 'ped':
        sumpas=sumpas-1
        passenger=passenger+1
        if answer2[5] == 'FL':
            sumlaw=sumlaw+1
            law=law+1
        else:
            sumlaw=sumlaw-1
            law=law+1     
    
        if answer1[1] == '0':
            sumswerve=sumswerve+1
            swerve=swerve+1
        else:
            sumswerve=sumswerve-1
            swerve=swerve+1     
            
        if sumpeople1 > sumpeople2:
            sumsaving =sumsaving -1
            saving=saving+1
            if ((male1 and female2) or (male2 and female1)):
                if male1>female1:
                    sum1=1
                elif male1<female1:
                    sum1=-1
                else:
                    sum1=0
                if male2>female2:
                    sum2=1
                elif male2<female2:
                    sum2=-1
                else:
                    sum2=0
                if sum1>sum2:
                    sumgender =sumgender-1
                    
                    gender=gender+1 
                elif sum1<sum2:
                    
                    sumgender =sumgender+1
                    
                    gender=gender+1
                else:
                    
                    sumgender =sumgender
                    gender=gender+1   


            
        elif sumpeople1 < sumpeople2:
            sumsaving =sumsaving +1
            saving =saving+1
        else:
            if ((male1 and female2) or (male2 and female1)):
                if male1>female1:
                    sum1=1
                elif male1<female1:
                    sum1=-1
                else:
                    sum1=0
                if male2>female2:
                    sum2=1
                elif male2<female2:
                    sum2=-1
                else:
                    sum2=0
                if sum1>sum2:
                    sumgender =sumgender-1
                    
                    gender=gender+1 
                elif sum1<sum2:
                    
                    sumgender =sumgender+1
                    
                    gender=gender+1
                else:
                    
                    sumgender =sumgender
                    gender=gender+1              
            
                                    
            
            
            
            
    else:


        if answer1[5] == 'FL':
            sumlaw=sumlaw-1
            law=law+1
        else:
            sumlaw=sumlaw+1
            law=law+1           
            
        if answer1[1] == '0':
            sumswerve=sumswerve+1
            swerve=swerve+1
        else:
            sumswerve=sumswerve-1
            swerve=swerve+1                 
            
            
        if sumpeople1 > sumpeople2:
            sumsaving =sumsaving -1
            saving=saving+1
            if ((male1 and female2) or (male2 and female1)):
                if male1>female1:
                    sum1=1
                elif male1<female1:
                    sum1=-1
                else:
                    sum1=0
                if male2>female2:
                    sum2=1
                elif male2<female2:
                    sum2=-1
                else:
                    sum2=0
                if sum1>sum2:
                    sumgender =sumgender-1
                    
                    gender=gender+1 
                elif sum1<sum2:
                    
                    sumgender =sumgender+1
                    
                    gender=gender+1
                else:
                    
                    sumgender =sumgender
                    gender=gender+1   


            
        elif sumpeople1 < sumpeople2:
            sumsaving =sumsaving +1
            saving =saving+1
        else:
            if ((male1 and female2) or (male2 and female1)):
                if male1>female1:
                    sum1=1
                elif male1<female1:
                    sum1=-1
                else:
                    sum1=0
                if male2>female2:
                    sum2=1
                elif male2<female2:
                    sum2=-1
                else:
                    sum2=0
                if sum1>sum2:
                    sumgender =sumgender-1
                    
                    gender=gender+1 
                elif sum1<sum2:
                    
                    sumgender =sumgender+1
                    
                    gender=gender+1
                else:
                    
                    sumgender =sumgender
                    gender=gender+1              
            
                                  
            
            
  
            



    i=+1
##########################################

 


sumpas = sumpas /passenger
if law:
    sumlaw = sumlaw /law
else:
    sumlaw=0

if law:
    sumlaw = sumlaw /law
else:
    sumlaw=0

if saving:
    sumsaving = sumsaving /saving
else:
    sumsaving=0


if swerve:
    sumswerve= sumswerve /swerve
else:
    sumswerve=0



plt.style.use('dark_background')
x=[-1 ,1]
y=[ 0,0]
plt.yticks([])
plt.plot(x,y, 'r-')
plt.plot(sumpas,0.1,'go',label="Protecting Passengers")
plt.plot(sumlaw,0.2,'bo',label="Upholding the law")
plt.plot(sumsaving,0.3,'ro',label="Saving more lives")
plt.plot(sumswerve,0.4,'yo',label="Avoiding Intervention")
plt.xlabel("Doesn't matter           -            Matters a lot")
plt.axis('equal')
plt.legend()
plt.show()




if (sumpas>=-0.25 and sumpas<=0.25):
    weight_sumpas=2
elif (sumpas>-0.75 and sumpas<-0.25):
    weight_sumpas=1
elif (sumpas>=-1 and sumpas<=-0.75):
    weight_sumpas=0
elif (sumpas>0.25 and sumpas<0.75):
    weight_sumpas=3
else:
    weight_sumpas=4

if (sumlaw>=-0.25 and sumlaw<=0.25):
    weight_sumlaw=2
elif (sumlaw>-0.75 and sumlaw<-0.25):
    weight_sumlaw=1
elif (sumlaw>=-1 and sumlaw<=-0.75):
    weight_sumlaw=0
elif (sumlaw>0.25 and sumlaw<0.75):
    weight_sumlaw=3
else:
    weight_sumlaw=4    
    
if (sumsaving>=-0.25 and sumsaving<=0.25):
    weight_sumsaving=2
elif (sumsaving>-0.75 and sumsaving<-0.25):
    weight_sumsaving=1
elif (sumsaving>=-1 and sumsaving<=-0.75):
    weight_sumsaving=0
elif (sumsaving>0.25 and sumsaving<0.75):
    weight_sumsaving=3
else:
    weight_sumsaving=4      


if (sumgender>=-0.25 and sumgender<=0.25):
    weight_sumgender=2
elif (sumgender>-0.75 and sumgender<-0.25):
    weight_sumgender=1
elif (sumgender>=-1 and sumgender<=-0.75):
    weight_sumgender=0
elif (sumgender>0.25 and sumgender<0.75):
    weight_sumgender=3
else:
    weight_sumgender=4   


if (sumswerve>=-0.25 and sumswerve<=0.25):
    weight_sumswerve=2
elif (sumswerve>-0.75 and sumswerve<-0.25):
    weight_sumswerve=1
elif (sumswerve>=-1 and sumswerve<=-0.75):
    weight_sumswerve=0
elif (sumswerve>0.25 and sumswerve<0.75):
    weight_sumswerve=3
else:
    weight_sumswerve=4   





##################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################
########################################################################################################################################################################
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################

while True:
    
    if weight_sumpas == weight_sumlaw:
        print("The self-driving car, with sudden brake failure, will drive through a pedestrian crossing in the lane legally and will save the passenger.")
        print("Do you agree?")
    #getting user's answer
    ##########################################
        while True:
            try:
                data = (raw_input('Enter your decision y or n : '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        
            if data != 'y' and data != 'n':
                print("Sorry, your response must be Y or n.")
                continue
            else:
                #we're ready to exit the loop.
                break    
    ##########################################   
        if  data == 'y':
            weight_sumpas=weight_sumpas+1
            weight_sumlaw=weight_sumlaw-1
            
        else:
            weight_sumpas=weight_sumpas-1
            weight_sumlaw=weight_sumlaw+1
    
    ##########################################
    ##########################################
    ##########################################
                
                
                
    elif weight_sumpas == weight_sumsaving:
        print("The self-driving car, with sudden brake failure, will drive through two pedestrians crossing and will save the passenger.")
        print("Do you agree?")
    #getting user's answer
    ##########################################
        while True:
            try:
                data = (raw_input('Enter your decision y or n : '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        
            if data != 'y' and data != 'n':
                print("Sorry, your response must be Y or n.")
                continue
            else:
                #we're ready to exit the loop.
                break    
    ##########################################   
        if  data == 'y':
            weight_sumpas=weight_sumpas+1
            weight_sumsaving=weight_sumsaving-1
            
        else:
            weight_sumpas=weight_sumpas-1
            weight_sumsaving=weight_sumsaving+1
                
                
                
                
    ##########################################
    ##########################################
    ##########################################            
    
    elif weight_sumsaving == weight_sumlaw:
        print("The self-driving car, with sudden brake failure, will drive through three pedestrian crossing in the lane ilegally and will save another pedestrian who is crossing legally.")
        print("Do you agree?")
    #getting user's answer
    ##########################################
        while True:
            try:
                data = (raw_input('Enter your decision y or n : '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        
            if data != 'y' and data != 'n':
                print("Sorry, your response must be Y or n.")
                continue
            else:
                #we're ready to exit the loop.
                break    
    ##########################################   
        if  data == 'y':
            weight_sumsaving=weight_sumsaving-1
            weight_sumlaw=weight_sumlaw+1
            
        else:
            weight_sumsaving=weight_sumsaving+1
            weight_sumlaw=weight_sumlaw-1


    ##########################################
    ##########################################
    ##########################################  


    elif weight_sumswerve == weight_sumlaw:
        print("The self-driving car, with sudden brake failure, will swerve and drive through a pedestrian crossing in the other lane ilegally and will save another pedestrian who is crossing your lane legally.")
        print("Do you agree?")
    #getting user's answer
    ##########################################
        while True:
            try:
                data = (raw_input('Enter your decision y or n : '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        
            if data != 'y' and data != 'n':
                print("Sorry, your response must be Y or n.")
                continue
            else:
                #we're ready to exit the loop.
                break    
    ##########################################   
        if  data == 'y':
            weight_sumswerve=weight_sumswerve-1
            weight_sumlaw=weight_sumlaw+1
            
        else:
            weight_sumswerve=weight_sumswerve+1
            weight_sumlaw=weight_sumlaw-1


    ##########################################
    ##########################################
    ##########################################   


    elif weight_sumswerve == weight_sumsaving:
        print("The self-driving car, with sudden brake failure, will swerve and drive through a pedestrian crossing in the other lane and will save three pedestrians who is crossing your lane.")
        print("Do you agree?")
    #getting user's answer
    ##########################################
        while True:
            try:
                data = (raw_input('Enter your decision y or n : '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        
            if data != 'y' and data != 'n':
                print("Sorry, your response must be Y or n.")
                continue
            else:
                #we're ready to exit the loop.
                break    
    ##########################################   
        if  data == 'y':
            weight_sumswerve=weight_sumswerve-1
            weight_sumsaving=weight_sumsaving+1
            
        else:
            weight_sumswerve=weight_sumswerve+1
            weight_sumsaving=weight_sumsaving-1


    ##########################################
    ##########################################
    ##########################################  

    elif weight_sumswerve == weight_sumpas:
        print("The self-driving car, with sudden brake failure, will swerve and drive through a pedestrian crossing in the other lane and will save the passenger.")
        print("Do you agree?")
    #getting user's answer
    ##########################################
        while True:
            try:
                data = (raw_input('Enter your decision y or n : '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        
            if data != 'y' and data != 'n':
                print("Sorry, your response must be Y or n.")
                continue
            else:
                #we're ready to exit the loop.
                break    
    ##########################################   
        if  data == 'y':
            weight_sumswerve=weight_sumswerve-1
            weight_sumpas=weight_sumpas+1
            
        else:
            weight_sumswerve=weight_sumswerve+1
            weight_sumpas=weight_sumpas-1


    ##########################################
    ##########################################
    ##########################################  
    
        
    else:
        break









x=[ 0,4]
y=[ 0,0]
plt.yticks([])
plt.plot(x,y, 'r-')
plt.plot(weight_sumpas,0.1,'go',label="Protecting Passengers")
plt.plot(weight_sumlaw,0.1,'bo',label="Upholding the law")
plt.plot(weight_sumsaving,0.1,'ro',label="Saving more lives")
plt.plot(weight_sumswerve,0.1,'yo',label="Avoiding Intervention")
plt.xlabel("Doesn't matter           -            Matters a lot")

plt.axis('equal')
plt.legend()
plt.show()





























