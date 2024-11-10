import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt
import os
import matplotlib.colors as mcolors
import imageio
from pathlib import Path

file_path = 'bi_2015.nc'
ds = xr.open_dataset(file_path)
print("Dataset Summary:")
print(ds)
print("\nVariables in the dataset:")
print(ds.variables.keys())
print("\nAttributes of the dataset:")
print(ds.attrs)
file_path = 'fm100_2015.nc'
ds = xr.open_dataset(file_path)
print("Dataset Summary:")
print(ds)
print("\nVariables in the dataset:")
print(ds.variables.keys())
print("\nAttributes of the dataset:")
print(ds.attrs)
file_path = 'fm1000_2015.nc'
ds = xr.open_dataset(file_path)
print("Dataset Summary:")
print(ds)
print("\nVariables in the dataset:")
print(ds.variables.keys())
print("\nAttributes of the dataset:")
print(ds.attrs)
file_path = 'sph_2015.nc'
ds = xr.open_dataset(file_path)
print("Dataset Summary:")
print(ds)
print("\nVariables in the dataset:")
print(ds.variables.keys())
print("\nAttributes of the dataset:")
print(ds.attrs)


file_path_bi = "bi_2015.nc"
file_path_sph = "sph_2015.nc"
file_path_fm100 = "fm100_2015.nc"
file_path_fm1000 = "fm1000_2015.nc"

# Select the date range
bi_data = xr.open_dataset(file_path_bi).sel(day=slice("2015-08-01", "2015-09-30"))
sph_data = xr.open_dataset(file_path_sph).sel(day=slice("2015-08-01", "2015-09-30"))
fm100_data = xr.open_dataset(file_path_fm100).sel(day=slice("2015-08-01", "2015-09-30"))
fm1000_data = xr.open_dataset(file_path_fm1000).sel(day=slice("2015-08-01", "2015-09-30"))

# Calculate global min and max values for consistent scaling
global_bi_min, global_bi_max = bi_data['burning_index_g'].min().values, bi_data['burning_index_g'].max().values
global_sph_min, global_sph_max = sph_data['specific_humidity'].min().values, sph_data['specific_humidity'].max().values
global_fm100_min, global_fm100_max = fm100_data['dead_fuel_moisture_100hr'].min().values, fm100_data['dead_fuel_moisture_100hr'].max().values
global_fm1000_min, global_fm1000_max = fm1000_data['dead_fuel_moisture_1000hr'].min().values, fm1000_data['dead_fuel_moisture_1000hr'].max().values

# Define a helper function to adjust threshold if out of range
def validate_threshold(threshold, vmin, vmax):
    if threshold <= vmin or threshold >= vmax:
        return (vmin + vmax) / 2  # Use midpoint if out of range
    return threshold

# Set thresholds, ensuring they lie within the range
threshold_bi = validate_threshold(200, global_bi_min, global_bi_max)
threshold_fm100 = validate_threshold(10, global_fm100_min, global_fm100_max)
threshold_fm1000 = validate_threshold(10, global_fm1000_min, global_fm1000_max)

# Define colormap norms with validated thresholds
norm_bi = mcolors.TwoSlopeNorm(vmin=global_bi_min, vcenter=threshold_bi, vmax=global_bi_max)
norm_fm100 = mcolors.TwoSlopeNorm(vmin=global_fm100_min, vcenter=threshold_fm100, vmax=global_fm100_max)
norm_fm1000 = mcolors.TwoSlopeNorm(vmin=global_fm1000_min, vcenter=threshold_fm1000, vmax=global_fm1000_max)
norm_sph = mcolors.LogNorm(vmin=global_sph_min, vmax=global_sph_max)

