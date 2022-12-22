"""This is a main file to run the application"""
from flask import Flask, request, abort
from container import checker, user_request
# ------------------------------------------------------------------------
app = Flask(__name__)
# ------------------------------------------------------------------------


@app.route("/perform_query/", methods=['POST'])
def perform_query():
    """This function is a view to work with route /perform_query/ with
    different query parameters

    Returns:
        flask response with result of the query execution
    """
    args = request.values

    if not checker.is_valid(args):
        abort(400, 'Bad Request, arguments is invalid')

    try:
        result = user_request.execute(**args)

    except Exception as e:
        abort(400, f'Bad Request, there is an error {e}')

    if not result:
        abort(404, 'Nothing was found')

    return app.response_class(result, content_type="text/plain")
