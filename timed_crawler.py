import argparse
import logging
import traceback
import warnings
import time
from crawler_class import InstagramCrawler
from pythonosc import osc_message_builder
from pythonosc import udp_client

'''
    This script tries to crawl the latest N images every M seconds either in an infinite loop or for a specified amount of time
    If duplicate images are found, they won't be downloaded by default
    Usage:
    python timed_crawler.py -q '#test_tag' -n 10 -r 10 -m 40
    Download latest 10 images with tag #test_tag every 10 seconds until 40 seconds have passed

    python timed_crawler.py -q '#test_tag' -n 10 -r 10 -m 40 --osc 1 --ip 127.0.0.2 --port 5006
    Download latest 10 images with tag #test_tag every 10 seconds until 40 seconds have passed and send an OSC message with the filename

'''

def main():
    parser = argparse.ArgumentParser(description='Instagram Crawler')
    parser.add_argument('-q','--query',type=str, help="target to crawl, add '#' for hashtags")
    parser.add_argument('-t','--type',type=str, default='photos', help = 'photos | followers | followed')
    parser.add_argument('-n', '--number', default='12', help='Number of posts to download: integer or "all"')
    parser.add_argument('-c','--caption', action='store_true', help='Add this flag to download caption when downloading photos')
    parser.add_argument('-d', '--dir', type=str, default = './data/',
                            help='directory to save results')
    parser.add_argument('-r', '--refresh', type=int, default = 25,
                            help='refresh rate in seconds')
    parser.add_argument('-m', '--maxtime', type=int, default = 100,
                            help='max running time in seconds, if -1, will run infinitely')

    parser.add_argument('--osc', type=int, default=0, help='If 0, will not send OSC messages, if 1, will send')
    parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005, help="The port the OSC server is listening on")
    parser.add_argument("--address", type=str, default="/image", help="The address to which the OSC messages will be sent")
    args = parser.parse_args()


    if args.osc == 1:
        osc_client = udp_client.SimpleUDPClient(args.ip, args.port)
    else:
        osc_client = None
    crawler = InstagramCrawler(args.dir, osc_client=osc_client, osc_address=args.address)
    time_counter = 0
    while (time_counter < args.maxtime) or (args.maxtime < 0):
        crawler.browse(args.query,args.type).crawl(args.number,args.caption).save()
        crawler.clear()
        time.sleep(args.refresh)
        time_counter += args.refresh

if __name__ == "__main__":
    main()
