# backup

**backup.py - backup running-config on multiple devices listed in a JSON file**

_James Sanders ' <ciscoguru72' *at* 'yahoo' *dot* 'com' *dot 'au'_

A python script to backup running-config on multiple Cisco devices that are listed in a JSON file. JSON file must have the following key:value pair - “name” for hostname and “ip” for ip address. The script read each of these and perform the backup. The result displays if a backup was successful. Other JSON key:value pair are ignored. Please see my "csv_json_convert" script to create a JSON file from CSV Spreadsheet. 

Please Note, I have not error proofed this script.

I’m a network engineer who enjoys writing Python scripts to make life easy for myself and others. As a Python newbie, I’m always learning to improve my code. Therefore, I’m keen to hear your thoughts on my code and how I should improve. Also, I’m eager to hear new ideas and meet likewise people who write network-related Python scripts.

## Why?

Before doing a change, I always back up the running-config on devices I’m working on. We have multiple tools such or Solarwinds and Ansible doing daily backups, but I still prefer a copy while doing a change. So I created this script to quickly backup multiple devices listed in JSON file.


## Userguide

**./backup.py _[JSON file]_**

or 

**python3 backup.py _[JSON file]_**

The script will read a JSON file and using its data to backup multiple devices. For example:

**JSON file format**

JSON file must include these two key:value pair to make this script work, and they are "name" and "ip". Other key:value pairs are ignored. Here's an example JSON file:

![JSON Format](https://github.com/Sandworks/backup/blob/cc8e659c35e0e1155892629a0bcc9b814686e90f/json_format.png)

Using this json file, we can run the script as shown:

./backup.py device_list.json

Here an example output from this script:

**/backup# python backup.py device_list.json**

**Username: admin**

**password:**

**Successfully backed up:  SWI01**

**Successfully backed up:  SWI02**

**Successfully backed up:  SWI03**

**Task Completed.**

## Additional Notes:

You can change the backup directory, but changing this variable - BACKUP_DIR

Enjoy!

James.
