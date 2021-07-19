import pymysql
import vo

class cProduct_dao :
    def __init__(self) :
        self.conn = None  # db와 연결하여 접근할 변수

    def Connect(self) :  # db와 연결
        self.conn = pymysql.connect(host = "localhost", user = "root", password = "1234",
                                    database = "flasktest", charset = "utf8")
    def Disconnect(self) :  # db와 연결 해제
        self.conn.close()

    def Insert(self, prod) :  # db에 insert해주는 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "insert into product(name, price, amount) values(%s, %s, %s)"
        vals = (prod.name, prod.price, prod.amount)
        cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()

    def Select(self, num) :  # db에 num인 것을 조회하는 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "select * from product where num = %s"
        vals = (num,)
        cur.execute(sql, vals)
        row = cur.fetchone()
        self.Disconnect()
        if row != None :
            prod = vo.cProduct(row[0], row[1], row[2], row[3])
            return prod

    def SelectAll(self) :  # db에 모든것을 조회하는 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "select * from product"
        cur.execute(sql)
        prods = []
        for row in cur :
            prods.append(vo.cProduct(row[0], row[1], row[2], row[3]))
        self.Disconnect()
        return prods

    def update(self, prod) :  # db에 제품을 수정하는 함수
        self.Connect()
        cur = self.conn.cursor()
        sql = "update product set price = %s, amount = %s where num = %s"
        vals = (prod.price, prod.amount, prod.num)
        cur.execute(sql, vals)
        self.conn.commit()
        self.Disconnect()

class cProduct_service :  # 뷰와 db 사이의 매개체 역할을 해주는 서비스 클래스
    def __init__(self) :
        self.dao = cProduct_dao()  # db에 접근할 dao 객체 생성

    # dao에 접근하여 db에 기능 수행

    def AddProduct(self, prod) :
        self.dao.Insert(prod)

    def GetProduct(self, num) :
        return self.dao.Select(num)

    def GetAll(self) :
        return self.dao.SelectAll()

    def EditProduct(self, prod) :
        return self.dao.update(prod)

