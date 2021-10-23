from flask import Flask,render_template,request 

app = Flask(__name__) 

@app.route("/") 

def home(): 
    return render_template("index.html") 

@app.route("/Submit",methods=["POST"]) 

def Submit(): 
    if request.method == 'POST':
        numbers = [int(x) for x in request.form.values()]
        return  render_template("index.html",text = sum(numbers))
    
if __name__=="__main__": 
    app.run(debug=True)