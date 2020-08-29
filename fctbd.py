import sqlite3



def nouveauutil(user,mp,level):#add user ,return None if already exists
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()

    infoutil=[(user,mp,level)]
    try:
        c.executemany('INSERT INTO utilisateur(username,password,level) VALUES (?,?,?)', infoutil)
        conn.commit()
        conn.close()
    except:
        return None

    return True

def check_name(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    tmp=""

    for row in c.execute("SELECT username FROM utilisateur WHERE username='%s'" % usern):
        tmp=row[0]


    conn.close()

    if(tmp==""):
        return False
    else:
        return True

def check_password(usern,mp):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    tmp=""

    for row in c.execute("SELECT password FROM utilisateur WHERE username='%s'" % usern):
        tmp=row[0]
        

    conn.close()

    if(tmp==mp):
        return True
    else:
        return False




def set_algoch(usern,algonum):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()

    

    c.execute("UPDATE utilisateur set algo='%d' WHERE username='%s'" %(algonum,usern))

    conn.commit()

    conn.close()


def get_algoch(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()

    algo=None
    

    for row in c.execute("SELECT algo from utilisateur WHERE username='%s'" % usern):

        algo=row[0]
    

    conn.close()

    return algo

def get_level(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()

    lev=None
    

    for row in c.execute("SELECT level from utilisateur WHERE username='%s'" % usern):

        lev=row[0]
    

    conn.close()

    return lev


#function bd cesar
def add_cesar(usern,p):

    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("INSERT INTO cesar(iduser,pas) VALUES('%d','%d')" % (id,p))

    conn.commit()

    conn.close()

def maj_cesar(usern,p):

    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("UPDATE cesar set cle='%d' WHERE iduser='%d'" % (p,id))

    conn.commit()

    conn.close()


def supprimer_algo(usern,ch):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("DELETE FROM '%s' WHERE iduser='%d'" % (ch,id ))

    conn.commit()

    conn.close()

# function bd hill
def add_hill(usern,a,b,cc,d):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("INSERT INTO hill(iduser,a,b,c,d) VALUES('%d','%d','%d','%d','%d')" % (id,a,b,cc,d))

    conn.commit()

    conn.close()

def maj_hill(usern,a,b,cc,d):

    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("UPDATE hill set a='%d',b='%d',c='%d',d='%d' WHERE iduser='%d'" % (a,b,cc,d,id))

    conn.commit()

    conn.close()

def supp_hill(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("DELETE FROM hill WHERE iduser='%d'" % id )

    conn.commit()

    conn.close()


#function rsa bd
def add_rsa(usern,n,e,d):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("INSERT INTO rsa(iduser,n,e,d) VALUES('%d','%d','%d','%d')" % (id,n,e,d))

    conn.commit()

    conn.close()

def maj_rsa(usern,n,e,d):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("UPDATE rsa set n='%d',e='%d',d='%d' WHERE iduser='%d'" % (n,e,d,id))

    conn.commit()

    conn.close()

def supp_rsa(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("DELETE FROM rsa WHERE iduser='%d'" % id )

    conn.commit()

    conn.close()

# function bd vignere
def add_vignere(usern,clee):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("INSERT INTO vignere(iduser,cle) VALUES('%d','%s')" % (id,clee))

    conn.commit()

    conn.close()

def maj_vignere(usern,clee):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("UPDATE vignere set cle='%s' WHERE iduser='%d'" % (clee,id))

    conn.commit()

    conn.close()

def sup_vignere(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    id=None

    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]


    c.execute("DELETE FROM vignere WHERE iduser='%d'" % id )

    conn.commit()

    conn.close()

#function des bd

def add_des(usern,clee):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    id=None
    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]
    c.execute("INSERT INTO des(iduser,cle) VALUES('%d','%s')" % (id,clee))
    conn.commit()
    conn.close()
def maj_des(usern,clee):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    id=None
    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]
    c.execute("UPDATE des set cle='%s' WHERE iduser='%d'" % (clee,id))
    conn.commit()
    conn.close()
def supp_des(usern):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    id=None
    for row in c.execute("SELECT id from utilisateur WHERE username='%s'" % usern):
        id=row[0]
    c.execute("DELETE FROM des WHERE iduser='%d'" % id )
    conn.commit()
    conn.close()

def get_cle(usern):
    conn = sqlite3.connect('crypto.db')

    c = conn.cursor()
    ide=None


    for row in c.execute("SELECT id,algo from utilisateur WHERE username='%s'" % usern):
        ide=row[0]
        alg=row[1]



    if(alg==0):
        for row in c.execute("SELECT pas FROM cesar WHERE iduser='%d'" % ide ):
            return row[0]
    if(alg==1):
        for row in c.execute("SELECT cle FROM vignere WHERE iduser='%d'" % ide ):
            return row[0]
    if(alg==2):
        for row in c.execute("SELECT a,b,c,d FROM hill WHERE iduser='%d'" % ide ):
            return row[0],row[1],row[2],row[3]
    if(alg==3):
        for row in c.execute("SELECT n,e,d FROM rsa WHERE iduser='%d'" % ide ):
            return row[0],row[1],row[2]
    if(alg==4):
        for row in c.execute("SELECT cle FROM des WHERE iduser='%d'" % ide ):
            return row[0]
    
    conn.commit()
    
    conn.close()
    return None