# Website Tester

This repository contains scripts I developed to automate the testing process for my college's website. The project aimed to identify vulnerabilities and improve website security.

## Background

During my testing, I found a severe vulnerability in the **Campus Book** website used for campus-related tasks. It stored and showed personal information of students, hence it was prone to leaking data from outside parties or companies. I created this project to expose these security flaws.

## Project Overview

This repository contains three scripts, each serving a distinct purpose:

1. **Automating On-Screen Interactions**
- The main script automates on-screen interactions by recognizing and reacting to the color of certain pixels on the website.
- This method was applied to track changes after every action taken on the website.

2. **Pixel Color Detection**
- This script finds the color of a pixel at given coordinates.
- It is essential for calibrating and fine-tuning the automation process.

3. **Student ID Generation**
- This script creates the student login IDs used on the website.
- It served as a vital part in demonstrating the vulnerability of the ID management system.

## Impact

The findings from this project have shown the requirement for better security in storing student personal data. Because of these scripts, the college replaced its vulnerable campusbook website with etlab, ensuring better protection of student data.

## Usage

Note: This project is solely created for the purpose of ethical hacking to improve the security of websites. Do not misuse or deploy these scripts without permission.

1. Clone the repository:
```bash
git clone https://github.com/your-username/website-tester.git
cd website-tester
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Execute the scripts according to their purpose:
- **Automation Script**:
```bash
python3 main_script.py
```

## Disclaimer

This project was developed for educational purposes and ethical security testing. Any unauthorized use of these scripts to exploit vulnerabilities is strictly forbidden.
