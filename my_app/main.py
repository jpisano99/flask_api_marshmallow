# import my_app.tool_box as tools


# Use this file to place scripts that are called from views.py
def do_something(bookings_data):
    print('\tHello from main.py where i am doing something !')
    print('\t', bookings_data)

    # Try creating a Test_Table in the mySQL DB from Models.py
    # tools.create_tables("Test_Table")

    return
    # return ('Hello from Main.py: I read: '+ str(len(ss_test_list)) + ' rows from SmartSheets',ss_test_list)
