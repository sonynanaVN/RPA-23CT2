*** Settings ***
Library           SeleniumLibrary

Suite Setup       Open Browser    ${URL}    chrome
Suite Teardown    Close Browser

*** Variables ***
${URL}            https://the-internet.herokuapp.com/login
${USERNAME}       tomsmith
${PASSWORD}       SuperSecretPassword!
${TITLE}          The Internet

*** Test Cases ***

TC01 - Kiem tra title trang Login
    [Documentation]    Kiểm tra title của website
    Title Should Be    ${TITLE}

TC02 - Dang nhap thanh cong
    [Documentation]    Đăng nhập với tài khoản hợp lệ và kiểm tra đăng nhập thành công
    Go To             ${URL}
    Input Text        id=username    ${USERNAME}
    Input Text        id=password    ${PASSWORD}
    Click Button      css=button[type='submit']
    Page Should Contain    You logged into a secure area!
    # Open Browser    ${URL}    chrome
    # Log  Opened Browser Successfully
    # Sleep  4s
    # Input Text    id=username    ${USERNAME}
    # Input Text    id=password    ${PASSWORD}

TC03 - Dang nhap that bai voi username sai
    [Documentation]    Đăng nhập với tài khoản không hợp lệ và kiểm tra thông báo lỗi
    Go To             ${URL}
    Input Text        id=username    invaliduser
    Input Text        id=password    wrongpassword
    Click Button      css=button[type='submit']
    Wait Until Page Contains    Your username is invalid!    timeout=10s
