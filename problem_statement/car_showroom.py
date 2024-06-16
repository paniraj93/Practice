'''create a class car shoroom in which 
1. create a function named car company which will allow user to select a car company out of the displayed companies.
if the suer enters and random car company he/she should be asked to re enter
2. according to the car company selected the user should be redirected to selecting the modelsof that company out of the given list. if any random model is selected it should ask for reenter
3. after selecting the model the user should be redirecter to selecting the varing(petrol or disel).
4. according to the car company model and variant a price should be calculated to which sgst and cgst are added to make it the total price.

NOTE: SGST AND CGST ARE COMMON FOR ALL THE CARS.'''

class CarShowroom:
    def __init__(self):
        self.br = ""
        self.mdl = ""
        self.typ = ""
        self.cgst = 5555
        self.sgst = 5555

    def company_selection(self):
        print("SELECT THE COMPANY\n1.TOYATA\n2.BMW")
        while True:
            ch_com = int(input("SELECT THE NUMBER: "))
            if ch_com == 1:
                self.br = "TOYATA"
                break
            elif ch_com == 2:
                self.br = "BMW"
                break
            else:
                print("SELECT FROM THE DISPLAYED OPTIONS")
        car.model_selection()

    def model_selection(self):
        if self.br == "TOYATA":
            while True:
                print("SELECT MODEL\n1.SUPRA\n2.FORTUNER")
                ch_mdl = int(input("SELECT THE NUMBER: "))
                if ch_mdl == 1:
                    self.mdl = "SUPRA"
                    break
                elif ch_mdl == 2:
                    self.mdl = "FORTUNER"
                    break
                else:
                    print("SELECT FROM THE DISPLAYED OPTIONS")
        elif self.br == "BMW":
            while True:
                print("SELECT MODEL\n1.M3 COMPETITION\n2.M4 COMPETITION")
                ch_mdl = int(input("SELECT THE NUMBER: "))
                if ch_mdl == 1:
                    self.mdl = "M3 COMPETITION"
                    break
                elif ch_mdl == 2:
                    self.mdl = "M4 COMPETITION"
                    break
                else:
                    print("SELECT FROM THE DISPLAYED OPTIONS")
        car.type_selection()

    def type_selection(self):
        while True:
            print("SELECT TYPE\n1.PETROL\n2.DIESEL")
            ch_typ = int(input("SELECT THE NUMBER: "))
            if ch_typ == 1:
                self.typ = "Petrol"
                break
            elif ch_typ == 2:
                self.typ = "Diesel"
                break
            else:
                print("SELECT FROM THE DISPLAYED OPTIONS")
        car.calculate_price()

    def calculate_price(self):
        if self.br == "TOYATA" and self.mdl == "SUPRA" and self.typ == "Petrol":
            price = 5000000
        elif self.br == "TOYATA" and self.mdl == "SUPRA" and self.typ == "Diesel":
            price = 4000000
        elif self.br == "TOYATA" and self.mdl == "FORTUNER" and self.typ == "Petrol":
            price = 3000000
        elif self.br == "TOYATA" and self.mdl == "FORTUNER" and self.typ == "Diesel":
            price = 25000000
        elif self.br == "BMW" and self.mdl == "M3 COMPETITION" and self.typ == "Petrol":
            price = 7000000
        elif self.br == "BMW" and self.mdl == "M3 COMPETITION" and self.typ == "Diesel":
            price = 6000000
        elif self.br == "BMW" and self.mdl == "M4 COMPETITION" and self.typ == "Petrol":
            price = 7500000
        elif self.br == "BMW" and self.mdl == "M4 COMPETITION" and self.typ == "Diesel":
            price = 6500000
        else:
            price = 0

        # sgst = 2.09 * price
        # cgst = 2.09 * price
        total_price = price + self.sgst + self.cgst
        print("Total Price: ", total_price)

car = CarShowroom()
car.company_selection()
#car.model_selection()
#car.type_selection()
#car.calculate_price()