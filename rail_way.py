
'''
1.welcome to irctc
2.login
3.enter source destination
4.select seats
5.price
6.book tickets
7.passenger details
8.checkout
'''
import random #to generate random pnr numbers
print("Welcome to IRCTC.")#just greeting
# o is string which contains option list visible for user
o='''
1.don't have account? Register    
2.Login
3.Book Tickets 
4.Check PNR Status
'''
#account class is used for account details
class Account:
    def __init__(self,username,password):#arguements will be give on object creation
        self.username=username
        self.password=password

    def check_password(self,password):#checking the password
        return self.password==password
    
#train class is used for display train details
class Train():
    def __init__(self,train_num,available_seats,berth,train_class,wl,price):
        self.train_num = train_num
        self.available_seats = int(available_seats)
        self.berth = berth
        self.train_class = train_class
        self.wl = wl
        self.price=price

    def book_tickets(self,num_tickets):#used to book tickets
        pnr_list=[]
        waiting_list=[]

        if num_tickets > self.available_seats:#no.of tickets>available seats
            confirmed_tickets = self.available_seats#available seats get confirmed
            waiting_tickets = num_tickets - self.available_seats#extra seats on wl

            for _ in range(confirmed_tickets):#generates pnr randomly for confirm tickets
                pnr_list.append(random.randint(100000,999999))
            
            for _ in range(waiting_tickets):#generates pnr randomly for waiting tickets
                waiting_list.append(random.randint(100000,999999))

            self.available_seats=0#waiting list means there is no available seats
        else:#if tickets < available seats
            for _ in range(num_tickets):#generates random pnrs for tickets
                pnr_list.append(random.randint(100000,999999))
            self.available_seats -= num_tickets#1 ticket confirm means 1 ticket less in available seats
        
        return {#returns confirm&waiting pnrs in dict form
            "confirmed_tickets" : pnr_list,
             "waiting_tickets" : waiting_list
         }
    

class Passenger:
    def __init__(self,name,age,gender,mobile_no):#used to entry passengers when object created
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile_no = mobile_no

    def display_info(self):#to display passengers info
        print(f"Passenger Name:",{self.name})
        print(f"Age:",{self.age})
        print(f"Gender: " ,{self.gender})  
        print(f"Mobile Number:",{self.mobile_no})


class Ticket:#for ticket details
    def __init__(self,train_num,source,destination,passengers,pnr,berth,cls,status):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
        self.berth = berth
        self.cls = cls
        self.status = status

    def display_info(self):#to display ticket details
        print(f"Train number: {self.train_num}")
        print(f"source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR : {self.pnr}")
        print(f"Berth: {self.berth}")
        print(f"Class: {self.cls}")
        print(f"status: {self.status}")
        for p in self.passengers:
            p.display_info()
        print()

accounts = [#predefined some users act as arguments for account class
     Account("teja","1234"),
    Account("sony","5678")
       ]

logged_in_account = None#default no login account 

while True:#used while to repeatedly loop options until we find train
    print(o)
    option=input("Enter your option:")#give our option
    if option=="1":#compare with input
        username=input("Enter the username: ")#account creating
        password=input("Enter the password: ")
        accounts.append(Account(username,password))#new account added to accounts list

        print(f"Account created successfully!./n PLEASE LOGIN to continue")

    elif option=="2":#to login
        username=input("Enter username: ")#take inputs
        password=input("Enter the password: ")
        for account in accounts:#validates username and check password fun
            if account.username == username and account.check_password(password):
                logged_in_account=account#if true logged in as account
                break#and breakes for loop
        if logged_in_account is None:#if no login account
            print("Invalid username or password !")
        
        else:
            print(f"\n logged in as {username}")

            
    
    elif option=="3":#to book tickets
        
        if logged_in_account is None:#if not login..need to login
            print(f"You need to LOGIN for ticket booking")
            print("enter option 2")#tells us select option 2
            option=input("enter the number:")#enter 2
        else:#if logged in account is not none
           trains={("hyd","vij"):{"vandebharat":20707,"BZA.intercity":12796,"janmabhoomi":12806},
        ("vizag","bhubaneswar"):{"coromandel":12842,"falaknama":12704,"howrah":12864},
        ("bangalore","ooty"):{"suvidha":80636,"kannur":16511}}#trains dict
           source=input("Enter the Source:")#asks source
           destination=input("Enter the Destination:")#asks destination
           route=(source,destination)#defined routes for clear check
           re_route=(destination,source)
    
           if route in trains:#if our route in trains
               print("*****".center(75,"-"))
               print(f"Available trains between {source} and {destination} are:")
               for train_name,train_num in trains[route].items():#prints trains list of that route
                   print(f"-{train_name} ({train_num})")#for is used to get trains one by one
               print("*****".center(75,"-"))   
               
                    
           elif re_route in trains:#if route false it comes here
               print("*****".center(75,"-"))
               print(f"Available trains between {destination} and {source} are:")
               for train_name,train_num in trains[re_route].items():
                   print(f"{train_name} ({train_num})")
               print("*****".center(75,"-"))#prints trains list when elif true

           else:#if and elif false then no trains available
               print(f"There is no Direct trains between {source} and {destination}")
           break#breakes while loop
        

    elif option=="4":#to check pnr status
        pnr_data={"123456":"confirmed",#predefined pnrs
                  "987654":"waiting list 1",
                  "112233":"waiting list 2"}
        pnr_no = input("Enter your Pnr number:").strip()#input pnr
        
        if pnr_no in pnr_data:#checking input pnr in pnrdata or not
            print(f"\nPNR status for {pnr_no} is : {pnr_data[pnr_no]}\n")
            print("*****".center(100,'-'))
        else:
            print("PNR not found")
        
    else:
        print("The option you entered is Invalid")

