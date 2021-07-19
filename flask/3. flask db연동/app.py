from flask import Flask, request, render_template
import vo, model

app = Flask(__name__)  # flask 객체 생성
prod_service = model.cProduct_service()  # 제품 객체 생성

@app.route('/')  # 제일 상위 url
def home() :
    return render_template("index.html")  # index.html을 보여준다

@app.route("/product/add")  # /product/add을 get방식으로 요청 받으면
def add_form() :
    return render_template("/product/form.html")  # /product/form.html을 보여준다

@app.route("/product/add", methods=["POST"])  # /product/add을 post방식으로 요청 받으면
def add() :
    # /product/form.html에서 입력받은 정보를 받아옴
    name = request.form.get("name", '', str)
    price = request.form.get("price", 0, int)
    amount = request.form.get("amount", 0, int)
    prod = vo.cProduct(name = name, price = price, amount = amount)  # 받은 정보로 제품객체를 생성
    prod_service.AddProduct(prod)  # 제품객체를 넘겨서 db에 insert 해줌
    return render_template("/index.html")  # 제일 상위 url로 이동

@app.route("/product/get", methods=["POST"])  # /product/get을 post방식으로 요청 받으면
def get() :
    num = request.form.get("num", -1, int)  # 입력받은 num을 받아온다
    if num == -1 :  # 입력받은게 없으면 -1
        return render_template("/index.html", num = num)  # index.html을 보여주고 num값을 넘겨준다
    else :
        prod = prod_service.GetProduct(num)
        if prod == None :  # 검색한 제품번호가 없으면
            num = -2
            return render_template("/index.html", num = num)  # index.html을 보여주고 num값을 넘겨준다
        else :
            return render_template("/product/detail.html", prod = prod)  # /product/detail.html을 보여준다

@app.route("/product/list")  # /product/list을 get방식으로 요청 받으면
def list() :
    prods = prod_service.GetAll()  # db에서 제품 정보들을 제품객체 리스트로 받아옴
    return render_template("/product/list.html", prods = prods)  # /product/list.html를 보여주고 제품객체리스트를 넘긴다

@app.route("/product/edit")  # /product/edit을 get방식으로 요청 받으면
def edit_form() :
    num = request.args.get("num", 0, int)  # 입력받은 num을 받아와서
    prod = prod_service.GetProduct(num)  # db에서 num의 정보를 제품객체로 받아옴
    return render_template("/product/edit_form.html", prod=prod)  # /product/edit_form.html을 보여주고 prod를 넘겨줌

@app.route("/product/edit", methods=["POST"])  # /product/edit을 post방식으로 요청 받으면
def edit() :
    # /product/edit_form.html에서 입력받은 정보를 받아옴
    num = request.form["num"]
    name = request.form["name"]
    price = request.form["price"]
    amount = request.form["amount"]
    prod = vo.cProduct(num, name, price, amount)  # 받은 정보로 제품객체를 생성
    prod_service.EditProduct(prod)  # 제품객체를 넘겨서 db에 update 해줌
    return render_template("/product/detail.html", prod = prod)  # 수정한 정보를 /product/detail.html에서 보여줌


if __name__ == "__main__" :
    app.run()  # flask 서버 실행
