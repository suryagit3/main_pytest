from flask import *
import requests
app = Flask(__name__)
app.secret_key = "asdfa"
host = "http://localhost:5000/"
@app.route("/",methods=['POST','GET'])
def index():
    tree_list = [["test_py_parent",["test_children1","test_children2","test_children3"]],["test_py_parent2",["test_children1","test_children2","test_children3"]]]
    # issues = []
    return render_template("homepage.html",tree_lists=tree_list,host_name=host+"run")
@app.route("/run",methods=['POST'])
def run():
    if request.method == "POST":
        return request.form
    else:
        return 400,"Method not allowed"

if __name__ == "__main__":
    app.run()