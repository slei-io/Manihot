from core.manihot import app, api
from views import Main

api.add_resource(Main, "/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
