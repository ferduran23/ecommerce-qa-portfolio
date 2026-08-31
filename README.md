🛒 E-Commerce Web Application — End-to-End QA Project
📌 Project Overview

This project demonstrates an end-to-end Quality Assurance process for an e-commerce web application.

The goal is to validate the application's core functionality, identify defects, and demonstrate both manual and automated testing skills using industry-standard QA practices.

The project covers the complete testing lifecycle, from test planning and test case design to defect reporting, UI automation, API testing, and test execution reporting.

🎯 Objectives
Analyze and identify the application's main functional areas.
Design and execute functional and negative test cases.
Perform exploratory testing to identify unexpected behavior.
Document and report software defects.
Create an automated regression test suite.
Perform API testing.
Validate application data using SQL.
Integrate automated tests into a CI/CD pipeline.
Document test results and overall application quality.
🧪 Testing Scope
In Scope
User Registration
User Authentication
Login and Logout
Product Catalog
Product Search
Product Details
Shopping Cart
Checkout
Payment
Order Confirmation
User Account Functionality
Out of Scope
Real payment processing
Production infrastructure testing
Load and performance testing
Security penetration testing
Production database access
🔍 Testing Types

This project will include:

Functional Testing
Regression Testing
Smoke Testing
Exploratory Testing
Negative Testing
Boundary Value Testing
UI Testing
API Testing
Database Validation
Cross-Browser Testing
Automated Testing
🛠️ Tools & Technologies
Tool	Purpose
Python	Test automation
Pytest	Test framework
Selenium WebDriver	UI automation
Postman	API testing
SQL	Database validation
Jira	Defect tracking
Git	Version control
GitHub	Source code & documentation
GitHub Actions	CI/CD automation
📋 QA Process

The project follows the following QA workflow:

Requirements Analysis
        ↓
Test Planning
        ↓
Test Scenario Design
        ↓
Test Case Design
        ↓
Manual Test Execution
        ↓
Defect Reporting
        ↓
Defect Retesting
        ↓
Regression Testing
        ↓
UI Test Automation
        ↓
API Testing
        ↓
Database Validation
        ↓
CI/CD Integration
        ↓
Test Summary Report
📁 Project Structure
ecommerce-qa-portfolio/
│
├── README.md
│
├── documentation/
│   ├── test-plan.md
│   ├── test-scenarios.md
│   └── test-summary-report.md
│
├── test-cases/
│   └── Ecommerce_Test_Cases.xlsx
│
├── bug-reports/
│
├── automation/
│   ├── pages/
│   ├── tests/
│   ├── utils/
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── api-testing/
│   ├── postman-collection.json
│   └── tests/
│
└── evidence/
    ├── screenshots/
    └── videos/
📊 Test Coverage

Test coverage and execution results will be updated throughout the project.

Module	Test Cases	Passed	Failed	Blocked
Authentication	TBD	TBD	TBD	TBD
Product Catalog	TBD	TBD	TBD	TBD
Search	TBD	TBD	TBD	TBD
Shopping Cart	TBD	TBD	TBD	TBD
Checkout	TBD	TBD	TBD	TBD
Payment	TBD	TBD	TBD	TBD
🐛 Defect Management

Defects identified during testing will be documented with:

Bug ID
Summary
Environment
Preconditions
Steps to Reproduce
Expected Result
Actual Result
Severity
Priority
Evidence
Status

Defects will be tracked throughout their lifecycle from identification through retesting and closure.

🤖 Automation Strategy

The automation framework will focus on critical and repetitive user workflows.

Initial automated scenarios will include:

Valid user login
Invalid login
Product search
Product selection
Adding products to cart
Removing products from cart
Updating product quantity
Checkout workflow

The automation framework will use the Page Object Model (POM) to improve maintainability and reusability.

🔌 API Testing

API testing will be performed using Postman and Python/Pytest.

Testing will cover:

HTTP methods
Status codes
Request and response validation
Required parameters
Invalid requests
Response data
Error handling
🗄️ Database Validation

SQL queries will be used to validate application data where applicable.

Examples include:

Verifying customer records
Validating order information
Checking product data
Validating transaction information
Identifying duplicate records
🚀 CI/CD

Automated tests will eventually be integrated with GitHub Actions.

The CI pipeline will:

Install project dependencies.
Execute the automated test suite.
Generate test results.
Report test failures.
Provide visibility into the status of the test suite.
📈 Final Test Report

At the end of the project, a test summary report will document:

Total test cases
Execution results
Defects identified
Defects resolved
Automation coverage
API testing results
Regression results
Known limitations
Overall quality assessment
👩‍💻 About This Project

This project was created as part of my QA engineering portfolio to demonstrate practical experience in manual testing, test automation, API testing, defect management, SQL, and CI/CD.

QA Engineer: Fernanda Durán

Focus: Manual QA | Test Automation | API Testing | Python | Selenium | Pytest
