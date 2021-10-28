1. activate environment(python > 3.6)

2. Run the file run.py in the shell

3.You can get list of all users by - http://localhost:8080/users

4. Execute requests
res = requests.post('http://localhost:8080/users',data=json.dumps({'name':'Jack','phone':'7276654655','email': 'jack@g.com','age':22}))
res = requests.put('http://localhost:8080/users/1',data=json.dumps({'name':'Steve'}))
res = requests.delete('http://localhost:8080/users/1')


















































