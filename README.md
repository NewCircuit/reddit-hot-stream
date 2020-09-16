# Reddit hot stream

This script posts every post in hot that gets above 15k upvotes in a discord channel, it saves the post in memory for 24 hours to prevent dupes and then removes it. 

## How to run

Clone the repo
```sh
git clone https://github.com/Floor-Gang/reddit-hot-stream.git
```
Install the requirements
```sh
python3 -m pip -r install requirements.txt
```
Create conf.ini from existing template
```sh
cp conf.example.ini conf.ini
```
Edit conf.ini with the correct info
```sh
vim/nano conf.ini
```
Run the script
```sh
nohup python3 main.py &
```

