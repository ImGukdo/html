from flask import Flask

app = Flask(__name__)  # flask 객체 생성, 웹 어플리케이션 객체

# 라우트 등록, 클라이언트 요청 url을 지정 및 이 요청이 왔을때 실행할 코드작성
# / 는 최상위 url로 보통 첫화면을 나타낸다.
# methods를 지정하지 않으면 defult로 get 방식으로 지정된다.
@app.route("/")
def my_root() :
    return "hello test"  # 요청 url에 hello test 출력

# get 방식으로 요청 url 출력
@app.route("/test1")
def test1() :
    return "test1"

# post 방식으로 요청 url 출력, get 방식처럼 주소창에 url을 입력해서 접근할 수 없다.
@app.route("/test2", methods=["POST"])
def test2() :
    return "test2"


if __name__ == "__main__" :
    app.run()  # flask 서버 실행
