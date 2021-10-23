from flask import Flask,render_template,request 

app = Flask(__name__) 

@app.route("/") 

def home(): 
    return render_template("index.html") 

@app.route("/Submit",methods=["POST"]) 

def Submit(): 
    if request.method == 'POST':
        numbers = [x for x in request.form.values()] 
        name = numbers[0]+" " + numbers[1]
        return  render_template("index.html",text = name)
    
if __name__=="__main__": 
    app.run(debug=True)