"""
This file is to plot the density of ligand in the case that the ligand is modeled by a PDE instead of particles
"""
import os
from .plotcore import load, build_df
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def make_frame(cell_pos_df, Lslice, index, axis, kwargs):
    # make one frame of the animation
    # this should include:
    #   -selecting cells by position
    dx = kwargs['grid_dx']
    grid_N = kwargs['grid_N']
    # this slice position relies on the PDE grid being fixed in the particular way that it happens to be now.
    # a more future-proof implementation would be to use the L_grid attribute of the PolarPDE object
    grid_coord = (dx*(np.arange(grid_N) - (grid_N - 1)/2))
    slice_position = grid_coord[index]
    slice_width = dx
    col_names = ['x1', 'x2', 'x3']
    col = col_names[axis-1]
    col_names.remove(col)
    sliced_df = cell_pos_df[(cell_pos_df[col] < slice_position+slice_width)
                            & (cell_pos_df[col] > slice_position-slice_width)]
    frame = go.Frame(data=[go.Scatter(x=sliced_df[col_names[0]], y=sliced_df[col_names[1]],
                     mode='markers')])
    return frame


def plot(df, L, axis, index, kwargs):
    frame_dfs = [df[df.t == t] for t in sorted(df.t.unique())]
    frames = [make_frame(cell_pos_df, Lslice, index, axis, kwargs)
              for cell_pos_df, Lslice in zip(frame_dfs, L.take(index, axis))]
    dx = kwargs['grid_dx']
    grid_N = kwargs['grid_N']
    grid_coord = (dx*(np.arange(grid_N) - (grid_N - 1)/2))
    fig = px.imshow(L.take(index, axis).transpose(0,2,1), animation_frame=0, x=grid_coord, y=grid_coord)
    for i, frame in enumerate(frames):
        fig['frames'][i]['data'] += frame.data
    fig.add_traces(data=fig["frames"][0]["data"][-1])
    return fig


def save(fig, fname):
    fig.write_html(os.path.join('animations',os.path.basename(fname)).replace('.pkl', f'_ligand_density_pde_with_cells.html'),
                   include_plotlyjs='directory',
                   full_html=False)
    return

if __name__ == '__main__':
    fname = input(
        'Enter data filename (default: most recent): ') or 'most recent'
    data, kwargs, fname = load(fname)
    df, L, kwargs = build_df(data, kwargs)
    axis = int(input('axis along which to slice? default 1') or 1)
    index = int(input('which slice to take? (default: halfway) ')
                or L.shape[-1]/2)
    fig = plot(df, L, axis, index, kwargs)
    save(fig, fname)
