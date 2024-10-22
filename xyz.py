import ezdxf

# Data for the section (Meter and Height in meters)
meter_values = list(range(121))
height_values = [
    3.18, 2.91, -1.24, 3.45, 2.82, -0.58, 3.09, 4.25, 2.49, 1.96, -0.83, 3.07, 2.63, 3.57, 4.11, 1.23,
    -1.08, 2.95, 4.32, 3.04, 2.76, 3.21, -0.53, 2.57, 3.74, 3.39, 4.02, 2.36, 1.04, 3.31, -0.92, 2.83,
    3.61, 4.14, 2.99, 2.91, -1.28, 3.13, 2.69, 4.23, 3.42, 1.15, -0.75, 2.92, 3.28, 4.01, 3.67, 2.12,
    -1.34, 2.96, 3.05, 3.41, 4.13, 1.52, -0.86, 3.25, 2.72, 3.83, 4.39, 2.34, -1.15, 3.04, 3.64, 2.59,
    1.93, 3.36, -0.61, 3.75, 3.35, 2.81, 1.44, -0.97, 3.18, 4.08, 2.65, 3.03, 4.31, 1.87, -1.06, 3.01,
    3.71, 4.22, 2.94, 1.18, -0.56, 3.35, 2.84, 4.05, 2.54, 1.74, -0.68, 3.21, 3.94, 4.28, 2.47, 1.05,
    -1.12, 3.17, 2.91, 4.07, 3.23, -0.87, 2.78, 3.43, 4.24, 2.96, 2.65, -0.95, 3.84, 4.11, 2.53, 1.21,
    -1.03, 3.04, 3.97, 2.93, 3.63, 2.32, -0.67, 4.12, 3.32
]

# Create a new DXF document
doc = ezdxf.new(dxfversion='R2010')

# Adding model space
msp = doc.modelspace()

# Draw the polyline using the given meter and height values
for i in range(121):
    x = meter_values[i]  # meter
    y = height_values[i]  # height in meters
    msp.add_line((x, 0), (x, y))  # vertical line representing the section

# Save the DXF document
doc.saveas("cutting_filling_sections.dxf")
