# -*- coding: utf-8 -*-

import tweepy
import csv, sys, os, json

# 設定ファイルから認証情報を読み取る
dir_name = os.getenv("HOME")
file_name = 'bluebird.json'
setting = json.load(open(os.path.join(dir_name, file_name)))

consumer_key = setting['consumer_key']
consumer_secret = setting['consumer_secret']
access_token = setting['access_token']
access_token_secret = setting['access_token_secret']


def print_famous_tweets(api, threshold_retweet_count=100):
    '''

    :param api:
    :param threshold_retweet_count:
    :return:
    '''
    # 出力
    writer = csv.writer(sys.stdout)

    # タイムラインを取得する
    public_tweets = api.home_timeline()

    #
    for tweet in public_tweets:
        tweet_id = tweet._json['id']
        retweet_count = tweet._json['retweet_count']
        name = tweet._json['user']['name']
        screen_name = tweet._json['user']['screen_name']
        text = tweet._json['text']

        if retweet_count > threshold_retweet_count:
            writer.writerow([screen_name, name, tweet_id, str(retweet_count), text])

def retweet(api, tweet_id):
    api.retweet(tweet_id)

if __name__ == '__main__':
    #

    #
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # 閾値以上のリツイートを持つツイートを表示
    # print_famous_tweets(api)

    # リツイートする
    # retweet(api, tweet_id)