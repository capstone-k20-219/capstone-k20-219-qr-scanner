# QR code scanner

This is a simple program to simulate a QR code scanner, which is used as an alternative for the traditional parking card in our project.

Please follow these steps to run this program on your local machine:

- **Step 1:** Clone this repository to your local machine.
- **Step 2:** Create a python virtual environment with `<virtual_env_name>\Scripts\activate`.
- **Step 3:** Activate the virtual environment `python -m venv <virtual_env_name>`.
- **Step 4:** Install the packages using this command `pip install -r requirements.txt`.
- **Step 5:** Change .env.example file to .env.
- **Step 6:** Add the Firebase real-time database URL to the .env file. You can find this URL in your Firebase real-time database.
- **Step 7:** Add your credentials.json file to the repository. You can find this file in your Firebase project settings.
- **Step 8:** Run the command `[python | python3 | py] main.py` to execute the program.

**Note:** If you haven't had a Firebase real-time database, please create one in advance like the following:

```
"scanData": {
  plateNumberIn: string type
  plateNumberOut: string type
  qrCode: string type
}
```
