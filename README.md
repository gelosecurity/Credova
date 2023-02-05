# Credova
Credova is a script used for assisting static analysis of Cordova mobile applications (Cross-Platform, iOS & Android). It scans for hardcoded secrets, such as API keys, access tokens, and private keys, in JavaScript files.

![image](https://user-images.githubusercontent.com/49821326/216807568-5df4c320-2432-4c36-9c4e-ae9878d86fd5.png)

## Requirements
Python 3.x

`pip3 install jsbeautifier`

## Usage
Run the script in the directory containing the www subdirectory of the mobile application:

`python3 credova.py`

The script will print out the locations of any javascript files it finds, and highlight the lines containing hardcoded secrets in green. If no javascript files are found, the script will exit with an error message.

## Output
The output of the script will display the path to any javascript files containing hardcoded secrets, along with the line(s) containing the secrets. The format will be as follows:

```
[SECRETS] path/to/file.js
- line containing secret
```

## Limitations
The script only searches for hardcoded secrets in javascript files, and will not detect secrets stored in other file formats or obfuscated in the code. Additionally, the script only searches for a predefined list of secrets, so it may not detect all potential secrets in the application.
