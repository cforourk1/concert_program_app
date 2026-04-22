from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    data = request.form
    print(data)  # For now, just print it
    return "Form received!"

if __name__ == '__main__':
    app.run(debug=True)