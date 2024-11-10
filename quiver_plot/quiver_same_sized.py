import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Loading datasets 
wind_speed_data = xr.open_dataset(r"D:\DV-Assignment-2\Datasets\vs_2015.nc")
wind_direction_data = xr.open_dataset(r"D:\DV-Assignment-2\Datasets\th_2015.nc")

#DATE
wind_speed = wind_speed_data['wind_speed'].sel(day="2015-09-11")
wind_direction = wind_direction_data['wind_from_direction'].sel(day="2015-09-11")

lat_bins = np.arange(wind_speed_data.lat.min(), wind_speed_data.lat.max(), 2)
lon_bins = np.arange(wind_speed_data.lon.min(), wind_speed_data.lon.max(), 2)
lat_midpoints = lat_bins[:-1] + 1  # Midpoint for latitude bins
lon_midpoints = lon_bins[:-1] + 1  # Midpoint for longitude bins

# Group data by bins and calculate the mean within each 2°x2° region
wind_speed_binned = wind_speed.groupby_bins("lat", lat_bins).mean().groupby_bins("lon", lon_bins).mean()
wind_direction_binned = wind_direction.groupby_bins("lat", lat_bins).mean().groupby_bins("lon", lon_bins).mean()


fixed_magnitude = 1 # Fixed magnitude for arrow length
u = fixed_magnitude * np.cos(np.radians(wind_direction_binned))
v = fixed_magnitude * np.sin(np.radians(wind_direction_binned))

# Plot
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=":")

# Color will indicate wind speed, while arrow length is fixed
magnitude = wind_speed_binned  # Color intensity based on wind speed
quiver = ax.quiver(
    lon_midpoints, lat_midpoints, u, v, magnitude,
    scale=50, transform=ccrs.PlateCarree(), cmap="plasma", width=0.0015
)

# Color Bar
cbar = plt.colorbar(quiver, ax=ax, orientation="vertical", pad=0.02)
cbar.set_label("Wind Speed (m/s)", fontsize=12)

gl = ax.gridlines(draw_labels=True, linewidth=0.5, color="gray", alpha=0.5)
gl.top_labels = False
gl.right_labels = False
plt.title("Quiver Plot (Fixed Length Arrows) showing Wind Speed and Direction across the US on 11th September, 2015")
plt.tight_layout()
plt.savefig(r'D:\DV-Assignment-2\Images\quiver-11th-sept-fixed-size.png')
plt.show()
