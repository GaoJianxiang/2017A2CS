#1.1 
A structure that display the relationship between different processes and the components below them. It can contain elementary components and composite components

#1.2 
No symbol: sequence
Star: repeated/ iteration
Circle: choice/selection

#1.3
NOT EOF(‘Salary.txt’)
Salary > 50
Salary >= 90
Project Manager 
Lead Developer
Manager

#1.4
see attached file


#1.5
IF Salary >= 90
	THEN
		Role <— Project Manager
	ELSE
		IF Salary > 70
			THEN
				Role <— Consultant
			ELSE
				Role <—Assign Lead Developer
		ENDIF
ENDIF


#1.6(python)
def DetermineSalary(salary):
	if salary > 50:
		if salary >= 90:
			return ('Project Manager')
		elif salary < 90 and salary >70:
			return ('Consultant')
		else:
			return ('Lead Developer')
	return('Manager')
		
#1.7
see attached file

