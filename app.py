from flask import Flask,render_template,request
from procy import dean



app=Flask(__name__)

@app.route('/')
def show():
	return render_template('form1.html')

@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']
	bot_response,user_input=dean(user_input)
	if(bot_response==""):
                bot_response=' I am still trying to learn things, I didnt understand what you said'
	

	return render_template('form1.html',user_input=user_input,bot_response=bot_response)

if __name__=='__app__':
	app.run(debug=True)
