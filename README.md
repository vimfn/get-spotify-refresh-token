# Guide: How to get spotify refresh token

The refresh token allows you to access the Spotify API on behalf of the authenticated user without the need for manual authorization.

## Prerequisites

Before proceeding, make sure you have the following prerequisites:

- Python 3 installed on your machine.
- You **don't** need premium account to get refresh token.

## Step 1: Set up Spotify Developer Account

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account credentials.

2. Click on the Create an App button and fill in the necessary details, such as the app name and app description.

3. Once your app is created, you will be redirected to the app dashboard. Note down the **Client ID** and **Client Secret**. You will need these later.

4. In the app dashboard, click on Edit Settings and add a redirect URI. Set it to **http://localhost:8888** for this example.

5. Save the changes.

## Step 2: Set up a Python Virtual Environment (Optional but Recommended)

Setting up a virtual environment helps isolate the project dependencies and avoids conflicts with other Python projects. Follow these steps to set up a Python virtual environment:

Open a command prompt or terminal.

1. Navigate to the directory where you want to create the virtual environment.

2. Run the following command to create a new virtual environment named "spotify-env":

- For Windows:

```powershell
python -m venv spotify-env
```

- For macOS/Linux:

```bash
python3 -m venv spotify-env
```

3. Activate the virtual environment:

For Windows:

```
.\spotify-env\Scripts\activate
```

For macOS/Linux:

```bash
source spotify-env/bin/activate
```

You will see the virtual environment name (e.g., "spotify-env") in your command prompt or terminal.

## Step 3: Clone this repository

1. Clone this repository to your local machine.

```bash
git clone https://github.com/arnvgh/get-spotify-refresh-token
```

2. Navigate to the project directory.

```bash
cd get-spotify-refresh-token
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Step 4: Create a .env file

1. Create a .env file in the project directory. (either manually or by below command)

```bash
touch .env
```

2. Open the .env file and add the following lines:

```bash
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888
```

(Make sure that you have port `:8888` avaiable in your system.)

3. Replace the values of `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` with the values you noted down in Step 1.

## Step 5: Run the script

1. Run the script.

- For Windows:

```powershell
python main.py
```

- For macOS/Linux:

```bash
python3 main.py
```

2. You will be redirected to a Spotify authorization page. Click on Agree to authorize the app.

3. You will be redirected to a page that says "You can close this window now". Close the window.

4. You will see a new file named `.cache` in the project directory. This file contains your refresh token (also an access token with expiration time).

Congratulations! You have successfully stored your Spotify refresh token using Spotipy. Now you can use this token to access the Spotify API on behalf of the authenticated user.

Please note that it's important to keep the .env file containing your credentials and the .cache file secure and not share them with others.

---

If you have any further questions, feel free to ask !
