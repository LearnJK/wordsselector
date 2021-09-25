import os
from app import app

print(int(os.environ.get("PORT", 5000)))
if __name__ == "__main__":
	port = 5000
	app.run(port=port)

app.run()
# export FLASK_ENV=development
# flask run
