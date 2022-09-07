#-*- coding: utf-8 -*-

#exit()
from flask import *
from mai import *
import random
import time
global chlrh
from flask import Flask, render_template
import random
 
app = Flask(__name__)
aiseo = 0

print("서버 시작중")
@app.errorhandler(404)
def page_not_found(error):
    return "nots"

@app.errorhandler(500)
def page_not_found(error):
    return "처리서버와 연결하지 못했습니다. ⛌"





@app.route('/', methods=['GET'])
def index():
    return """
<title>딥러닝</title>
<!-- Channel Plugin Scripts -->
<script>
  (function() {
    var w = window;
    if (w.ChannelIO) {
      return (window.console.error || window.console.log || function(){})('ChannelIO script included twice.');
    }
    var ch = function() {
      ch.c(arguments);
    };
    ch.q = [];
    ch.c = function(args) {
      ch.q.push(args);
    };
    w.ChannelIO = ch;
    function l() {
      if (w.ChannelIOInitialized) {
        return;
      }
      w.ChannelIOInitialized = true;
      var s = document.createElement('script');
      s.type = 'text/javascript';
      s.async = true;
      s.src = 'https://cdn.channel.io/plugin/ch-plugin-web.js';
      s.charset = 'UTF-8';
      var x = document.getElementsByTagName('script')[0];
      x.parentNode.insertBefore(s, x);
    }
    if (document.readyState === 'complete') {
      l();
    } else if (window.attachEvent) {
      window.attachEvent('onload', l);
    } else {
      window.addEventListener('DOMContentLoaded', l, false);
      window.addEventListener('load', l, false);
    }
  })();
  ChannelIO('boot', {
    "pluginKey": "5611c175-d6ae-4927-9c4c-6cc0a1753e69"
  });
</script>
<!-- End Channel Plugin -->

<a>AI학습을 위해 정보를 적어주십시오</a><br>
<a>사용자말----------------봇대답----------------</a>
<form action="\post" method="post" class="input-form">
    <textarea type="text" name='id_name' value="tmp tmp tmp" class="input-text"></textarea>
    <a> </a>
    <textarea type="text" name='id_names' value="tmp tmp tmp" class="input-text"></textarea>
    <input type="submit" value="전송" class="input-btn">
</form>
"""
    
@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        value = request.form['id_name']
        value = str(value)
        values = request.form['id_names']
        values = str(values)
        print("--------------------------------")
        print(value)
        print(values)
        print("--------------------------------")
    return "감사합니다"

#da = "두둥탁"

#import time

#nots = []
#stopa = 0
#wjs = ""
#while True:
#    da = ai(da)
#    #print(wjs + "        " + str(chlrh))
#    if chlrh == 0:
#        if not wjs in nots:
#            stopa = stopa + 1
#            nots.append(str(wjs))
#    
#    if stopa == 25:
#        break
#    wjs = da
#    #time.sleep(0.25)
#print(nots)

def check_string(text):
    with open('data.txt', encoding='utf8') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'text' in line:
            return True # The string is found
    return False  # The string does not exist in the file

wjs = "안녕"
gn = ""

@app.route('/data/logs', methods=['POST', "GET"])
def datalogs():
    global aiseo
    try:
        datalog = ""
        fas = open("data.txt", 'r', encoding='utf8')
        m = 0
        errorn = 0
        aiseo = 0
        while True:
            m = m + 1
            line = fas.readline()
            #linej = fas.readline()
            if not line: break
            ok = 1
            try:
                line = line.strip()
                lines = line.find("=")
                #print(line)
                noset = 0
                test = line[:lines-1]
                if test == "":
                    noset = 1
                    print("!1-" + str(m))
                test = line[lines+2:]
                if test == "":
                    print("!2-" + str(m))
                    noset = 1
                #print(test)
                ok = 0
                if noset == 0:
                    ok = 1
                if noset == 1:
                    errorn = errorn + 1
            except:
                print("?")
                ok = 0
            if ok == 1:
                datalog = datalog + line + "     (O)" + "<br>"
            if ok == 0:
                datalog = datalog + line + "     (X)" + "<br>"
        fas.close()
        print("오류수:" + str(errorn))
    except:
        aiseo = 2
        errorn = 99
    try:
        print(aiseo)
        if errorn >= 2:
            datalog = "DB데이터 상태:불량 <br>수집데이터--------------------<br>" + datalog
        else:
            datalog = "DB데이터 상태:성공 <br>수집데이터--------------------<br>" + datalog
        if aiseo == 2:
            datalog = "ai서버 상태:불량 <br> DB서버 상태:불량 <br>데이터--------------------<br>" + datalog
        if aiseo == 1:
            datalog = "ai서버 상태:성공 <br> DB서버 상태:성공 <br>데이터--------------------<br>" + datalog
        if aiseo == 0:
            datalog = "ai서버 상태:불량 <br> DB서버 상태:성공 <br>데이터--------------------<br>" + datalog
    except Exception as mg:
        datalog = "점검서버와 연결하지못했습니다 오류:" + str(mg)
    return datalog

