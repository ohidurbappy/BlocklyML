from sys import stdout
from flask import Flask, render_template, Response
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask import Flask, render_template, request, redirect, url_for, abort
from libs.DataFrameGenerator import DataFrameGenerator
from libs.DataFrameGenerator import DataFrameReportGenerator

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True



    

@app.route('/DataViewer', methods=['POST','GET'])
def DFreturn():
    listDF = DataFrameGenerator(request.form)
    #return render_template('tableviewer.html', table=listDF)
    return str(listDF)


    

@app.route('/DataReport', methods=['POST','GET'])
def DFRreturn():
    print("IDK")
    listDF = DataFrameReportGenerator(request.form)
    #return render_template('tableviewer.html', table=listDF)
    return str(listDF)


@app.route('/')
def root():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/', methods=['POST','GET'])
def my_form_post():
    if request.method == 'POST':
        print(request.form)
        print("WTH")
    else:
        print("WYH")
    #processed_text = text.upper()
    return render_template('index.html')



@app.route('/DataViewer')
def DataViewer():
    return render_template('tableviewer.html')



@app.route('/ReportViewer')
def ReportViewer():
    return render_template('reportViewer.html')


if __name__ == '__main__':
    app.run()
