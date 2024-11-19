from sinhvien import SinhVien
from giaovien import GiaoVien


dsn = []

def check_ma(ma):
    for i in dsn:
        if(isinstance(i , SinhVien)):
            if(i.get_ma_sv() == ma):
                return True
        if(isinstance(i , GiaoVien)):  
            if(i.get_ma_gv() == ma):
                return True
    return False

while True:
    print('1. nhap ds: ')
    print('2. in ds: ')
    print('3. tim kiem ma trong ds: ')
    print('4. sua thong tin trong ds: ')
    print('5. sl sv va gv trong ds: ')
    print('6. tong luong gv nhap ds: ')
    print('0. thoat: ')
    
    chon = input('nhap lua chon: ')
    if(chon == '1'):
        print('1. nhap sv 2. nhap gv: ')
        tmp = input('nhap lua chon cua ban: ')
        ten = input('nhap ten: ')
        dia_chi = input('nhap dia chi: ')
        if(tmp == '1'):
            ma_sv = input('nhap ma sv: ')
            if(len(dsn) > 0):
                if(not check_ma(ma_sv)):
                    nganh = input('nhap nganh: ')
                    dtb = float(input('nhap diem trung binh: '))
                    sv = SinhVien(ten , dia_chi , ma_sv , nganh , dtb)
                    dsn.append(sv)
                else:
                    print('ma da ton tai!')
            else:
                nganh = input('nhap nganh: ')
                dtb = float(input('nhap diem trung binh: '))
                sv = SinhVien(ten , dia_chi , ma_sv , nganh , dtb)
                dsn.append(sv)
        elif(tmp == '2'):
            ma_gv = input('nhap ma gv: ')
            if(len(dsn) > 0):
                if(not check_ma(ma_gv)):
                    nganh = input('nhap chuyen nganh: ')
                    luong = float(input('nhap luong: '))
                    gv = GiaoVien(ten , dia_chi , ma_gv , nganh , luong)
                    dsn.append(gv)
                else:
                    print('ma da ton tai!')
            else:
                nganh = input('nhap chuyen nganh: ')
                luong = float(input('nhap luong: '))
                gv = GiaoVien(ten , dia_chi , ma_gv , nganh , luong)
                dsn.append(gv)
        else:
            print('lua chon khong ton tai!')
        
    elif(chon == '2'):
        if(len(dsn) > 0):
            for i in dsn:
                print(i)
        else:
            print('ds trong!')
            
    elif(chon == '3'):
        if(len(dsn)> 0):
            ma = input('nhap ma can tim kiem: ')
            has_ma = False
            tmp = None
            for i in dsn:
                if(isinstance(i , SinhVien)):
                    if(i.get_ma_sv() == ma):
                        has_ma = True
                        tmp = i
                        break
                if(isinstance(i , GiaoVien)):
                    if(i.get_ma_gv() == ma):
                        has_ma = True
                        tmp = i
                        break
            if(has_ma):
                print(tmp)
            else:
                print('ma khong ton tai!')
        else:
            print('ds trong!')
            
    elif(chon == '4'):
        if(len(dsn)> 0):
            ma = input('nhap ma can sua: ')
            if(check_ma(ma)):
                for i in dsn:
                    if(isinstance(i , SinhVien)):
                        if(i.get_ma_sv() == ma):
                            ten = input('nhap ten: ')
                            dia_chi = input('nhap dia chi: ')
                            nganh = input('nhap nganh: ')
                            dtb = float(input('nhap diem trung binh: '))
                            i.set_ho_ten(ten)
                            i.set_dia_chi(dia_chi)
                            i.set_nganh(nganh)
                            i.set_dtb(dtb)
                            break
                    if(isinstance(i , GiaoVien)):
                        if(i.get_ma_gv() == ma):
                            ten = input('nhap ten: ')
                            dia_chi = input('nhap dia chi: ')
                            nganh = input('nhap chuyen nganh: ')
                            luong = float(input('nhap luong: '))
                            i.set_ho_ten(ten)
                            i.set_dia_chi(dia_chi)
                            i.set_chuyen_nganh(nganh)
                            i.set_luong(luong)
                            break
            else:
                print('ma khon ton tai!')
        else:
            print('ds trong!')
    elif(chon == '5'):
        if(len(dsn) > 0):
            sl_sv = 0
            sl_gv = 0
            for i in dsn:
                if(isinstance(i , SinhVien)):
                    sl_sv += 1
                if(isinstance(i , GiaoVien)):
                    sl_gv += 1
            print('sl sv: ' , sl_sv)
            print('sl gv: ' , sl_gv)
        else:
            print('ds trong!')
    
    elif(chon == '6'):
        if(len(dsn)> 0):
            tong_luong = 0
            for i in dsn:
                if(isinstance(i , GiaoVien)):
                    tong_luong =  i + tong_luong
            print('tong luong: ' , tong_luong)   
        else:
            print('ds trong!')     
    
    elif(chon == '0'):
        break
    else:
        print('chon khong co trong he thong!')