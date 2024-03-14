# A bot that replaces Rythem
This bot uses slash commands to play youtube videos and play spotify songs.
Still a WIP


## How to get a Discord token
https://discord.com/developers/applications
To get a Discord bot token, you need to create a new bot application on the Discord Developer Portal and obtain the token associated with it. Here's a step-by-step guide on how to do it:

Navigate to the Discord Developer Portal: Open your web browser and go to the Discord Developer Portal.

Log in: If you haven't already logged in, you'll need to log in with your Discord account.

Create a new application: Once logged in, click on the "New Application" button at the top-right corner of the page. Enter a name for your bot application and click "Create".

Create a bot user: After creating the application, navigate to the "Bot" tab in the left sidebar. Click on the "Add Bot" button. Confirm when prompted.

Obtain the token: Once the bot user is created, you'll see a "Token" section under the bot's username. Click on the "Copy" button to copy the bot token to your clipboard.

Use the token: Now that you have obtained your bot token, you can use it to authenticate your bot when connecting to the Discord API.




## How to get a Youtube API Key
To obtain a YouTube API key, you need to create a project in the Google Cloud Console and enable the YouTube Data API v3 for that project. Here's a step-by-step guide on how to do it:

Go to the Google Cloud Console: Open your web browser and go to the Google Cloud Console.

Create a new project: If you haven't already created a project, click on the project dropdown menu at the top of the page and then click on "New Project". Follow the prompts to create a new project.

Enable the YouTube Data API v3: Once your project is created (or if you already have a project), navigate to the "APIs & Services" > "Library" section in the left sidebar.

Search for the YouTube Data API v3: In the search bar, type "YouTube Data API v3" and select it from the search results.

Enable the API: Click on the "YouTube Data API v3" card, then click the "Enable" button.

Create credentials: After enabling the API, navigate to the "APIs & Services" > "Credentials" section in the left sidebar.

Create an API key: Click on the "Create credentials" dropdown menu and select "API key". Copy the generated API key.

Restrict the API key (optional): For security reasons, you may want to restrict the usage of your API key. You can restrict it by IP address, HTTP referrer, or by specifying which APIs it can access.

Use the API key: Now that you have obtained your API key, you can use it in your applications to access the YouTube Data API v3.


## How to get Spotipy Id and Secret
https://developer.spotify.com/dashboard
To create a Spotify client ID and secret, you need to register your application with the Spotify Developer Dashboard. Here's a step-by-step guide on how to do it:

Navigate to the Spotify Developer Dashboard: Open your web browser and go to the Spotify Developer Dashboard.

Log in or sign up: If you haven't already logged in, you'll need to log in with your Spotify account. If you don't have an account, you'll need to sign up for one.

Create a new application: Once logged in, click on the "Create an App" button. Enter a name and description for your application.

Complete the form: Fill out the required fields in the form, including the application name, description, and website (if applicable). You may also need to agree to the terms of service.

Create the application: Click on the "Create" button to create your application. Your application will be created, and you'll be redirected to the application dashboard.

Obtain the client ID and secret: In the application dashboard, you'll see your client ID and client secret. Click on the "Show Client Secret" button to reveal the client secret. Make sure to copy both the client ID and client secret and store them securely.

Set up redirect URIs (optional): If your application requires user authentication (e.g., for accessing user data), you may need to set up redirect URIs in the application settings. This allows Spotify to redirect users back to your application after they have authenticated.

Use the client ID and secret: Now that you have obtained your Spotify client ID and secret, you can use them to authenticate your application and access the Spotify API.
