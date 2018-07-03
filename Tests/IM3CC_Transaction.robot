*** Settings ***
Documentation  This script is for Devcie Setup using Ethernet network (Skip wifi)
Library  AppiumLibrary
Library  AppiumLibrary
Resource  ../Resources/IM3_Login_AddItems.robot
Resource  ../Resources/IM3_CC.robot
Resource  ../Resources/ConnectRobot.robot




*** Variables ***


*** Test Cases ***
IM3 login, credit Transaction/s and Print receipt
    [Documentation]  This test case will log into IM3 demo app with credentials and do a credit transaction. Receipt is also printed
    [Tags]  Smoke

    IM3_Login_AddItems.Open applicaiton and login
    IM3_CC.Save Register Settings
    IM3_Login_AddItems.Add line-items
    IM3_CC.Select payment method (CC)
    ConnectRobot.do card swipe

    IM3_Login_AddItems.Print receipt

    sleep   5
    click element  com.vantiv.pos:id/btn_back
    repeat keyword  1  Add line-items
    repeat keyword  1   select payment method (cc)
    ConnectRobot.do contactless
    repeat keyword  1  print receipt


    sleep   5
    click element  com.vantiv.pos:id/btn_back
    repeat keyword  1  Add line-items
    repeat keyword  1   select payment method (cc)
    ConnectRobot.do chip insert
    repeat keyword  1  print receipt

    #IM3_Login_AddItems.Gift Card Transaction

    #IM3_Login_AddItems.Full Refund




