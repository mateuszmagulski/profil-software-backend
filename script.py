import argparse
from datetime import datetime
from peewee import *

db = SqliteDatabase("people.db")
db.connect()


class App:
    @staticmethod
    def valid_date(date):
        try:
            return datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            msg = "Not a valid date: {0}".format(date)
            raise argparse.ArgumentTypeError(msg)

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
            choices=["male", "female"],
            nargs="?",
            help="Average age of: without argument - all, with 'male'/'female' - one gender",
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
        args = parser.parse_args()


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


App.parse()
db.close()
