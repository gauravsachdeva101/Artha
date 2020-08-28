import pymysql

def dailylog(cursor,path,filetostore,mydb):
    #opening file
    f = open(path+'\\'+filetostore,'r')
    fString = f.read()
    fList= []
    #making the list
    for line in fString.split('\n'):
        fList.append(line.split(','))

    #defined columns as the column in csv file
    col1 = str(fList[0][0])
    col1 = col1[4:12]
    col2 = str(fList[0][1])
    col2 = col2[1:23]
    querydailygenerationtable = """CREATE TABLE IF NOT EXISTS daily_generation({} DATE,`{}` VARCHAR(255))""".format(col1,col2)
    #creating table
    cursor.execute(querydailygenerationtable)
    del fList[0]
    rows = ''
    #defining rows
    for i in range(len(fList)):
        value1=str(fList[i][0]);value2=str(fList[i][1])
        rows+="('{}','{}')".format(value1[1:11],value2)
        if i!=len(fList)-1:
            rows+=','
    #inserting rows in db
    queryinsert = "INSERT INTO daily_generation VALUES"+ rows
    cursor.execute(queryinsert)
    mydb.commit()


def errorlog(cursor,path,filetostore,mydb):
    #opening file
    f = open(path+'\\'+filetostore,'r')
    fString = f.read()
    fList= []
    #creating lists
    for line in fString.split('\n'):
        fList.append(line.split(','))
    del fList[0]
    del fList[0]
    
    #defining columns
    col1 = str(fList[0][0]);col1 = col1[0:13]
    col2 = str(fList[0][1]);col2 = col2[1:5]
    col3 = str(fList[0][2]);col3 = col3[0:14]
    col4 = str(fList[0][3]);col4 = col4[0:8]
    col5 = str(fList[0][4]);col5 = col5[0:14]
    col6 = str(fList[0][5]);col6 = col6[0:14]
    col7 = str(fList[0][6]);col7 = col7[0:13]
    #creating table
    querydailygenerationtable = """CREATE TABLE IF NOT EXISTS error_logs(
                                    `{}` VARCHAR(255),
                                    `{}` VARCHAR(255),
                                    `{}` VARCHAR(255),
                                    `{}` VARCHAR(255),
                                    `{}` DATETIME,
                                    `{}` DATETIME,
                                    `{}` VARCHAR(255)
                                    )""".format(col1,col2,col3,col4,col5,col6,col7)

    cursor.execute(querydailygenerationtable)
    del fList[0]
    #defining rows
    rows = ''
    for i in range(len(fList)-1):
        val1=str(fList[i][0]);val2=str(fList[i][1]);val3=str(fList[i][2]);val4=str(fList[i][3]);val5=str(fList[i][4]);val6=str(fList[i][5]);val7=str(fList[i][6])
        rows+="('{}','{}','{}','{}','{}','{}','{}')".format(val1[1:6],val2[1:11],val3[1:6],val4[1:4],val5[1:20],val6[1:20],val7[1:])
        if i!=len(fList)-2:
            rows+=','

    #inserting rows in db
    queryinsert = "INSERT INTO error_logs VALUES"+ rows
    cursor.execute(queryinsert)
    mydb.commit()