from app import app

import matlab.engine
eng = matlab.engine.start_matlab()

folder = '/home/jafffy/Dropbox/research/liver/liver_images/F0/1/Potal/2136918_20171124/';

I = eng.imread(folder + 'gross0070.jpg')
I = eng.imadjust(I, matlab.double([0.2, 1.0]))
I = eng.imbinarize(I)
I = eng.edge(I, 'log')
I = eng.bwareaopen(I, matlab.double([100]))

eng.workspace['I'] = I

app.run(host='0.0.0.0')
