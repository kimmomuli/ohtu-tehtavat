*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  seppo
    Set Password  Password123
    Set Password2  Password123
    Submit Credentials
    Register Should Succeed

    
Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  Password123
    Set Password2  Password123
    Submit Credentials
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  seppo
    Set Password  Pas123
    Set Password2  Pas123
    Submit Credentials
    Register Should Fail With Message  Too short password

Register With Nonmatching Password And Password Confirmation
    Set Username  paavo
    Set Password  Password123
    Set Password2  Password321
    Submit Credentials
    Register Should Fail With Message  Passwords are not same

Login After Successful Registration
    Set Username  anni
    Set Password  Password123
    Set Password2  Password123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  anni
    Set Password  Password123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  p
    Set Password  Password123
    Set Password2  Password123
    Submit Credentials
    Register Should Fail With Message  Too short username
    Go To Login Page
    Set Username  p
    Set Password  Password123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password2
    [Arguments]  ${password2}
    Input Password  password_confirmation  ${password2}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