# Define a function to plot and save each variable with global and local scaling
def plot_variable(data, var_name, title, global_min=None, global_max=None, local_scale=False, cmap="YlOrRd", norm=None, save_path=None):
    days = data.day.values[::10]  # Plot every 10th day for clarity

    # Create directory if save_path is provided
    if save_path and not os.path.exists(save_path):
        os.makedirs(save_path)

    for day in days:
        plt.figure(figsize=(12, 8))
        daily_data = data[var_name].sel(day=day)

        # Choose global or local min/max for color scaling if no norm is provided
        if not norm:
            vmin, vmax = (daily_data.min().values, daily_data.max().values) if local_scale else (global_min, global_max)
            daily_data.plot(cmap=cmap, vmin=vmin, vmax=vmax,
                            cbar_kwargs={'label': f"{var_name} ({'Local' if local_scale else 'Global'} Scaling)"})
        else:
            daily_data.plot(cmap=cmap, norm=norm,
                            cbar_kwargs={'label': f"{var_name} with Custom Scaling"})

        # Customize plot labels and title
        date_str = np.datetime_as_string(day, unit='D')
        plt.title(f"{title} - {date_str}")
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        # Save each plot if save_path is specified
        if save_path:
            filename = f"{title}_{date_str}_{'local' if local_scale else 'global'}.png"
            plt.savefig(os.path.join(save_path, filename), dpi=300)
            print(f"Saved {filename} at {save_path}")

        plt.show()

# Set output directory for saved maps
output_dir = "Map_Outputs"

# Plot and save each variable with both global and local scaling

# Burning Index (BI) - Global and Local Scaling with Diverging Colormap
print("Burning Index - Global Scaling with Diverging Colormap")
plot_variable(bi_data, 'burning_index_g', 'Burning Index', global_min=global_bi_min, global_max=global_bi_max, cmap="coolwarm", norm=norm_bi, save_path=output_dir)

print("Burning Index - Local Scaling with Diverging Colormap")
plot_variable(bi_data, 'burning_index_g', 'Burning Index', cmap="coolwarm", local_scale=True, save_path=output_dir)

# Specific Humidity (SPH) - Global and Local Scaling with Continuous Colormap and Log Scaling
print("Specific Humidity - Global Scaling with Logarithmic Scaling")
plot_variable(sph_data, 'specific_humidity', 'Specific Humidity', global_min=global_sph_min, global_max=global_sph_max, cmap="Blues", norm=norm_sph, save_path=output_dir)

print("Specific Humidity - Local Scaling with Continuous Colormap")
plot_variable(sph_data, 'specific_humidity', 'Specific Humidity', cmap="Blues", local_scale=True, save_path=output_dir)

# Fuel Moisture (FM100) - Global and Local Scaling with Diverging Colormap
print("Fuel Moisture (100-hr) - Global Scaling with Diverging Colormap")
plot_variable(fm100_data, 'dead_fuel_moisture_100hr', 'Fuel Moisture (100-hr)', global_min=global_fm100_min, global_max=global_fm100_max, cmap="PiYG", norm=norm_fm100, save_path=output_dir)

print("Fuel Moisture (100-hr) - Local Scaling with Diverging Colormap")
plot_variable(fm100_data, 'dead_fuel_moisture_100hr', 'Fuel Moisture (100-hr)', cmap="PiYG", local_scale=True, save_path=output_dir)

# Fuel Moisture (FM1000) - Global and Local Scaling with Diverging Colormap
print("Fuel Moisture (1000-hr) - Global Scaling with Diverging Colormap")
plot_variable(fm1000_data, 'dead_fuel_moisture_1000hr', 'Fuel Moisture (1000-hr)', global_min=global_fm1000_min, global_max=global_fm1000_max, cmap="PiYG", norm=norm_fm1000, save_path=output_dir)

print("Fuel Moisture (1000-hr) - Local Scaling with Diverging Colormap")
plot_variable(fm1000_data, 'dead_fuel_moisture_1000hr', 'Fuel Moisture (1000-hr)', cmap="PiYG", local_scale=True, save_path=output_dir)

norm_bi = (bi_data['burning_index_g'] - global_bi_min) / (global_bi_max - global_bi_min)
norm_sph = (sph_data['specific_humidity'] - global_sph_min) / (global_sph_max - global_sph_min)
norm_fm100 = (fm100_data['dead_fuel_moisture_100hr'] - global_fm100_min) / (global_fm100_max - global_fm100_min)
norm_fm1000 = (fm1000_data['dead_fuel_moisture_1000hr'] - global_fm1000_min) / (global_fm1000_max - global_fm1000_min)

# Create a composite index (adjust weights based on domain knowledge)
composite_index = (0.5 * norm_bi + 0.2 * norm_sph + 0.15 * norm_fm100 + 0.15 * norm_fm1000)

