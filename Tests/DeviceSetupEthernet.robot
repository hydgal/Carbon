*** Settings ***
Documentation  This script is for Devcie Setup using Ethernet network (Skip wifi)
Library  AppiumLibrary
Resource  ../Resources/SetupEthernet.robot

*** Variables ***


*** Test Cases ***
Device Setup with Ethernet (Skip wifi)
    [Documentation]  Ethernet setup
    [Tags]  Smoke

    Launch Setup application
    Select environment (QA)
    Select ethernet as network
    SSO login
    Test print receipt
    Finish setup



