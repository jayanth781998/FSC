import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username FROM users")
	users = cur.fetchall()
	con.close()
	return users
	
def CompareUsers(username,password):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users where username == (?) and password ==(?)",(username,password))
	users = cur.fetchall()
	con.close()
	return users
	
def Fetchparts():
	con = sql.connect("services.db")
	cur = con.cursor()
	cur.execute("SELECT parts,price FROM services")
	parts = cur.fetchall()
	con.close()
	return parts
	
def deleteUser(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("DELETE FROM users WHERE username == (?)",(username,))
	con.commit()
	con.close()
	
def CompareAdmins(username,password):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM admins where username == (?) and password ==(?)",(username,password))
	users = cur.fetchall()
	con.close()
	return users
