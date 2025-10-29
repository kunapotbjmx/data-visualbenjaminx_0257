mon = 1500
while True:
    print('ระบบธนาคาร')
    admin = input('กรอกชื่อผู้ใช้ : ' )
    pas = int(input('กรอกรหัส :  '))

    if admin == ('bjmx') and pas == (1234):
        print('เข้าสู่ระบบสำเร็จ')

        money = True
        while money:
            print('ยอดคงเหลือ : ' , mon)
            ton = input('โปรดเลือกรายการที่จะทำการ '
            '(1) ถอนเงิน  '
            '(2) ฝากเงิน '
            '(3) ยอดคงเหลือ '
            '(4) ออกจากระบบ  : ')
            
            if ton == "1":
                try:
                    one = int(input('ถอนเงิน : '))
                    if one > 0 and one <= mon:
                        mon -= one
                        print('ถอนเงินสำเร็จ : ' , one , 'บาท')
                        print('ยอดเงินคงเหลือ :' , mon , 'บาท')
                    elif one <= 0 :
                        print('ยอดจำนวนที่จะถอนต้องมากกว่า 0 ')
                    else:
                        print('ยอดจำนวนเงินในบัญชีไม่เพียงพอที่จะถอน : ', one , 'บาท')

                except ValueError:
                    print('โปรดป้อนข้อมูลที่จะทำการให้ถูกต้อง')

            elif ton == "2":
                try:
                    two = int(input('ฝากเงิน : '))
                    if two > 0:
                        mon += two
                        print('ฝากเงินสำเร็จ : ' , two , 'บาท')
                        print('ยอดเงินคงเหลือ :' , mon , 'บาท')
                    else:
                        print('จำนวนเงินที่ฝากต้องมากกว่า 0')

                except ValueError:
                    print('โปรดป้อนข้อมูลที่จะทำการให้ถูกต้อง')
            elif ton == "3":
                print('ยอดเงินคงเหลือ : ' , mon , 'บาท')
            
            elif ton == "4":
                print('ออกจากระบบ :' , pas)
                money = False
            else:
                print('ผิดพลาดโปรดลองใหม่')
    else:
        print('ผิดพลาดเข้าสู่ระบบใหม่')

    stop = input('พิมพ์ หยุด เพื่อออกจากระบบ หรือ กด enter เพื่อเข้าสู่ระบบใหม่อีกครั้ง : ')
    if stop.lower() == 'หยุด':
        print("ออกจากระบบเสร็จสิ้น")
        break

# ton = input('โปรดเลือกรายการที่จะทำการ 1 และ 2 : ')
#         if ton == "1":
#             one = input("ถอนเงิน : ")
#             print(mon-one)
#         elif ton == '2':
#             two = input("ฝากเงิน : ")
#             print(mon+two)
#         else:
#             print('ผิดพลาดโปรดลองใหม่')