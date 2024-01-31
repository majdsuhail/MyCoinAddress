# MyCoinAddress

MyCoinAddress is a user-friendly web app designed to simplify the sharing of crypto coin addresses. Users can input essential information such as the coin's name, coin's address (required fields), and additional details like Display name, Network, Memo, and Description (optional fields). After filling in the necessary information, users are provided with a unique link that directs them to a page displaying all the provided details, along with a QR code for the coin's address. This project utilizes a MySQL database and incorporates Bootstrap for an interactive and visually appealing user interface.

## Usage

1. Visit [MyCoinAddress](https://maegox.pythonanywhere.com/).
2. Fill in the required fields (coin's name, coin's address) and optional fields (Display name, Network, Memo, Description).
3. Provide a password for future link deletion.
4. Submit the form to generate your unique link and QR code.
5. Use the link to access and share your crypto coin details.

## Delete Link

To delete your link and associated information, visit the [Delete Page](https://maegox.pythonanywhere.com/delete). Enter the coin's address and the password you provided during link creation. Your link will be deleted.

## Requirements

- Flask
- Requests
- mysql.connector
- Datetime
- Gunicorn
- Streamlit
- QRCode

## Deployment

The app is deployed using [PythonAnywhere](https://www.pythonanywhere.com/). Access the live app at [MyCoinAddress](https://maegox.pythonanywhere.com/).

## Installation

To run the app locally, make sure you have the required dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.
