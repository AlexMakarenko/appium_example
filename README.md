# Test assignment

## To run tests:
- Clone the repository
- You should have Python3
- Install XCode on you machine from App Store
- Install appium on you machine `npm install -g appium`
- Install safari driver for appium `appium driver install safari`
- Install virtual env `python3 -m venv /path/to/new/virtual/environment`
- Activate venv `source <venv>/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run tests with a basic report `pytest -v tests --html=report.html  `
- Run tests with allure report `pytest -v tests --alluredir=allure_report`

## To open the basic report:
    Open `report.html` in a browser, or copy a full path to it and paste into a browser.

## To open the Allure report:
- [Install allure](https://formulae.brew.sh/formula/allure), on mac it's `brew install allure`
- [Install openjdk](https://formulae.brew.sh/formula/openjdk), on mac it's `brew install openjdk`
- Open the report: `allure serve allure_report`
