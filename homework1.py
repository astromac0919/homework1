import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#creating connection to mysql database
conn = create_connection('test2.cf5ja1cnbyhq.us-east-2.rds.amazonaws.com', 'admin', 'kariskim1031','test2db')

#menu options for user to pick
user_menu = input(
    'MENU\n'
    + 'a - Add car\n' 
    + 'd- Remove car\n' 
    + 'u - update car details\n'
    + 'r1 - Output all cars sorted by year (ascending)\n'
    + 'r2 - Output all cars of a certain color\n' 
    + 'q - Quit\n'
)

#add car
if user_menu == 'a':
    print("Tell me the new car detail for garage list...")
    #ask user what type of car they want to add onto their tale
    make = input("Enter the make: \n")
    model = input("Enter the model: \n")
    year = input("Enter the year: \n")
    color = input("Enter the color: \n")
    #create new entry and execute it to the table
    query = "INSERT INTO garage (make, model, year, color) VALUES ('%s', '%s', '%s', '%s')" % (make, model, year, color)
    execute_query(conn, query)

#remove car
elif user_menu == 'd':
    select_garage = "SELECT * FROM garage"
    garage_table = execute_read_query(conn, select_garage)
    for select_car in garage_table:
            print(select_car["id"], select_car["make"], select_car["model"], select_car["year"], select_car["color"])
    delete_id = input("Remove car from garage: ")
    remove_car = "DELETE FROM garage WHERE id = %s" % delete_id
    execute_query(conn, remove_car)

#update table
elif user_menu == 'u':
    select_garage = "SELECT * FROM garage"
    garage_table = execute_read_query(conn, select_garage)
    for select_car in garage_table: #show entire table so the user can see
        print(select_car["id"], select_car["make"], select_car["model"], select_car["year"], select_car["color"])
    id = input("Enter the id: \n") #to input new information
    make = input("Enter the make: \n")
    model = input("Enter the model: \n")
    year = input("Enter the year: \n")
    color = input("Enter the color: \n")
    update_car = "UPDATE garage set make = '%s', model = '%s', year= %s, color = '%s' WHERE id = %s" % (make, model, year, color, id)
    execute_query(conn, update_car)

#sorting cars in an acsending order
elif user_menu == 'r1':
    order_by_year = ("Output all cars sorted by year (acsending)")
    order_cars = "SELECT * FROM garage ORDER by year"
    acsended_car = execute_read_query(conn, order_cars)
    for acsended_cars in acsended_car: #prints the table in acsended order
        print(acsended_cars["id"], acsended_cars["make"], acsended_cars["model"], acsended_cars["year"], acsended_cars["color"])

#allows user to choose what color they want to see in the list
elif user_menu == 'r2':
    select_garage = "SELECT * FROM garage"
    garage_table = execute_read_query(conn, select_garage)
    color_car = input('Output all cars of a certain color: ')
    for select_car in garage_table:
        if color_car == select_car['color']:
            print(select_car["id"], select_car["make"], select_car["model"], select_car["year"], select_car["color"])

#quits from the menu altogether
elif user_menu == 'q':
    print('\n Quit from menu')

#just in case the user accidently chooses a wrong menu options
else:
    print("Please choose a valid menu choie")