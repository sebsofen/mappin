from flask import Flask, request
from mapautopin import pointstomap
import json

app = Flask(__name__)


@app.route('/api/v1/countrypoints')
def get_points_in_country():
    pointsstr = request.args.get('points', "[]")
    points = json.loads(pointsstr)
    return  Response(pointstomap.pointstomap(points).read(), mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5123')