import argparse
from datetime import datetime
from collections import Counter
import functools
import json

from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateField,
    DateTimeField,
    IntegerField,
)
import requests

db = SqliteDatabase("people.db")


class App:
    def __init__(self):
        pass

    @classmethod
    def parse(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--api", type=int, help="Add N records from API")
        parser.add_argument(
            "-f", "--file", action="store_true", help="Add records from 'persons.json'"
        )
        parser.add_argument(
            "-p",
            "--percent",
            type=str,
            choices=["male", "female"],
            help="Show percentage of one gender",
        )
        parser.add_argument(
            "-A",
            "--age",
            type=str,
            choices=["all", "male", "female"],
            help="Average age of: 'all' - all, 'male'/'female' - one gender",
        )
        parser.add_argument("-C", "--city", type=int, help="The most common N cities")
        parser.add_argument(
            "-P", "--password", type=int, help="The most common N passwords"
        )
        parser.add_argument(
            "-d",
            "--date",
            type=App.valid_date,
            nargs=2,
            help="Users borned between two dates in format DD-MM-YYYY",
        )
        parser.add_argument(
            "-s", "--secure", action="store_true", help="Most secure password"
        )
        cls.args = parser.parse_args()

    @staticmethod
    def valid_date(date):
        try:
            return datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            msg = "Not a valid date: {0}".format(date)
            raise argparse.ArgumentTypeError(msg)


class Person(Model):

    gender = CharField()
    name_title = CharField()
    name_first = CharField()
    name_last = CharField()
    location_street_number = CharField()
    location_street_name = CharField()
    location_city = CharField()
    location_state = CharField()
    location_country = CharField()
    location_postcode = CharField()
    location_coordinates_latitude = CharField()
    location_coordinates_longitude = CharField()
    location_timezone_offset = CharField()
    location_timezone_description = CharField()
    email = CharField()
    login_uuid = CharField()
    login_username = CharField()
    login_password = CharField()
    login_salt = CharField()
    login_md5 = CharField()
    login_sha1 = CharField()
    login_sha256 = CharField()
    dob_date = DateTimeField()
    dob_age = IntegerField()
    dob_next = IntegerField()
    registered_date = DateTimeField()
    registered_age = IntegerField()
    phone = IntegerField()
    cell = IntegerField()
    id_name = CharField(null=True)
    id_value = CharField(null=True)
    nat = CharField()

    class Meta:
        database = db


class Actions:
    def __init__(self, arguments):
        self.age = arguments.age
        self.api = arguments.api
        self.city = arguments.city
        self.date = arguments.date
        self.file = arguments.file
        self.password = arguments.password
        self.percent = arguments.percent
        self.secure = arguments.secure
        self.execute()

    def execute(self):
        with db:
            if self.file:
                try:
                    with open("persons.json") as json_file:
                        data = json.load(json_file)["results"]
                        self.add_records(data)
                except FileNotFoundError as e:
                    print(e)
            if self.api:
                print("connecting...")
                try:
                    response = requests.get(
                        "https://randomuser.me/api/?results={}".format(self.api)
                    )
                    data = response.json()["results"]
                except:
                    print("Connection error...")
                self.add_records(data)

            if self.percent:
                self.show_gender_percentage()
            if self.age:
                self.show_average_age()
            if self.city:
                self.show_top_n_cities()
            if self.password:
                self.show_top_n_passwords()
            if self.date:
                self.show_people_in_range()
            if self.secure:
                self.show_most_secure_password()

    def add_records(self, data):
        print("adding records...")
        if not db.table_exists("person"):
            db.create_tables([Person])
        today = datetime.now()
        for person in data:
            birthday = datetime.strptime(person["dob"]["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
            del person["picture"]
            person
            person["cell"] = Actions.filter_numbers(person["cell"])
            person["phone"] = Actions.filter_numbers(person["phone"])
            keys_to_delete = []
            keys_to_add = [("dob_next", Actions.days_to_next_birthday(birthday, today))]
            for key, value in person.items():
                if type(value) == dict:
                    keys_to_add = keys_to_add + Actions.flattening_data(key, value)
                    keys_to_delete.append(key)
            for key in keys_to_delete:
                del person[key]
            for key, value in keys_to_add:
                person[key] = value
        Person.insert_many(data).execute()

    def show_gender_percentage(self):

        if not db.table_exists("person"):
            print("Add records to database, add -h for help")
            return
        all_count = Person.select().count()
        if not all_count:
            print("Add records to database, add -h for help")
            return
        gender_count = Person.select().where(Person.gender == self.percent).count()
        percentage = round((gender_count / all_count) * 100, 2)
        print("Percentage of {} is {}%".format(self.percent, percentage))

    def show_average_age(self):

        if not db.table_exists("person"):
            print("Add records to database, add -h for help")
            return
        if self.age == "all":
            querry = Person.select(fn.AVG(Person.dob_age))
        else:
            querry = Person.select(fn.AVG(Person.dob_age)).where(
                Person.gender == self.age
            )
        age_sum = querry.scalar()
        print("Average age of {} is {}".format(self.age, age_sum))

    def show_top_n_cities(self):
        if not db.table_exists("person"):
            print("Add records to database, add -h for help")
            return
        querry = Person.select(Person.location_city)
        cities_count = {}
        for person in querry:
            if person.location_city in cities_count:
                cities_count[person.location_city] += 1
            else:
                cities_count[person.location_city] = 1
        n_most_common = Counter(cities_count).most_common(self.city)
        print("Top {} most common cities:".format(self.city))
        for city in n_most_common:
            print(city[0])

    def show_top_n_passwords(self):
        if not db.table_exists("person"):
            print("Add records to database, add -h for help")
            return
        querry = Person.select(Person.login_password)
        password_count = {}
        for person in querry:
            if person.login_password in password_count:
                password_count[person.login_password] += 1
            else:
                password_count[person.login_password] = 1
        n_most_common = Counter(password_count).most_common(self.password)
        print("Top {} most common passwords:".format(self.password))
        for password in n_most_common:
            print("{}, {}".format(password[0], password[1]))

    def show_people_in_range(self):
        if not db.table_exists("person"):
            print("Add records to database, add -h for help")
            return
        querry = Person.select(
            Person.name_first, Person.name_last, Person.dob_date
        ).where((Person.dob_date >= self.date[0]) & (Person.dob_date <= self.date[1]))
        for person in querry:
            print(person.name_first, person.name_last)

    def show_most_secure_password(self):
        if not db.table_exists("person"):
            print("Add records to database, add -h for help")
            return
        querry = Person.select(Person.login_password)

        top_rank = ("", 0)

        for person in querry:
            current_rank = Actions.rate_password(person.login_password)
            if current_rank[1] > top_rank[1]:
                top_rank = current_rank

        print("Most secure password: {}".format(top_rank[0]))

    @staticmethod
    def flattening_data(key, value):
        result = []
        if type(value) == dict:
            for nested_key, nested_value in value.items():
                result = result + Actions.flattening_data(
                    "{}_{}".format(key, nested_key), nested_value
                )
        else:
            result.append((key, value))
        return result

    @staticmethod
    def rate_password(password):
        rate = 0
        if any(x.islower() for x in password):
            rate += 1
        if any(x.isupper() for x in password):
            rate += 2
        if any(x.isdigit() for x in password):
            rate += 1
        if any(not x.isalnum() for x in password):
            rate += 3
        if len(password) >= 8:
            rate += 5
        return (password, rate)

    @staticmethod
    def days_to_next_birthday(birthday, today):
        if birthday.day == 29 and birthday.month == 2:
            leap_year = Actions.next_leap_year(today.year)
            next_birthday = birthday.replace(
                year=leap_year
                if birthday.replace(year=leap_year) >= today
                else today.year + 4
            )
        else:
            next_birthday = birthday.replace(
                year=today.year
                if birthday.replace(year=today.year) >= today
                else today.year + 1
            )
        return (next_birthday - today).days

    @staticmethod
    def next_leap_year(given_year):
        leap_year = None
        while not leap_year:
            if given_year % 4 == 0 or given_year % 400 == 0 and given_year % 100 == 0:
                leap_year = given_year
            given_year = given_year + 1
        return leap_year

    @staticmethod
    def filter_numbers(string):
        return functools.reduce(lambda a, b: a + b if b.isnumeric() else a, string, "")


App.parse()
actions = Actions(App.args)
