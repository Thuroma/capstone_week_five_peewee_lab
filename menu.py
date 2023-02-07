"""
A menu - you need to add the database and fill in the functions. 
"""
from peewee import *
db = SqliteDatabase('chainsaw_records.sqlite')

class Juggler(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()
    
    class Meta:
        database = db

    def __str__(self):
        return f'{self.name}, {self.country}, {self.catches}'
    

def main():


    create_table()

    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def create_table():
    db.connect()
    db.create_tables([Juggler])


def display_all_records():
    all_jugglers = Juggler.select()
    for contestant in all_jugglers:
        print(contestant)


def search_by_name():
    name_to_search = input('Enter the name of the contestant you want to look up: ')
    contestant = Juggler.get_or_none(name=name_to_search)
    if contestant:
        print(contestant)
    else:
        print('There were no players with that name in the database.')


def add_new_record():
    contestant_name = input('Enter name: ')
    contestant_country = input('Enter country: ')
    number_of_catches = int(input('Enter the number of catches: '))

    new_record = Juggler(name=contestant_name, country=contestant_country, catches=number_of_catches)
    new_record.save()
    print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    contestant = input('Enter the name of the contestant you want to update: ')
    new_number_of_catches = int(input('Enter the new number of catches: '))
    rows_modified = Juggler.update(catches=new_number_of_catches).where(Juggler.name == contestant).execute()
    if rows_modified > 0:
        print(f'{contestant}\'s number of catches was updated to {new_number_of_catches}.')
    else:
        print(f'{contestant} could not be found.')


def delete_record():
    contestant = input('Enter the name of the contestant you want to delete: ')
    rows_modified = Juggler.delete().where(Juggler.name == contestant).execute()
    if rows_modified > 0:
        print(f'{contestant} has been deleted')
    else:
        print(f'{contestant} could not be found.')
 


if __name__ == '__main__':
    main()