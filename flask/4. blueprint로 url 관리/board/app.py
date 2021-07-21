from flask import Flask, render_template
import board.routes.mem_route as rm
import board.routes.board_route as rb

app = Flask(__name__)
app.register_blueprint(rm.bp)  # 블루프린트 등록
app.register_blueprint(rb.bp)  # 블루프린트 등록

@app.route('/')
def home() :
    return render_template("index.html")

if __name__ == "__main__" :
    app.secret_key = 'super secret key'  # 세션 시크릿키 초기화
    app.config['SESSION_TYPE'] = 'filesystem'  # 세션 확장
    app.run()