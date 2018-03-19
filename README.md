# LIGO-plots
Plotting program for LIGO lab data acquisition.

#### quickplot.py

On ws1, cd to `~/Git/LIGO-plots`. In Ipython: 
```
%run quickplot.py <channel 1> <channel 2> ... <(optional) gpsLength> <(optional) gpsStop>
```

#### Examples
```
In [1]: %run quickplot.py C3:PSL-SCAV_FSS_SLOWOUT
2018-03-19 02:57:09 (1205463447)
['C3:PSL-SCAV_FSS_SLOWOUT']
gpsLength = 3600
gpsStop = 1205463447
```
Data was fetched from `1205459847` to `1205463447`. The first output line displays the current time that fb4 thinks it is.
![alt text][graph2]

<br></br>
```
In [1]: %run quickplot.py C3:PSL-SCAV_FSS_SLOWOUT 50000 1201952464
2018-03-19 02:46:31 (1205462809)
['C3:PSL-SCAV_FSS_SLOWOUT']
gpsLength = 50000
gpsStop = 1201952464
```
Data fetched from `1201902464` to `1201952464`. 
![alt text][graph1]


[graph1]: https://github.com/shufay/LIGO-plots/blob/master/figures/Figure_1.png
[graph2]: https://github.com/shufay/LIGO-plots/blob/master/figures/Figure_2.png