# Calculate global min and max for the composite index
global_composite_min, global_composite_max = composite_index.min().values, composite_index.max().values

# Define a logarithmic normalization for the composite index
log_norm_composite = mcolors.LogNorm(vmin=global_composite_min + 1e-6, vmax=global_composite_max)

# Define a function to plot and save each variable with global and local scaling
def plot_variable(data, var_name, title, global_min=None, global_max=None, local_scale=False, cmap="YlOrRd", norm=None, save_path=None):
    days = data.day.values[::10]  # Plot every 10th day for clarity

    # Create directory if save_path is provided
    if save_path and not os.path.exists(save_path):
        os.makedirs(save_path)

    for day in days:
        plt.figure(figsize=(12, 8))
        daily_data = data.sel(day=day)

        # Choose global or local min/max for color scaling if no norm is provided
        if not norm:
            vmin, vmax = (daily_data.min().values, daily_data.max().values) if local_scale else (global_min, global_max)
            daily_data.plot(cmap=cmap, vmin=vmin, vmax=vmax,
                            cbar_kwargs={'label': f"{var_name} ({'Local' if local_scale else 'Global'} Scaling)"})
        else:
            daily_data.plot(cmap=cmap, norm=norm,
                            cbar_kwargs={'label': f"{var_name} with Custom Scaling"})

        # Customize plot labels and title
        date_str = np.datetime_as_string(day, unit='D')
        plt.title(f"{title} - {date_str}")
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        # Save each plot if save_path is specified
        if save_path:
            filename = f"{title}_{date_str}_{'local' if local_scale else 'global'}.png"
            plt.savefig(os.path.join(save_path, filename), dpi=300)
            print(f"Saved {filename} at {save_path}")

        plt.show()

# Set output directory for saved maps
output_dir = "Map_Outputs"

# Plot and save the Composite Index with both global and local scaling using Logarithmic Scaling

print("Composite Index - Global Scaling with Logarithmic Scaling")
plot_variable(composite_index, 'composite_index', 'Composite Fire Risk Index', cmap="viridis", norm=log_norm_composite, save_path=output_dir)

print("Composite Index - Local Scaling with Logarithmic Scaling")
plot_variable(composite_index, 'composite_index', 'Composite Fire Risk Index', cmap="viridis", local_scale=True, save_path=output_dir)



file_path_bi = "bi_2015.nc"
file_path_sph = "sph_2015.nc"
file_path_fm100 = "fm100_2015.nc"
file_path_fm1000 = "fm1000_2015.nc"

# Select the date range
bi_data = xr.open_dataset(file_path_bi).sel(day=slice("2015-08-01", "2015-09-15"))
sph_data = xr.open_dataset(file_path_sph).sel(day=slice("2015-08-01", "2015-09-15"))
fm100_data = xr.open_dataset(file_path_fm100).sel(day=slice("2015-08-01", "2015-09-15"))
fm1000_data = xr.open_dataset(file_path_fm1000).sel(day=slice("2015-08-01", "2015-09-15"))

# Calculate global min and max values for consistent scaling
global_bi_min, global_bi_max = bi_data['burning_index_g'].min().values, bi_data['burning_index_g'].max().values
global_sph_min, global_sph_max = sph_data['specific_humidity'].min().values, sph_data['specific_humidity'].max().values
global_fm100_min, global_fm100_max = fm100_data['dead_fuel_moisture_100hr'].min().values, fm100_data['dead_fuel_moisture_100hr'].max().values
global_fm1000_min, global_fm1000_max = fm1000_data['dead_fuel_moisture_1000hr'].min().values, fm1000_data['dead_fuel_moisture_1000hr'].max().values

# Define thresholds, adjusting to stay within valid ranges
def validate_threshold(threshold, vmin, vmax):
    if threshold <= vmin or threshold >= vmax:
        return (vmin + vmax) / 2  # Use midpoint if out of range
    return threshold

threshold_bi = validate_threshold(200, global_bi_min, global_bi_max)
threshold_fm100 = validate_threshold(10, global_fm100_min, global_fm100_max)
threshold_fm1000 = validate_threshold(10, global_fm1000_min, global_fm1000_max)

