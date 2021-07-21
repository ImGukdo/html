from flask import Blueprint, render_template, session, request, redirect
import board.models.member as m

bp = Blueprint("member", __name__, url_prefix = "/member")  # 블루프린트 선언, (이름, 모듈, url 앞에 고정으로 넣을거)
mem_service = m.cMember_service()  # dao에 접근할 service 객체

@bp.route("/join")  # 회원가입 요청시
def add_form_mem() :
    return render_template("/member/form.html")

@bp.route("/join", methods = ["POST"])  # 회원가입 등록 요청시
def add_mem() :
    id = request.form["id"]  # 회원가입폼에서 정보를 입력받음
    pwd = request.form["pwd"]
    name = request.form["name"]
    email = request.form["email"]
    mem = m.cMember(id, pwd, name, email)
    mem_service.AddMember(mem)  # db에 저장
    return redirect('/')  # 회원가입 후 다시 회원가입으로 가서 오류가 발생하는 것을 방지하기 위해 redirect로

@bp.route("/get")  # 내정보 요청
def get_mem() :
    id = request.args.get("id", "", str)
    mem = mem_service.GetMember(id)
    return render_template("/member/getResult.html", mem = mem)

@bp.route("/edit", methods = ["POST"])  # 수정 요청
def edit_mem() :
    id = request.form["id"]
    pwd = request.form["pwd"]
    mem = m.cMember(id = id, pwd = pwd)
    mem_service.EditMember(mem)
    return redirect('/')

@bp.route("/del")  # 삭제 오청
def del_mem() :
    id = session["id"]
    mem_service.DeleteMember(id)
    session.pop("id", None)
    return redirect('/')

@bp.route("/login", methods = ["POST"])  # 로그인 요청
def login() :
    msg1 = ''
    msg2 = ''
    path = "/index.html"
    id = request.form["id"]
    pwd = request.form["pwd"]
    mem = mem_service.GetMember(id)
    if mem == None :
        msg1 = "없는 아이디 입니다."
    else :
        if pwd == mem.pwd :
            session["id"] = id  # 로그아웃할때까지 유지해야하는 정보를 저장
            path = "index.html"
        else :
            msg2 = "패스워드가 틀렸습니다."
    return render_template(path, msg1 = msg1, msg2 = msg2)

@bp.route("/logout")  # 로그아웃 요청
def logout() :
    if "id" in session :
        session.pop("id", None)
    return redirect('/')
