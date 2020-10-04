import datetime

from flask import Flask, Response, request, render_template
from hashlib import md5
import requests
from os import environ
from dotenv import find_dotenv,load_dotenv
from typing import Optional

load_dotenv(find_dotenv())

URL_PARAMETER_PAGE_ID = environ.get('URL_PARAMETER_PAGE_ID')
URL_PARAMETER_LABEL = environ.get('URL_PARAMETER_LABEL')
URL_PARAMETER_COLOR = environ.get('URL_PARAMETER_COLOR')
URL_PARAMETER_SHIELDS_QUERY = environ.get('URL_PARAMETER_SHIELDS_QUERY').split(' ')
DEFAULT_LABEL_TEXT = environ.get('DEFAULT_LABEL_TEXT')
DEFAULT_MESSAGE_COLOR = environ.get('DEFAULT_MESSAGE_COLOR')

app = Flask(__name__)


def invalid_count_resp(err_msg) -> Response:
    """
    Return a svg badge with error info when cannot process repo_id param from request
    :return: A response with invalid request badge
    """
    svg = requests.get('https://img.shields.io/badge/{label}-{message}-{color}?link={link}'.format(
            label='Error',
            message=err_msg,
            color=DEFAULT_MESSAGE_COLOR,
            link='https://github.com/jwenjian/visitor-badge'
        )
    )
    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0', 'Expires': expiry_time.strftime('%a, %d %b %Y %H:%M:%S GMT')}

    return Response(response=svg, content_type='image/svg+xml', headers=headers)


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
    Return a svg badge with latest visitor count of 'Referrer' header value

    :return: A svg badge with latest visitor count
    """

    req_source = get_request_value(URL_PARAMETER_PAGE_ID)

    if not req_source:
        return invalid_count_resp(f'Missing required param: {URL_PARAMETER_PAGE_ID}')

    latest_count = update_counter(req_source)

    if not latest_count:
        return invalid_count_resp("Count API Failed")

    label_text = get_request_value(URL_PARAMETER_LABEL)
    color_value = get_request_value(URL_PARAMETER_COLOR)

    shields_query_strings = list(filter(None, [get_request_value(p) for p in URL_PARAMETER_SHIELDS_QUERY]))

    shields_url = 'https://img.shields.io/badge/{label}-{message}-{color}{query}'.format(
        label=label_text if label_text else DEFAULT_LABEL_TEXT,
        message=str(latest_count),
        color=color_value if color_value and len(color_value) else DEFAULT_MESSAGE_COLOR,
        query='?{}'.format('&'.join(shields_query_strings)) if shields_query_strings else ''
    )

    svg = requests.get(shields_url)

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime('%a, %d %b %Y %H:%M:%S GMT')}

    return Response(response=svg, content_type='image/svg+xml', headers=headers)


@app.route("/index.html")
@app.route("/index")
@app.route("/")
def index() -> Response:
    return render_template('index.html')


def get_request_value(url_parameter_name: str) -> Optional[str]:
    url_parameter_value = request.args.get(url_parameter_name)
    if url_parameter_value is not None and len(url_parameter_value):
        if url_parameter_name == URL_PARAMETER_PAGE_ID:
            m = md5(url_parameter_value.encode('utf-8'))
            m.update(environ.get('md5_key').encode('utf-8'))
            return m.hexdigest()
        elif url_parameter_name in URL_PARAMETER_SHIELDS_QUERY:
            return f'{url_parameter_name}={url_parameter_value}'
        else:
            return url_parameter_value
    else:
        return None if url_parameter_value is None else url_parameter_value


if __name__ == '__main__':
    app.run()
