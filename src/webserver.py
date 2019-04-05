from flask import Flask, request, Response
from mapautopin import pointstomap, constants
import json


app = Flask(__name__)


@app.route('/api/v1/countrypoints')
def get_points_in_country():
    pointsstr = request.args.get('points', "[]")
    points = json.loads(pointsstr)

    markerStyleStr = request.args.get('markerstyle', "dot")
    markerStyle = parse_marker_style(markerStyleStr)


    return  Response(pointstomap.pointstomap(points, markerStyle).read(), mimetype='image/svg+xml')


def parse_marker_style(style: str) ->  constants.MARKER_STYLE_TYPE:

    switcher = {
        "line": constants.MARKER_STYLE_LINE,
        "dot": constants.MARKER_STYLE_DOT
    }

    return switcher.get(style, constants.MARKER_STYLE_DOT)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5123')