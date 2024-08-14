from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store the collected responses
responses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    user_response = {
        'talk_about': request.form.get('talk-about'),
        'different': request.form.get('different'),
        'sleeping': request.form.get('sleeping'),
        'feeling': request.form.get('feeling'),
        'treatment': request.form.get('treatment')
    }

    print("Received response:", user_response)  # Debugging print statement

    # Store the response
    responses.append(user_response)

    # Redirect to the response page
    return redirect(url_for('show_responses'))

@app.route('/responses')
def show_responses():
    return render_template('responses.html')

@app.route('/view_responses')
def view_responses():
    print("Current responses:", responses)  # Debugging print statement
    return render_template('view_responses.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
