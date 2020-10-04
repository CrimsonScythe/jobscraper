import pickle
import re
import psycopg2

with open('responses.pkl', 'rb') as f:
    newlst = pickle.load(f)

def getTime(listing):
    match = re.findall(r'Oprettet.*', listing[0].decode("utf-8"))
    match = list(set(match))
    if (len(match)==0):
        return
    time = re.findall(r'[0-9]\s\w+', match[0])
    if (len(time)==0):
        return    
    return time[0]

def getPosition(listing):
    match = re.findall(r'<meta property=\"og:title\".*', listing[0].decode("utf-8"))
    
    if (len(match)==0):
        return
    
    return match[0][34:]
     
'''
load languages and frameworks in lists
'''
# def cleanframes(fra):
    
frames=''
langes=''
with open('cleanedframe.txt', 'r') as f:
    frames=f.read()

with open('rawlanguages2.txt', 'r') as f:
    langes=f.read()

lstframes=frames.split('\n')
lstlang = langes.split('\n')


for i in range(len(lstframes)):
    lstframes[i]=lstframes[i].strip('\t')


def getLang(listing):
    
    l_p = listing[0].decode('utf-8').split('\n')
    setla=set()
    for rr in lstlang:
        for tt in l_p:
            if (rr in tt):
                setla.add(rr)
    # print(setla)
    return list(setla)
            
def getFrame(listing):

    l_p = listing[0].decode('utf-8').split('\n')
    setla=set()
    for rr in lstframes:
        for tt in l_p:
            if (rr in tt):
                setla.add(rr)
    # print(setla)
    return list(setla)


frameworks = map(getFrame, newlst)
frameworks=list(frameworks)
print(len(frameworks))

languages = map(getLang, newlst)
languages=list(languages)
print(len(languages))

times = map(getTime, newlst)
times=list(times)
print(len(times))

positions = map(getPosition, newlst)
positions=list(positions)
print(len(positions))

#################
# PGADMIN
try:
    conn = psycopg2.connect(dbname='grad', user='postgres', password='root')
    cursor = conn.cursor()
    query=""" INSERT INTO jobs (des, languages, frameworks) VALUES (%s, %s, %s) ON CONFLICT ON CONSTRAINT uni DO NOTHING"""
    for i in range(len(frameworks)):
        cursor.execute(query, (positions[i], languages[i], frameworks[i]))
    # cursor.execute(query, ("mmdfg", 2, ["s", "s"], ["ss", "s"]))
    conn.commit()

except (Exception, psycopg2.Error) as error:
    print(error)

finally:
    if (conn):
        cursor.close()
        conn.close()
#################


