from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_root() :
    return render_template("index.html")  # 처음 화면 index.html로 출력

@app.route("/input1")  # index.html에서 입력하러 가기(post 방식)를 누르면 요청 url /input1을 서버에 전송
def input_form() :
    return render_template("input1.html")  # input1.html 출력

@app.route("/value1", methods=["POST"])  # input1.html에서 post 방식으로 요청 url /value1을 서버에 전송
def value1() :
    name = request.form["name"]
    num = request.form["num"]
    eng = request.form["eng"]
    # view.html에 입력값을 전달해서 출력
    return render_template("view.html", name = name, num = num, eng = eng)

@app.route("/input2")  # index.html에서 입력하러 가기(get 방식)를 누르면 요청 url /input2을 서버에 전송
def input2() :
    return render_template("input2.html")

@app.route('/value2')  # input2.html에서 get 방식으로 요청 url /value2을 서버에 전송
def value2() :
    # request.args.get(파라메터 이름, 기본값(default값), 타입) : url 뒤에 ?로 붙인 파라메터 읽는 함수
    name = request.args.get("name", "", str)
    num = request.args.get("num", 0, int)
    eng = request.args.get("eng", "", str)
    return "name : {}<br>num : {}<br>eng : {}".format(name, num, eng)  # 입력받은 값 출력


if __name__ == "__main__" :
    app.run()