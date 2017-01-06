import argparse
import logging
import traceback
import warnings
from crawler_class import InstagramCrawler

def main():
    parser = argparse.ArgumentParser(description='Instagram Crawler')
    parser.add_argument('-q','--query',type=str, help="target to crawl, add '#' for hashtags")
    parser.add_argument('-t','--type',type=str, help = 'photos | followers | followed')
    parser.add_argument('-n', '--number', default='12', help='Number of posts to download: integer or "all"')
    parser.add_argument('-c','--caption', action='store_true', help='Add this flag to download caption when downloading photos')
    parser.add_argument('-d', '--dir', type=str, default = './data/',
                            help='directory to save results')
    args = parser.parse_args()

    crawler = InstagramCrawler(args.dir)

    try:
        crawler.browse(args.query,args.type).crawl(args.number,args.caption).save()
        logging.info("Crawl {0} {1} succeeded!\n".format(args.type,args.query))
    except:
        err_msg = traceback.format_exc()
        print(err_msg)
        logging.info("Crawl {0} {1} failed:\n {2}".format(args.type,args.query, err_msg))

if __name__ == "__main__":
    main()
