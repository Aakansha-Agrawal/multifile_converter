from app import app

# if __name__ == "__main__":
#     if flask_app.config.get('FLASK_ENV') == 'development':
#         flask_app.run(debug=1)
#     else:
#         flask_app.run()
if __name__ == "__main__":
    app.run()
    # app.run(host="127.0.0.1",port=8080)