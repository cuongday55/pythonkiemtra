from nguoi import Nguoi

class SinhVien(Nguoi):
    def __init__(self, ho_ten="", dia_chi="" , ma_sv = "" , nganh = "" , dtb = 0.0):
        super().__init__(ho_ten, dia_chi)
        self.__ma_sv = ma_sv
        self.__nganh = nganh

        if(dtb < 0):
            self.__dtb = 0
        else:
            self.__dtb = dtb
            

    def get_dtb(self):
        return self.__dtb

    def set_dtb(self, value):
        if(value < 0):
            self.__dtb = 0
        else:
            self.__dtb = value

    def get_ma_sv(self):
        return self.__ma_sv

    def set_ma_sv(self, value):
        self.__ma_sv = value

    def get_nganh(self):
        return self.__nganh

    def set_nganh(self, value):
        self.__nganh = value
        
    def nhan_xet(self):
        if(self.get_dtb()>= 5):
            return 'Dat'
        else:
            return "Hong dat"    
        
    def __str__(self):
        return super().__str__() + f" ma sv: {self.get_ma_sv()} nganh: {self.get_nganh()} dtb: {self.get_dtb()} nhan xet: {self.nhan_xet()}"