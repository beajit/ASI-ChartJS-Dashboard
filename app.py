from datetime import time
import main_code
from werkzeug.utils import secure_filename
import os
import glob
import urllib.request
from flask import Flask, flash,send_file, request, redirect, render_template


app = Flask(__name__)

app.secret_key = "secret key"
ALLOWED_EXTENSIONS = set(['xls','csv','xlsx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

# @app.route("/simple_chart")
# def chart():
#     legend = 'Monthly Data'
#     labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
#     values = [10, 9, 8, 7, 6, 4, 7, 8]
#     return render_template('chart.html', values=values, labels=labels, legend=legend)

@app.route('/line_chart')
def upload_form():
    return render_template('line_chart.html')

@app.route("/line_chart", methods=['POST'])
def line_chart():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('/home/ajitkumar/Documents/code/python/Flask/AIS_flask_chartjs/Upload', filename))
            flash('File successfully uploaded')

    # legend = 'Temperatures'
    # temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
    #                 61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
    #                 70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    # times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
    #          '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
    #          '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
            cost,dates=main_code.summation()
            files = glob.glob('/home/ajitkumar/Documents/code/python/Flask/AIS/upload/*')
            for f in files:
                os.remove(f)
            return render_template('line_chart.html', values=cost, labels=dates)
        else:
                flash('Allowed file types are xls,csv,xlsx')
                return redirect(request.url)


# @app.route("/time_chart")
# def time_chart():
#     legend = 'Temperatures'
#     temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
#                     61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
#                     70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
#     times = [time(hour=11, minute=14, second=15),
#              time(hour=11, minute=14, second=30),
#              time(hour=11, minute=14, second=45),
#              time(hour=11, minute=15, second=00),
#              time(hour=11, minute=15, second=15),
#              time(hour=11, minute=15, second=30),
#              time(hour=11, minute=15, second=45),
#              time(hour=11, minute=16, second=00),
#              time(hour=11, minute=16, second=15),
#              time(hour=11, minute=16, second=30),
#              time(hour=11, minute=16, second=45),
#              time(hour=11, minute=17, second=00),
#              time(hour=11, minute=17, second=15),
#              time(hour=11, minute=17, second=30),
#              time(hour=11, minute=17, second=45),
#              time(hour=11, minute=18, second=00),
#              time(hour=11, minute=18, second=15),
#              time(hour=11, minute=18, second=30)]
#     return render_template('time_chart.html', values=temperatures, labels=times, legend=legend)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG']=1
    app.run(host='0.0.0.0', port=5000, debug=True)
