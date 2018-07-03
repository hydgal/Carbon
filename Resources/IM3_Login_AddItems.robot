*** Settings ***
Library  AppiumLibrary

*** Variables ***
${ACCOUNT_ID} =  101470
${USERNAME} =  retail
${PASSWORD} =  Verifone@1234

*** Keywords ***
Open applicaiton and login
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.7.46   	deviceName=282898160094  appPackage=com.vantiv.pos  appActivity=com.imobile3.pos.ui.activity.AppDesignationActivity
    Tap  account_id
    input text  account_id  ${Account_ID}
    Tap  username
    input text  username  ${USERNAME}
    Tap  password
    input password  password  ${PASSWORD}
    CLICK TEXT  Log In


Add line-items
    #wait until page contains  Rama _ Do_Not_Use  10
    #CLICK TEXT  Rama _ Do_Not_Use
    #CLICK TEXT  Save
    Sleep  10
    wait until page contains element  txt_orders
    CLICK TEXT  Orders
    CLICK TEXT  Baked Goods
    CLICK TEXT  Cheese Cake Slice
    sleep  5
    TAP  current_btn_checkout
    sleep  4


Print receipt
    sleep  25
    CLICK TEXT  Print
    sleep   5
    click element  com.vantiv.pos:id/btn_done

Gift Card Transaction
    sleep   5
    click element  com.vantiv.pos:id/btn_back
    CLICK TEXT  Orders
    click text  Manual Entry
    click element  com.vantiv.pos:id/number_pad_btn_0
    click element  com.vantiv.pos:id/number_pad_btn_5
    click element  com.vantiv.pos:id/number_pad_btn_0
    click element  com.vantiv.pos:id/number_pad_btn_enter
    click element  com.vantiv.pos:id/current_btn_checkout
    click text  Gift Card

Full Refund
    sleep   5
    #click element  com.vantiv.pos:id/btn_back
    CLICK TEXT  Orders
    click text  Completed
    click text  Retail v.
    sleep   3
    click element  com.vantiv.pos:id/completed_btn_refund_full


