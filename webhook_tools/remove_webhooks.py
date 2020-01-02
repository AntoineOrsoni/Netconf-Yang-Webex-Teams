import requests
import functions
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Usage:')
    parser.add_argument('-t', '--token', type=str, required=True,
                        help="Token of the Webex Teams bot.")
    args = parser.parse_args()

    functions.delete_wehbook(functions.list_webhook(args.token), args.token)

