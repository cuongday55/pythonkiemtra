from nhanviensx import NhanVienSanXuat
from nhanvienvp import NhanVienVanPhong
dsnv = []

def show_dsnv():
    for nv in dsnv:
        print(nv)

def check_ma(ma):
    has_ma = False
    for nv in dsnv:
        if(nv.get_ma_nv() == ma):
            return True
           
    return has_ma

while True:
    print("1. nhap dsnv: ")
    print("2. hien thi dsnv: ")
    print("3. tim kiem theo ma nv: ")
    print("4. nv co luong cao nhat: ")
    print("5. sap xep giam dan: ")
    print("0. thoat ")
    chon = input('nhap lua chon: ')
    if(chon == '1'):
        print("1. nhap nvvp: ")
        print("2. nhap nvsx: ")
        tmp = input('nhap lua chon: ')
        manv = input('nhap manv: ')
        if(not check_ma(manv)):
            ten = input('nhap ten: ')
            gt = int(input('nhap gioi tinh: '))
            luong_cb = float(input('nhap luongcb: '))
            dia_chi = input('nhap diachi: ')
            if(tmp == '1'):
                he_so_luong = int(input('nhap so luong: '))
                nvvp = NhanVienVanPhong(manv , ten , gt , luong_cb , dia_chi , he_so_luong)
                dsnv.append(nvvp)
            elif (tmp == '2'):
                so_sp = int(input('nhap so sp: '))
                nvsx = NhanVienSanXuat(manv , ten , gt , luong_cb , dia_chi , so_sp)
                dsnv.append(nvsx)
            else:
                print('chon sai vui long chon lai!')
        else:
            print('khong the them ma da ton tai!')
    elif(chon == '2'):
        if(len(dsnv) > 0):
            show_dsnv()
        else:
            print('ds rong')
    elif(chon == '3'):
        if(len(dsnv) > 0):
            ma_nv = input('nhap ma nv: ')
            has_ma_nv = False
            nv = None
            for i in dsnv:
                if(i.get_ma_nv() == ma_nv):
                    has_ma_nv = True
                    nv = i
                    break
        
            if(has_ma_nv):
                print(i)
            else:
                print('ma khong ton tai!')
        else:
            print('ds rong')
    elif(chon == '4'):
        if(len(dsnv) > 0):
            max = dsnv[0].luong()
            nv =None
            for i in range(0, len(dsnv)):
                if(dsnv[i].luong() >= max):
                    max = dsnv[i].luong()
                    nv = dsnv[i]
            print(nv)
        else:
            print('ds rong')
        
    elif(chon == '5'):
        if(len(dsnv) > 0):
            ds = sorted(dsnv , key=lambda x: x.luong())
            ds.reverse()
            for i in ds:
                print(i)
        else:
            print('ds rong')
    elif(chon == '6'):
        break
    else:
        print('khong ton tai!')
    