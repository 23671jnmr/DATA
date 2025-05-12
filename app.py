#docstring - Jonemar - mlbb heroes
#Imports
import sqlite3

#CONTENTS AND VARIABLES
DATABASE = "mlbb.db"

    
#functions
def print_all_heroes():
        ''''print all the heroes nicely'''
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()
        sql = "SELECT * from mlbb;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop results
        print(results)
        print(f"id      hero                                    role_id")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()


def print_all_heroes_sorted_by_id():
        ''''print all the heroes sorted by id'''
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()
        sql = "SELECT * from mlbb ORDER BY role_id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop results
        print(results)
        print(f"id      hero                                    role_id")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()


def print_hero_by_name():
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()

        hero_name = input("Enter the hero name: ")
        sql = "SELECT * from mlbb WHERE hero LIKE ?;"
        cursor.execute(sql, ('%' + hero_name + '%',))
        results = cursor.fetchall()
        #loop results
        print(f"id|      hero|                                   role_id|")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()

def print_hero_by_first_letter():
        db = sqlite3.connect(DATABASE) 
        cursor = db.cursor()

        first_letter = input("Enter the first letter: ")
        sql = "SELECT * from mlbb WHERE hero LIKE ?;"
        cursor.execute(sql, (first_letter + '%',))
        results = cursor.fetchall()
        #loop results
        print(f"id|      hero|                                   role_id|")
        for mlbb in results:
            print(f"{mlbb[0]:<8}{mlbb[1]:<40}{mlbb[2]:<6}")
        #finish loop
        db.close()


    #main code
while True:
        user_input = input("What would you like to do. \n1. Search all heroes \n2. Search heroes sorted by role id \n3. Search a hero using an id\n4. Search heroes using the first letters\n")
        if user_input == "1":
            print_all_heroes()
        elif user_input == "2":
            print_all_heroes_sorted_by_id()
        elif user_input == "3":
            print_hero_by_name()
        elif user_input == "4":
            print_hero_by_first_letter()
        elif user_input == "0":
            break
        else:
            print("That was not an option\n")