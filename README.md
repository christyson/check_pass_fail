# Veracode Check Pass Fail

A simple example script to check pass/fail status of a Veracode app profile (or sandbox) 
or for a list of app profiles with out sandboxes.

## Setup

Clone this repository:

    git clone https://github.com/christyson/check_pass_fail

Install dependencies:

    cd check_pass_fail
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## usage for a single app profile or and app profile with a sandbox

usage: check_pass_fail.py [-h] -a APP [-s SANDBOX] 

Note: at a minimum APP is required.  

## Run

If you have saved credentials as above you can run:

    python check_pass_fail.py -a <your app name>
    or
    python check_pass_fail.py -a <your app name> -s <your sandbox name>

Otherwise you will need to set environment variables before running `example.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python check_pass_fail.py -a <your app name>
    or
    python check_pass_fail.py -a <your app name> -s <your sandbox name>
	
## usage for a list of apps

usage: check_pass_fail_app_only.py [-h] -a APP

Note: at a minimum at least one APP is required.  

## Run

If you have saved credentials as above you can run:

    python check_pass_fail_app_only.py -a <your app name>
    or
    python check_pass_fail_app_only.py -a <your app name> -a <your second app name> -a <your third app name> ...

Otherwise you will need to set environment variables before running `example.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python check_pass_fail.py -a <your app name>
    or
    python check_pass_fail_app_only.py -a <your app name> -a <your second app name> -a <your third app name> ...
