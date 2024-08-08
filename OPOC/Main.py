import random
import string
import datetime
import pandas as pd

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.pan_id = None
        self.voter_id = None
        self.ration_id = None
        self.person_id = None
        self.card_number = None

    def generate_alphanumeric_id(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=5))
        digits = ''.join(random.choices(string.digits, k=5))
        return letters + digits

    def generate_ids(self, used_ids):
        while True:
            new_id = random.randint(1000000000, 9999999999)
            if new_id not in used_ids:
                used_ids.add(new_id)
                self.pan_id = self.generate_alphanumeric_id()
                self.voter_id = self.generate_alphanumeric_id()
                self.ration_id = self.generate_alphanumeric_id()
                self.person_id = self.generate_alphanumeric_id()
                self.card_number = self.generate_alphanumeric_id()
                break



    def age_check(self):
        if self.age < 18:
            today = datetime.date.today()
            eighteenth_birthday = datetime.date(today.year + (18 - self.age), today.month, today.day)
            time_diff = eighteenth_birthday - today
            print("\n\n\t\t*******************************************")
            print(f"\t\t{self.name} is currently {self.age} years old.")
            print(f"\t\tTime remaining to reach 18 years of age: {time_diff.days} days")
            print("\n\t\t*******************************************")
        else:
            print("\n\n\t\t*******************************************")
            print(f"\t\t{self.name} is {self.age} years old and eligible for the O.P.O.C. card.")
            print("\t\tO.P.O.C. card created successfully...!!")
            print("\n\n\t\t*******************************************")

class CardManager:
    def __init__(self):
        self.used_ids = set()
        self.male_cards = []
        self.female_cards = []

    def create_card(self, name, age, gender):
        new_person = Person(name, age, gender)
        new_person.generate_ids(self.used_ids)
        new_person.age_check()
        if age >= 18:
            if gender.lower() == "male" or gender.lower() == 'm':
                self.male_cards.append(new_person)
            else:
                self.female_cards.append(new_person)

    def display_cards(self):
        for idx, card in enumerate(self.male_cards, start=1):
            print("\n\n\t\tDisplaying Male Cards:")
            print(f"\nMale Card {idx}:")
            print(f"\tName: {card.name}")
            print(f"\tAge: {card.age}")
            print(f"\tGender: {card.gender}")
            print(f"\tPAN ID: {card.pan_id}")
            print(f"\tVoter ID: {card.voter_id}")
            print(f"\tRation ID: {card.ration_id}")
            print(f"\tPerson ID: {card.person_id}")
            print(f"\tCard Number: {card.card_number}")
            print()

        for idx, card in enumerate(self.female_cards, start=1):
            print("\n\n\t\tDisplaying Female Cards:")
            print(f"\n\tFemale Card {idx}:")
            print(f"\tName: {card.name}")
            print(f"\tAge: {card.age}")
            print(f"\tGender: {card.gender}")
            print(f"\tPAN ID: {card.pan_id}")
            print(f"\tVoter ID: {card.voter_id}")
            print(f"\tRation ID: {card.ration_id}")
            print(f"\tPerson ID: {card.person_id}")
            print(f"\tCard Number: {card.card_number}")
            print()

    def create_excel_sheet(self):
        data = {
            "Name": [card.name for card in self.male_cards + self.female_cards],
            "Age": [card.age for card in self.male_cards + self.female_cards],
            "Gender": [card.gender for card in self.male_cards + self.female_cards],
            "PAN ID": [card.pan_id for card in self.male_cards + self.female_cards],
            "Voter ID": [card.voter_id for card in self.male_cards + self.female_cards],
            "Ration ID": [card.ration_id for card in self.male_cards + self.female_cards],
            "Person ID": [card.person_id for card in self.male_cards + self.female_cards],
            "Card Number": [card.card_number for card in self.male_cards + self.female_cards]
        }
        df = pd.DataFrame(data)
        df.to_excel("/content/drive/MyDrive/O.P.O.C_card.xlsx", index=False)

if __name__ == "__main__":
    card_manager = CardManager()
    while True:
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))
        gender = input("Enter your Gender : ")

        card_manager.create_card(name, age, gender)

        reExecute = input("\n\nDo you want to view the cards now? (YES/NO): ").upper()
        if reExecute == "YES":
            card_manager.display_cards()
            card_manager.create_excel_sheet()

        reExecute = input("\n\nDo you want to execute again? (YES/NO): ").upper()
        if reExecute == "NO":
            print(f"\n\n\tThank you, Mr. Manish\n\tVisit again \n\tProgram end...!!")
            break
