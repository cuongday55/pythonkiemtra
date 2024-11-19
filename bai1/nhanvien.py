

class NhanVien:
    def __init__(self , ma_nv = "" , ho_ten = "" ,  gioi_tinh =1 , luong_co_ban = 0.0 , dia_chi = ""):
        self.__ma_nv = ma_nv
        self.__ho_ten = ho_ten
        if(gioi_tinh != 1 and gioi_tinh != 0):
            self.__gioi_tinh= True
        elif(gioi_tinh == 1):
            self.__gioi_tinh = True
        elif(gioi_tinh == 0):
            self.__gioi_tinh = False
        if(luong_co_ban <= 0.0):
            self.__luong_co_ban = 0.0
        else:
            self.__luong_co_ban = luong_co_ban      
        self.__dia_chi = dia_chi

    def get_ma_nv(self):
        return self.__ma_nv

    def set_ma_nv(self, value):
        self.__ma_nv = value

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, value):
        self.__ho_ten = value
        
    def get_gioi_tinh(self) -> bool:
        return self.__gioi_tinh

    def set_gioi_tinh(self, value):
        if(value != True or value != False):
            self.__gioi_tinh= True
        else:
            self.__gioi_tinh = value
        
    
    def get_luong_co_ban(self) -> float:
        return self.__luong_co_ban

    def set_luong_co_ban(self, value):
        if(value <= 0.0):
            self.__luong_co_ban = 0.0
        else:
            self.__luong_co_ban = value   
         
    def get_dia_chi(self):
        return self.__dia_chi

    def set_dia_chi(self, value):
        self.__dia_chi = value
        
    def __str__(self):
        gt = ""
        if(self.get_gioi_tinh() == True):
            gt = "Nam"
        else:
            gt = "Nu"
        return f"manv: {self.get_ma_nv()} ten nv: {self.get_ho_ten()} gioi tinh: {gt} luongcb: {self.get_luong_co_ban()} diachi: {self.get_dia_chi()}"