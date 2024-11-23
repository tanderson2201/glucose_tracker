# Glucose Tracker

![Project Status](https://img.shields.io/badge/build-passing-brightgreen)

Glucose Tracker is a Python application that allows glucose readings from LibreLinkUp to be displayed on your desktop screen. The purpose of the application is to provide a more efficient way to monitor your glucose levels compared to the official LibreLink/LibreLinkUp application by displaying the glucose reading on your screen, allowing you to set the refresh interval, and enabling you to easily see the trend of your glucose levels. More details about this project can be found [here](https://tanderson.net/posts/LibreLink-Tracker-Project/).

### Features:

- Always visible glucose display.
- Set glucose reading refresh interval.
- Refresh button to get the latest reading (or if the connection is lost).
- Error notifications if glucose readings cannot be displayed.
- Color-coded glucose levels: 
  - **Red**: Out of range
  - **Orange**: Slightly out of range
  - **Green**: Within range
- Trend indicator for glucose levels: 
  - Dropping Fast
  - Going Low
  - Stable
  - Going High
  - Increasing Fast

---

## Table of Contents

1. [Installation](#installation)
2. [Dependencies](#dependencies)
3. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

---

## Installation

To install this project, clone the repository and install the dependencies:

```bash
git clone https://github.com/tanderson2201/glucose_tracker.git
```

---

## Dependencies

You will need the following Python dependencies:

```bash
pip install requests
pip install tk
```
Make sure to import `tkinter` in your code where necessary.

---

## Usage

Once the repository has been downloaded and the dependencies are installed, navigate to `\glucose_tracker-main\glucose_tracker-main\config.conf`. Update the `patient_id` and `token` fields to match your LibreLinkUp account. To obtain this information, follow the guide here: [LibreLink Tracker Project Guide](https://tanderson.net/posts/LibreLink-Tracker-Project/).

After updating and saving the `config.conf` file, run the application by executing `\glucose_tracker-main\glucose_tracker-main\glucose_tracker_5.exe`. This will launch the Glucose Tracker application.

---

## Contributing

I welcome contributions! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/tanderson2201/glucose_tracker.git
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-namet
   ```
4. Make your changes and commit them:
   ```bash
   git commit -m "Add feature"
   ```
5. Push your changes:
   ```bash
   git push origin feature-name
   ```
6. Create a pull request on GitHub.

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## Acknowledgments

Thanks to Ronaldr1985 for assisting with this application and for building a version that works directly on a Raspberry Pi Zero using an OLED Display Hat. More details about this project can be found on their github page.





