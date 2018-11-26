#!/usr/bin/env bash

# Create database and table
echo "input mysql password"
mysql -u root -p < pdns.sql

# MAC OSX launchctl service
scripts=$(cd `dirname $0`; pwd)"/pdns.py"
path="/Library/LaunchDaemons/com.monitor.pdns.plist"
sudo tee $path <<< `cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
        <string>com.monitor.pdns</string>
    <key>ProgramArguments</key>
    <array>
        <string>python</string>
        <string>$scripts</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
        <string>/var/log/pdns.log</string>
    <key>StandardErrorPath</key>
        <string>/var/log/pdns_err.log</string>
</dict>
</plist>
EOF
`
sudo chown root:wheel /Library/LaunchDaemons/com.monitor.pdns.plist
sudo chmod +x /Library/LaunchDaemons/com.monitor.pdns.plist
sudo launchctl load -w /Library/LaunchDaemons/com.monitor.pdns.plist
chmod +x $scripts
sudo launchctl start com.monitor.pdns
