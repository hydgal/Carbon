*** Settings ***
Library  AppiumLibrary

*** Variables ***
${EMAIL_ID} =  louis14@getnada.com
${PASSWORD} =  Veri1234

*** Keywords ***

Launch Setup application
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.7.46   	deviceName=270383310050  appPackage=com.verifone.swordfish.vfiSetup  appActivity=com.verifone.swordfish.vfiSetup.Welcome.MainActivity

Select environment (QA)
    click button  QA
    wait until page contains  button_welcome_continue
    click element  button_welcome_continue
    sleep  10

Select ethernet as network
    click button  Skip
    sleep  10
    click element  imageButtonContinue
    sleep  5


SSO login
    wait until page contains  Email
    tap  email
    input text  email   ${EMAIL_ID}
    tap  password
    input password  password  ${PASSWORD}
    sleep  10
    press keycode  66
    sleep  20
    #wait until element is visible   PRINT TEST RECEIPT 15
    #wait until page contains element  com.verifone.peripherals.service:id/test 20


Test print receipt
    click text  PRINT TEST RECEIPT
    #wait until page contains  next_button 10
    sleep  10
    click element  com.verifone.peripherals.service:id/next_button
    #wait until page contains  button_setup_finish 10
    sleep  15


Finish setup
    click element  com.verifone.swordfish.vfiSetup:id/button_setup_finish
