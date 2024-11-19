from nhanvien import NhanVien

class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv="", ho_ten="", gioi_tinh=True, luong_co_ban=0, dia_chi="" , he_so_luong = 0):
        super().__init__(ma_nv, ho_ten, gioi_tinh, luong_co_ban, dia_chi)
        if(he_so_luong < 0):
            self.__he_so_luong = 0
        else:
            self.__he_so_luong = he_so_luong

    def get_he_so_luong(self):
        return self.__he_so_luong

    def set_he_so_luong(self, value):
        if(value < 0):
            self.__he_so_luong = 0
        else:
            self.__he_so_luong = value
    
    def luong(self):
        return self.get_luong_co_ban() * self.get_he_so_luong()
        
    def __str__(self):
        return super().__str__() + f" he so luong: {self.get_he_so_luong()} luong: {self.luong()}"
