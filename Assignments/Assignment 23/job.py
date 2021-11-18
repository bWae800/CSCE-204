class Job:
    def __init__(self,title,description,skills,length,pay):
        
        self.title = title
        self.description = description
        self.skills = skills
        self.length = length
        self.pay = pay
        


    def display(self):
        print(f"""
        *** {self.title} ***
        {self.description}
        Skills: {self.skills}
        Contract length: {self.length}
        Pay rate: {self.pay}""")


    def is_match(self, title):
        if title == self.title: 
            return True
        else:
            return False
        

        
