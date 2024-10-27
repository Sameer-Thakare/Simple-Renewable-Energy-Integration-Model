# Simple Renewable Integration Model Using PyPSA

## Overview

This project implements a simple renewable integration model using the **PyPSA (Python for Power System Analysis)** framework. The model simulates the integration of renewable energy sources into an electricity grid, optimizing for cost and emissions. It serves as a foundational tool for analyzing how renewable energy can be effectively incorporated into the existing energy system.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Scenarios](#example-scenarios)
- [Streamlit Visualization](#streamlit-visualization)
- [Contributing](#contributing)
- [License](#license)

## Features

- Model integration of renewable energy sources (e.g., solar, wind)
- Cost optimization for energy generation
- Emission reduction analysis
- Visualization of generation mix and results
- Simple configuration for various scenarios

## Requirements

- Python 3.7 or later
- PyPSA
- NumPy
- Pandas
- Matplotlib (for result visualization)
- Streamlit (for interactive visualizations)

You can install the required packages using pip:

```bash
pip install pypsa numpy pandas matplotlib streamlit
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/simple-renewable-integration.git
   ```

2. Navigate to the project directory:

   ```bash
   cd simple-renewable-integration
   ```

3. Install the required Python packages if you haven't already.

## Usage

1. Set up the renewable integration model in the `model.py` script. This file defines the components of the energy system, including generation sources, demand, and optimization parameters.

2. Run the model:

   ```bash
   python model.py
   ```

3. After executing the model, visualize the results using:

   ```bash
   python visualize_results.py
   ```

## Project Structure

```
/simple-renewable-integration
│
├── /data                # Input datasets for generation and demand
├── model.py             # Main script for renewable integration using PyPSA
├── visualize_results.py  # Script for visualizing simulation results
├── app.py               # Streamlit app for interactive visualization
├── /results             # Output results and figures
└── README.md            # Project documentation
```

## Example Scenarios

1. **Solar Integration**: Analyze the impact of integrating solar power into the grid, assessing cost and emissions.
   
2. **Wind Integration**: Evaluate the effects of wind energy on the generation mix and overall system performance.

3. **Combined Renewable Sources**: Study the combined effects of both solar and wind on costs and emissions reduction.

### Running a Scenario

To explore specific scenarios, modify the parameters in `model.py` to adjust generation sources and demand characteristics. For example, you can define the capacities of solar and wind:

```python
# Example of defining renewable capacities
renewable_sources = {
    "solar": 500,  # kW
    "wind": 300    # kW
}
```

Run the model again to see the effects of the changes:

```bash
python model.py
```

## Streamlit Visualization

To create an interactive visualization using Streamlit:

1. Create a file named `app.py` in the project directory.
2. Use the following code to visualize the results:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load results (replace with actual path)
results = pd.read_csv('results/generation_results.csv')

# Title of the Streamlit app
st.title("Renewable Integration Model Results")

# Sidebar for user input
st.sidebar.header("User Input")

# User input for renewable capacities
solar_capacity = st.sidebar.slider('Solar Capacity (kW)', 0, 1000, 500)
wind_capacity = st.sidebar.slider('Wind Capacity (kW)', 0, 1000, 300)

# Display results based on user input
st.subheader("Generation Mix")
st.bar_chart(results[['solar', 'wind', 'thermal', 'gas']])

# Plotting costs and emissions
fig, ax = plt.subplots()
ax.plot(results['time'], results['total_cost'], label='Total Cost')
ax.plot(results['time'], results['emissions'], label='Emissions')
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Total Cost and Emissions Over Time')
ax.legend()
st.pyplot(fig)

# Run the app with: streamlit run app.py
```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please submit a pull request or open an issue. For larger changes, it's a good idea to discuss them in an issue first.

## License

This project is licensed under the MIT License.
