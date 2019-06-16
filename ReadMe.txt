Read Me:

This is Page Object Model + Test Data Driven  = Hybrid Framework made with python with selenium for web automation

Mainly framework is designed in manner so can easily convert it into TDD as per our requirements

currently , this framework can run on CHROME browser version 74+ only
With some modification( such as in , DesiredCapabilities , Browser profiling and browser options) of machine's IE and firefox browsers it can be run on it.
Because for IE/Firefox browser we need to set up some browserOptions or RemoteWebdriver (for protected mode and JavaScript issues)
https://github.com/SeleniumHQ/selenium/issues/5531
https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html
https://www.technipages.com/internet-explorer-enabledisable-javascript

******************************
Areas to improve for this framework with following features:

1. Allure reporting
2. Capturing Screenshot for failed cases
3. Implement correct try and catch fields for error reporting (which includes Screenshot in it )
4. Additional REST API cases 
5. Run on multiple environment with same core framework 
6. Data-Parameterization (Input) from CSV or EXCEL or JSON file can be done within this framework
7. Selenium Grid can be set up to run same cases on multiple machines at same time (with help of RemoteWebdriver)


******************************
For this project we use repository:
 
 - pytest (for Testcase sequence)
 - pytest-html (for html report generation and verify case failure)
 - selenium (for web application automation)
 - selenium drivers (Chrome + IE+ Firefox) (for browser configuration) 
 
********************************
Additional repos to be added later

 - desired_capabilities (for running as per browser profiling)
 - rest assured (for rest api testing)
 - Jmeter (for rest api testing)
 - http client (for page status)
 - sql connections (for database testing)
 - screenshot capture (for failed test case reporting with screenshot)
 - allure(for better HTML reporting )



******************************
<---------- THIS IS MUST ------------->
Pre requisite: 
1. Run this test on Windows 8 or windows 10 (64-bit) OS machines 
2. Following should be installed in your machine
- Python version 3.7.3 
- pip version 19.1.1  
- setuptools version 40.8.0 
- PyCharm community edition IDE(2019.1.3
3. Python environment variables should be set up 
https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages
http://coding-guru.com/easy_install-on-windows/
4. install "pytest-html" in your machine: pip install pytest-html ( to check the html reporting )
5. install selenium in your machine: pip install selenium ( to check the html reporting )
6. install PyCharm community edition IDE(2019.1.3) to run this framework 
7. Download chrome driver on your machine : http://chromedriver.chromium.org/downloads  <----------THIS IS MUST
8. Install Chrome Browser version 74 (64-bit)  version  ( this framework will run on the chromebrowser for now, it works on other browser fluently after some modification)<----------THIS IS MUST

######################################
How to run the test case: 

If test case does not run in environment : PLEASE let me know. I have already same configured in my system with same code so i can show you. If its needed and required.
######################################

1. Above mentioned pre-requisite is setup correctly
2. Import project from github to your PyCharm IDE
3. Open Project go to File Menu > settings > Project Interpreter 
- Make sure you have installed pytest, pytest-html, selenium repository
4. Make sure, project is set to uses the own "virtualenv"
5. check "RunConfiguration" are set as mentioned in the screenshot (RunConfiguration)
6. Go to: Project > utils > util.py file and provide the directory for CHROME DRIVER
7. Now Open command prompt ( to open it : type cmd in windows) with administrator rights
8. Go to root directly location of this project
9. Type command : 
python -m pytest (to simply run the test cases without  html report )
python -m pytest --html=reports/report1.html --self-contained-html (to see html reports after test execution )
python -m pytest --html=reports/report2.html (to see html reports after test execution with css files folder )

10. It should invoke your chrome browser and test should be started.
11. Chrome browser will invoke two times to run cases of two different classes
12. Check case execution is running on the command prompt and on browser
13. After test case run is completed : = 5 passed in ...seconds == message will be shown on command prompt
14. Now go to Project: > reports > report1.html file is generated
15. Open it in the browser and check the result of each test case  ( first 4 cases are the set of our task)
16. Expand the each test case to see result.
17. If there is any issue while running the test case( Like: Collecting test cases 0 )
Kindly clear/delete the "pytest cache" of the project or of environment/pycharm and try to run. Hopefully it will resolve the issue.
Cause it may happen when there is new environment set up for the Framework.
Still It does not work PLEASE let me know. I have already same configured in my system with same code so i can show you. If its needed and required.

Check the screenshot(FrameworkStructure) to understand the Framework Structure

------------------------------
Some other command for installation and run test case : 

python -m pytest --html=reports/report2.html
python -m pytest --html=reports/report2.html --self-contained-html
To install pytest: pip install pytest
To install pytest-html: pip install pytest-html 
To install selenium: pip install selenium 
To run test with any specific browser: python -m pytest --browser chrome

######################################