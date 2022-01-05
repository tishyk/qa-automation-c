# qa-automation-c

1. install python, create venv
2. run venv, install requirements.txt
3. run install_drivers.py

If you wont  test  run locally change in
tests/plugins/browser.py
```local = True```

You also must upload or create secret.json to project folder
        
    {"amazon":
          {"username": "username",
          "password": "password",
          "access_kid":"amazon access key id",
          "secret_acc_key": "amazon secret access key",
          "console_login": "https://link4console.aws.amazon.com/console",
          "arn": "arn:aws:devicefarm:copy&your&oun"
          },
        "google": {
          "login": "test@gmail.com",
          "password": "password"
          }
        }

For run all test just type

```$> pytest```

Bug in GitHub Issue