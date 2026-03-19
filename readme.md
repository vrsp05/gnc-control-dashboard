# GNC-Control-Dashboard: SCADA HMI & Data Historian

This project is a web-based Human-Machine Interface (HMI) designed for Supervisory Control and Data Acquisition (SCADA). Built with the Django framework, it serves as a centralized control hub for embedded systems (such as water level sensors or remote cameras). The application allows an operator to monitor system health in real-time, update critical operational thresholds with built-in safety validation, and maintain a persistent Data Historian using an integrated SQLite database. By bridging high-level web architecture with low-level control logic, this project demonstrates a "Mission Assurance" approach to software development, featuring a suite of 8 automated unit tests to ensure system reliability and data integrity.

## Instructions for Build and Use

Steps to build and/or run the software:

1. **Clone and Navigate:** Download the repository to your local machine and navigate into the gnc-control-dashboard root directory.
2. **Virtual Environment:** Create and activate a Python virtual environment to isolate dependencies:
    * ``python -m venv .venv``
    * ``.\.venv\Scripts\Activate.ps1 (Windows) or source .venv/bin/activate (Mac/Linux).``
3. **Install Dependencies:** Install the Django framework using pip:
    * ``pip install django``
4. **Database Migration:** Initialize the SQLite "Historian" database by running the migration commands:
5. **Launch Server:** Start the local development server:
    * ``python manage.py runserver``

Instructions for using the software:

1. **Access the HMI:** Open a web browser and navigate to ``http://127.0.0.1:8000/`` to view the SCADA Dashboard.
2. **Update Set-Points:** Use the **Alert Threshold** form to input a new control value (0–500 cm) and click **UPDATE SET-POINT**.
3. **Monitor System State:** Observe the "System Status" at the top; if the value exceeds 400, the UI will dynamically trigger a **WARNING** state.
4. **Verify Historian:** Scroll down to the **System Historian** table to see a persistent chronological log of all valid operator inputs and timestamps.
5. **Run Verification Suite:** To verify system integrity, run the automated test suite using:
    * ``python manage.py test hmi``

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* **Python 3.12+:** The core programming language used for backend logic and scripting.
* **Django 5.x:** The high-level web framework used for MVT (Model-View-Template) architecture and database ORM.
* **SQLite 3:** A lightweight, disk-based database used as the "System Historian" for persistent data logging.
* **Visual Studio Code:** The primary IDE used for development, debugging, and terminal management.
* **Git:** Version control system used for daily progress tracking and code integrity.
* **Django Test Framework:** Built-in library used for creating the 8 automated unit tests for validation and UI states.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* **[Django Documentation.](https://docs.djangoproject.com/en/stable/)**
* **[Real Python - Django Tutorials.](https://realpython.com/tutorials/django/)**
* **[tutorialspoint Django Programming Langugage.](https://www.tutorialspoint.com/django/index.htm)**
* **[Net Ninja's Django YouTube Tutorial.](https://www.youtube.com/watch?v=3EzKBFc9_MQ&list=PL4cUxeGkcC9iqfAag3a_BKEX1N43uJutw)**

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] **Physical Hardware Integration:** Transition from simulated sensor data to live telemetry from my STM32/Arduino Tinaco sensor via a REST API or WebSockets.
* [ ] **Visual Telemetry (ESP32-CAM):** Integrate a dedicated "Optical Navigation" tab to receive and display real-time images or video feeds from a remote ESP32-CAM module.
* [ ] **Predictive Control Logic:** Implement a Python-based PID (Proportional-Integral-Derivative) controller within the Django backend to automatically adjust set-points based on historical data trends.
* [ ] **Advanced Data Visualization:** Replace the basic HTML historian table with dynamic Chart.js graphs to visualize water levels and system health over 24-hour periods.
* [ ] **User Authentication:** Add an "Operator Login" system to ensure only authorized users can modify critical system thresholds.