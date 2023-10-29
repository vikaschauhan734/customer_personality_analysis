from flask import Flask, render_template, request, redirect, url_for
import pickle
app= Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/true')
def true():
    return render_template('true.html')

@app.route('/false')
def false():
    return render_template('false.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        acceptedcmp1 = request.form['acceptedcmp1']
        acceptedcmp2 = request.form['acceptedcmp2']
        acceptedcmp3 = request.form['acceptedcmp3']
        acceptedcmp4 = request.form['acceptedcmp4']
        acceptedcmp5 = request.form['acceptedcmp5']
        mntwines = int(request.form['mntwines'])
        mntmeatproducts = int(request.form['mntmeatproducts'])
        numcatalogpurchases = int(request.form['numcatalogpurchases'])
        recency = int(request.form['recency'])

        prediction = model.predict([[acceptedcmp5,acceptedcmp1,acceptedcmp3,mntwines,mntmeatproducts,numcatalogpurchases,recency,acceptedcmp4,acceptedcmp2]])[0]
        output = ""
        if prediction == 0:
            output="false"
        else:
            output="true"
    return redirect(url_for(output))


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)
