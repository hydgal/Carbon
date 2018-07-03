*** Settings ***
Library  AppiumLibrary

*** Keywords ***
Select payment method (cash)
    CLICK TEXT  Cash
    CLICK TEXT  Exact
    Sleep  6
    CLICK TEXT  Finish


