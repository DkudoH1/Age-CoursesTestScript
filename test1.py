print("#"*80)
print( "  Welcome to my script This SCript By Ryuzaki Ryuga "  .center(80 , "#"))
print("#"*80)
print("Please  Specif The Options That You Will use?")
sl = input("Age \"1\" , Courses \"2\"  ? ")
if sl=="1" :


    Age = int(input("How OLd Are You ? "))
    print("Please Specify How your age ?")
    Year = input("Mounth(M) or Weeks(W) or Days(D) ? ")
    Mounth = int(Age)*12
    Weeks = int(Age)*4
    Days = int(Age)*365

    if Year=="Mounth" or Year=="mounth" or Year=="m" or Year=="M" :
        print(f"Your lived Mounth is {Mounth}")
    elif Year=="Weeks" or Year=="weeks" or Year=="w" or Year=="W" :
        print(f"Your lived Weeks is {Weeks}")

    elif Year=="Days" or Year=="days" or Year=="d" or Year=="D" :
        print(f"Your lived Days is {Days}")


if sl=="2" :

    name = input("Please Write Your Name? ").strip().capitalize().title().split()
    country = input("Where Are You From? ")
    student = input("Are You Student? ")
    Cousre = "Python And CyberSecurity"
    price = 450

    if country=="Egypt" or country=="egypt" or country=="Ksa" or country=="Baharin":
        print(f"Hello {name} Becuse Are you {country}")
        if student == "Yes" or student == "yes" or student =="y" :
            print(f"{name} Your pay Courses {Cousre} Price is ${price - 200}")
        if  student =="no" or student == "No" or student =="n" :
            print(f"{name} Your pay Courses {Cousre} Price is ${price - 100}")

    else:
        print(f"{name} Your pay Courses {Cousre} Price is ${price}")
