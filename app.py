from flask import Flask,render_template,request
import requests
import bs4
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
	return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	text.replace(' ','_')
	answer = "No nepotism"
	res = requests.get(f'https://en.wikipedia.org/wiki/{text}')
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	for x in soup.find_all('p'):
		if 'was born on' in x.text:
			for y in ['director','producer','actor','actress','directors','producers','actresses','actors','singer','filmmaker']:
				if (' ' + y + ' ') in (' ' + x.text + ' '):
					answer = 'nepotism founded'
					break
	return render_template('answer.html',text=text,answer=answer)

if __name__ == '__main__':
	app.run(host='127.0.0.1',debug=True)