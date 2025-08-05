# # CWE-89: SQL Injection

# import sqlite3

# def get_user_input():
#     user_input = input("Enter username: ")
#     return user_input

# def query_db(username):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
    
#     # SQL Injection (Bandit & Semgrep)
#     query = f"SELECT * FROM users WHERE username = '{username}'"
#     cursor.execute(query)
    
#     return cursor.fetchall()

# user = get_user_input()
# print(query_db(user))