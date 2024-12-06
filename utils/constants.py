from configparser import ConfigParser
import os


parser = ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf'))


# SPOTIFY CONNECTION
SPOTIFY_CLIENT_ID = parser.get("spotify","spotify_client_id")
SPOTIFY_SECRET_KEY = parser.get("spotify","spotify_secret_key")

# FILE PATH
OUTPUT_PATH = parser.get('dir','output_path')

# AWS
AWS_ACCESS_KEY_ID = parser.get("aws","aws_access_key_id")
AWS_SECRET_KEY = parser.get("aws","aws_secret_access_key")
AWS_BUCKET_NAME = parser.get("aws","aws_bucket_name")

