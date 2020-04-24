class Learning:    
    
    def __init__(self, answer):
        self.answer= answer    

    def learn(self):
        #.swerve.male.female.child.elder.followinglaw      
        a=[['','pas.0.3.0.0.0','ped.1.0.3.0.0.FL'],
           ['','ped.0.0.2.0.0.FL','ped.1.1.0.0.0.FL'],
           ['','ped.1.1.0.1.0.NL','pas.0.0.0.0.2'],
           ['','ped.0.0.1.0.0.NL','ped.1.1.0.0.0.FL'],
           ['','ped.0.0.0.1.0.FL','pas.1.0.1.0.0'],
           ['','ped.1.0.1.2.0.FL','pas.0.0.1.1.0']]
        i,sumpas,passenger,sumlaw,law,sumsaving,saving,gender,sumgender,sumchild,sumelder,swerve,sumswerve=0,0,0,0,0,0,0,0,0,0,0,0,0
        for i in range(6):
        #getting user's answer
        ##########################################
            if 	(self.answer[i]== "first"):
                data=1
            if 	(self.answer[i]== "second"):
                data=2       
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
#            summale=male1+male2
#            sumfemale=female1+female2
#            sumchild=child1+child2
#            sumelder=elder1+elder2
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
        sumpas = sumpas //passenger
        if law:
            sumlaw = sumlaw /law
        else:
            sumlaw=0
        
        if law:
            sumlaw = sumlaw //law
        else:
            sumlaw=0
        
        if saving:
            sumsaving = sumsaving //saving
        else:
            sumsaving=0
        if swerve:
            sumswerve= sumswerve //swerve
        else:
            sumswerve=0
           ##########################################
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
        return weight_sumpas, weight_sumlaw, weight_sumsaving, weight_sumswerve