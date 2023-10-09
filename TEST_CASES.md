# Automated test cases

## api_test.py

    1. test_create_user
        - Create a new user
        - Get user by id
        - Verify the response is as expected

    2. test_deactivate_user
        - Create a new user
        - Update the user using patch request
        - Get user by ID
        - Verify status is 'inactive'

    3. test_delete_user
        - Create a new user
        - Delete the user with DELETE request
        - Try to get user by ID
        - Verify the response status code is 404

## ios_test.py

    1. test_user_can_open_login_page
        - Open Gorest home page in iOS Safari
        - Open burger menu
        - Click on login link
        - Check that login page has 3 login buttons
        - Verify login buttons links are: "/oauth/github", "/oauth/facebook", "/oauth/microsoft"

    2. test_base64_encode_tool
        - Open Gorest home page in iOS Safari
        - Open burger menu
        - Click on tools dropdown list
        - Click on base64 tool
        - Enter text into input: "text_to_check base64"
        - Click on encode button
        - Verify the result is "dGV4dF90b19jaGVjayBiYXNlNjQ="

    3. test_url_decode
        - Open Gorest home page in iOS Safari
        - Open burger menu
        - Click on tools dropdown list
        - Click on url encode tool
        - Enter text into input: "%7C%7C%7CM%20O%20N%20E%20S%20E%20i%20s%20c%20o%20o%20l%20a%20n%20d"%20n%20i%20c%20e%20p%20l%20a%20c%20e%20t%20o%20w%20o%20r%20k%20.%21%25"
        - Click on decode button
        - Verify the result is: "|||M O N E S E i s c o o l a n d n i c e p l a c e t o w o r k .!%"
