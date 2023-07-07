from zk import ZK, const
import time 
import datetime
try:
    import pywhatkit
except:
     print("No internet!")

conn = None

zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
with open("message.txt","r",encoding='utf-8') as file:
     message=file.read()
try:
    conn = zk.connect()
    users = conn.get_users()
    AllUsers={}
    timeStd={
        "01":[],
        "02":[],
        "03":[],
        "04":[],
        "05":[],
        "06":[],
        "07":[],
        "08":[],
        "09":[],
        "10":[],
        "11":[],
        "12":[],
        "13":[],
        "14":[],
        "15":[],
        "16":[],
        "17":[],
        "18":[],
        "19":[],
        "20":[],
        "21":[],
        "22":[],
        "23":[],
        "00":[]
    }
    for user in users:
        namy=user.name
        namy=namy.split("\\")[-1]
        AllUsers[user.uid]='{}'.format(namy)

    for key,value in AllUsers.items():
        timeStd[value[:2]].append(key)
except Exception as e:
         print("Device isn't connected!")
Student={
        "01":[],
        "02":[],
        "03":[],
        "04":[],
        "05":[],
        "06":[],
        "07":[],
        "08":[],
        "09":[],
        "10":[],
        "11":[],
        "12":[],
        "13":[],
        "14":[],
        "15":[],
        "16":[],
        "17":[],
        "18":[],
        "19":[],
        "20":[],
        "21":[],
        "22":[],
        "23":[],
        "00":[]
    }
while True:
    try:
        now = datetime.datetime.now()
        if now.minute == 30 and now.second == 0:

            hour = now.strftime("%H")
            attendances = conn.get_attendance()
            for attend in attendances:
                idAttend=int(str(attend).split(":")[1])
                Student[f"{hour}"].append(idAttend)
            WaSender=[x for x in timeStd[f"{hour}"] if x not in Student[f"{hour}"]]
            conn.clear_attendance()
            for std in WaSender:
                pywhatkit.sendwhatmsg_instantly(f"+2{AllUsers[std][2:]}",message,15,True,3)
            for value in Student.values():
                 value.clear()
        time.sleep(1)
        
    except:
        pass