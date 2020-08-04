import unittest
import argparse
import datetime
import json
from peewee import SqliteDatabase
from types import SimpleNamespace
from datetime import date

from script import App, Person, Actions

test_db = SqliteDatabase(":memory:")
data = [
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Gdynia",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "UjjK@O2OR",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Gdynia",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "UjjKO2OR",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Sopot",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "brownzebra890",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Sopot",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "brownzebra890",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Gdansk",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "de5a54bf",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Gdansk",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "de5a54bf",
            "salt": "de5a54bf",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Rumia",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "de5a54bf",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Rumia",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "ecb9a329fe97",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Reda",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "ecb9a329fe97",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Reda",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "ecb9a329fe97",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Feira de Santana",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "ecb9a329fe97",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Feira de Santana",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "flash",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu", "last": "Silveira"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Feira de Santana",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "flash",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "1985-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Amanda_test", "last": "Silveira_test"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Feira de Santana",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "flash",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "2000-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
    {
        "gender": "male",
        "name": {"title": "Mr", "first": "Riu_test", "last": "Silveira_test"},
        "location": {
            "street": {"number": 6316, "name": "Rua João Xxiii"},
            "city": "Feira de Santana",
            "state": "Rio Grande do Norte",
            "country": "Brazil",
            "postcode": 98688,
            "coordinates": {"latitude": "-71.7399", "longitude": "-53.7696"},
            "timezone": {"offset": "-2:00", "description": "Mid-Atlantic"},
        },
        "email": "riu.silveira@example.com",
        "login": {
            "uuid": "de5a54bf-c229-4ada-b53f-ecb9a329fe97",
            "username": "brownzebra890",
            "password": "flash",
            "salt": "UjjKO2OR",
            "md5": "030c1379017a1ebb9311870b575c6c50",
            "sha1": "0e5e8a3e5f684f922b708bccf50329d5e2edd93d",
            "sha256": "ca7043321521d04f3ffe838b92f7cf979e1a0787ec3b3a32a089b7d92653bbaa",
        },
        "dob": {"date": "2000-08-09T05:52:32.614Z", "age": 35},
        "registered": {"date": "2015-04-25T08:09:24.288Z", "age": 5},
        "phone": "(62) 1699-5442",
        "cell": "(72) 3735-5671",
        "id": {"name": "", "value": None},
        "picture": {
            "large": "https://randomuser.me/api/portraits/men/58.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/58.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/58.jpg",
        },
        "nat": "BR",
    },
]


class TestActionsStaticMethods(unittest.TestCase):
    def test_filter_numbers(self):
        result = Actions.filter_numbers("1qazxsw@#EDc4566ddfJE )rt46677")
        self.assertEqual(result, "1456646677")

    def test_next_leap_year(self):
        result = [
            Actions.next_leap_year(2000),
            Actions.next_leap_year(2001),
            Actions.next_leap_year(2002),
            Actions.next_leap_year(2003),
        ]
        self.assertEqual(result, [2000, 2004, 2004, 2004])

    def test_days_to_next_birthday(self):
        dob_1 = datetime.datetime(2009, 1, 9, 15, 8, 24, 78915)
        today_1 = datetime.datetime(2010, 1, 6, 15, 8, 24, 78915)
        dob_2 = datetime.datetime(2000, 2, 29, 15, 8, 24, 78915)
        today_2 = datetime.datetime(2003, 2, 28, 15, 8, 24, 78915)
        result = [
            Actions.days_to_next_birthday(dob_1, today_1),
            Actions.days_to_next_birthday(dob_2, today_2),
        ]
        self.assertEqual(result, [3, 366])

    def test_rate_password(self):
        result = [Actions.rate_password("supertajne"), Actions.rate_password("Ab1337")]
        self.assertEqual(result, [("supertajne", 6), ("Ab1337", 4)])

    def test_flattening_data(self):
        data = {"key1": "value1", "key2": {"2key1": "value2", "2key2": "value3"}}
        result = Actions.flattening_data("master_key", data)
        self.assertEqual(
            result,
            [
                ("master_key_key1", "value1"),
                ("master_key_key2_2key1", "value2"),
                ("master_key_key2_2key2", "value3"),
            ],
        )


class TestActionsWithDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_db.bind(Person, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables([Person])
        args = SimpleNamespace(
            age="male",
            api=None,
            city=5,
            date=[datetime.date(2000, 1, 1), datetime.date(2001, 1, 1)],
            file=False,
            password=2,
            percent="male",
            secure=True,
        )
        cls.actions = Actions(args)

    @classmethod
    def tearDownClass(cls):
        # test_db.drop_tables(Person)
        test_db.close()

    def test_add_records(self):
        TestActionsWithDatabase.actions.add_records(data)
        self.assertEqual(Person.select().count(), 15)

    def test_gender_percentage(self):
        result = TestActionsWithDatabase.actions.gender_percentage()
        self.assertEqual(result, 100)

    def test_average_age(self):
        result = TestActionsWithDatabase.actions.average_age()
        self.assertEqual(result, 35)

    def test_n_most_common_cities(self):
        result = TestActionsWithDatabase.actions.n_most_common_cities()
        self.assertEqual(
            result,
            [
                ("Feira de Santana", 5),
                ("Gdynia", 2),
                ("Sopot", 2),
                ("Gdansk", 2),
                ("Rumia", 2),
            ],
        )

    def test_n_most_common_passwords(self):
        result = TestActionsWithDatabase.actions.n_most_common_passwords()
        self.assertEqual(
            result, [("ecb9a329fe97", 4), ("flash", 4)],
        )

    def test_people_in_range(self):
        result = TestActionsWithDatabase.actions.people_in_range()
        self.assertEqual(
            result, [("Amanda_test", "Silveira_test"), ("Riu_test", "Silveira_test")],
        )

    def test_most_secure_password(self):
        result = TestActionsWithDatabase.actions.most_secure_password()
        self.assertEqual(
            result, "UjjK@O2OR",
        )


class TestApp(unittest.TestCase):
    def test_valid_date_succes(self):
        result = App.valid_date("01-01-2000")
        self.assertEqual(
            result, datetime.date(2000, 1, 1),
        )

    def test_valid_date_failure(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            App.valid_date("01-01-20004")


if __name__ == "__main__":
    unittest.main()
