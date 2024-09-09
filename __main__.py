from backend.core.app import App, app
from backend.core.db import user_manager

runtime = App(app)

if __name__ == '__main__':
    user_manager.create_db()
    runtime.run()
