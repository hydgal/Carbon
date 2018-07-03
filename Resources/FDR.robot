*** Settings ***
Library  AppiumLibrary


*** Keywords ***

Launch Settings application
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.7.46   	deviceName=270383310050  appPackage=com.android.settings  appActivity=com.android.settings.Settings


Click Backup & reset option
    click text  Backup & reset
    click text  Factory data reset
    click button  Reset tablet
    #select window  com.verifone.swordfish.ssologin:id/container_login


Authenticate user with SSO credentials
    tap  com.verifone.swordfish.ssologin:id/email
    input text  com.verifone.swordfish.ssologin:id/email   louis14@getnada.com
    #tap  com.verifone.swordfish.ssologin:id/password
    input password  com.verifone.swordfish.ssologin:id/password  Veri1234
    press keycode  66
    sleep  10
    #wait until element is visible  com.android.settings:id/execute_master_clear 20


Confirm reset
    click element  com.android.settings:id/execute_master_clear