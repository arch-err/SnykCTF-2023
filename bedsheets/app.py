from flask import Flask, render_template, request, send_file, redirect, url_for
from xml2xlsx import xml2xlsx 
from glob import glob
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/error')
def errs():
    return render_template('error.html')

@app.route('/createSheets', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        output_folder = "calcSheets"
        try:
            new_repo = request.data.decode('ascii')
            template_xml = f'<!--?xml version="1.0" ?--> {new_repo}'
            now = datetime.now()

            filename = f"{now.strftime('%Y_%m_%d_%H_%M_%S')}.xlsx"
            f = open(f'{output_folder}/{filename}', 'wb') 
            f.write(xml2xlsx(template_xml)) 
            f.close()
            
            return redirect(url_for('sheets'))
        except:
            return redirect(url_for('errs'))
        
    else: # GET request
        return render_template('calculations.html')
@app.route('/finishedSheets/<sheetname>')
def finished_select(sheetname):
    path = f"./calcSheets/{sheetname}"
    a = send_file(path, as_attachment=True,download_name = sheetname,
        mimetype='application/vnd.ms-excel')
    return a

@app.route('/finishedSheets')
def sheets():
    all_repos = glob("./calcSheets/*")
    return render_template('finishedSheets.html', sheets = [i.split("/")[-1] for i in all_repos])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)