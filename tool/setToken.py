from selenium import webdriver
from time import sleep


def setToken():
    """
    设置localStorage中的token值
    :return:
    """
    driver = webdriver.Chrome()
    driver.get("https://hxgl.huxin315.com/merHome")
    sleep(2)
    #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2OTM0NDQ2NDUsInVzZXJJZCI6IkowKzN1MU1peGl0UXlkNGxwakxpY2duT3VCZnUrVE1LaktiWWFFT3BGYnBFUCtlekZMK3dlb3RHUEUzRFdJMU1sZDNYT1o4MGxhWGV5bjVsVWVLeTFyRFZJU2kwM2djZmZBREp0M3VGYnMxZGY1aldEUzg4SWthZFByY0h2UkRKYWNDd0FZVzVRdmh6bGxCanVZQUluTWo4dS9QbTNTY1hic05EK1RTZTh2dz0iLCJpYXQiOjE2MDcxMzEwNDV9.UQYpxgpdJ6Os2fWD339e1_w84QM6_9s_rTZ8Zsz6b-MCKn_joI52X288wqb6sBl8Go8V8xGxTww92-9KyHlIx53PLAGHo-qdwDzIRKcFmaOiLjyyroMm3tt79Eulz7W-W0CRjK-0bmXfQloq53d5gilQOao6TptOz-vpHtUObRUL69AJ3F9rOfCT5aTFcB7Ve2N9YITbxBOQuHNAlY2Rubw3BxwL74FXYZ5e1zewP8SGGZx-AUa-ocoCFJUsQ3UqN_J6NuZpefJtte5p4W-C0le6EIZB93rox8IhwxknC6-krpsQmCa6VgXIIQJrSDqBMIPz6raKHZe2tlcVAfiUsg"
    token ="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2OTM0NDcyODYsInVzZXJJZCI6IkhuL3J3U01CUVRMc0cwZG1TdWJQaGVnejJJYis5TlQvckJscEN2YXJZbjdYQVFEOTZ4ZUY1dU9CVW5XRFRGOTY0NllVU0xQdnhPVThkRHlvZ2Q3aklkdTdwTlhGZTA0OHNLdjhHb3o0c3J6SU1UaGIwUlJCRDJZQ01kS3hOcDJDOUltRTFLVVZBUGxubFBMSVdJNmdNRC84VGNJZDBZZVc3dG82MjRjZDZhTT0iLCJpYXQiOjE2MDcxMzM2ODZ9.AMkgjR8Y_znaE12K0GE8bt5VBrqG_-wEu7z6Da_rq3YymGd29_BMo4pT7ZoWhlwS0nUTOEJycOGZzQ-5lCe3m6pI6Rrp_9Zkv1ni2ONwnpG7hWGB9nzHAik64Jzsev8QFia6lw_RY8yfM82pbs15ELcJJOSwuPhrxLQktLLsmiOiJ68ttKqaKJzsglGFrl04x55VKKkABA8KgeOK3Boiot1ZN0G4snSm140JIfImmqwKpt5THc9FmjcRQ7e-NOW_zo4qq9LRzSAlvl0-x0dwIwt8YhTjeLu5832dG0q3YRXdPhgSogk4gGVwsiYULcPmwwB6sIss7lZ0B3V6mXRFxw"
    js = 'window.localStorage.setItem("jwtToken",arguments[0])'
    driver.execute_script(js,token)

    js = "window.open('https://hxgl.huxin315.com/merHome')"
    driver.execute_script(js)
    sleep(5)
    driver.quit()


if __name__ == '__main__':
    setToken()
