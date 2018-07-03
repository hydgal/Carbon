*** Settings ***
Documentation  This script will install Android apps on tablet
Library  AppiumLibrary
Resource  ../Apps



*** Variables ***


*** Test Cases ***
Android apps installation
    [Documentation]  Android apps such as IM3, MT, Payment Service apk's will be installed
    [Tags]  Smoke
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.6.93   	deviceName=284055490376  appPackage=com.android.sflauncher  appActivity=com.android.sflauncher.Launcher
    click element  all_aps
    click text  OK
    sleep  10
    install app  Apps\\im3pos-vantiv-android-demo-0721-afb37001f_signed_796.apk  com.vantiv.pos
    #run  process  adb install im3pos-vantiv-android-demo-0721-afb37001f_signed_796.apk





*** Keywords ***


