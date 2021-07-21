import pymysql

class cMember :  # 회원 클래스
    def __init__(self, id = None, pwd = None, name = None, email = None) :
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email


class cMember_dao :  # db에 접근할 dao
    def __init__(self) :
        self.conn = None  # db와 연결 변수 선언

    def Connect(self) :  # db 연결 함수
        self.conn = pymysql.connect(host = "localhost", user = "root", password = "1234",
                                    database = "flasktest", charset = "utf8")
    def Disconnect(self) :  # db 해제 함수
        self.conn.close()

    def Insert(self, vo) :  # db에 insert 작업할 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "insert into member values(%s, %s, %s, %s)"
        vals = (vo.id, vo.pwd, vo.name, vo.email)
        cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()

    def Select(self, id) :  # db에 select 작업할 함수
        self.Connect()
        cur = self.conn.cursor()
        try :
            sql = "select * from member where id = %s"
            vals = (id, )
            cur.execute(sql, vals)
            row = cur.fetchone()
            mem = cMember(row[0], row[1], row[2], row[3])
            self.Disconnect()
            return mem
        except :
            return None

    def Update(self, vo) :  # db에 update 작업할 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "update member set pwd = %s where id = %s"
        vals = (vo.pwd, vo.id)
        cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()

    def Delete(self, id) :  # db에 delete 작업할 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "delete from member where id = %s"
        vals = (id,)
        cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()


class cMember_service:  # 서비스 클래스
    def __init__(self):
        self.dao = cMember_dao()  # dao 객체 생성

    def AddMember(self, vo):  # dao의 Insert 함수에 전달
        self.dao.Insert(vo)

    def GetMember(self, id):  # dao의 Select 함수에 전달
        return self.dao.Select(id)

    def EditMember(self, vo):  # dao의 Update 함수에 전달
        return self.dao.Update(vo)

    def DeleteMember(self, id) :  # dao의 Delete 함수에 전달
        return self.dao.Delete(id)

