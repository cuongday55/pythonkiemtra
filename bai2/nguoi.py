from abc import ABC , abstractmethod

class Nguoi(ABC):
    def __init__(self , ho_ten="" , dia_chi = ""):
        self.__ho_ten = ho_ten
        self.__dia_chi = dia_chi
    
    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, value):
        self.__ho_ten = value

    def get_dia_chi(self):
        return self.__dia_chi

    def set_dia_chi(self, value):
        self.__dia_chi = value

    @abstractmethod
    def nhan_xet(self):
        pass
    
    def __str__(self):
        return f"ho ten: {self.get_ho_ten()} dia chi: {self.get_dia_chi()}"