# Define norms
norm_bi = mcolors.TwoSlopeNorm(vmin=global_bi_min, vcenter=threshold_bi, vmax=global_bi_max)
norm_fm100 = mcolors.TwoSlopeNorm(vmin=global_fm100_min, vcenter=threshold_fm100, vmax=global_fm100_max)
norm_fm1000 = mcolors.TwoSlopeNorm(vmin=global_fm1000_min, vcenter=threshold_fm1000, vmax=global_fm1000_max)
norm_sph = mcolors.LogNorm(vmin=global_sph_min, vmax=global_sph_max)

# Helper function to generate GIFs for a dataset
def generate_gif(data, var_name, title, global_min, global_max, cmap, norm, output_dir, local_scale=False):
    days = data.day.values[::4]  # Take every 10th day to reduce GIF length
    frames = []

    temp_dir = Path(output_dir) / "temp_frames"
    temp_dir.mkdir(parents=True, exist_ok=True)

    for i, day in enumerate(days):
        plt.figure(figsize=(12, 8))
        daily_data = data[var_name].sel(day=day)

        # Define color scaling
        vmin, vmax = (daily_data.min().values, daily_data.max().values) if local_scale else (global_min, global_max)
        norm_to_use = norm if not local_scale else None

        # Plot and save the frame
        daily_data.plot(cmap=cmap, vmin=vmin, vmax=vmax, norm=norm_to_use,
                        cbar_kwargs={'label': f"{var_name} ({'Local' if local_scale else 'Global'} Scaling)"})
        plt.title(f"{title} - {np.datetime_as_string(day, unit='D')}")
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        frame_path = temp_dir / f"{var_name}_{'local' if local_scale else 'global'}_{i}.png"
        plt.savefig(frame_path)
        frames.append(imageio.imread(frame_path))
        plt.close()

    # Save GIF
    gif_path = Path(output_dir) / f"{var_name}_{'local' if local_scale else 'global'}.gif"
    imageio.mimsave(gif_path, frames, duration=0.1)
    print(f"GIF saved at: {gif_path}")

    # Clean up temporary frames
    for frame_file in temp_dir.glob("*.png"):
        frame_file.unlink()

# Output directory for GIFs
output_dir = "GIF_Outputs"
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Generate GIFs for each variable with both global and local scaling
print("Generating GIFs...")

# Burning Index (BI) - Global and Local Scaling
generate_gif(bi_data, 'burning_index_g', 'Burning Index', global_bi_min, global_bi_max, cmap="coolwarm", norm=norm_bi, output_dir=output_dir, local_scale=False)
generate_gif(bi_data, 'burning_index_g', 'Burning Index', global_bi_min, global_bi_max, cmap="coolwarm", norm=norm_bi, output_dir=output_dir, local_scale=True)

# Specific Humidity (SPH) - Global and Local Scaling
generate_gif(sph_data, 'specific_humidity', 'Specific Humidity', global_sph_min, global_sph_max, cmap="Blues", norm=norm_sph, output_dir=output_dir, local_scale=False)
generate_gif(sph_data, 'specific_humidity', 'Specific Humidity', global_sph_min, global_sph_max, cmap="Blues", norm=norm_sph, output_dir=output_dir, local_scale=True)

# Fuel Moisture (FM100) - Global and Local Scaling
generate_gif(fm100_data, 'dead_fuel_moisture_100hr', 'Fuel Moisture (100-hr)', global_fm100_min, global_fm100_max, cmap="PiYG", norm=norm_fm100, output_dir=output_dir, local_scale=False)
generate_gif(fm100_data, 'dead_fuel_moisture_100hr', 'Fuel Moisture (100-hr)', global_fm100_min, global_fm100_max, cmap="PiYG", norm=norm_fm100, output_dir=output_dir, local_scale=True)

# Fuel Moisture (FM1000) - Global and Local Scaling
generate_gif(fm1000_data, 'dead_fuel_moisture_1000hr', 'Fuel Moisture (1000-hr)', global_fm1000_min, global_fm1000_max, cmap="PiYG", norm=norm_fm1000, output_dir=output_dir, local_scale=False)
generate_gif(fm1000_data, 'dead_fuel_moisture_1000hr', 'Fuel Moisture (1000-hr)', global_fm1000_min, global_fm1000_max, cmap="PiYG", norm=norm_fm1000, output_dir=output_dir, local_scale=True)

print("GIF generation complete.")
