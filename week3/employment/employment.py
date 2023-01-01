class Employees:
    def __init__(self,name,last) -> None:
        self.name=name
        self.last=last

class Supervisors(Employees):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password=password

class Chefs(Employees):
    def __init__(self, name, last) -> None:
        super().__init__(name, last)
        
    def leave_request(self,days):
        return "May I ("+self.name+") take a leave for "+ str(days)+ " days."
        

adrian=Supervisors("Adrian","A",password="apple")

emily=Chefs("Emily","E")
June=Chefs("June","J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)