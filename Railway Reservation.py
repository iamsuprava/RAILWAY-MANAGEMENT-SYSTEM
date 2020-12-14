import mysql.connector
#import MySQLdb
#import os
#import platform
#import pondos os pd
#pnr=1010


mydb=mysql.connector.connect(host="localhost",user="root",password="123456,daatabase= "rail");
#mydb=MySQLdb.connect(host="localhost",user="root",db="rail")

mycursor=mydb.cursor()                             






#GET THE LAST PNR NO.:
sql="select pnrno from passengers order by pnrno desc limit 1;"
print(sql)
mycursor.execute(sql)
res=mycursor.fetchall()
pnr=1000; if len(res)>0:
    pur=int(res[0][0])print(pnr)
print(res)

def railresmenu():
    print("Railway Reservation")
     print("1.train Details")
      print("2.Reservation of Ticket")
       print("3.cancellation of Ticket")
        print("4.Display PNR status")
        print("5.Quit")

n=int(input("Enter your choice")
      if n==1:
      traindetails()
      elif n==2:
          reservation()
      elif n==3:
          cancel()
      elif n==4:
          displayPNR()
      elif n==5:
           exit(0)
      else:
           print("Wrong choice")

def traindetail():
    print("Train Details")
    ch="y"
    while(ch=="y"):
        I=[]
        name=input("Enter train name")
        I.append(name)
        tname=int(input("Enter train name:"))
        I.append(tname)
        ac1=int(input("enter number of AC 1 class seats"))
        I.append(ac1)
        ac2=int(input("enter number of AC 2 class seats"))
        I.append(ac2)
        ac3=int(input("enter number of AC 3 class seats"))
        I.append(ac3)
        slp=int(input("enter number of sleeper class seats"))
        I.append(slp)
        train=(I)
        sql= "insert into traindetail(tname, tnum,ac1,ac2,ac3,slp)values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,train)
        mydb.commit()
        print("insertion completed")
        print("Do you want to insert more train Detail")
        ch=input("enter yes/no")
        print('/n'*10)
        print("=======================================================")

railresmenu()
def reservation():
global pnr
I1=[]
pname=input("enter passenger name=")
I1.append(pname)
age=input("enter train number")
I1.append(age)
tainno=input("enter train number")
I1.append(trainno)
np=int(input("Enter number of passengers"))
I1.append(np)
print("select a class you would like to travel in")
print("1.AC FIRST CLASS")
print("2.AC SECOND CLASS")
print("3.AC THIRD CLASS")
print("4.SLEEPER CLASS")
cp=int(input("Enter your choise"))
       if cp==1:
           ammount=np*1000
           cls="ac1"
       elif cp==2:
           ammount=np*800
           cls="ac2"
       elif cp==3:
            ammount=np*500
            cls="ac3"
       elif cp==3:
            ammount=np*350
            cls="slp"  
I1=append(cls)
print("Total amount to be paid:",amount) 
I1=append(amount)
pnr=pnr+1
print("PNR Number:",pnr)
print("Status: CONFIRMED")
sts="conf"
I1.append(sts)
I1.append(pnr)train1=(I1)
sql= "insert into traindetail(pname,age,trainno,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"
mycursor.execute(sql.train1)
mydb.commit()
print("insertion completed")
print("Go back to menu")
print('/n'*10)
print("=======================================================")



railresmenu()
def cancel():
print("Ticket cancel window")
pnr=input("enter PNR for cancellation of Ticket")
pn=(pnr,)
sql="update passengers set status=deleted pnrno=%s"
mycursor.execute(sql,pn)
mydb.commit()
print("Deletion completed")
print("Go back to menu")
print('/n'*10)
print("=======================================================")


railresmenu()
def displayPNR():
    print("PNR STATUS window")
    pnr=input("enter PNR NUMBER")
    pn=(pnr,)
    sql="select * from passengers where pnrno=%s")
mycursor.execute(sql,pn)
res=mycursor.fetchall()
#mydb.commit()
print("PNR STATUS are as followrs:")
print("pname,age,trainno,noofpas,cla,amt,status,pnrno")
     for x in res:
         print(x)
print("Deletion completed")
print("GO back to menu")
print('/n'*10)
print("=======================================================")
railresmenu()
