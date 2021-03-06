import json
from shapely.geometry import shape, Point
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import os
import sys
import io

from .constants import *


def pointstomap(points: list, marker_style, contourfile = 'ne_10m_admin_0_countries.geojson') -> io.BytesIO:
    #load points from actual blog
    with open(contourfile, 'r') as f:
        js = json.load(f)

    features = [x for x in js['features'] if len([y for y in points if  shape(x['geometry']).contains(Point(y))]) > 0]

    

    proj=ccrs.Miller()
    fig = plt.figure( dpi=96, facecolor='w',  frameon=False)    
    ax = fig.add_subplot(1, 1, 1, projection=proj)
    fig.patch.set_visible(False)
    ax.patch.set_visible(False)
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    
    if marker_style == MARKER_STYLE_DOT:
        ax.scatter(*np.array(points).T, s=1, color='black', marker=".", linewidth=3, transform=ccrs.PlateCarree())
    elif marker_style == MARKER_STYLE_LINE:
        ax.plot(*np.array(points).T, color='black', linewidth=1, transform=ccrs.PlateCarree())

 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.box(False)
    plt.axis('off')
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    
    for feature in features:
        geo = shape(feature['geometry'])
        if geo.geom_type == 'MultiPolygon':
            polygons = list(geo)
            for polygon in polygons:
                ax.plot(*np.array(polygon.exterior.xy), color='grey', linewidth=1, solid_capstyle='round', transform=ccrs.PlateCarree())
            
        elif geo.geom_type == 'Polygon':
            ax.plot(*np.array(geo.exterior.xy), color='grey', linewidth=1, solid_capstyle='round',transform=ccrs.PlateCarree())


    

    imgdata = io.BytesIO()
    plt.savefig(imgdata, format='svg', bbox_inches=0, transparent=True)
    
    plt.close(fig)
    imgdata.seek(0)  # rewind the data

    return imgdata



