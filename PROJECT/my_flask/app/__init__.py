# flask  앱 설정 및 초기화 

from flask import Flask

def create_app():
    app = Flask(__name__)

    # 기본 설정
    app.config['SECRET_KEY'] = 'your_secret_key'

    # 블루프린트 등록
    from .routes import main
    app.register_blueprint(main)

    return app