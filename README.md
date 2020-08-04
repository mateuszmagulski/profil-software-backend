Recruitment task for Profil Software

## Project launch:

To run the project, follow instructions:

* create virtual environment: 
```bash
python3 -m venv [virtual_environment_name]
```
* activate virtual environment:
```bash
source <virtual_environment_name>/bin/activate
```
* install all requirements from requirements.txt:
```bash
pip3 install -r requirements.txt
```
* upload data to database:
two ways to upload data, check Using script

# Using script

You can use script with flags:

* -h or --help: show help message and exit
```bash
python3 script.py -h 
or
python3 script.py --help
```
* -f or --file: add records from file ```persons.json```
```bash
python3 script.py -f
or
python3 script.py --file
```
* -a or --api with one numeric argument: add N records from API - ```https://randomuser.me/```
```bash
python3 script.py -a [N]
or
python3 script.py --api [N]
```
* -p or --percent with one argument 'male' or 'female': show percentage of one gender, male or female
```bash
python3 script.py -p [male or female]
or
python3 script.py --percent [male or female]
```
* -A or --age with one argument 'all', 'male' or 'female': show average age of all/male/female
```bash
python3 script.py -A [all, male or female]
or
python3 script.py --age [all, male or female]
```
* -c or --city with one numeric argument: show N most common cities
```bash
python3 script.py -c [N]
or
python3 script.py --city [N]
```
* -P or --password with one numeric argument: show N most common passwords and number of appearances
```bash
python3 script.py -P [N]
or
python3 script.py --password [N]
```
* -d or --date with two arguments in format dd-mm-yyyy: show people born between this dates, first date - start, second - end of range
```bash
python3 script.py -d [dd-mm-yyyy] [dd-mm-yyyy]
or
python3 script.py --date [dd-mm-yyyy] [dd-mm-yyyy]
```
* -s or --secure: show one most secure password: 
passwords get rank (sum of points) depending on:
- at least one lowercase letter: 1 point
- at least one uppercase letter: 2 points
- at least one digit: 1 points
- at least one special character: 3 points
- at least 8 characters long: 5 points
```bash
python3 script.py -s
or
python3 script.py --secure
```
# Tests

To run tests:

```bash
python3 tests.py
```
