import os
from routes import *

app.register_blueprint(table)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug= True, use_reloader=False)
