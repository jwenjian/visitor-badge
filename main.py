import datetime

from flask import Flask, Response, request, render_template
from pybadges import badge
from hashlib import md5
import requests
from os import environ
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)


def invalid_count_resp(err_msg) -> Response:
    """
    Return a svg badge with error info when cannot process repo_id param from request
    :return: A response with invalid request badge
    """
    svg = badge(left_text="Error", right_text=err_msg,
                whole_link="https://github.com/jwenjian/visitor-badge")
    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


def update_counter(key):
    url = 'https://api.countapi.xyz/hit/visitor-badge/{0}'.format(key)
    try:
        resp = requests.get(url)
        if resp and resp.status_code == 200:
            return resp.json()['value']
        else:
            return None
    except Exception as e:
        return None


@app.route("/badge")
def visitor_svg() -> Response:
    """
    Return a svg badge with latest visitor count of 'Referer' header value

    :return: A svg badge with latest visitor count
    """

    req_source = identity_request_source()

    if not req_source:
        return invalid_count_resp('Missing required param: page_id')

    latest_count = update_counter(req_source)

    if not latest_count:
        return invalid_count_resp("Count API Failed")

    # get left color and right color
    left_color = "#595959"
    if request.args.get("left_color") is not None:
        left_color = request.args.get("left_color")

    right_color = "#1283c3"
    if request.args.get("right_color") is not None:
        right_color = request.args.get("right_color")

    left_text = "visitors"
    if request.args.get("left_text") is not None:
        left_text = request.args.get("left_text")

    svg = badge(left_text=left_text, right_text=str(latest_count),
                left_color=str(left_color), right_color=str(right_color))

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(response=svg, content_type="image/svg+xml", headers=headers)


@app.route("/index.html")
@app.route("/index")
@app.route("/")
def index() -> Response:
    return render_template('index.html')


def identity_request_source() -> str:
    page_id = request.args.get('page_id')
    if page_id is not None and len(page_id):
        m = md5(page_id.encode('utf-8'))
        m.update(environ.get('md5_key').encode('utf-8'))
        return m.hexdigest()
    return None


if __name__ == '__main__':
    host = environ.get('host', '127.0.0.1')
    port = environ.get('port', 5000)
    app.run(host=host, port=port)
