import StudentClass as sc

studentid = 1001
name = 'John'
dob = '10/15/2001'
classification = 'junior'

john = sc.Student(studentid,name,dob,classification)

john.calc_age()

john.register()

print(f"Student age is: {john.get_age()}")
print(f"Student can register between {john.get_registration()}")