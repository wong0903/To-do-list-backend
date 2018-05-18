import utils
from datetime import datetime as dt

def getTask():
	conn = utils.connect1()
	cur = conn.cursor()
	cur.execute('SELECT * FROM "Task"')
	data = cur.fetchall()
	task = []
	for i in data:
		i = list(i)
		task.append(i)
	cur.close()
	conn.close()
	print(type(task))
	return task

def createTask(task):
	conn = utils.connect1()
	cur = conn.cursor()
	taskname = task.get('taskname')
	loginID = task.get('loginID')
	deadline = task.get('deadline')
	if verifyTaskName(taskname):
		timestamp = dt.now()
		cur.execute('INSERT INTO "Task"(task_name, timestamp, deadline, loginid) VALUES(%s,%s,%s,%s)',(taskname,timestamp,deadline,loginID))
		conn.commit()
		cur.close()
		conn.close()
		return "successful"
	else:
		cur.close()
		conn.close()
		return "access denied"

def removeTask(id):
	conn = utils.connect1()
	cur = conn.cursor()
	cur.execute('DELETE FROM "Task" WHERE id = {}'.format(id))
	conn.commit()
	cur.close()
	conn.close()
	return "delete succesful"

def viewUserTask(id):
	conn = utils.connect1()
	cur = conn.cursor()
	cur.execute('SELECT * FROM "Task" WHERE id={}'.format(id))
	data = cur.fetchall()
	task = []
	for i in data:
		i = list(i)
		task.append(i)
	cur.close()
	conn.close()
	return task

def register(user):
	conn = utils.connect1()
	cur = conn.cursor()
	creationDate = dt.now()
	loginID = user.get('loginID')
	password = user.get('password')
	password2 = user.get('confirm')
	cur.execute('SELECT * FROM "User" WHERE loginid = (%s)',(loginID,))
	user = cur.fetchone()
	print(user)
	if user == None:
		if(verifyRegisterID(loginID)):
			if(verifyRegisterPassword(password)):
				if(confirmPassword(password, password2)):
					cur.execute('INSERT INTO "User"(loginid, password, creationDate) VALUES(%s,%s,%s)',(loginID,password,creationDate))
					conn.commit()
					cur.close()
					conn.close()
					return "Registration successful"
				return "Password does not match"
		return "Registration failed"
	else:
		cur.close()
		conn.close()
		return "Registration failed. Found Existing User"



def login(user):
	loginID = user.get('loginID')
	password = user.get('password')
	if(authLoginIDAndPassword(loginID, password)):
		return "Login successful"
	else:
		return "Incorrect LoginID or Password"


def confirmPassword(password1, password2):
	if (password1 == password2):
		return True
	else:
		return False

def verifyRegisterPassword(password):
	if not password or len(password) > 20:
		return False
	else:
		return True

def verifyRegisterID(loginID):
	if not loginID or len(loginID) > 20:
		return False
	else:
		return True

def authLoginIDAndPassword(loginID, password):
	conn = utils.connect1()
	cur = conn.cursor()
	cur.execute('SELECT * FROM "User" WHERE loginid = (%s)',(loginID,))
	user = cur.fetchone()
	if user != None:
		user = list(user)
		cur.close()
		conn.close()
		if (user[2] == password):
			return True
		else:
			return False
	else:
		return False


def verifyTaskName(taskname):
	if not taskname:
		return False
	else:
		return True







