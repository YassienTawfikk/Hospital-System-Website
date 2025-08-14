# Hospital System Website

## Welcome to the Hospital Management System

This is a comprehensive **Hospital Management System** built to streamline healthcare operations. The platform features a user-friendly interface with a secure backend that enables patients, doctors, and administrators to interact seamlessly.

---
## 🌐 Live Demo
<a href="https://hospital-system-website.vercel.app/login" target="_blank" rel="noopener noreferrer">Hospital System</a>
> Loading may take a few seconds

### Test Credentials

You can use the following test accounts to explore different user roles:

#### **Doctor Logins**
| Email                 | Password  |
|----------------------|------------|
| `Doctor01@gmail.com` | `Doctor01` |
| `Doctor02@gmail.com` | `Doctor02` |
| `Doctor03@gmail.com` | `Doctor03` |
| `Doctor04@gmail.com` | `Doctor04` |
| `Doctor05@gmail.com` | `Doctor05` |
| `Doctor06@gmail.com` | `Doctor06` |
| `Doctor07@gmail.com` | `Doctor07` |
| `Doctor08@gmail.com` | `Doctor08` |

#### **Nurse Logins**
| Email                 | Password  |
|----------------------|------------|
| `Nurse01@gmail.com`  | `Nurse01`  |
| `Nurse02@gmail.com`  | `Nurse02`  |
| `Nurse03@gmail.com`  | `Nurse03`  |
| `Nurse04@gmail.com`  | `Nurse04`  |
| `Nurse05@gmail.com`  | `Nurse05`  |
| `Nurse06@gmail.com`  | `Nurse06`  |
| `Nurse07@gmail.com`  | `Nurse07`  |
| `Nurse08@gmail.com`  | `Nurse08`  |

#### **Patient Logins**
| Email                 | Password  |
|----------------------|------------|
| `Patient01@gmail.com` | `Patient01` |
| `Patient02@gmail.com` | `Patient02` |
| `Patient03@gmail.com` | `Patient03` |
| `Patient04@gmail.com` | `Patient04` |
| `Patient05@gmail.com` | `Patient05` |
| `Patient06@gmail.com` | `Patient06` |
| `Patient07@gmail.com` | `Patient07` |
| `Patient08@gmail.com` | `Patient08` |

---

## Video Demonstration

A full video walkthrough of the system is available for you to explore all features.
<video src="https://github.com/user-attachments/assets/482d3c58-1b43-4893-b731-8c3f08c38bc4" controls="controls" style="max-width: 100%;"></video>


---

## Key Features

### 1. **Dark Mode Interface**
   - Provides a comfortable browsing experience with dark mode functionality.
    ![Homepage](https://github.com/user-attachments/assets/dfc57138-1e24-4fdd-b52b-0c02ef3075ad)

### 2. **Doctor Profiles**
   - View detailed profiles for doctors, including ratings and reviews.
    ![Doctor Profiles](https://github.com/user-attachments/assets/c3a1a1a3-6fb9-4060-a294-c1f1ea6dacc3)

### 3. **Appointment Management**
   - Patients can book, view, and manage appointments efficiently.
    ![Patient Profiles](https://github.com/user-attachments/assets/9710cbb9-69c6-4947-bf8d-eedb3e75aa32)

### 4. **Prescription Management**
   - Doctors can create precise prescriptions and diagnostic reports.
    ![Prescription Management](https://github.com/user-attachments/assets/08093038-a92b-4276-8880-908e32884853)

### 5. **Patient Profiles**
   - Patients can manage their personal details, medications, and upcoming appointments.
   ![Patient Profile Screenshot](https://github.com/user-attachments/assets/bc2b8988-58d7-4d28-88a0-d2ccd1e95e75)

---

## Installation Instructions

To set up and run this project on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YassienTawfikk/Hospital-System-Website.git
   cd Hospital-System-Website
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file based on the `.env.example` file:
     ```bash
     cp .env.example .env
     ```
   - Fill in your database credentials in the `.env` file.

4. **Run the Application**:
   ```bash
   index.py run
   ```
   - Open your browser and go to `http://127.0.0.1:5000`.

---

## Technologies Used

- **Python**: Flask Framework
- **PostgreSQL**: Database
- **HTML, CSS, JavaScript**: Frontend
- **Bootstrap**: Responsive Design

---

## Database Schema

Here is a brief overview of the database tables used in this project:

### Tables
- **patients**: Stores patient details.
- **doctors**: Stores doctor information and specialties.
- **appointments**: Tracks appointments and their status.
- **prescriptions**: Records prescription details provided by doctors.


---

## Contributors
<table align="center">
  <tr>
        <td align="center">
      <a href="https://github.com/YassienTawfikk" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/126521373?v=4" width="150px;" alt="Yassien Tawfik"/>
        <br />
        <sub><b>Yassien Tawfik</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/madonna-mosaad" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/127048836?v=4" width="150px;" alt="Madonna Mosaad"/>
        <br />
        <sub><b>Madonna Mosaad</b></sub>
      </a>
    </td>
        <td align="center">
      <a href="https://github.com/nancymahmoud1" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/125357872?v=4" width="150px;" alt="Nancy Mahmoud"/>
        <br />
        <sub><b>Nancy Mahmoud</b></sub>
      </a>
    </td>
      <td align="center">
        <a href="https://github.com/Mazenmarwan023" target="_blank">
          <img src="https://avatars.githubusercontent.com/u/127551364?v=4" width="150px;" alt="Mazen Marwan"/>
          <br />
          <sub><b>Mazen Marwan</b></sub>
        </a>
      </td>
    </td>
        <td align="center">
      <a href="https://github.com/yousseftaha167" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/128304243?v=4" width="150px;" alt="Youssef Taha"/>
        <br />
        <sub><b>Youssef Taha</b></sub>
      </a>
    </td>    
  </tr>
</table>
