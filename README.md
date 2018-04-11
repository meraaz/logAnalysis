## News Log Analysis System

### Overview

> This Project is about analyzing the newspaper logs and get reports about it .
You can know the most viewed articles and the top popular authors and so on .

### Prerequisites
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* [Python3](https://www.python.org/)
* install psycopg2

  `$ pip3 install psycopg2`

### Install the Project

* Install VirtualBox and Vagrant
* Clone or Download the configuration file from [FSND-VM](https://github.com/udacity/fullstack-nanodegree-vm) repository
* Download the Database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Extract the file you've downloaded , then copy the newsdata.sql file into vagrant folder

### Launching the VM
* Install the vagrant VM after change directory to the directory you have cloned from FSND-VM repo

  `$ vagrant up `
* After installing vagrant virtual machine successfully , you need to log into it
  `$ vagrant ssh `
* Change directory to `$ cd /vagrant ` , this is the directory shared between the vagrant VM and your host machine

### Setting up the DB

* Load the Database from your sql file

  `$ psql -d news -f newsdata.sql`
* DB contains 3 tabels

  1 - `authors` , which includes information about authors and their names
  2 -  `articles` , which includes the articles themselves and which author write each article
  3 - `log` , which keeps tracking for articles views and if it successfully opened or failed
* Now you can connect to the DB by

  `$ psql news`

#### Running the Project
- After downloading this repo into `/vagrant` directory
- change directory into it `$ cd logAnalysis`
- then use Python3 to run log.py file

  `python3 log.py`
- check the *results.txt* file to results examples 
