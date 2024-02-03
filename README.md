# Weather App with Proper Error Handling

This project is a Weather Forecast application developed using Python and Streamlit, with proper error handling. It allows users to obtain weather forecasts for specified locations over the next few days, with options to view temperature or sky conditions.

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

1. Ensure that you have set up your API key in a `.env` file in the project directory. Add the following line to your `.env` file:

    ```plaintext
    API_KEY=your_api_key_here
    ```

2. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

3. Access the application via the provided URL in the terminal.

4. Enter the desired location, select the forecast days, and choose between temperature or sky condition view.

5. View the weather forecast for the specified location.

## Backend API

The `backend.py` file contains the backend logic for fetching weather data from the OpenWeatherMap API. Ensure that you have set up your API key in the `.env` file as described in the Usage section.

## Contributions

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests via the GitHub repository.


**Note**: This README provides an overview of the Weather App with Proper Error Handling. For detailed implementation and code explanations, please refer to the `main.py` and `backend.py` files in the repository.
