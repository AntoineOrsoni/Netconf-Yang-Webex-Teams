python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
mv ./core/variables_template.py ./core/variables.py
printf "You now have to sart ngrok on port 8080. Then, use ./webhook_tools/post_webhook.py to POST the two webhooks.
* One for when the bot is mentioned,
* one for when the bot is added in a room.\n
Don't forget to edit the ./core/variables.py file with your both token and the ngrok URL."
