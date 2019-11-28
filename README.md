# anonyrai
This is Anonyrai source code.
Anonyrai is simple system to make BBS on Twitter.

# Terms of service
Everyone can use and modify Anonyrai.
Ι take no responsibility whatsoever.

# Usage
Please install
Python3.7
Apache
mod-wsgi

cp -r anonyrai/www/cgi-bin/* /var/www/cgi-bin/
cp -r anonyrai/httpd/* /etc/httpd/

Get CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET from Twitter and fill "/www/cgi-bin/mysite/anonirai/views.py".

If you want to block someone's IP, you can edit "/httpd/conf.d/deny.conf". Add last line following text.

Deny from "SOMEONE_IP"

You can use IP or Domeins.I think you should allow only your countly's domein.
