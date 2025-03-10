# LinkedIn "Easy Apply" Automation

This project automates the process of applying for jobs on LinkedIn using the "Easy Apply" feature. The script logs into LinkedIn, searches for job listings, and applies to jobs with minimal user intervention.

## Prerequisites

Python 3.x installed on your system

Google Chrome browser

ChromeDriver compatible with your Chrome browser version

Environment variables set in a .env file

## Installation

### Clone the repository:

git clone https://github.com/seanm123-FI/Automating_LinkedIn_Job_Applications.git

cd Automating_LinkedIn_Job_Applications

### Install the required Python packages:

pip install selenium python-dotenv


### Download and set up ChromeDriver:

Ensure your ChromeDriver is compatible with your installed version of Chrome. 

Download ChromeDriver and add it to your system PATH.

### Create a .env file in the project directory:

Add your LinkedIn credentials and phone number to the .env file:

EMAIL=your-email@example.com

PASSWORD=your-password

PHONE=your-phone-number


## Usage
### Run the script using the following command:

python Job_Application_Automation.py


### The script will:

Log into LinkedIn using the credentials provided in the .env file.

Navigate to the job search page.

Scroll to load all job listings.

Apply to jobs marked with the "Easy Apply" feature.

## Disclaimer
Use at your own risk. This script automates interactions with LinkedIn, which may violate LinkedIn's terms of service. The author of this script is not responsible for any consequences resulting from its use, including but not limited to account suspension or ban.
