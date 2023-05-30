from flask import Flask,render_template,request


fai=Flask(__name__)

@fai.route('/form_data',methods=['GET','POST'])
def form_data():
    if request.method=='POST':
        data=request.form
        print(data)
        return data['name']


    return render_template('form_data.html')


if __name__=='__main__':
    fai.run(debug=True)