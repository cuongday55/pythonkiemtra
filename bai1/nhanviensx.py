from nhanvien import NhanVien

class NhanVienSanXuat(NhanVien):
    def __init__(self, ma_nv="", ho_ten="", gioi_tinh=True, luong_co_ban=0, dia_chi="" , so_sp = 0):
        super().__init__(ma_nv, ho_ten, gioi_tinh, luong_co_ban, dia_chi)
        if(so_sp < 0):
            self.__so_sp = 0
        else:
            self.__so_sp = so_sp

    def get_so_sp(self):
        return self.__so_sp

    def set_so_sp(self, value):
        if(value < 0):
            self.__so_sp = 0
        else:
            self.__so_sp = value
            
    def luong(self):
        return self.get_so_sp() * 10 + self.get_luong_co_ban()
    
    def __str__(self):
        return super().__str__() + f" so sp: {self.get_so_sp()} luong: {self.luong()}"
