*** Settings ***
Library  AppiumLibrary




*** Variables ***
${PASSWORD_1} =   12345678
${EMAIL_ID} =  louis14@getnada.com
${PASSWORD_2} =  Veri1234

*** Test Cases ***
Device Setup with wifi
    [Documentation]  Choose wiif as network druing setup
    [Tags]  Smoke
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.7.46   	deviceName=284055490375  appPackage=com.verifone.swordfish.vfiSetup  appActivity=com.verifone.swordfish.vfiSetup.Welcome.MainActivity

    # Select environment
    click button  QA
    wait until page contains  button_welcome_continue
    click element  button_welcome_continue
    sleep  6

    #set wifi network connection
    click text  SprintHotspot_D49 [WPA2]
    click element  com.verifone.swordfish.vfiSetup:id/text_password
    input password  com.verifone.swordfish.vfiSetup:id/text_password  ${PASSWORD_1}
    sleep  6
    press keycode  66
    sleep  5
    HIDE KEYBOARD
    #click element  com.verifone.swordfish.vfiSetup:id/imageButtonContinue
    sleep  3
    click element  imageButtonContinue
    sleep  10
    click element  com.verifone.swordfish.vfiSetup:id/imageButtonContinue
    sleep  10

   # SSO login
    wait until page contains  Email
    tap  email
    input text  email   ${EMAIL_ID}
    tap  password
    input password  password  ${PASSWORD_2}
    sleep  7
    press keycode  66
    sleep  25
    page should contain element  com.verifone.swordfish.vfiSetup:id/button_setup_finish
    click element  com.verifone.swordfish.vfiSetup:id/button_setup_finish


*** Keywords ***


