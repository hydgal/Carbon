*** Settings ***
Library  AppiumLibrary



*** Variables ***


*** Test Cases ***
About Carbon
    [Documentation]  Verify data is present using assertions
    [Tags]  Smoke
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.6.93   	deviceName=284055490376  appPackage=com.verifone.swordfish.settings  appActivity=com.verifone.swordfish.settings.SettingsActivity
    Sleep   15
    #wait until element is visible  com.verifone.swordfish.settings:id/category_caption
    text should be visible  284055490376    exact_match=False
    scroll up  Terminal Status
