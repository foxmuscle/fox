#라우팅(경로) 설정 

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')  # templates/index.html 파일 로드


아래와 같이 Flask에서 각 HTML 파일에 해당하는 라우트를 정의하면 됩니다.

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    return render_template('index.html')

# About 페이지
@app.route('/about')
def about():
    return render_template('about.html')

# Features 페이지
@app.route('/features')
def features():
    return render_template('features.html')

# Pricing 페이지
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

# User Example 페이지
@app.route('/user_example')
def user_example():
    return render_template('user_example.html')

if __name__ == '__main__':
    app.run(debug=True)