import math
print("GIAI PHUONG TRINH BAC 2")
def Giai_Phuong_Trinh_Bac_2(a,b,c):
    delta = b**2 - 4*(a*c)
    if a + b + c == 0:
        x1 = 1
        x2 = float(c/a)
        print("x1 = ",x1,"x2 = ",x2)
    elif a - b + c == 0:
        x1 = -1
        x2 = float(-c/a)
        print("x1 = ",x1,"x2 = ",x2)
    elif delta > 0:
        x1 = (float)((-b+ math.sqrt(delta))/2*a)
        x2 = (float)((b + math.sqrt(delta)) / 2 * a)
        print('Phuong trinh co nghiem x1 =',x1,"Phuong trinh co nghiem x2 = ",x2)
    elif delta == 0:
        x1 = x2 = float(-b/2*a)
        print("Phuong trinh co nghiem kep x1 = x2 = ",x1)
    elif delta < 0:
        print("Phuong trinh vo nghiem")
a = float(input("Nhập hệ số bậc 2, a = "))
b = float(input("Nhập hệ số bậc 1, b = "))
c = float(input("Nhập hằng số tự do, c = "))
Giai_Phuong_Trinh_Bac_2(a, b, c)
a=float(input("Nhập chiều rộng:")) 
b=float(input("Nhập chiều dài"))
print("Chu vi hình chữ nhật là:",(a+b)*2)
print("Diện tích hình chữ nhật là:",a*b)
