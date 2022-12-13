#Student Course Selector(BTech Specific)
#Made by:
#SRN:PES1202202179 - Ankush S
#SRN:PES1202202543 - Akash Babu
#SRN:PES1202202305 - Anshuman Gokhale

cs=0
ec=0
ce=0
bt=0
mc=0

def pot():
    print("Your affinity towards Computer Science:",cs)
    print("Your affinity towards Electronics and Comms:",ec)
    print("Your affinity towards Civil Engineering:",ce)
    print("Your affinity towards Mechanical Engineering:",mc)
    print("Your affinity towards Biotechnology:",bt)


while cs<=8 and ec<=8 and ce<=8 and bt<=8 and mc<=8:
    
    ans=input("1.Do you like technology?: ")
    if(ans=='y'):
        cs+=1
        ec+=1
        mc+=1
    else:
        ce+=1
        bt+=1
    

    ans=input("2.Do you like cars?: ")
    if(ans=='y'):
        mc+=1
    else:
        cs+=1
        bt+=1
        ec+=1
        ce+=1
    

    ans=input("3.Do you like building homes in minecraft?: ")
    if(ans=='y'):
        ce+=1
        mc+=1
        cs+=1
    else:
        ec+=1
        bt+=1
    

    ans=input("4.Do you like to play with chemicals?: ")
    if(ans=='y'):
        bt+=1
    else:
        cs+=1
        ec+=1
        ce+=1
        mc+=1
    

    ans=input("5.Do you like fixing things rather than replacing?: ")
    if(ans=='y'):
        mc+=1
        ec+=1
        ce+=1
        cs+=1
    else:
        cs+=1
        bt+=1
    

    ans=input("6.Do you like to study plants and animals?: ")
    if(ans=='y'):
        bt+=1
    else:
        cs+=1
        mc+=1
        ec+=1
        ce+=1
    

    ans=input("7.Do you want to settle abroad?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
    else:
        ce+=1
        bt+=1
    

    ans=input("8.Do you like building things in lego?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
        ce+=1
    else:
        bt+=1
    

    ans=input("9.Do you open up broken machines to see what's inside?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
    else:
        ce+=1
        bt+=1
    
    
    ans=input("10.Do you want to find cures to new diseases?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
    else:
        ce+=1
        bt+=1
    

    ans=input("11.Have you ever wondered how humans think?: ")
    if(ans=='y'):
        cs+=1
        bt+=1
    else:
        ce+=1
        mc+=1
        ec+=1
    

    ans=input("12.Did you like the movie I,Robot?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
    else:
        ce+=1
        bt+=1
    
    
    ans=input("13.Do you like smart homes?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
        ce+=1
    else:
        bt+=1
    
    
    ans=input("14.Have you used any Linux distros before?: ")
    if(ans=='y'):
        cs+=1
        mc+=1
        ec+=1
    else:
        ce+=1
        bt+=1
    

    ans=input("15.Do you prioritze a high income over passion?: ")
    if(ans=='y'):
        cs+=1
        
    else:
        cs+=1
        mc+=1
        ec+=1
        ce+=1
        bt+=1


    pot()
ls=[cs,ec,mc,ce,bt]
max=max(ls)
if max==bt:
    print("Biotechnology is the right choice for you!")
if max==cs:
    print("Computer Science is the right choice for you!")
if max==ec:
    print("Electronics and Comminications is the right choice for you!")
if max==ce:
    print("Civil Engineering is the right choice for you!")
if max==mc:
    print("Mechanical Engineering is the right choice for you!")

ans=input("Do you wish to know your potential in the subjects? ")
if ans=='y':
    pot()