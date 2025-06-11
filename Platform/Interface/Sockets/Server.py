# -------------------------------------------------------------------------------------------------
# ----------------------- Platform :: Interface :: Sockets :: Simple Server -----------------------
# -------------------------------------------------------------------------------------------------
from threading import Thread
from pathlib   import Path

from flask import Response
from flask import Flask
from flask import send_file
from flask import send_from_directory


# -------------------------------------------------------------------------------------------------
# ----------------------------- Visitor :: State-Based Rules Enforcer -----------------------------
# -------------------------------------------------------------------------------------------------
class Server(object):

    # -----------------------------------------------------------------------------------------
    # ------------------------------ CONSTRUCTOR :: Constructor -------------------------------
    # -----------------------------------------------------------------------------------------
    def __init__(self, host: str = '127.0.0.1', port: int = 5000, debug: bool = True) -> None:

        self.app = Flask('', static_folder='Platform/Interface/')

        @self.app.route('/')
        def index() -> str:
            return Path('Platform/Interface/Html/Interface.html').read_text()

        @self.app.route('/Css/<path:filename>')
        def css(filename: str):
            return send_from_directory('Platform/Interface/Css', filename)

        @self.app.route('/Javascript/<path:filename>')
        def javascript(filename: str):
            return send_from_directory('Platform/Interface/Javascript', filename)

        @self.app.route('/ThreeJS/<path:filename>')
        def threejs(filename: str):
            return send_from_directory('Platform/Interface/ThreeJS', filename)

        @self.app.route('/Assets/Symbols/<name>.svg')
        def symbol(name: str) -> str:
            path = Path(f'Platform/Interface/Assets/Symbols/{name}.svg')
            return Response(path.read_text(), mimetype='image/svg+xml')

        @self.app.route('/Assets/Fonts/<path:filename>')
        def font(filename: str):
            path = Path(f'Platform/Interface/Assets/Fonts/{filename}')
            return send_file(path, mimetype='font/ttf')  # Or 'font/woff' or similar

        @self.app.route('/Assets/Textures/<path:filename>')
        def texture(filename: str):
            path = Path(f'Platform/Interface/Assets/Textures/{filename}')
            return send_file(path)

        self.host  = host
        self.port  = port
        self.debug = debug

    def start(self) -> None:

        thread = Thread(target=self.app.run, kwargs={
            'host':  self.host,
            'port':  self.port,
            'debug': self.debug,
            'use_reloader': False,
        })

        thread.daemon = True
        thread.start()