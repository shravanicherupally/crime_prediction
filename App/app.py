from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load('model/model.pkl')
le = joblib.load('model/label_encoder.pkl')

ipc_map = {
    'IPC 302 - Life Imprisonment': "IPC 302 - Life Imprisonment (Murder)",
    'IPC 324 - Up to 3 years': "IPC 324 - Up to 3 years (Assault)",
    'IPC 379 - Up to 3 years': "IPC 379 - Up to 3 years (Theft)",
    'IPC 420 - Up to 7 years': "IPC 420 - Up to 7 years (Fraud)"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    inputs = None

    if request.method == 'POST':
        crime_category = int(request.form['crime_category'])
        severity_level = int(request.form['severity_level'])
        use_of_weapon = int(request.form['use_of_weapon'])
        repeat_offender = int(request.form['repeat_offender'])
        severity_weapon_flag = int(request.form['severity_weapon_flag'])

        input_data = pd.DataFrame([[crime_category, severity_level, use_of_weapon, repeat_offender, severity_weapon_flag]],
                                  columns=["Crime_Category", "Crime_Severity_Level", "Use_of_Weapon", "Repeat_Offender", "Severity_Weapon_Flag"])

        predicted_code = model.predict(input_data)[0]
        ipc_label = le.inverse_transform([predicted_code])[0]
        ipc_section = ipc_map.get(ipc_label, ipc_label)

        prediction = f"✅ Predicted IPC Section: {ipc_section}"

        inputs = {
            'crime_category': crime_category,
            'severity_level': severity_level,
            'use_of_weapon': use_of_weapon,
            'repeat_offender': repeat_offender,
            'severity_weapon_flag': severity_weapon_flag
        }

    return render_template('index.html', prediction=prediction, inputs=inputs)

if __name__ == '__main__':
    app.run(debug=True)
