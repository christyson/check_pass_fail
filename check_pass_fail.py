import sys
import requests
import argparse
from lxml import etree
import datetime as dt
from dateutil.parser import parse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py import VeracodeAPI
api_target = "https://analysiscenter.veracode.com/api/5.0/deletebuild.do"
headers = {"User-Agent": "Python HMAC Example"}

def main():

    parser = argparse.ArgumentParser(
        description='This script checks to see if an app is currently building a policy scan and returns 0 if not and 1 otherwise or if the --delete flag is set it will delete that build if you have permissions and return a 0 if the build is deleted and 1 if the build is not deleted. Note: Sandbox is optional')
    parser.add_argument('-a', '--app', help='App name to check',required=True)
    parser.add_argument('-s', '--sandbox', default="", help='Sandbox name to check',required=False)
    args = parser.parse_args()

    data = VeracodeAPI().get_app_list()
    results = etree.fromstring(data)
    found = False
    for app in results:
        if (app.attrib["app_name"] == args.app) and (args.sandbox == ""):
           found = True
           build_info = VeracodeAPI().get_build_info(app.attrib["app_id"])
           info=etree.fromstring(build_info)
           for child in info :
             time=parse(child.attrib["policy_updated_date"])
             print("App: "+args.app +" build: "+child.attrib["build_id"]+ " on: " +str(time.date()) +" at: " +str(time.time())+" policy compliance is: " + child.attrib["policy_compliance_status"])
           exit(0)
        if (app.attrib["app_name"] == args.app) and (args.sandbox != ""):
           sandbox_list=VeracodeAPI().get_sandbox_list(app.attrib["app_id"])
           sandboxes = etree.fromstring(sandbox_list)
           for sandbox in sandboxes:
              if sandbox.attrib["sandbox_name"] == args.sandbox:
                 found = True
                 build_info = VeracodeAPI().get_build_info(app.attrib["app_id"],"0",sandbox.attrib["sandbox_id"])
                 info=etree.fromstring(build_info)
                 for child in info :
                    time=parse(child.attrib["launch_date"])
                    print("App: "+args.app +"Sandbox: "+args.sandbox +" build: "+child.attrib["build_id"]+ " on: " +str(time.date()) +" at: " +str(time.time())+" policy compliance is: " + child.attrib["policy_compliance_status"])
                    exit(0)
                 print ('No completed scans in sandbox: '+args.sandbox+' of app: '+args.app)
                 exit(0)
    if (not found) and (args.sandbox == ""):
       print ('App: '+args.app+' does not exist')
    elif (not found) and (args.sandbox != ""):
       print ('App: '+args.app+' with sandbox: '+args.sandbox+' does not exist')
    exit(0)

if __name__ == '__main__':
    main()
