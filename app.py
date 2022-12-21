from flask import Flask, request, abort
from container import checker, service, query
# ------------------------------------------------------------------------
app = Flask(__name__)
# ------------------------------------------------------------------------


@app.route("/perform_query/")
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    args = request.args

    if not checker.is_valid(args):
        abort(400, 'Bad Request, arguments is invalid')

    try:
        service.add_new_file(args.get('file'))
        query[args.get('cmd1')](args.get('value1'))
        query[args.get('cmd2')](args.get('value2'))
        result = service.get_result()

    except Exception as e:
        abort(400, f'Bad Request, there is an error {e}')

    return app.response_class(result, content_type="text/plain")
