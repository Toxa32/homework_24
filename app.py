"""This is a main file to run the application"""
from flask import Flask, request, abort, Response
from marshmallow import ValidationError
from marshmallow_dataclass import class_schema
from container import user_request
from models import RequestArgs
# ------------------------------------------------------------------------
app = Flask(__name__)
# ------------------------------------------------------------------------


@app.route("/perform_query/", methods=['POST'])
def perform_query() -> Response:
    """This function is a view to work with route /perform_query/ with
    different query parameters

    Returns:
        flask response with result of the query execution
    """
    args = request.values
    RequestSchema = class_schema(RequestArgs)

    try:
        request_args = RequestSchema().load(args)
        result = user_request.execute(request_args)
    except ValidationError:
        abort(400, 'Bad Request, arguments is invalid')
    except Exception as e:
        abort(400, f'Bad Request, there is an error {e}')

    if not result:
        abort(404, 'Nothing was found')

    return app.response_class(result, content_type="text/plain")


if __name__ == '__main__':
    app.run()
