from flask import *

app = Flask(__name__)
app.secret_key = "asdfa"

@app.route("/",methods=['POST','GET'])
def index():
    tree_list = [["test_py_parent",["test_children1","test_children2","test_children3"]],["test_py_parent2",["test_children1","test_children2","test_children3"]]]
    # issues = []
    return render_template("homepage.html",tree_lists=tree_list)

if __name__ == "__main__":
    app.run()