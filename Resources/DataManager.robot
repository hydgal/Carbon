*** Settings ***
Documentation  This file will read data from external csv file
Library  ../Libraries/csv.py


*** Keywords ***
Get CSV Data
    [Arguments]  ${FilePath}
    ${Data} =  read csv file  ${FilePath}
    [Return]  ${Data}