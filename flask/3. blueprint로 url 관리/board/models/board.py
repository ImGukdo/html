import  pymysql

class cBoard :  # 게시판 클래스
    def __init__(self, num = None, writer = None, w_date = None, title = None, content = None) :
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content

class cBoard_dao :  # db에 접근할 dao
    def __init__(self) :  # db와의 연결을 위한 변수 선언
        self.conn = None

    def Connect(self) :  # db 연결 함수
        self.conn = pymysql.connect(host = "localhost", user = "root", password = "1234",
                                    database = "flasktest", charset = "utf8")
        self.cur = self.conn.cursor()  # db에 접근할 커서

    def Disconnect(self) :  # db와 연결 해제 함수
        self.cur = None
        self.conn.close()

    def Insert(self, bd) :  # db에 insert 작업할 함수
        self.Connect()
        sql = "insert into board(writer, w_date, title, content) values(%s, now(), %s, %s)"
        vals = (bd.writer, bd.title, bd.content)
        self.cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()

    def SelectAll(self) :  # db에 전체 데이터를 select 작업할 함수
        self.Connect()
        sql = "select * from board order by num desc"
        self.cur.execute(sql)
        bds = []
        for row in self.cur :
            bd = cBoard(row[0], row[1], row[2], row[3], row[4])
            bds.append(bd)
        self.Disconnect()
        return bds

    def SelectNum(self, num) :  # db에 번호로 데이터를 select 작업할 함수
        self.Connect()
        sql = "select * from board where num = " + str(num)
        self.cur.execute(sql)
        row = self.cur.fetchone()
        self.Disconnect()
        if row :
            return cBoard(row[0], row[1], row[2], row[3], row[4])

    def SelectWriter(self, writer) :  # db에 작성자로 데이터를 select 작업할 함수
        self.Connect()
        sql = "select * from board where writer = %s order by num desc"
        vals = (writer,)
        self.cur.execute(sql, vals)
        bds = []
        for row in self.cur :
            bd = cBoard(row[0], row[1], row[2], row[3], row[4])
            bds.append(bd)
        self.Disconnect()
        return bds

    def SelectTitle(self, title) :  # db에 제목으로 데이터를 select 작업할 함수
        self.Connect()
        sql = "select * from board where title like %s order by num desc"
        vals = ('%' + title + '%',)
        self.cur.execute(sql, vals)
        bds = []
        for row in self.cur:
            bd = cBoard(row[0], row[1], row[2], row[3], row[4])
            bds.append(bd)
        self.Disconnect()
        return bds

    def Update(self, bd) :  # db에 update 작업할 함수
        self.Connect()
        sql = "update board set title = %s, content = %s, w_date = now() where num = " + str(bd.num)
        vals = (bd.title, bd.content)
        self.cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()

    def Delete(self, num) :  # db에 delete 작업할 함수
        self.Connect()
        sql = "delete from board where num = " + str(num)
        self.cur.execute(sql)
        self.conn.commit()
        self.Disconnect()

class cBoard_service :  # 서비스 클래스
    def __init__(self) :
        self.dao = cBoard_dao()  # dao 객체 생성

    def AddBoard(self, bd) :  # # dao의 Insert 함수에 전달
        return self.dao.Insert(bd)

    def GetAll(self) :  # dao의 SelectAll 함수에 전달
        return self.dao.SelectAll()

    def GetByNum(self, num) :  # dao의 SelectNum 함수에 전달
        return self.dao.SelectNum(num)

    def GetByWriter(self, writer) :  # dao의 SelectWriter 함수에 전달
        return self.dao.SelectWriter(writer)

    def GetByTitle(self, title) :  # dao의 SelectTitle 함수에 전달
        return self.dao.SelectTitle(title)

    def EditBoard(self, bd) :  # dao의 Update 함수에 전달
        return self.dao.Update(bd)

    def DeleteBoard(self, num) :  # dao의 Delete 함수에 전달
        return self.dao.Delete(num)

