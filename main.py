class Attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
   
    def get_details(self):
        print(f"Attraction: {self._name}, Capacity: {self._capacity}.")
   
    def start(self):
        print("The ride is about to start!")

class Thrills(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._minheight = min_height
   
    def start(self):
        print(f"The thrill ride {self._name} is about to start! Hold on tight!")
       
    def is_eligible_height(self, height):
        if height >= self._minheight:
            print("This person is eligible to ride the thriller.")
        else:
            print("This person is ineligible to ride the thriller.")
   
class Family(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._minage = min_age
   
    def start(self):
        print(f"The family attraction {self._name} is about to start! Enjoy the ride!")
   
    def is_eligible_age(self, age):
        if age >= self._minage:
            print("This person is eligible to ride the thriller.")
        else:
            print("This person is ineligible to ride the thriller.")
   
class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role
    
    def work(self):
        print(f"{self._name} is performing their role {self._role}")

class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
       
    def ride_attraction(self):
        choice = input(f"{self._name} would you like to ride a thriller or a family ride?\n")
        while True:
            if choice.lower() == "thriller":
                choice2 = input(f"Would you like to ride the {thrill1._name} or the {thrill2._name}?\n")
                if choice2 == thrill1._name.lower():
                    Thrills.is_eligible_height(thrill1, self._height)
                    thrill1.start()
                if choice2 == thrill2._name.lower():
                    Thrills.is_eligible_height(thrill2, self._height)
                    thrill2.start()
                break
            elif choice == "family":
                choice2 = input(f"Would you like to ride the {family1._name} or the {family2._name}?\n")
                if choice2 == family1._name.lower():
                    Family.is_eligible_age(family1, self._age)
                    family1.start()
                if choice2 == family2._name.lower():
                    Family.is_eligible_age(family2, self._age)
                    family2.start()
                break
            else:
                print("That is not a choice.")

thrill1 = Thrills("The Euthanasia Coaster", 24, 140)
thrill2 = Thrills("The Big Dipper", 18, 110)
family1 = Family("The Gruffalo River Ride Adventure", 6, 16)
family2 = Family("Dolphin Exhibit", 300, 5)
djkhaled = Visitor("DJ Khaled", 49, 169)
chad = Visitor("Yasutora Sado", 16, 197)
djkhaled.ride_attraction()
chad.ride_attraction()
