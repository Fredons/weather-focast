# Weather App with Proper Error Handling

This project is a Weather Forecast application developed using Python, Streamlit, Plotly Express, and geopy library. The application allows users to obtain weather forecasts for specified locations over the next few days, with options to view temperature or sky conditions.

## Features

- **Input Interaction**: Users can input the desired location and select the number of forecast days.
- **Data Visualization**: Visual representations of temperature trends or sky conditions using Plotly Express.
- **Error Handling**: Proper error handling is implemented to handle invalid inputs or unexpected errors gracefully.

## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd weather_app
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. Access the application via the provided URL in the terminal.

3. Enter the desired location, select the forecast days, and choose between temperature or sky condition view.

4. View the weather forecast for the specified location.

## Error Handling

- **Invalid Location**: If the provided location is not found, a warning message will be displayed prompting the user to check the spelling or provide a valid location.
- **Unexpected Errors**: Any unexpected errors during the execution of the application will be caught and displayed to the user.

## Contributions

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests via the GitHub repository.


**Note**: This README provides an overview of the Weather App with Proper Error Handling. For detailed implementation and code explanations, please refer to the `main.py` file in the repository.
