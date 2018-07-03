*** Settings ***
Library  AppiumLibrary




*** Keywords ***

Save Register Settings
    #wait until page contains  Rama _ Do_Not_Use  10
    sleep  10
    #CLICK TEXT  Rama _ Do_Not_Use
    CLICK TEXT  Kash4
    CLICK TEXT  Save
    Sleep  10
    wait until page contains element  txt_orders
    click button  Register Settings
    tap  com.vantiv.pos:id/terminal_description
    click text  Verifone Carbon
    sleep  6
    click element  terminal_test_button
    tap  android:id/content
    click element  btn_cancel
    #tap  com.vantiv.pos:id/printer_description
    #click text  Verifone Carbon
    click element  com.vantiv.pos:id/printer_test
    #click button  printer_test
    click element  btn_cancel
    click element  com.vantiv.pos:id/container_right
    sleep  8


Select payment method (CC)
    CLICK TEXT  Credit Card
    click element  btn_enter
    Sleep  6