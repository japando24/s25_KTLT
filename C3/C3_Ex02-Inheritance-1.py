#%% Superclass
class Employee:
    def __init__(self, ten, nam_vao_lam, luong_co_ban):
        self.ten = ten
        self.nam_vao_lam = nam_vao_lam
        self.luong_co_ban = luong_co_ban
        self.luong = luong_co_ban*1.5

    def thong_tin(self):
        print(f"Tên: {self.ten} vào làm: {self.nam_vao_lam}, lương: {self.luong}")

#%% Subclass kế thừa từ Employee
class SaleEmployee(Employee):
    def __init__(self, ten, nam_vao_lam, luong_co_ban, phu_cap):
        super().__init__(ten,nam_vao_lam,luong_co_ban)
        self.phu_cap = phu_cap
    def tinh_luong(self):
        self.luong=self.luong_co_ban*3+self.phu_cap

class DeliveryEmployee(Employee):
    def tinh_luong(self):
        self.luong=self.luong_co_ban*2

#%% Tạo đối tượng từ superclass
nv=Employee("Nam Anh", 2012, 5000000)
nv.thong_tin()

#%% Tạo đối tượng NV bán hàng từ subclass
nv1=SaleEmployee("Huỳnh Giao", 2018, 5000000,2000000)
nv1.tinh_luong()
nv1.thong_tin()

#%% Tạo đối tượng NV giao nhận từ lớp con
nv2=DeliveryEmployee("Tuấn Kiêth",2017,5000000)
nv2.tinh_luong()
nv2.thong_tin()

