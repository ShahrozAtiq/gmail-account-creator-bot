# GAMIL ACCOUNT CREATION BOT

This Python bot uses the BrowserStack free APIs to automate the creation of Gmail accounts using Appium and Android device API provided by BrowserStack. The bot also utilizes the Google Sheets APIs to save the account credentials on a Google Sheet. It chooses a random date of birth and name from names.json for the account creation.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

The following technologies were used in the development of this bot:

- Python 
- Selenium 
- Appium 
- BrowserStack APIs 
- Google Sheets APIs

## Installation

To install the dependencies, run the following command:

```pip install -r requirements.txt```


## Usage

To run the bot, follow these steps:

1. Set up a BrowserStack account and obtain the access keys required for the API calls.

2. Set up a Google Cloud Platform account and create a project to obtain the credentials required for the Google Sheets API.

3. Clone the repository and navigate to the project directory.

4. Update the following variables:
   
   - `BROWSERSTACK_USERNAME`: Your BrowserStack username.
   - `BROWSERSTACK_ACCESS_KEY`: Your BrowserStack access key.
   - `GOOGLE_CLIENT_SECRET_FILE`: The path to your Google Sheets API client secret file.
   - `SHEET_ID`: The ID of the Google Sheet where the account credentials will be saved.
   
5. Run the following command to start the bot:

    `python main.py`

## Demo
<img src="https://raw.githubusercontent.com/ShahrozAtiq/gmail-account-creator-bot/master/demo.gif?token=GHSAT0AAAAAACB6OJRXPF5CO6MV5QQBPVJAZCOVLYA" />


## Contributing

Contributions to this project are welcome via pull requests on GitHub.

## License

This project is licensed under the [MIT License](https://github.com/<username>/<repository>/blob/main/LICENSE).
## Contact Me

<table>
  <tr>
    <td align="center"><a href="https://www.upwork.com/freelancers/~01c437b099d917194b" title="View my Upwork profile"><img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/48/null/external-upwork-a-global-freelancing-platform-where-professionals-connect-and-collaborate-remotely-logo-shadow-tal-revivo.png" alt="Upwork Icon"/></a></td>
    <td align="center"><a href="mailto:shahrozatiq@outlook.com" title="Send me an email"><img src="https://img.icons8.com/fluent/48/000000/email-open.png" alt="Email Icon"/></a></td>
    <td align="center"><a href="#" title="Join my Discord server"><img src="https://img.icons8.com/color/48/000000/discord-new-logo.png" alt="Discord Icon"/></a></td>
    <td align="center"><a href="skype:live:.cid.d443850fdc6504ea?chat" title="Chat with me on Skype"><img src="https://img.icons8.com/color/48/000000/skype--v1.png" alt="Skype Icon"/></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/shahroz-atiq-73335b270/" title="Connect with me on LinkedIn"><img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn Icon"/></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.upwork.com/freelancers/~01c437b099d917194b">View my Upwork profile</a></td>
    <td align="center"><a href="mailto:shahrozatiq@outlook.com">Send me an email</br>shahrozatiq@outlook.com</a></td>
    <td align="center"><a href="#">Chat on discord</br>shz#1259</a></td>
    <td align="center">Chat with me on Skype<a href="skype:live:.cid.d443850fdc6504ea?chat"></br>live:.cid.d443850fdc6504ea</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/shahroz-atiq-73335b270/">Connect with me on LinkedIn</a></td>
  </tr>
</table>
