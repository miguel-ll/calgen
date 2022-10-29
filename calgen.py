from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import calendar
import os
import datetime
import sys

def create_mcal(y,mo):
    li = ["","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    mname = li[mo]

    m = calendar.monthcalendar(y,mo)

    mcal = [None for _ in range(6)]
    for r in range(6):
        mcal[r] = [" " for _ in range(7)]

    z = len(m)

    for i in range(z):
        for j in range(7):
            if m[i][j] != 0:
                if len(str(m[i][j])) == 1:
                    mcal[i][j] = " " + str(m[i][j])
                else:
                    mcal[i][j] = str(m[i][j])

    font = ImageFont.truetype("droid.ttf",50)
    font3 = ImageFont.truetype("roboto.ttf",55)
    font2 = ImageFont.truetype("droid.ttf",80)

    img = Image.open('template.png')

    I1 = ImageDraw.Draw(img)

    hs = 56
    vs = 222

    I1.text((40, 10), mname, font=font2, fill=(0, 0, 0))
    #for f in range(240,1000,80):
    #    I1.text((23, f), "__________________________________", font=font3, fill=(0, 0, 0))
    I1.text((640, 10), str(y), font=font2, fill=(255, 0, 0))

    for a in range(6):
        if a > 0:
            hs = 56
            vs+=80
        for b in range(7):
            I1.text((hs, vs), mcal[a][b], font=font3, fill=(0, 0, 0))
            hs+=112

    #img.show()
    img.save(f"cal{mo}.png")

def generate_cal(year):
    for d in range(1,13):
        create_mcal(year,d)

    li=[]
    for i in range(1,13):
        li.append(Image.open(f"cal{i}.png"))

    main = Image.open("white.png")

    sp=25
    ysp=760
    q = 0

    for b in range(4):
        for a in range(3):
            main.paste(li[q], (900*a + 25,100 + ysp*b), mask=li[q])
            q+=1

    #main.show()
    main.save(f"{year}_cal.png")
    for f in range(1,13):
        os.remove(f"cal{f}.png")

if len(sys.argv) > 0:
    generate_cal(int(sys.argv[1]))
else:
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    yr = int(date.strftime("%Y"))
    generate_cal(yr)
