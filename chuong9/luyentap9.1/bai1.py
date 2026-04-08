class HocVien:
    def __init__(self, ht, email, dienthoai, diachi, lop):
        self.ten_hv = ht
        self.email = email
        self.dienthoai = dienthoai
        self.diachi = diachi
        self.lop = lop
    def showInfo(self):
        print("Ten HV: ", self.ten_hv)
        print("Email: ", self.email)
        print("Dien thoai: ", self.dienthoai)
        print("Dia chi: ", self.diachi)
        print("Lop: ", self.lop)
    def setinfo(self, diachi="hanoi", lop="it12.x"):
        self.diachi = diachi
        self.lop = lop
class Main:
    hv1=HocVien("Nguyen Van A", "nguyenvana@email.com", "0123456789", "Ha Noi", "IT12.1")
    hv1.showInfo()
    print("-------------")
    hv1.setinfo()
    hv1.showInfo()
    print("-------------")
    hv1.setinfo("Ha Nam", "IT12.2")
    hv1.showInfo()