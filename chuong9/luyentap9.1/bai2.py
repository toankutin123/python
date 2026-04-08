from math import gcd


class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        if mau_so == 0:
            raise ValueError("Mau so khong duoc bang 0.")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def toi_gian(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

        if self.mau_so < 0:
            self.tu_so *= -1
            self.mau_so *= -1
        return self

    def nhan(self, phan_so_khac):
        return PhanSo(
            self.tu_so * phan_so_khac.tu_so,
            self.mau_so * phan_so_khac.mau_so
        ).toi_gian()

    def chia(self, phan_so_khac):
        if phan_so_khac.tu_so == 0:
            raise ValueError("Khong the chia cho phan so co tu so bang 0.")
        return PhanSo(
            self.tu_so * phan_so_khac.mau_so,
            self.mau_so * phan_so_khac.tu_so
        ).toi_gian()

    def tong(self, phan_so_khac):
        return PhanSo(
            self.tu_so * phan_so_khac.mau_so + phan_so_khac.tu_so * self.mau_so,
            self.mau_so * phan_so_khac.mau_so
        ).toi_gian()

    def hieu(self, phan_so_khac):
        return PhanSo(
            self.tu_so * phan_so_khac.mau_so - phan_so_khac.tu_so * self.mau_so,
            self.mau_so * phan_so_khac.mau_so
        ).toi_gian()

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"


class Main:
    ps1 = PhanSo(2, 3)
    ps2 = PhanSo(4, 5)

    print("Phan so 1:", ps1)
    print("Phan so 2:", ps2)
    print("Tong:", ps1.tong(ps2))
    print("Hieu:", ps1.hieu(ps2))
    print("Nhan:", ps1.nhan(ps2))
    print("Chia:", ps1.chia(ps2))
    print("Toi gian 8/12:", PhanSo(8, 12).toi_gian())
