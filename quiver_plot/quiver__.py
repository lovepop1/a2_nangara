import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature  

# Loading Datasets
wind_speed_data = xr.open_dataset(r"D:\DV-Assignment-2\Datasets\vs_2015.nc")
wind_direction_data = xr.open_dataset(r"D:\DV-Assignment-2\Datasets\th_2015.nc")

# Selecting date
wind_speed = wind_speed_data['wind_speed'].sel(day="2015-10-05")
wind_direction = wind_direction_data['wind_from_direction'].sel(day="2015-10-05")

# Define 2° bins and calculate the midpoints -- to maintain good density of vectors
lat_bins = np.arange(wind_speed_data.lat.min(), wind_speed_data.lat.max(), 2)
lon_bins = np.arange(wind_speed_data.lon.min(), wind_speed_data.lon.max(), 2)
lat_midpoints = lat_bins[:-1] + 1  # Midpoint for latitude bins
lon_midpoints = lon_bins[:-1] + 1  # Midpoint for longitude bins

# Grouping data by bins and calculating the mean within each 2°x2° region
wind_speed_binned = wind_speed.groupby_bins("lat", lat_bins).mean().groupby_bins("lon", lon_bins).mean()
wind_direction_binned = wind_direction.groupby_bins("lat", lat_bins).mean().groupby_bins("lon", lon_bins).mean()

#U and V components for quiver plot
u = wind_speed_binned * np.cos(np.radians(wind_direction_binned))
v = wind_speed_binned * np.sin(np.radians(wind_direction_binned))

#PLOT
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=":")

magnitude = np.sqrt(u**2 + v**2)  # Magnitude of wind for color scaling
quiver = ax.quiver(lon_midpoints, lat_midpoints, u, v, magnitude,
                   scale=150, transform=ccrs.PlateCarree(), cmap="plasma", width=0.002)

# Color Bar for speed values
cbar = plt.colorbar(quiver, ax=ax, orientation="vertical", pad=0.02)
cbar.set_label("Wind Speed (m/s)", fontsize=12)
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color="gray", alpha=0.5)
gl.top_labels = False
gl.right_labels = False

plt.title("Quiver Plot showing Wind Speed and Direction across the US on 5th October,2015 ", fontsize=15)
plt.tight_layout()
plt.savefig(r'D:\DV-Assignment-2\Images\quiver-oct-5th.png')
plt.show()
