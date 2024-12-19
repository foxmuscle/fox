from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from database_connection import get_database_connection
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle
import os

app = Flask(__name__)

# 현재 선택된 모델을 저장할 변수
selected_model = None


@app.route('/')
def index():
    # Get the list of models
    model_dir = 'models'
    models = os.listdir(model_dir) if os.path.exists(model_dir) else []
    return render_template('가로로 다시 만들기블랙.html', models=models, selected_model=selected_model)


@app.route('/filter-data', methods=['POST'])
def filter_data():
    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')

    # Database connection and query
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT c_temp_pv, k_rpm_pv, n_temp_pv, scale_pv, s_temp_pv 
        FROM total_refill_rf_time 
        WHERE date_only BETWEEN %s AND %s
    """
    cursor.execute(query, (start_date, end_date))
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    if not result:
        models = os.listdir('models') if os.path.exists('models') else []
        return render_template('가로로 다시 만들기블랙.html', mse=None, model_name=None, models=models)

    df = pd.DataFrame(result)

    # Train the model (assuming 'scale_pv' is the target column)
    X = df.drop(columns=['scale_pv'])
    y = df['scale_pv']
    model = RandomForestRegressor()
    model.fit(X, y)

    # Calculate MAE
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
    print(mae)

    # Save the model
    model_name = f"RF_{start_date}_to_{end_date}_mae{mae}.pkl"
    model_path = os.path.join('models', model_name)
    os.makedirs('models', exist_ok=True)
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

    # Get updated list of models
    models = os.listdir('models') if os.path.exists('models') else []

    return render_template('가로로 다시 만들기블랙.html', mse=mae, model_name=model_name, models=models, selected_model=selected_model)


@app.route('/select-model', methods=['POST'])
def select_model():
    global selected_model
    # 사용자가 선택한 모델을 selected_model에 저장
    selected_model = request.form.get('model_name')
    return redirect(url_for('index'))


@app.route('/delete-model', methods=['POST'])
def delete_model():
    # 사용자가 삭제 요청한 모델 파일
    model_name = request.form.get('model_name')
    model_path = os.path.join('models', model_name)
    if os.path.exists(model_path):
        os.remove(model_path)  # 파일 삭제
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
