class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self): return self.__sid
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa