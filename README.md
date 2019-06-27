# OnlySnarf
  
`git clone git@github.com:skeetzo/onlysnarf`
OR
`pip3 install OnlySnarf`

## Preview
![preview](https://github.com/skeetzo/onlysnarf/blob/master/OnlySnarf/images/preview.jpeg)

## Scripts
First run:  
  * `(sudo) python3 setup.py install`  
Then from within project's OnlySnarf directory either:  
  * `(sudo) onlysnarf [args]`
  * `(sudo) onlysnarf-config [args]`
  * or directly via `python3 onlysnarf.py (-debug) -image|-gallery|-video`

## args

-debug  
  `python3 onlysnarf.py -debug`  
Tests configuration. Does not upload or remove from Google Drive.

-image  
  `python3 onlysnarf.py -image`  
Uploads an image labeled: 'imageName - %d%m%y'  

-gallery  
  `python3 onlysnarf.py -gallery`  
Uploads a gallery labeled: 'folderName - %d%m%y'  

-video  
  `python3 onlysnarf.py -video`  
Uploads a video labeled: 'folderName - %d%m%y'  

-text  
  `python3 onlysnarf.py -video -text "your mom"`  
Uploads a video labeled: 'your mom - %d%m%y'  

-hash(tag)  
  `python3 onlysnarf.py -hash`  
Uploads a video with the source folder split into hash tags: '#folderName'  

-force (upload)  
  `python3 onlysnarf.py -force`  
Attempts to upload limit regardless of file size. 

-show
  `python3 onlysnarf.py -show`
Shows the Chromium browser

## Description

Downloads a random file or gallery of files from a random Google Drive folder as specified by run time arguments and then uploads the image, video, or gallery to an OnlyFans account.

## Authentication  
--------------
###### from [Auth Quickstart](https://raw.githubusercontent.com/gsuitedevs/PyDrive/master/docs/quickstart.rst)
Drive API requires OAuth2.0 for authentication. *PyDrive* handles complex authentication steps that need to be personally authorized for your Drive account.

1. Go to `APIs Console`_ and make your own project.
2. Search for 'Google Drive API', select the entry, and click 'Enable'.
3. Select 'Credentials' from the left menu, click 'Create Credentials', select 'OAuth client ID'.
4. Now, the product name and consent screen need to be set -> click 'Configure consent screen' and follow the instructions. Once finished:

 a. Select 'Application type' to be *Web application*.
 b. Enter an appropriate name.
 c. Input *http://localhost:8080* for 'Authorized JavaScript origins'.
 d. Input *http://localhost:8080/* for 'Authorized redirect URIs'.
 e. Click 'Create'.

5. Click 'Download JSON' on the right side of Client ID to download **client_secret_<really long ID>.json**.

The downloaded file has all authentication information of your application.
**Rename the file to "client_secrets.json" and place it in the OnlySnarf folder.**

## Config
##### config.json  
Create or update the "config.json" file with the following values:
  * username -> the Twitter connected to your OnlyFans's username  
  * password -> the Twitter conencted to your OnlyFans's password  

###### Why Twitter credentials?
OnlyFans uses a captcha to prevent malicious bots from accessing user accounts. However, this captcha is only necessary when logging in with your OnlyFans username and password. Logging in with the provided Twitter authentication does not provide a captcha and thus allows an easier automated entry.

##### google_creds.txt   
Generated by Google Drive's authentication process. Saves Google authentication for repeat access.

##### settings.yaml  
Used to facilitate Google Drive's python authentication. Requires generating an app w/ credentials via Google Console. Credentials are authenticated once and then saved to "google_creds.txt".

## Example Crons  

Upload an image once a day at noon:  
  `* 12 * * * python3 onlysnarf.py -image`

Upload a gallery of images every Wednesday at 2:30pm:  
  `30 14 * * 3 python3 onlysnarf.py -gallery`

Upload a random video every Friday in the month of June at 6:00pm:  
  `00 18 * 6 5 python3 onlysnarf.py -video`

Text will be generated if not provided with `-text`
  `* 12 * * * python3 onlysnarf.py -image -text "Your mother is a dirty whore"`

## Dependencies
  * Chromium / Google Chrome -> `sudo apt install -y chromium-browser`
  * Chromedriver: binary installed via chromedriver-binary
