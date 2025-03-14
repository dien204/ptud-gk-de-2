from flask import Flask
from routes import app_routes  # Import Blueprint từ routes.py

app = Flask(__name__)

# Đăng ký Blueprint
app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)






