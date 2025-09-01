salaries = []
#CRUD - Create, Read ID/All/salary, Update , Delete

def create_salary(salary):
    global salaries
    salaries.append(salary)
    
def read_all():
    return salaries

def read_by_salary(salary):
    for I in range(len(salaries)):
        if salaries[I] == salary :
            return I
    return -1
    
def update(old_salary,new_salary):
    index=read_by_salary(old_salary)
    salaries[index]
    return 

def delete_by_salary(salary):
    global salaries
    index = read_by_salary(salary)
    salaries.pop(index)

from salary_manager import create_salary,read_all,read_by_salary,salaries,update,delete_by_salary
 
create_salary(1000)
create_salary(5000)
create_salary(8000)
create_salary(3000)
result_salaries = read_all()
for salary in result_salaries:
    print(salary)

print(read_by_salary(8000))
print(read_by_salary(4000))
print(salaries[read_by_salary(8000)])

update(8000,8500)
print(read_all())
delete_by_salary(1000)
print(read_all())

