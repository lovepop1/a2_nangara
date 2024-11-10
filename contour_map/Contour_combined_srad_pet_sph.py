import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

# Loading all three datsets
srad_data = xr.open_dataset(r'D:\DV-Assignment-2\Datasets\srad_2015.nc')
pet_data = xr.open_dataset(r'D:\DV-Assignment-2\Datasets\pet_2015.nc')
sph_data = xr.open_dataset(r'D:\DV-Assignment-2\Datasets\sph_2015.nc')

# Function to plot contours on a selected date
def plot_contour_on_date(selected_date):
    # Selecting data from the datasets for the specific date
    srad = srad_data['surface_downwelling_shortwave_flux_in_air'].sel(day=selected_date)
    pet = pet_data['potential_evapotranspiration'].sel(day=selected_date)
    sph = sph_data['specific_humidity'].sel(day=selected_date)
    
    # Coarsen data by averaging over every 2 degrees-- to maintain proper densisty
    srad_coarse = srad.coarsen(lat=2, lon=2, boundary='trim').mean()
    pet_coarse = pet.coarsen(lat=2, lon=2, boundary='trim').mean()
    sph_coarse = sph.coarsen(lat=2, lon=2, boundary='trim').mean()
    
    # Extract latitude and longitude for plotting
    lons, lats = srad_coarse.lon, srad_coarse.lat
    fig, ax = plt.subplots(figsize=(12, 8))

    # Solar Radiation (srad) - filled contour plot
    srad_plot = ax.contourf(lons, lats, srad_coarse, cmap='YlOrRd', levels=np.linspace(srad_coarse.min(), srad_coarse.max(), 10))
    cbar_srad = fig.colorbar(srad_plot, ax=ax, orientation="vertical", pad=0.1)
    cbar_srad.set_label('Solar Radiation (W/m²)')
    
    # Evapotranspiration (pet) - contour lines
    pet_plot = ax.contour(lons, lats, pet_coarse, colors='blue', linewidths=0.8, levels=np.linspace(pet_coarse.min(), pet_coarse.max(), 10))
    ax.clabel(pet_plot, inline=True, fontsize=8, fmt='%1.1f')
    
    # Specific Humidity (sph) - additional contour lines
    sph_plot = ax.contour(lons, lats, sph_coarse, colors='green', linewidths=0.8, levels=np.linspace(sph_coarse.min(), sph_coarse.max(), 10))
    ax.clabel(sph_plot, inline=True, fontsize=8, fmt='%1.1f')
    
    ax.set_title(f"Contour Plot on {selected_date}\nSolar Radiation, Evapotranspiration, and Specific Humidity")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{abs(val):.0f}° {'W' if val < 0 else 'E'}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{abs(val):.0f}° {'S' if val < 0 else 'N'}"))
    blue_line = plt.Line2D([0], [0], color='blue', linewidth=2, label='Evapotranspiration (PET)')
    green_line = plt.Line2D([0], [0], color='green', linewidth=2, label='Specific Humidity (SPH)')
    ax.legend(handles=[blue_line, green_line], loc='upper right')

    plt.savefig(f"Images/contour-srad_sph_pet_{selected_date}.png", dpi=300)
    plt.show()

#Give date below
selected_date = '2015-09-11'
plot_contour_on_date(selected_date)
