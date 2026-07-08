# Centered Moving Average Filter

A simple Python implementation of a centered moving average filter for smoothing noisy signals.

This project generates a synthetic signal, adds random noise, and applies a centered moving average algorithm implemented from scratch. The filtered signal is then compared with the original noisy signal through visualization.

## Features

* Synthetic signal generation
* Gaussian noise simulation
* Centered moving average smoothing
* Edge handling for boundary samples
* Signal visualization using Matplotlib
* Educational implementation without relying on built-in smoothing functions

## Background

Moving average filtering is one of the simplest signal smoothing techniques. The method replaces each point in a signal with the average value of its neighboring points within a specified window.

This approach reduces random noise while preserving the overall trend of the signal.

## Requirements

Install the required Python packages:

```bash
pip install numpy matplotlib
```

## Usage

Run the script:

```bash
python MovingAverage1.2.py
```

The program will:

1. Generate a synthetic signal.
2. Add random Gaussian noise.
3. Apply a centered moving average filter.
4. Display a plot comparing the noisy signal and the smoothed signal.

## Algorithm

For each point in the signal:

1. A centered window is created around the current sample.
2. Neighboring values inside the window are averaged.
3. Boundary conditions are handled by using only available samples.
4. The computed average replaces the current point in the filtered signal.

## Parameters

```python
window_size = 15
```

The smoothing intensity depends on the window size:

* Smaller windows preserve more detail.
* Larger windows produce stronger smoothing.

## Example Output

The resulting figure displays:

* Original noisy signal
* Centered moving average filtered signal

allowing visual comparison of the smoothing performance.

## Applications

* Signal processing
* Spectroscopy preprocessing
* Near-Infrared (NIR) data analysis
* Sensor data filtering
* Educational demonstrations of smoothing techniques

## Author

Developed as an educational example of moving average signal smoothing implemented from first principles.

## License

This project is licensed under the MIT License.
