import base64
import hashlib
#from Crypto import Random
#from Crypto.Cipher import AES
from flask import *
import random
global chlrh


def fu(text):
    fuckdata = ["@", "@", "<", ">", "똥", "떵", "물", "F", "U", "C", "K", "이", "노", "마", "썅", "씨", "발", "미", "친", "븅", "병", "신", "개", "새", "끼", "애", "미", "닥", "쳐", "꺼", "져", "창", "녀", "사", "팔", "f", "c", "u", "k", "도", "샹", "놈", "이", "좆", "좃", "좇"]
    ma = ""
    lista = list(text)
    for ia in lista:
        da = ia
        for i in fuckdata:
            if ia == i:
                print(i + " - " + ia)
                da = "𐁔"
        ma = ma + da
    return ma


def ck(text):
    f = fu(text)
    print("검열: " + f.replace('𐁔','X'))
    print("욕점수: " + str(int(f.count('𐁔') * 1.25)))
    #print(str(f.count('𐁔') + " - " + str(len(str(f.count('𐁔'))))))
    if int(f.count('𐁔') == int(len(str(f.count('𐁔'))))):
        return 2
    else:
        if int(f.count('𐁔') * 1.25) < 2:
            print("채팅")
            return 1
        else:
            if int(f.count('𐁔') * 1.25) >= 9:
                print("채팅X")
                return 2
            else:
                if int(f.count('𐁔') * 1.25) >= 2:
                    print("검열후 채팅")
                    return 3
#print(ck("똥물"))
def ai(texts, datatxt):
    #chlrhs = 100
    #return "테스트입니다."
    try:
        #data.txt
        f = open(datatxt, 'r', encoding='UTF8')
        global chlrh
        chlrh = 0
        chlrhs = 33
        lists = []
        lines = f.readlines()
        f.close()
        for line in lines:
            #print(line)
            line = line.strip()
            lines = line.find("=")
            #print(line)
            #print(line[:lines-1])
            #print(line[lines+2:])


            text = line[:lines-1]

            #texts = "머해"
            i = 0
            tn = 0
            while True:
                i = i + 1
                i2 = 0
                if i == len(text):
                    break
                while True:
                    i2 = i2 + 1
                    #print("---------------------")
                    #print(i2)
                    #print(len(texts))
                    if i2 == len(texts):
                        break
                    try:
                        if text[i] == texts[i2]:
                            tn = tn + 1
                    except:
                        pass
            wjatn = tn / len(text)
            wjatn = wjatn * 100
            wjatn = round(wjatn, 2)
            #print(wjatn)



            
            if chlrhs < wjatn:
                lists = [""]
                chlrhs = wjatn
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                #print("!")

            if 70 < wjatn:
                #chlrh = wjatn
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                #print("!")

            if chlrh <= wjatn:
                chlrh = wjatn
                lists.append(line[lines+2:])
                #print("!")

            if chlrh-2 < wjatn:
                chlrh = wjatn
                lists.append(line[lines+2:])
                #print("!")




            if 85 < wjatn:
                #chlrh = wjatn
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                #print("!")

            if 100 < wjatn:
                #chlrh = wjatn
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                lists.append(line[lines+2:])
                #print("!")
            
                
        #f.close()
        #print(lists)
        chlrhk = round(chlrh)
        fjs = open("ds.txt", 'w')
        fjs.write(str(chlrhk))
        fjs.close
        #return "테스트입니다."
        return lists[random.randrange(0,len(lists))]
    except Exception as error:
        print(error)
        return "파일 서버와 연결을 실패했습니다. (2) ⛌"
