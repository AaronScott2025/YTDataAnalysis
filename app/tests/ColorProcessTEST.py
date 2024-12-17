import app.processes.color_process as c

def test_color_process():
    # Sample RGB values with expected colors
    rgb_values = [
        [78, 167, 241],  # Expected: Purple
        [255, 0, 0],  # Expected: Red
        [0, 255, 0],  # Expected: Green
        [0, 0, 255],  # Expected: Blue
        [255, 255, 0],  # Expected: Yellow
        [0, 255, 255],  # Expected: Blue
        [255, 165, 0],  # Expected: Orange
        [128, 128, 128],  # Expected: Gray
        [255, 192, 203],  # Expected: Pink
        [0, 0, 0],  # Expected: Gray
        [23, 4, 100]  # Expected: Blue
    ]

    # Loop through each RGB value and predict the color
    for rgb_value in rgb_values:
        predicted_color = c.predict_color(rgb_value)  # Ensure predict_color function is defined
        print(f"The predicted color for RGB value {rgb_value} is {predicted_color}")

if __name__ == '__main__':
    test_color_process()