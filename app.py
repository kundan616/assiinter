from flask import Flask, render_template, request,send_file
import urllib.request, json 
from getdata import getdata
app = Flask(__name__)

@app.route('/' ,methods=['GET','POST'])
def upload_file():
   return render_template('index.html')

@app.route('/invite' ,methods=['GET'])
def invite():
   if request.method == 'GET':
      link=request.args.get('link', '')
      data=getdata(link)
      return render_template('invite.html',senddata=data["invitations"])
   else:

      return render_template('invite.html')


@app.route('/orders' ,methods=['GET'])
def orders():
   if request.method == 'GET':
      link=request.args.get('link', '')
      data=getdata(link)
      return render_template('orders.html',senddata=data["orders"])
   else:

      return render_template('orders.html')



@app.route('/members' ,methods=['GET'])
def members():
   if request.method == 'GET':
      link=request.args.get('link', '')
      data=getdata(link)
      return render_template('members.html',senddata=data["members"])
   else:

      return render_template('members.html')   
   
          
if __name__ == '__main__':
   app.run(debug = True)










