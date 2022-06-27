"""
This script should open a data file in the legacy format and save it in a forward-compatible format
"""
import plot.plotcore as pc
import pickle as pkl

def convert(fname):
    data, kwargs, fname = pc.load(fname)
    df, lig, kwargs = pc.build_df(data, kwargs)
    fname_new = fname.replace('.pkl','-converted.pkl')
    mdict = {'df':df, 'lig':lig}
    with open(fname_new, 'wb') as fobj:
        pkl.dump([mdict, kwargs], fobj)
    return

if __name__ == '__main__':
    fname = input('file name? (default: most recent) ') or 'most recent'
    convert(fname)