from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Direct map: Crime_Category → IPC Section & Punishment
ipc_map = {
    0: "IPC 379 - Up to 3 years (Theft)",
    1: "IPC 302 - Life Imprisonment (Murder)",
    2: "IPC 324 - Up to 3 years (Assault)",
    3: "IPC 420 - Up to 7 years (Fraud)"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        crime_category = int(request.form['crime_category'])
        
        # Just lookup the correct IPC Section
        ipc_section = ipc_map.get(crime_category, "Unknown")

        prediction = f"✅ Predicted: {ipc_section}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
