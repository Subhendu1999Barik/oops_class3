class person :
    def __init__(sudh,name,surname,emailid,year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def age(sudh , current_year):
        return current_year - sudh.year_of_birth

anuj_var = person("anuj","bhandari","anuj@gmail.com",1994)
sudh = person("subhendu","sekhar","subhendu@gmail.com",1999)

print(sudh.age(2022))

s = "sudh"
s.upper()


