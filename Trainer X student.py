import mysql.connector as py
from datetime import date,timedelta
from mysql.connector import Error
myd=py.connect(host='localhost',user='root',passwd='root',database='gym')
myc=myd.cursor()
#----------------------------------------login--------------------------------------------------------------------
  
def login():
    while True:
        userS=input('enter username-->')
        passD=input('enter password-->')
        squer='select password from reg where username="{}"'.format(userS)
        myc.execute(squer)
        rec=myc.fetchone()
        if rec==None:
            print('No valid User')
            break
        else:
            if rec[0]==passD:
                print('| ☻ Logged in Succesfull2 ☻  |')
                while True:
                    print('[1] veiw ur profile\n[2] Update Profile\n[3]LOGOUT')
                    try:
                        ch=int(input('ENTER YOUR Choice-->'))
                    except ValueError:
                        print('USE INTEGERS')
                        continue
                    if ch==1:
                          print('|UR PROFILE|')
                          profile='select * from membert where name ="{0}"'.format(userS)
                          
                          myc.execute(profile)
                          
                          FP=myc.fetchone()
                          veryfy(FP)
                    elif ch==2:
                        print('What u want to update\n[1]:Name\n[2]PH NO\n[3]NONE')
                        ask1=input('\n->')
                        if ask1== '1':
                            profile_2='select name from membert where name ="{0}"'.format(userS)
                            myc.execute(profile_2)
                            NM=myc.fetchone()
                            print(NM[0],' is ur current name do u wish to change it?')
                            ch=input("YES/NO:")
                            if ch in ['yes',"YES","Y","y"]:
                                   new_name=input("Enter new name:")
                                   name_end="select username from reg where username='{0}'".format(new_name)
                                   myc.execute(name_end)
                                   name_rec=myc.fetchone()
                                   if name_rec == None:
                                       myc.execute("update membert set name='{n}' where name = '{N}'".format(n=new_name,N=NM[0]))
                                       myd.commit()
                                       myc.execute("update reg set username='{n}' where username = '{N}'".format(n=new_name,N=NM[0]))
                                       myd.commit()
                                       userS = new_name
                                   else:
                                    print('Name alredy exist ,no change made')
                                   
                            elif ch=="NO"or"no":
                                print("NO CHANGE")
                        elif ask1=="2":
                            query2="select  Contact from membert where name='{}'".format(userS)
                            myc.execute(query2)
                            MN=myc.fetchone()
                            print(MN[0],'is your current phone no: do you wish to change it?')
                            ch1=input("YES/NO")
                            if ch1 in ['yes',"YES","Y","y"]:
                                      new_number=int(input("Enter new phone number:"))
                                      if new_number>10000000000:
                                          print("WRONG NUMBER")
                                      else:
                                          q3="update membert set Contact={0} where name='{1}'".format(new_number,userS)
                                          myc.execute(q3)
                                          myd.commit()
                        elif ask1=='3':
                            password_change(userS)
                            
                        else:
                            print('NO valid option')
                            
                            
                            
                                    
                    elif ch==3:
                        print('|LOGGED OUT|\n\n')
                        return 
                        
                    else:
                        print('No option')
                        continue    
            else:

               print('wrong password')

def password_change(userS):
    query_1='select password from reg where username="{}"'.format(userS)
    myc.execute(query_1)
    p_w=myc.fetchone()
    print("|",p_w[0],"|",'>-this is ur current password ')
    q1=input('do u want to change it?}|YES/NO|-->')
    if q1 in ['yes',"YES","Y","y"]:
        new_password=input('Enter the new password-->')
        query_2='update reg set password="{pw}" where username="{N}"'.format(pw=new_password,N=userS)
        myc.execute(query_2)
        myd.commit()
        print('successful changed')
    
