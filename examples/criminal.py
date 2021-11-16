class Criminal:
    def __init__(self,first_name, last_name, gender, crime_type, in_jail, description):
        self.first_name = first_name
        self.description = description
        self.last_name = last_name
        self.gender = gender
        self.crime_type = crime_type
        self.in_jail = in_jail


    def is_match(self, gender, crime_type):
        if self.in_jail == True: #They did not commit the crime if they were in jail
            return False

        if self.gender == gender and self.crime_type == crime_type:
            return True

        return False 

    def display(self):
        jail_desc = "Not incarcerated"

        if self.in_jail == True:
            jail_desc = "Incarcerated"

        print(f"""{self.first_name} {self.last_name}
                Gender: {self.gender}
                Crime: {self.crime_type}
                {self.description}
                {jail_desc}""")