from flask import *
app = Flask(_name_)

app.route('/table/<int:num>')
def table(num):
	return render_template('print-table.html',n=num)
if _name_ == '_main_':
	app.run(debug = True)