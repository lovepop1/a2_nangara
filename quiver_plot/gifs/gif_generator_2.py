import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from PIL import Image
import io

# Load the datasets
wind_speed_data = xr.open_dataset(r"D:\DV-Assignment-2\vs_2015.nc")
wind_direction_data = xr.open_dataset(r"D:\DV-Assignment-2\th_2015.nc")

# List of dates to generate plots for
dates = ["2015-09-28","2015-09-29","2015-09-30", "2015-10-01", "2015-10-02", "2015-10-03", "2015-10-04", "2015-10-05"]

# Initialize a list to store frames for the GIF
frames = []

for date in dates:
    # Select data for the specific day
    wind_speed = wind_speed_data['wind_speed'].sel(day=date)
    wind_direction = wind_direction_data['wind_from_direction'].sel(day=date)
    
    # Define 2° bins and calculate the midpoints
    lat_bins = np.arange(wind_speed_data.lat.min(), wind_speed_data.lat.max(), 2)
    lon_bins = np.arange(wind_speed_data.lon.min(), wind_speed_data.lon.max(), 2)
    lat_midpoints = lat_bins[:-1] + 1  # Midpoint for latitude bins
    lon_midpoints = lon_bins[:-1] + 1  # Midpoint for longitude bins

    # Group data by bins and calculate the mean within each 2°x2° region
    wind_speed_binned = wind_speed.groupby_bins("lat", lat_bins).mean().groupby_bins("lon", lon_bins).mean()
    wind_direction_binned = wind_direction.groupby_bins("lat", lat_bins).mean().groupby_bins("lon", lon_bins).mean()

    # Calculate U and V components for quiver plot
    u = wind_speed_binned * np.cos(np.radians(wind_direction_binned))
    v = wind_speed_binned * np.sin(np.radians(wind_direction_binned))
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=":")

    # Plot quiver with color mapped to wind speed
    magnitude = np.sqrt(u**2 + v**2)
    quiver = ax.quiver(lon_midpoints, lat_midpoints, u, v, magnitude,
                       scale=150, transform=ccrs.PlateCarree(), cmap="plasma", width=0.002)
    
    # Add color bar and title
    cbar = plt.colorbar(quiver, ax=ax, orientation="vertical", pad=0.02)
    cbar.set_label("Wind Speed (m/s)", fontsize=12)
    plt.title(f"Wind Flow on {date} - Heavy Rainfall and Floods in South East Region")

    # Convert plot to an image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames.append(Image.open(buf))
    plt.close(fig)  # Close the plot to free up memory

# Save frames as a GIF
gif_path = r"D:\DV-Assignment-2\wind_plots.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=500, loop=0)

print("GIF saved at:", gif_path)
