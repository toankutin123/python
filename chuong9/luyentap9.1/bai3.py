from abc import ABC, abstractmethod
import math

class HinhHoc(ABC):
    @abstractmethod
    def TinhDienTich(self):
        pass

    @abstractmethod
    def TinhChuVi(self):
        pass

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def TinhDienTich(self):
        return math.pi * self.ban_kinh ** 2

    def TinhChuVi(self):
        return 2 * math.pi * self.ban_kinh

class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def TinhDienTich(self):
        return self.chieu_dai * self.chieu_rong

    def TinhChuVi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)