class Course:
    def __init__(self, cid="", name="", credits=0):
        self.__cid = cid
        self.__name = name
        self.__credits = credits

    def get_id(self): return self.__cid
    def get_name(self): return self.__name
    def get_credits(self): return self.__credits