# Asset Management System
# A Django-based application to manage asset lending, tracking, and maintenance. This system allows users to add new assets, lend assets in bulk or individually, track asset usage, and handle returns with conditions.

# Table of Contents
# Features
# Installation
# Usage
# Contributing
# License
# Features
# Asset Management: Add, edit, and lend assets.
# Lending System: Lend assets in bulk or individually with tracking of quantities.
# Tracking: View lent assets and return them with conditions (good/bad).
# Dynamic Updates: Automatic updates to asset counts based on lending and returning actions.
# Maintenance: Manage asset maintenance schedules.
# Installation
## Prerequisites
1. Python 3.x
2. Django 3.x or later
3. pip (Python package installer)
# Steps
1. Clone the repository:

bash `git clone https://github.com/AbubakarMohamed/AssetManagement.git
2. bash `cd asset-management-system
3. Create and activate a virtual environment:

bash `python -m venv venv
source venv/bin/activate 
venv\Scripts\activate`
On windows use 
4. Apply migrations:

bash `python manage.py makemigrations
python manage.py migrate

5. Run the development server:
bash `python manage.py runserver

6.Access the application at http://127.0.0.1:8000/.
