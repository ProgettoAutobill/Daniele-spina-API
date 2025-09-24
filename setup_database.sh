#!/bin/bash

# Check and create virtual environment if it doesn't exist
VENV_PATH="/home/$(whoami)/virtualenvs/smartapi"
if [ ! -d "$VENV_PATH" ]; then
    echo "Creating virtual environment at $VENV_PATH..."
    python3 -m venv "$VENV_PATH"
    echo "Virtual environment created successfully!"
else
    echo "Virtual environment already exists at $VENV_PATH"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

echo "Starting PostgreSQL database in Docker..."
sudo docker-compose up -d postgres

echo "Waiting for PostgreSQL to be ready..."
sleep 10

# Check if PostgreSQL is ready
echo "Checking PostgreSQL connection..."
until sudo docker exec postgres_db pg_isready -U admin -d sistema_gestionale; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

echo "PostgreSQL is ready!"

# echo "Creating database tables..."
# "$VENV_PATH/bin/python" src/database/sessionDB.py

echo "Database setup complete!"
echo "PostgreSQL is running on localhost:5432"
echo "Database: sistema_gestionale"
echo "Username: admin"
echo "Password: password123"
echo "Virtual environment: $VENV_PATH"