@app.route('/data/log', methods=['POST', "GET"])
def datalog():
    tn = 0
    fas = open("data.txt", 'r', encoding='utf8')
    while True:
        line = fas.readline()
        if not line: break
        tn = tn + 1
    fas.close()
    return str(tn)

@app.route('/bot/<text>', methods=['POST', "GET"])
def bot(text):
    try:
        print("1")
        datal = ai(text, "data.txt")
        return datalog
    except Exception as errorl:
        aiseo = 2
        print(errorl)
        return "DB 서버와 연결을 실패했습니다. (1) ⛌"

#-----------------------------------

@app.route('/bots/<text>/<serverid>', methods=['POST', "GET"])
def botupdata(text, serverid):
    global aiseo
    if "\n" in text:
        return "두둥탁!"
    
    aiseo = 0
    ok = 0
    f = open('id.txt', 'r')
    line_num = 1
    line = f.readline()
    while line:
        line = line.strip()
        #print(line)
        if line == serverid:
            ok = 1
        #print(line)
        line = f.readline()
        line_num += 1
    f.close()


    if ok == 1:
        try:
            print("serverid:" + str(serverid))
            print("입력:" + text)
            datal = ai(text, "data.txt")
            print("결과:" + datal)
            #print("2")
            fa = open("ds.txt", 'r')
            chlrhk = fa.readline()
            fa.close()
            print("점수:" + str(chlrhk))
            datachlrhk = chlrhk
            #print(datal)
            #print(chlrhk)
        except:
            aiseo = 2
            return "DB 서버와 접근을시도했지만. 접근할수없습니다 (3) ⛌"
        try:
            chlrhk = int(chlrhk)
        except:
            pass
        try:
            chlrhk = round(chlrhk)
        except:
            return "대답하기 시러"
        try:
            #print("!")
            fa = open("dsm.txt", 'r')
            wjs = fa.readline()
            fa.close()
            

            gn = text
            if not check_string(datal):
                j = open("data.txt",'a+', encoding='utf8')
                j.write(str(wjs) + " = " + str(gn) + "\n")
                j.close()
            
            


            #print("!")
            fjs = open("dsm.txt", 'w')
            fjs.write(str(datal))
            fjs.close

            #print("@")
            if datal == None:
                datal = ""
            #print(str(datal))
            time.sleep(random.random())
            fah = open("ds.txt", 'r')
            fj = fah.readline()
            fah.close()
            print("원래점수:" + fj)
            print("확인된 점수:" + datachlrhk)
            man = ck(datal)
            if chlrhk < 50:
                return "nots"
            if fj == datachlrhk:
                if man == 1:
                    return datal
                if man == 3:
                    hhdf = fu(datal)
                    return hhdf.replace('𐁔','X')
                if man == 2:
                    return "(심한욕)"
                aiseo = 1
            else:
                aiseo = 1
                return "이용률이많아 잠시후 이용해주세요 ⛌"
        except Exception as errorl:
            aiseo = 2
            print(errorl)
            print("초기화중")
            nf = open("ds.txt",'w')
            nf.write("0")
            nf.close
            nf = open("dsm.txt",'w')
            nf.write("0")
            nf.close
            return "DB 서버와 연결을 실패했습니다. (1) ⛌ (자동 복구중입니다 기달려주세요)"
    if ok == 0:
        aiseo = 1
        return "처리서버와 연결할수없습니다 화이트리스트를 확인해주세요 (0) ⛌"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 
