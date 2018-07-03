*** Settings ***
Documentation  This script is for Devcie Setup using Ethernet network (Skip wifi)
Library  AppiumLibrary
Resource  ../Resources/FDR.robot

*** Variables ***


*** Test Cases ***
Factory data reset test case
    [Documentation]  Factory data reset deletes user-data and sets device in Setup mode
    [Tags]  Smoke

    Launch Settings application
    Click Backup & reset option
    Authenticate user with SSO credentials
    Confirm reset



