from flask import Flask,render_template,url_for,request
from flask_qrcode import QRcode

app=Flask(__name__)

qrcode=QRcode(app)

@app.route('/')
def home():
    return render_template('mydata.html')

@app.route('/myqr')
def mydata():
    mystring=request.args.get('mystring')
    return render_template('myqr.html',mystring=mystring)

if __name__ =='__main__':
    app.run(debug=True)