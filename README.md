# iShopApp

iShopApp is a prototype e-commerce platform designed to provide a seamless shopping experience. This repository contains the source code and necessary configurations to set up and run the application.
This service was created during the study of technology and practice

## Features

- User authentication and authorization
- Product catalog management
- Shopping cart functionality
- Order processing
- Integration with PostgreSQL database
- Dockerized environment for easy deployment

## Technologies Used

- Python
- Flask
- Marshmellow
- PostgreSQL
- Docker

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Python 3.8+ installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Newtonn00/iShopApp.git
   cd iShopApp
2. Build and run the Docker containers:
   docker-compose up --build
3. Access the application at http://localhost:5000

### Configuration

- Database settings can be adjusted in settings.ini.
- Environment variables can be set in the .env file.

### Development
#### Running Locally

1. Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
2. Install dependencies:
  pip install -r requirements.txt

#### Database Backup and Restore

- Backup: Scripts for backing up the PostgreSQL database are located in the psql_backup directory.
- Restore: Use the backup scripts to restore the database.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
