# Hospital System Website

A comprehensive web-based hospital management system designed to facilitate interaction between patients, doctors, and nurses. This application provides features for appointment scheduling, medical record management, and patient-doctor communication.

## Features

- **User Roles**: Distinct dashboards for Patients, Doctors, and Nurses.
- **Appointment Management**: Patients can book, view, and manage appointments. Doctors can view their schedule.
- **Medical Records**: Doctors can prescribe medication and nurses can view prescriptions.
- **Responsive Design**: Fully optimized for desktop, tablet, and mobile devices.
- **Profile Management**: Users can update their personal information and profile pictures.
- **Reviews**: Patients can rate and review doctors.

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Styling**: Custom CSS with Flexbox/Grid, FontAwesome for icons

## Project Structure

```
├── api/
│   ├── index.py          # Main Flask application entry point
│   └── main.py           # Database connection logic
├── static/
│   ├── css/              # Stylesheets (including responsive.css)
│   ├── js/               # Frontend JavaScript logic
│   └── assets/           # Images and other static assets
├── templates/            # HTML templates (Jinja2)
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Installation & Setup

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd Hospital-System-Website
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Configuration**:
    - Ensure you have a PostgreSQL database running.
    - Set the `DATABASE_URL` environment variable.

    ```bash
    export DATABASE_URL="postgresql://user:password@localhost:5432/hospital_db"
    ```

5. **Run the application**:

    ```bash
    python api/index.py
    ```

6. **Access the website**:
    Open your browser and navigate to `http://127.0.0.1:5000`.

## Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
