import numpy as np
import scipy 

def SegImageDisplay(V2D_path):
    import segyio
    with segyio.open(V2D_path, ignore_geometry=True) as segyfile:
        traces = segyfile.trace
        xr_traces = xr.DataArray(traces).transpose("dim_1", "dim_0")
        xr_traces.plot()
        plt.gca().invert_yaxis()
        plt.show()

def convolute(signal): 
    output = np.convolve(signal)
    return output

def TracePlot(signal, sr):
    nsamples = signal.size
    t_total = nsamples / sr #duracion de 3.004 segundos
    print("duration -> ", t_total)
    t = np.linspace(0, t_total, nsamples)
    
    plt.figure(figsize=(15,8))
    plt.subplot(4,1,1)
    plt.plot(t, signal)
    plt.show()

def Filter(typeF):
    if(typeF == 'low'):
        pass
    elif(typeF == 'high'):
        pass
    else:
        print('not recognized filter type')


if __name__ == '__main__':
    import pandas as pd
    import pathlib
    import matplotlib.pyplot as plt
    import xarray as xr

    import segysak
    from segysak.segy import segy_header_scan
    from segysak.segy import segy_loader
    from IPython.display import display

    #I must return images instead of showing them
    data2D = './Line_301_PSTM_Stack_Enh.segy'
    V2D_path = pathlib.Path(data2D)
    header = segy_header_scan(data2D)
    with pd.option_context("display.max_rows", 91):
        #display(scan2)
        pass

    dt = header.loc["TRACE_SAMPLE_INTERVAL"]["mean"]
    sr = 1000 / dt

    #SegImageDisplay(V2D_path)
    #TracePlotter(signal, sr)
