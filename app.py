#docstring - Jonemar - mlbb heroes
#Imports
import sqlite3

#CONTENTS AND VARIABLES
DATABASE = "mlbb.db"

#functions print all heroes and shows roles in numbers
def print_all_heroes():
        ''''print all the heroes nicely'''
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()
        sql = "SELECT * from mlbb;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop results
        
        print(f"id      hero                                    role_id")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()

# functions - print all heroes with specific roles - sorted
def print_all_heroes_sorted_by_role():
        '''print all the heroes sorted by role, with a specific name '''
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()
        sql = "SELECT mlbb.id, mlbb.hero, roles.role from mlbb JOIN roles ON mlbb.role_id = roles.role_id ORDER BY roles.role;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop results
       
        print(f"id      hero                                    role_id")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<8}")
        #finish loop
        db.close()

# functions -  print hero by choosing a name
def print_hero_by_name():
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()

        hero_name = input("Enter the hero name: ")
        sql = "SELECT * from mlbb WHERE hero LIKE ?;"
        cursor.execute(sql, ('%' + hero_name + '%',))
        results = cursor.fetchall()
        #loop results
        if not results:
            print("No heroes found with that name.")
        else:
            print(f"id|      hero|                                   role_id|")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()
# functions - print a heroes using first letter
def print_hero_by_first_letter():
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()

        first_letter = input("Enter the first letter: ")
        sql = "SELECT * from mlbb  WHERE hero LIKE ?;"
        cursor.execute(sql, (first_letter + '%',))
        results = cursor.fetchall()
        #loop results
        if not results:
            print("No heroes found with that letter.")
        else:
            print(f"id|      hero|                                   role_id|")
        for mlbb in results:
                print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()

#main code
while True:
        user_input = input("What would you like to do?\n"
                           "1. Search all heroes\n"
                           "2. Search heroes sorted by role id\n" 
                           "3. Search a hero using a heroes name\n" 
                           "4. Search heroes using a first letters\n"
                           "0. Exit\n"
                           "Enter your choice using a  number: ")
        if user_input == "1":
            print_all_heroes()
        elif user_input == "2":
            print_all_heroes_sorted_by_role()
        elif user_input == "3":
            print_hero_by_name()
        elif user_input == "4":
            print_hero_by_first_letter()
        elif user_input == "0":
            print("Good bye..")
            break
        else:
            print("Invalid option, please try again.")