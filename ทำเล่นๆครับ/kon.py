
# while True:
#     row = int(input("แม่สูตรคูณ :"))

#     for i in range(1,13):
#         print(row , "x" , i , "=" ,row*i)

#     stop = input('หยุด : ')
#     if stop == "st":
#         break


# mon = 0
# for i in range(1,6):
#     lal = int(input('ลำดับที่ ' + str(i) + ' : '))
#     mon += lal
# print('ผลรวม ' , mon)

# mon = 0
# while True:
#     tot = int(input("กรอกเลข : "))
#     if tot<=0:
#         break
#     mon+=tot
# print(mon)    

# while True:
#     op = int(input("กรอกเลข1 : "))
#     po = int(input("กรอกเลข2 : "))

#     for i in range(op,po+1):
#         print('แม่สูตรคูณ ' , i)
#         print('_____________')
#         for j in range(1,13):
#             print(i , 'x' , j , '=' , i*j)
#         print('_____________')

#     c = input('พิมพ์หยุด : ')
#     if c == 'หยุด':
#         print("หยุดการทำงาน")
#         break

# ohb = int(input('กรอกพ.ศ. : '))

# tor = f"อายุของคุณ {2569-ohb}"
# print(tor)

# while True:
#     name = input('กรอกชื่อของคุณ : ')
#     if name.startswith("นาย"):
#         print("เพศชาย")
#     elif name.startswith("นางสาว"):
#         print("เพศหญิง")
#     else:
#         print('ผิดพลาดโปรดกรอกชื่อใหม่อีกคร้ง')

name = input("กรอกชื่อ : ")
age = input("กรอกอ่ายุ : ")
iron = 'ผมชื่อ {} ครับ อายุ {} ปี'.format(name,age)
print(iron)