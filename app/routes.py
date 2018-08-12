from app import app

import matlab.engine
eng = matlab.engine.start_matlab()
eng.cd('kernel', nargout=0)

@app.route('/')
@app.route('/index')
def index():
    return eng.hello()
