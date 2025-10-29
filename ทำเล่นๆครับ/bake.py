
mon = 1000
while True:
    bake = input('กรอกชื่อบัญชีของคุณ : ')
    psw = input('รหัสผ่าน : ')

    if bake == 'bjmx' and psw == "1234":
        print("เข้าสู่ระบบสำเร็จ")

        ioi = True
        while ioi:
            irom = input("โปรดเลือกรายการ 1 และ 2 : ")

            if irom == '1':
                try:
                    if irom == '1':
                        ton = int(input('ถอนเงิน : '))
                        mon -= ton
                        print("ยอดคงเหลือ" , mon ,'บาท')

                except ValueError:
                    print('ผิดพลาดโปรดลองใหม่')

            if irom == "2":
                try:   
                        fek = int(input('ฝากเงิน : '))
                        mon += fek
                        print("ยอดคงเหลือ" , mon ,'บาท')
                    
                except ValueError:
                    print('ผิดพลาดโปรดลองใหม่')
    else:
        print('ผิดพลาด')

    pop = input('พิมพ์คำสั่ง หยุด = เพื่อหยุดการทำงาน หรือ กด Enter เพื่อทำรายการต่อ : ')
    if pop == "หยุด" :
        print('หยุดการทำงาน')
        break