def veryfy(FP):
    try:
        print('MID\t Name\t PH\t\tMEMBERSHIP\t JOINED\t\t END')
        m1,nam,ph,ship,jd,ed = FP[0],FP[1],FP[2],FP[3],str(FP[4]),str(FP[5])
        print(m1,'\t',nam,'\t',ph,'\t',ship,'\t',jd,'\t',ed)
        print()
    except TypeError:
        print('USER NOT FOUND')
#------------------------------------------------LOop for mid------------------------------------------------------
def mid_G():
    q1='select Mid from membert'
    myc.execute(q1)
    try:
        r=myc.fetchall()
        a=myc.rowcount
        L=r[a-1][0]+1
        return L
    except IndexError:
        L=1
        return L
#------------------------------------------------registeration------------------------------------------------------    
def reg():
    print('|REGISTER|')
    userR=input('Enter ur Name->')
    if userR.isspace():
        print('Atleast variable characters')
        reg()
    passD=input('Enter  ur password->')
    if passD in ['password','PASSWORD']:
        print('NOT A STRONG PASSWORD\n')
        reg()
    else:
        pass
    if passD.isspace():
         print('NOT A STRONG PASSWORD\n')
         reg()
        
    squer="insert into reg values('{}','{}')".format(userR,passD)
    try:
        myc.execute(squer)
        myd.commit()
    except Error:
        print('\n--name aleready Exist--\n') # due to primary key same value cause error
        
        return reg()
    try:    
        con=int(input('Enter the PH:NO->'))
    except ValueError:
        print('USE INTEGER ')
        myc.execute('delete from reg where username="{}"'.format(userR))
        myd.commit()
        reg()
    if con>10**9:#len(con)!=10 after debuging
        print('WRONG NUMBER')
        myc.execute('delete from reg where username="{}"'.format(userR))
        myd.commit()
        reg()
        
    print('\n')
    print('+∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞+∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞+∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞+')
    print('|[1]:3 month:9150$\t |[2]:6 month:12999$\t  |[3]:12 months:14999$     |')
    print('|->:Personal Trainer\t |->:Personal Trainer\t  |->:Personal Trainer      |')
    print('|->:10 days MPuase   \t |->:30 days MPuase \t  |->:60 days MPuase        |')
    print('|->:5 swiming session\t |->:5 swiming session \t  |->:5 swiming session     |')
    print('|->:free transfer in 7day|->:free transfer in 7day|->:free transfer in 7day |')
    print('+∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞+∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞+∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞+')
    ship=input('\nEnter the MemberShip [1] [2] [3] ->')
    

    join=date.today() #get todays date


    #for assigning Jdate and Edate
    if ship== '3':
        date_end= join + timedelta(days=365) #YEARLY
        me='YEARLY'
    elif ship== '2':
        date_end= join + timedelta(days=180) #MONTHLY
        me='6 MONTH'
    elif ship == '1':
        date_end= join + timedelta(days=90)  #3 MONTHS
        me='3 MONTHS'
    else:
        pass
    rec=myc.fetchall()
    if rec==None:
        myc.execute('delete from reg where username="{}"'.format(userR))
        print('Attempt was unsucessfull')
    else:
        try:
            print('Attempt Successfull')
            # usre name
            x1=mid_G()
            Lquery="insert into membert values({0},'{1}',{2},'{3}','{4}','{5}')".format(x1,userR,con,me,join,date_end)#L
            myc.execute(Lquery)
            myd.commit()
            print('UR M_ID is NO:',x1,'\n')
        
            print('|loggin|')
            return login()
        except Error:
            print('Some thing went Wrong\n')
            myc.execute('delete from reg where username="{}"'.format(userR))
            myd.commit()
            myc.execute('delete from membert where name="{}"'.format(userR))
            myd.commit()
            reg()


#main loop
while True:
    print('UR CHOICE \n [1]login \n [2]register \n [3]quit')
    try :
        ch=int(input('enter ur choice-->'))
    except ValueError:
        print('USE INTEGER')
        continue
    if ch==1:
        login()        
    elif ch==2:
        reg()
    elif ch==3:
        print('X----------------------------------------------------X')
        break
