#Tạo ra những đối tượng sản phẩm có các thuộc tính: code, name, price; có phương thưc xem thông tin sp: getProductInfo
#%% Định nghĩa Class Product
class Product:
    def __init__(self,code, name, price): #Tham số hình thức
        #Hàm khỏi tạo (contructor): định nghĩa thuộc tính cho đối tượng
        self.pCode=code
        self.pName =name
        self.pPrice =price

    #Định nghĩa phương thức cho đối tượng
    def getProductInfo(self):
        return (f"{self.pCode} {self.pName} {self.pPrice}")

    def __repr__(self):
        return f"{self.pCode} {self.pName.upper()} >> ${self.pPrice/25000}"

#%%
#Khởi tạo đối tượng sp có code:1, name: "Tiger", price:19000
p1=Product(1,"Tiger",19000)
p2=Product(2,"Heineken",20000)


#%%
#Truy vấn thuộc tính, phương thức của đối tượng
#print(p1.pName)
# print(f"Code: {p1.pCode}, Name: {p1.pName}, Price: {p1.pPrice}")
#print(p1.getProductInfo())
#rint(p1.__dict__)
print(p1) #Bắt buộc định nghĩa hàm: def __repr__ (self):