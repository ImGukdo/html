from flask import Blueprint, render_template, request, redirect
import board.models.board as b

bp = Blueprint("board", __name__, url_prefix = "/board")  # 블루프린트 선언, (이름, 모듈, url 앞에 고정으로 넣을거)
board_service = b.cBoard_service()  # dao에 접근할 service 객체

@bp.route("/add")  # 글쓰기 폼 요청
def add_form() :
    return render_template("/board/form.html")

@bp.route("/add", methods = ["POST"])  # 글 게시 요청
def add() :
    id = request.form["writer"]
    title = request.form["title"]
    content = request.form["content"]
    bd = b.cBoard(writer = id, title = title, content = content)
    board_service.AddBoard(bd)
    return redirect("/board/list")

@bp.route("/list")  # 게시글 목록 요청
def list() :
    bd = board_service.GetAll()
    return render_template("/board/list.html", bd = bd)

@bp.route("/detail")  # 게시글 보기 요청
def detail_form() :
    title = request.args.get("title", "", str)
    bd = board_service.GetByTitle(title)
    return render_template("/board/detail.html", bd = bd[0])

@bp.route("/del", methods = ["POST"])  # 게시글 지우기 요청
def delete() :
    num = request.form['num']
    board_service.DeleteBoard(num)
    return redirect("/board/list")


@bp.route("/edit", methods = ["POST"])  # 게시글 수정 요청
def edit() :
    num = request.form["num"]
    title = request.form["title"]
    content = request.form["content"]
    bd = b.cBoard(num = num, title = title, content = content)
    board_service.EditBoard(bd)
    return redirect("/board/list")

@bp.route("/getbywriter", methods = ["POST"])  # 작성자 아이디로 게시글 검색 요청
def getbywriter() :
    writer = request.form["writer"]
    bd = board_service.GetByWriter(writer)
    return render_template("/board/list.html", bd = bd)

@bp.route("/getbytitle", methods = ["POST"])  # 게시글 제목으로 게시글 검색 요청
def getbytitle() :
    title = request.form["title"]
    bd = board_service.GetByTitle(title)
    return render_template("/board/list.html", bd = bd)





