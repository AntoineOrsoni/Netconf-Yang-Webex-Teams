python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
mv variables_template.py variables.py
echo "You now have to sart ngrok on port 8080. Then, use ./webhook_tools/post_webhook.py to POST the two webhooks.
One for when the bot is mentioned, one for when the bot is added in a room"