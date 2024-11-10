import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# Load your .nc datasets
srad_data = xr.open_dataset('srad_2015.nc')
pet_data = xr.open_dataset('pet_2015.nc')
sph_data = xr.open_dataset('sph_2015.nc')

# List of dates to generate plots for
dates = ["2015-09-28", "2015-09-29", "2015-09-30", "2015-10-01", "2015-10-02", "2015-10-03", "2015-10-04", "2015-10-05","2015-10-06"]

# Initialize lists to store frames for each GIF
frames_srad_pet = []
frames_srad_sph = []

# Function to generate contour plot frames
def create_frame_srad_pet(date):
    # Select data for the specified date
    srad = srad_data['surface_downwelling_shortwave_flux_in_air'].sel(day=date)
    pet = pet_data['potential_evapotranspiration'].sel(day=date)
    
    # Coarsen data by averaging over every 2 degrees
    srad_coarse = srad.coarsen(lat=2, lon=2, boundary='trim').mean()
    pet_coarse = pet.coarsen(lat=2, lon=2, boundary='trim').mean()
    
    # Extract latitude and longitude for plotting
    lons, lats = srad_coarse.lon, srad_coarse.lat
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Solar Radiation (srad) - filled contour plot
    srad_plot = ax.contourf(lons, lats, srad_coarse, cmap='YlOrRd', levels=np.linspace(srad_coarse.min(), srad_coarse.max(), 10))
    cbar_srad = fig.colorbar(srad_plot, ax=ax, orientation="vertical", pad=0.1)
    cbar_srad.set_label('Solar Radiation (W/m²)')
    
    # Evapotranspiration (pet) - contour lines
    pet_plot = ax.contour(lons, lats, pet_coarse, colors='blue', linewidths=0.8, levels=np.linspace(pet_coarse.min(), pet_coarse.max(), 7))
    ax.clabel(pet_plot, inline=True, fontsize=8, fmt='%1.1f')
    
    # Titles and labels
    ax.set_title(f"Srad and PET Contour Plot on {date}")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Save plot as an image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames_srad_pet.append(Image.open(buf))
    plt.close(fig)

def create_frame_srad_sph(date):
    # Select data for the specified date
    srad = srad_data['surface_downwelling_shortwave_flux_in_air'].sel(day=date)
    sph = sph_data['specific_humidity'].sel(day=date)
    
    # Coarsen data by averaging over every 2 degrees
    srad_coarse = srad.coarsen(lat=2, lon=2, boundary='trim').mean()
    sph_coarse = sph.coarsen(lat=2, lon=2, boundary='trim').mean()
    
    # Extract latitude and longitude for plotting
    lons, lats = srad_coarse.lon, srad_coarse.lat
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Solar Radiation (srad) - filled contour plot
    srad_plot = ax.contourf(lons, lats, srad_coarse, cmap='YlOrRd', levels=np.linspace(srad_coarse.min(), srad_coarse.max(), 10))
    cbar_srad = fig.colorbar(srad_plot, ax=ax, orientation="vertical", pad=0.1)
    cbar_srad.set_label('Solar Radiation (W/m²)')
    
    # Specific Humidity (sph) - contour lines
    sph_plot = ax.contour(lons, lats, sph_coarse, colors='green', linewidths=1.0, levels=np.linspace(sph_coarse.min(), sph_coarse.max(), 10))
    ax.clabel(sph_plot, inline=True, fontsize=8, fmt='%1.1f')
    
    # Titles and labels
    ax.set_title(f"Srad and SPH Contour Plot on {date}")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Save plot as an image in memory
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames_srad_sph.append(Image.open(buf))
    plt.close(fig)

# Generate frames for each date for both srad vs pet and srad vs sph
for date in dates:
    create_frame_srad_pet(date)
    create_frame_srad_sph(date)

# Save frames as GIFs
frames_srad_pet[0].save('srad_pet.gif', save_all=True, append_images=frames_srad_pet[1:], duration=500, loop=0)
frames_srad_sph[0].save('srad_sph.gif', save_all=True, append_images=frames_srad_sph[1:], duration=500, loop=0)

print("GIFs created successfully!")
