# biz-stocktracker
**NEW UPDATE - 1.1: PATCH NOTES-------------------------------------------------------------------------**

Right now, the program just is easier to set up if you use python 3.8 (I run it with 3.8.6).
- Patched an issue where the stock numbers were only updating whenever the last thread would hit post limit and when the successor thread would hit post limit as well.
- There is an issue with the sorting algorithm that I am using, so after the first couple runs the most talked about stock tickers might not be at the top of the list, but the correct number of times mentioned is still printed despite the ordering in the output table. (will be addressed soon)

**BASIC DOWNLOAD INSTRUCTIONS-------------------------------------------------------------------------**

download python 3.8.6 from python.org as an altinstall if you are using linux so it doesn't mess up your entire OS

python3.8 -m pip install pandas BASC-py4chan

git clone https://github.com/carsonbring/biz-stocktracker

navigate to the folder and then run

python3.8 main.py

EASY AS PIE!

**INFORMATION ABOUT THE PROGRAM-------------------------------------------------------------------------**



What stock tickers are mentioned on /biz/'s Stock Market General? Use this program to find out which stocks to avoid at all costs

This program gets all of the messages from the current Stock Market General thread on /biz/ and updates with new tickers
whenever a thread hits post limit. If you are just curious as to what tickers are being talked about the most at a
moment in time, just run the program and stop it, otherwise it will continue to update if you just leave it on.

Had to make a couple of edits to the basc_py4chan library (what I used to get the message and thread info from /biz/) to
get it working with Python 3.9, so I've included the updated file that would need to be replaced after pip installing
py4chan.

You can use this program for whatever I don't care. 

Thank you to the guys who made py4chan since now I don't have to use a html parser which is a lot slower. 

Organization might not be perfect. I'll try to make up for it with comments



Pip install pandas and BASC-py4chan for the program to work

After pip installing both, run the program and there will be an error saying that the util.py file from the BAC-py4chan will not work if you are not using python 3.8
if this happens to you, find the folder labeled "py4chan util replacement' and copy paste the new code into util.py.
