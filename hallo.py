from flask import Flask

app = Flask(__name__)


# Когда браузер открывает главную страницу, Flask вызывает эту функцию.
@app.get("/")
def home():
    return """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Hello, world!</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>Это моя первая веб-страница на Python.</p>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(port=5001)