from flask import Flask, render_template, request, send_file, redirect, url_for
from git import Repo
from glob import glob
from zipfile import ZipFile
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clone', methods = ['POST', 'GET'])
def clone():
    if request.method == 'POST':
        new_repo = request.form['repo']
        try:
            Repo.clone_from(new_repo, f'repositories/{new_repo.split("/")[-1].split(".")[0]}', multi_options=["-c protocol.ext.allow=always"])
        except Exception as e:
            return redirect(url_for('repos'))
        return redirect(url_for('repos'))
    else:
        return render_template('clone.html')

@app.route('/repos')
def repos():
    all_repos = glob("./repositories/*/")
    return render_template('repos.html', repos = [i.split("/")[-2] for i in all_repos])

@app.route('/repos/<reponame>')
def repo_download(reponame):
    path = f"./repositories/{reponame}"
    root = os.path.dirname(path)
    files = glob(os.path.join(path, '*'))
    stream = BytesIO()
    with ZipFile(stream, 'w') as zf:
        for f in files:
            zf.write(f, os.path.relpath(f, root))
    stream.seek(0)
    return send_file(
        stream,
        as_attachment=True,
        download_name = "archive.zip",
        mimetype='application/zip'
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)