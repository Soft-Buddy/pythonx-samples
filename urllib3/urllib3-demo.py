import urllib.request

url = 'https://www.google.com'

try:
    # Making a GET request
    response = urllib.request.urlopen(url)

    # Retrieve and print headers
    headers = response.info()
    print("Headers:")
    print(headers)

    # Retrieve and print response code
    response_code = response.getcode()
    print("\nResponse Code:", response_code)

    # Retrieve and print response message
    response_message = response.msg
    print("\nResponse Message:", response_message)

    # Reading and printing the response text
    response_text = response.read().decode('utf-8')
    print("\nResponse Text:")
    print(response_text)

except urllib.error.URLError as e:
    print("Error:", e)
except urllib.error.HTTPError as e:
    print("HTTP Error:", e)
