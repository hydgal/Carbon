*** Settings ***
Library  AppiumLibrary


*** Variables ***


*** Test Cases ***
Add apps to Favorites placeholder
    [Documentation]  Add apps to favorites place-holder on launcher
    [Tags]  Smoke

    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.6.82   	deviceName=284055490375  appPackage=com.android.sflauncher  appActivity=com.android.sflauncher.Launcher
    Tap  com.android.sflauncher:id/root_layout
    #tap  com.android.sflauncher:id/list
    click text  About Carbon
    tap  com.android.sflauncher:id/root_layout
    scroll down  android.widget.RelativeLayout
    click text  Settings

*** Keywords ***



