import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

srad_data = xr.open_dataset(r'D:\DV-Assignment-2\Datasets\srad_2015.nc')
pet_data = xr.open_dataset(r'D:\DV-Assignment-2\Datasets\pet_2015.nc')
sph_data = xr.open_dataset(r'D:\DV-Assignment-2\Datasets\sph_2015.nc')

#SRAD - PET
def plot_srad_pet(selected_date):
    srad = srad_data['surface_downwelling_shortwave_flux_in_air'].sel(day=selected_date)
    pet = pet_data['potential_evapotranspiration'].sel(day=selected_date)
    srad_coarse = srad.coarsen(lat=2, lon=2, boundary='trim').mean()
    pet_coarse = pet.coarsen(lat=2, lon=2, boundary='trim').mean()
    
    # Extract latitude and longitude for plotting
    lons, lats = srad_coarse.lon, srad_coarse.lat
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Solar Radiation (srad) - filled contour plot
    srad_plot = ax.contourf(lons, lats, srad_coarse, cmap='YlOrRd', levels=np.linspace(srad_coarse.min(), srad_coarse.max(), 10))
    cbar_srad = fig.colorbar(srad_plot, ax=ax, orientation="vertical", pad=0.1)
    cbar_srad.set_label('Solar Radiation (W/m²)')
    
    # Evapotranspiration (pet) - contour lines
    pet_plot = ax.contour(lons, lats, pet_coarse, colors='blue', linewidths=0.8, levels=np.linspace(pet_coarse.min(), pet_coarse.max(), 8))
    ax.clabel(pet_plot, inline=True, fontsize=8, fmt='%1.1f')
    
    ax.set_title(f"Srad and PET Contour Plot on {selected_date}")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{abs(val):.0f}° {'W' if val < 0 else 'E'}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{abs(val):.0f}° {'S' if val < 0 else 'N'}"))

    #Legend
    blue_line = plt.Line2D([0], [0], color='blue', linewidth=2, label='Evapotranspiration (PET)')
    ax.legend(handles=[blue_line], loc='upper right')
    # Saving the plot
    plt.savefig(f"Images/contour-srad_pet_{selected_date}.png", dpi=300)
    plt.show()

# SRAD - SPH
def plot_srad_sph(selected_date):
    # Select data for the specified date
    srad = srad_data['surface_downwelling_shortwave_flux_in_air'].sel(day=selected_date)
    sph = sph_data['specific_humidity'].sel(day=selected_date)
    srad_coarse = srad.coarsen(lat=2, lon=2, boundary='trim').mean()
    sph_coarse = sph.coarsen(lat=2, lon=2, boundary='trim').mean()
    
    # Extract latitude and longitude for plotting
    lons, lats = srad_coarse.lon, srad_coarse.lat
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Solar Radiation (srad) - filled contour plot
    srad_plot = ax.contourf(lons, lats, srad_coarse, cmap='YlOrRd', levels=np.linspace(srad_coarse.min(), srad_coarse.max(), 10))
    cbar_srad = fig.colorbar(srad_plot, ax=ax, orientation="vertical", pad=0.1)
    cbar_srad.set_label('Solar Radiation (W/m²)')
    
    # Specific Humidity (sph) - contour lines
    sph_plot = ax.contour(lons, lats, sph_coarse, colors='green', linewidths=1.0, levels=np.linspace(sph_coarse.min(), sph_coarse.max(), 12))
    
    ax.clabel(sph_plot, inline=True, fontsize=8, fmt='%1.1f')
    ax.set_title(f"Srad and SPH Contour Plot on {selected_date}")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{abs(val):.0f}° {'W' if val < 0 else 'E'}"))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{abs(val):.0f}° {'S' if val < 0 else 'N'}"))

    #Legend
    green_line = plt.Line2D([0], [0], color='green', linewidth=2, label='Specific Humidity (SPH)')
    ax.legend(handles=[green_line], loc='upper right')
    plt.savefig(f"Images/contour-srad_sph_{selected_date}.png", dpi=300)
    plt.show()

#Give Date below
selected_date = '2015-10-05'
plot_srad_pet(selected_date)
plot_srad_sph(selected_date)
