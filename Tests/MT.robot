*** Settings ***
Library  AppiumLibrary
Resource  ../Resources/ConnectRobot.robot


*** Variables ***


*** Test Cases ***
MT transactions
    [Documentation]  Transactions and print receipt
    [Tags]  Smoke
    OPEN APPLICATION  http://localhost:4723/wd/hub  platformName=Android  platformVersion=2.7.46   	deviceName=282898160094  appPackage=com.verifone.swordfish.manualtransaction  appActivity=com.verifone.swordfish.manualtransaction.gui.StartActivity

    # Cash transaction
    #click text  New Order
   sleep  10
    #click element  com.verifone.swordfish.manualtransaction:id/button5
    #click element  com.verifone.swordfish.manualtransaction:id/button00
    #click element  com.verifone.swordfish.manualtransaction:id/btn_add
    #click element  com.verifone.swordfish.manualtransaction:id/btn_right
    #click element  com.verifone.swordfish.manualtransaction:id/cashButton
    #click element  com.verifone.swordfish.manualtransaction:id/button5
    #click element  com.verifone.swordfish.manualtransaction:id/button00
    #click text  Tender
    #sleep   10
    #ConnectRobot.connect to robot
    #click element  com.verifone.swordfish.manualtransaction:id/end


    # Credit card transaction
    click text  New Order
    sleep  5
    click element  com.verifone.swordfish.manualtransaction:id/button5
    click element  com.verifone.swordfish.manualtransaction:id/button00
    click element  com.verifone.swordfish.manualtransaction:id/btn_add
    click element  com.verifone.swordfish.manualtransaction:id/btn_right
    click element  com.verifone.swordfish.manualtransaction:id/chargeCreditButton
    sleep   10

    ConnectRobot.connect to robot

    #click element  com.verifone.swordfish.manualtransaction:id/print
    sleep   20
    click element  com.verifone.swordfish.manualtransaction:id/end
    sleep   5


    #Refund
    #click element  com.verifone.swordfish.manualtransaction:id/history
    #click element  com.verifone.swordfish.manualtransaction:id/historyRefundButton
    #click element  android:id/buttonPanel
    #click element  android:id/button1

    #Void
    #click element   com.verifone.swordfish.manualtransaction:id/history
    #click text  Void
    #click element  android:id/buttonPanel
    #click element  android:id/button1







