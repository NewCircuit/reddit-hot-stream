import praw
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from configparser import ConfigParser

conf = ConfigParser()
conf.read('conf.ini')

reddit = praw.Reddit(client_id=conf.get('reddit', 'client_id'),
                     client_secret=conf.get('reddit', 'client_secret'),
                     username=conf.get('reddit', 'username'),
                     password=conf.get('reddit', 'password'),
                     user_agent=conf.get('reddit', 'user_agent'))

posts = {}


def main():
    for submission in reddit.subreddit("pewdiepiesubmissions").hot():
        if not submission.over_18 and (submission.score >= 15000):
            if submission.id not in posts:
                webhook = DiscordWebhook(url=conf.get('discord', 'webhook_url'))
                embed = DiscordEmbed(color=0xf9013f)
                embed.add_embed_field(name=submission.title, value=f'[link](https://reddit.com{submission.permalink})')
                embed.set_author(name=submission.author.name, url='https://reddit.com/user/' + submission.author.name,
                                 icon_url=submission.author.icon_img)
                embed.set_image(url=submission.url)
                embed.set_footer(text=f'👍 {submission.score} | 💬 {submission.num_comments}')

                webhook.add_embed(embed)
                webhook.execute()
                posts[submission.id] = time.time()
                time.sleep(5)  # To prevent rate limit


if __name__ == '__main__':
    while True:
        main()
        day_from_now = time.time() - 60 * 60 * 24
        for submission_id, timestamp in posts.copy().items():
            if timestamp < day_from_now:  # Check if submission is one day old
                posts.pop(submission_id)

        time.sleep(60 * 60)  # Run every hour