if logged_in_account is not None:
    pass


train_details = [#arguments for train class
    Train("20707","23","(lower,upper,middle)","(2A,3Ac,sleeper,chaircar)","0","0"),
    Train("12796","12","(lower,upper,middle)","(2A,3Ac,sleeper)","0","0"),
    Train("12806","200","lower","chaircar","0","0"),
    Train("12842","2","(lower,upper,middle)","(2A,3Ac,sleeper)","0","0"),
    Train("12704","11","(upper,lower,middle)","(2A,sleeper)","0","0"),
    Train("12864","1","(upper,lower,middle)","(2A,3AC)","0","0"),
    Train("80636","14","(lower,upper,middle)","(2A,3Ac,sleeper,chaircar)","0","0"),
    Train("16511","3","(lower,upper,middle)","(2A,sleeper)","0","0")

]

search_number=input("\nenter the train number:").strip()#select train number

for train in train_details:#search in traindetails for every train
    if train.train_num == search_number:#if matches any number then prints below det
        print("Below are the train details you want:")
        print("Train no:", train.train_num)
        print("Available seats: " ,train.available_seats)
        print("Berth:" , train.berth)
        print("Class of journey:",train.train_class)
        print("Waiting list number:" , train.wl)
        print("Price :", train.price)
        break#and breaks
else:#no match means no trains with given input
    print("Train you entered is not Found")


while True:#to iterate until our requirement
    try:#try is used for error handling obtained by user inputs
        train_num = search_number
        num_tickets = int(input("\nEnter the number of tickets:"))
        if num_tickets<=0:
            raise ValueError("Number of tickets should not be 0") 
        berth= input("Select the berth:").strip()
        if berth not in train.berth:
            raise ValueError("This berth is not available")
        cls=input("Enter the type of class:")
        if cls not in train.train_class:
            raise ValueError("that coach is not available") 
    except ValueError as e:#if any error it shows invalid input
        print(f"Invalid input: {e}")

    break  #breaks

if num_tickets is None:#if no tickets selected
    print("You did not select number of tickets")
else:#if there is tickets selected
    passengers=[]#takes empty passenger list to add passenger details later
    for i in range(num_tickets):#is used to take inputs of passenger details
        print(f"Enter details for passenger {i+1}:")
        while True:
            try:
                name = input("Enter name:").strip()
                if not name:
                    raise ValueError("Name is required")
                age = int(input("age: "))
                if age<=0 or age>=120:
                    raise ValueError("Please enter valid age")
                gender = str(input("Enter gender:")).strip().lower()
                if gender not in ["male","female","other"]:
                    raise ValueError("Invalid Gender")
                mobile_no = input("Enter the mobile number:")
                if mobile_no is None or len(mobile_no)!= 10 or not mobile_no.isdigit():
                    raise ValueError("Invalid mobile number")
                passenger = Passenger(name,age,gender,mobile_no)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

    result = train.book_tickets(num_tickets)#in book tickets output is added to result in dict form

    if result is None:#if there is no pnrs means no bookings
        print("Booking Failed.")

    else:#if there is pnrs
        confirmed_pnrs = result["confirmed_tickets"]#value of result dict is assigned in list form
        waiting_pnrs = result["waiting_tickets"]

        print("Booking successfull!".center(75,'-'))
        print("\n Your Ticket Details are: \n")


        for i in range(num_tickets):#loops for no of passengers
            if i < len(confirmed_pnrs):#if i in confirmed pnrs, pnr assigned
                pnr = confirmed_pnrs[i]
                status = "confirmed"
            else:#i not in confirmed pnrs,means it is waiting
                pnr = waiting_pnrs[i-len(confirmed_pnrs)]#assigns waiting pnrs
                status = "waiting"
            ticket = Ticket(train_num,source,destination,#arguments for ticket class
                            [passengers[i]],pnr,berth,cls,status)
            
            ticket.display_info()#display tickets information
            print("Thankyou..! Have a Safe Journey".center(75,'*'))




