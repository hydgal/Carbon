*** Settings ***
Documentation  This script is for Devcie Setup using Ethernet network (Skip wifi)
Library  AppiumLibrary
Resource  ../Resources/IM3_Login_AddItems.robot
Resource  ../Resources/IM3_Cash.robot


*** Variables ***


*** Test Cases ***
IM3 login, Cash Transaction and Print receipt
    [Documentation]  This test case will log into IM3 demo app with credentials and do a cash transaction. Receipt is also printed
    [Tags]  Smoke

    IM3_Login_AddItems.Open applicaiton and login
    IM3_Login_AddItems.Add line-items
    IM3_Cash.Select payment method (cash)
    IM3_Login_AddItems.Print receipt



