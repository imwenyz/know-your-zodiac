from flask import Flask, jsonify, render_template, request, g
import sys
from models import EastZodiac, WestZodiac
from zodiac import get_zodiac_api
from __init__ import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/", methods=['GET', 'POST'])
def api():
    try:
        if request.method == 'POST':
            year = int(request.form['year'])
            month = int(request.form['month'])
            day = int(request.form['day'])
        else:
            year = int(request.args.get('year'))
            month = int(request.args.get('month'))
            day = int(request.args.get('day'))
    except ValueError:
        print "value error"
        return jsonify({"status" : "0", "error" : str(sys.exc_info()[1])}), 500
    except:
        print "Unexpected error"
        return jsonify({"status" : "0", "error" : str(sys.exc_info()[1])}), 500

    data = get_zodiac_api(year,month,day, request.url_root)

    if data.get('error') != None:
        return jsonify({"status" : "0", "error" : data.get('error')}), 500

    return jsonify({"apiVersion":"1.0", "status": "1", "data" : data})
