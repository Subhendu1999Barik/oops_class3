class person :
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = person("anuj","bhandari","anuj@gmail.com",1994)
sudh = person("subhendu","sekhar","subhendu@gmail.com",1999)
print(sudh.name)
print(sudh.surname)
print(sudh.emailid)
print(type(sudh))