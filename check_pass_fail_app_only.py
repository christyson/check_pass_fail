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
    parser.add_argument('-a', '--app', action='append', help='App name(s) to check',required=True)
    args = parser.parse_args()

    data = VeracodeAPI().get_app_list()
    results = etree.fromstring(data)
    for _, value in parser.parse_args()._get_kwargs():
       if value is not None:
          for name in value:
             found = False
             for app in results:
                if (app.attrib["app_name"] == name):
                   found = True
                   build_info = VeracodeAPI().get_build_info(app.attrib["app_id"])
                   info=etree.fromstring(build_info)
                   for child in info :
                      time=parse(child.attrib["policy_updated_date"])
                      print("App: "+name +" build: "+child.attrib["build_id"]+ " on: " +str(time.date()) +" at: " +str(time.time())+" policy compliance is: " + child.attrib["policy_compliance_status"])
             if (not found):
                print ('App: '+name+' does not exist')
    exit(0)

if __name__ == '__main__':
    main()
