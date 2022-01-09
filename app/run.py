from app import app

current_app=app_factory(app, config=DevConfig)

if __name__ == "__main__":
    current_app.run(debug=True, port=5555)