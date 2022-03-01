*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kalle  validPassword1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  validPassword1
    Input New Command
    Input Credentials  kalle  validPassword123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  k  validPassword1
    Output Should Contain  Too short username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  k
    Output Should Contain  Too short password 

Register With Valid Username And Long Enough Password Cointaining Only Letters
    Input New Command
    Input Credentials  kalle  passwordpassword
    Output Should Contain  Password must contain special characters