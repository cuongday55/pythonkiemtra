from nguoi import Nguoi

class GiaoVien(Nguoi):
    def __init__(self, ho_ten="", dia_chi="" , ma_gv = "" , chuyen_nganh = "" , luong = 0.0):
        super().__init__(ho_ten, dia_chi)
        self.__ma_gv = ma_gv
        self.__chuyen_nganh = chuyen_nganh

        if(luong < 0):
            self.__luong = 0
        else:
            self.__luong = luong


    def get_luong(self):
        return self.__luong

    def set_luong(self, value):
        if(value < 0):
            self.__luong = 0
        else:
            self.__luong = value

    def get_ma_gv(self):
        return self.__ma_gv

    def set_ma_gv(self, value):
        self.__ma_gv = value

    def get_chuyen_nganh(self):
        return self.__chuyen_nganh

    def set_chuyen_nganh(self, value):
        self.__chuyen_nganh = value

    def nhan_xet(self):
        if(self.get_luong()>= 15):
            return 'TOT'
        else:
            return 'Chua TOT'
        
    def __add__(self , other):
        return self.get_luong() + other

    def __str__(self):
        return super().__str__() + f" ma gv: {self.get_ma_gv()} chuyen nganh: {self.get_chuyen_nganh()} luong: {self.get_luong()} nhan xet: {self.nhan_xet()}"