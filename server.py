from flask import Flask, render_template,url_for,request,redirect
import csv

app = Flask(__name__)
print(__name__)
# @app.route("/<username>/<int:post_id>")

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
	with open('database.txt', mode ='a') as database:
	 email = data['email']
	 subject = data['subject']
	 message = data['message']
	 file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database1.csv', mode ='a') as database1:
	 email = data['email']
	 subject = data['subject']
	 message = data['message']
	 csv_writer = csv.writer(database1, delimiter = ',',quoting = csv.QUOTE_NONE)
	 csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
	    try:
	    	data = request.form.to_dict()
	    	write_to_csv(data)
	    	return redirect('/thanks.html')
	    except:
	      	return 'Did not save to database'
	else:
	        return 'errored'


# @app.route("/works.html")
# def my_works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def my_contact():
#     return render_template('contact.html')

# # @app.route("/components.html")
# # def my_components():
# #     return render_template('components.html')


# @app.route("/work.html")
# def my_work_sub():
#     return render_template('work.html')



# @app.route("/flavicon.ico")
# def blog():    
#     return 'Thoughts on blog'


# @app.route("/blog/2022/cars")
# def blogcars():    
#     return 'This is my dog'