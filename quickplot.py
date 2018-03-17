import nds2, subprocess, sys
from gwpy.time import tconvert, from_gps, to_gps
from pylab import *
ion()

def correct_time():
    HOST = 'controls@10.0.1.156'
    COMMAND = 'caget -t -f10 C4:DAQ-DC0_GPS'
    ssh = subprocess.Popen(['ssh', '%s'% HOST, COMMAND],
                            shell = False,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    
    result = ssh.stdout.readlines()
    fb4gps = to_gps(result[0].strip('\n'))
    print('{} ({})'.format(from_gps(fb4gps), fb4gps))
    return fb4gps

def quickplot(chanList, gpsLength=3600, gpsStop=correct_time().gpsSeconds):
    '''
    quickplot takes in a list of channels, and plots an hour worth of data for all 
    channels specified.
    Inputs: 
    chanList: list of channels valid for the CTN Lab fb4.
    gpsLength: length of time in seconds to plot from gpsStop. Default is one hour.
    gpsStop: gpstime to plot until.  Default is now.
    '''
    conn = nds2.connection('10.0.1.156', 8088)
    gpsStart = gpsStop - gpsLength
    data = conn.fetch(gpsStart, gpsStop, chanList)

    if gpsLength <= 60:
        units = 'seconds'
        timeDivisor = 1
    
    elif gpsLength <= 3600:
        units = 'minutes'
        timeDivisor = 60
    
    elif gpsLength <= 86400:
        units = 'hours'
        timeDivisor = 3600
    
    elif gpsLength <= 604800:
        units = 'days'
        timeDivisor = 86400
    
    displayTime = gpsLength/timeDivisor
    t = linspace(0, displayTime, gpsLength*16)

    for dat in data:
        plot(t, dat.data)

    xlabel('Time {} from {} ({})'.format(units, tconvert(gpsStart), gpsStart))

    print(chanList)
    print('gpsLength = {}'.format(gpsLength))
    print('gpsStop = {}'.format(gpsStop))

# terminal args
usage = 'quickplot.py <channel 1> <channel 2> ... <(optional) gpsLength> <(optional) gpsStop>'

if len(sys.argv) < 2:
    print(usage)

elif len(sys.argv) >= 2:
    chans = []
    times = []

    if sys.argv[1] == 'usage':
        print(usage)

    else: 
        for item in sys.argv[1:]:
            try:
                times.append(int(item))

            except ValueError:
                chans.append(item)
        
        if len(times) == 0:
            quickplot(chans)

        elif len(times) == 1:
            quickplot(chans, times[0])

        elif len(times) == 2:
            quickplot(chans, times[0], times[1])

