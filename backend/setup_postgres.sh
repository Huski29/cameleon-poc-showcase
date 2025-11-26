#!/bin/bash

# Setup script for PostgreSQL with pgvector for Cameleon project
# Run this script with: sudo bash setup_postgres.sh

set -e  # Exit on error

echo "=================================================="
echo "Setting up PostgreSQL for Cameleon"
echo "=================================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Please run this script with sudo: sudo bash setup_postgres.sh"
    exit 1
fi

# Database configuration
DB_NAME="cameleon_db"
DB_USER="cameleon_user"
DB_PASSWORD="cameleon_password_2024"

echo "📦 Installing pgvector extension..."
apt-get update -qq
apt-get install -y postgresql-16-pgvector

echo ""
echo "🗄️  Creating database and user..."

# Switch to postgres user and run commands
sudo -u postgres psql <<EOF
-- Drop database and user if they exist (for clean setup)
DROP DATABASE IF EXISTS ${DB_NAME};
DROP USER IF EXISTS ${DB_USER};

-- Create user
CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';

-- Create database
CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};

\c ${DB_NAME}

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO ${DB_USER};
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${DB_USER};
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${DB_USER};
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ${DB_USER};
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ${DB_USER};

EOF

echo ""
echo "✅ PostgreSQL setup complete!"
echo ""
echo "=================================================="
echo "Database Configuration:"
echo "=================================================="
echo "Database Name: ${DB_NAME}"
echo "Database User: ${DB_USER}"
echo "Database Password: ${DB_PASSWORD}"
echo "Host: localhost"
echo "Port: 5432"
echo ""
echo "Connection String:"
echo "postgresql://${DB_USER}:${DB_PASSWORD}@localhost:5432/${DB_NAME}"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Update your .env file with the database URL"
echo "2. Run: python seed.py (to populate the database)"
echo "3. Restart the backend server"
echo ""

