from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    roll=request.form['rollno']
    return render_template('result.html',name=username,r=roll)
if __name__=='__main__':
    app.run(debug=True)