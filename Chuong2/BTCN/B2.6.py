t=input("Ho ten: ")
n=int(input("So ngay cong: "))
dg=int(input("Don gia ngay cong: "))
hs=float(input("He so phu cap: "))
tu=int(input("Tam ung: "))
l=dg*n*hs
tl=l-tu
print("Nhan vien ",t,","," Co tien luong=",float(l),","," Tam ung=",tu," va Thuc linh=",float(tl),sep="")
