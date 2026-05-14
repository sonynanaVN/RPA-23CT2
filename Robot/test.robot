*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections

*** Variables ***
${EMAIL}        rokhananana98@gmail.com
${PASSWORD}     zdvctubzkhivpetz
${LOGIN_EMAIL}  ngovan15121977@gmail.com
${LOGIN_PASS}   0702749422Ads!
${URL}          https://www.automationexercise.com

*** Test Cases ***
Automation Exercise - Mua San Pham Re Nhat
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    # 1. Đăng nhập
    Click Link    Signup / Login
    Wait Until Element Is Visible    css:input[data-qa='login-email']
    Input Text    css:input[data-qa='login-email']    ${LOGIN_EMAIL}
    Input Text    css:input[data-qa='login-password']    ${LOGIN_PASS}
    Click Button    css:button[data-qa='login-button']
    Sleep    3s

    # 2. Vào trang Products
    Click Element    xpath://a[@href='/products']

    # 3. Tìm kiếm shirt
    Wait Until Element Is Visible    id:search_product
    Input Text    id:search_product    shirt
    Click Button    id:submit_search
    Sleep    2s

    # 4. Tìm sản phẩm rẻ nhất rồi thêm vào giỏ
    ${best_index}=    Find Cheapest Product
    Add Product To Cart    ${best_index}
    Sleep    2s

    # 5. Vào giỏ hàng
    Click Link    View Cart
    Sleep    2s

    # 6. Kiểm tra số lượng
    ${qty}=    Get Text    class:disabled
    Should Be Equal    ${qty}    1

    # 7. Checkout
    Click Element    class:check_out
    Click Link    Place Order

    # 8. Điền thông tin thẻ
    Wait Until Element Is Visible    name:name_on_card
    Input Text    name:name_on_card      Test User
    Input Text    name:card_number       4111111111111111
    Input Text    name:cvc               123
    Input Text    name:expiry_month      12
    Input Text    name:expiry_year       2030
    Click Button    id:submit
    Sleep    2s

    # 9. Lấy kết quả và gửi email
    ${result}=    Get Text    tag:h2
    Log To Console    Order Result: ${result}
    Send Result Email    ${result}

    Close Browser

*** Keywords ***
Find Cheapest Product
    [Documentation]    Trả về index sản phẩm rẻ nhất
    ${products}=    Get WebElements    class:product-image-wrapper
    ${min_price}=   Set Variable    ${999999999}
    ${best_index}=  Set Variable    ${0}
    ${index}=       Set Variable    ${0}
    FOR    ${product}    IN    @{products}
        ${text}=    Get Text    ${product}
        ${has_price}=    Run Keyword And Return Status    Should Contain    ${text}    Rs.
        IF    ${has_price}
            ${after_rs}=     Fetch From Right    ${text}    Rs.
            ${price_str}=    Get Substring    ${after_rs}    0    6
            ${price_str}=    Strip String    ${price_str}
            ${parts}=        Split String    ${price_str}
            ${price}=        Convert To Integer    ${parts}[0]
            IF    ${price} < ${min_price}
                ${min_price}=    Set Variable    ${price}
                ${best_index}=   Set Variable    ${index}
            END
        END
        ${index}=    Evaluate    ${index} + 1
    END
    Log To Console    San pham re nhat: index=${best_index}, gia=Rs.${min_price}
    RETURN    ${best_index}

Add Product To Cart
    [Arguments]    ${index}
    ${products}=    Get WebElements    class:product-image-wrapper
    Mouse Over    ${products}[${index}]
    Sleep    0.5s
    ${btns}=    Get WebElements    xpath://a[contains(@class,'add-to-cart')]
    Click Element    ${btns}[${index}]

Send Result Email
    [Arguments]    ${result_text}
    Evaluate
    ...    __import__('smtplib').SMTP_SSL('smtp.gmail.com',465).__enter__().login('${EMAIL}','${PASSWORD}') or True
    ${code}=    Set Variable
    ...    import smtplib; from email.mime.text import MIMEText; msg=MIMEText("${result_text}"); msg['Subject']='AutomationExercise Result'; msg['From']='${EMAIL}'; msg['To']='${EMAIL}'; s=smtplib.SMTP_SSL('smtp.gmail.com',465); s.login('${EMAIL}','${PASSWORD}'); s.send_message(msg); s.quit()
    Evaluate    exec("""${code}""")    modules=smtplib,email.mime.text