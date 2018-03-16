import nds2
from gwpy.time import tconvert
from pylab import *
ion()

def quickplot(chanList, gpsLength=3600, gpsStop=tconvert('now').gpsSeconds):
    '''
    quickplot takes in a list of channels, and plots an hour worth of data for all channels specified.
    Inputs: 
    chanList: list of channels valid for the CTN Lab fb4.
    gpsLength: length of time in seconds to plot from gpsStop. Default is one hour.
    gpsStop: gpstime to plot until.  Default is now.
    '''
    conn = nds2.connection('10.0.1.156', 8088)
    timeDiff = 171148 # Time differential between now and fb4 frames "now"
    data = conn.fetch(gpsStop - gpsLength - timeDiff, gpsStop - timeDiff, chanList)

    if gpsLength < 60:
        units = 'seconds'
        timeDivisor = 1
    elif gpsLength < 3600:
        units = 'minutes'
        timeDivisor = 60
    elif gpsLength < 86400:
        units = 'hours'
        timeDivisor = 3600
    elif gpsLength < 604800:
        units = 'days'
        timeDivisor = 86400

    for dat in data:
        plot(dat.data)
    xlabel('Time [' + units + '] from GPSTime = '+str(gpsStop-gpstime))
