Example Slack notifications
=============================

This example app shows a basic Notification message implementation.
This example is intended to be a starting point to allow you to get
messages posting into Slack which can be expanded to use interactive
message elements

🤖  Setup and running the app
------------------------------

**Set up your Python environment:**

See `virtualenv`_ docs for more info.

.. _virtualenv: https://virtualenv.pypa.io

.. code::

  virtualenv -p /your/path/to/python2 env
  source env/bin/activate


**Install the app's dependencies:**

.. code::

  pip install -r requirements.txt

**🤖  Create a Slack app**

Create a Slack app on https://api.slack.com/apps/

.. image:: https://cloud.githubusercontent.com/assets/32463/24877733/32979776-1de5-11e7-87d4-b5dc9e3e7973.png

**🤖  Add a bot user to your app**

.. image:: https://cloud.githubusercontent.com/assets/32463/24877750/47a16034-1de5-11e7-989b-2a90b9d8e7e3.png

**🤖  Install your app on your team**

Visit your app's **Install App** page and click **Install App to Team**.

.. image:: https://cloud.githubusercontent.com/assets/32463/24877770/61804c36-1de5-11e7-91ef-5cf2e0845729.png

Authorize your app

.. image:: https://cloud.githubusercontent.com/assets/32463/24877792/774ed94c-1de5-11e7-8857-ac8d662c5b27.png

**🤖  Save your app's credentials**

Once you've authorized your app, you'll be presented with your app's tokens.

.. image:: https://cloud.githubusercontent.com/assets/32463/24877652/d8eebbb4-1de4-11e7-8f75-2cfb1e9d45ee.png

Copy your app's **Bot User OAuth Access Token** and add it to your python environmental variables

.. code::

  export SLACK_BOT_TOKEN=xxxXXxxXXxXXxXXXXxxxX.xXxxxXxxxx

Next, go back to your app's **Basic Information** page

.. image:: https://cloud.githubusercontent.com/assets/32463/24877833/950dd53c-1de5-11e7-984f-deb26e8b9482.png

Add your app's **Client ID**, **Client Secret** and **Verification Token** to your python environmental variables

.. code::

  export SLACK_CLIENT_ID=xxxxxxxxxxx.xxxxxxxxxxxxx
  export SLACK_CLIENT_SECRET=XxxxXxxXXXxxXxxXX
  export SLACK_VERIFICATION_TOKEN=xxxxxxxxXxxXxxXxXXXxxXxxx

**🤖  Start ngrok**

In order for Slack to contact your local server, you'll need to run a tunnel. We
recommend ngrok or localtunnel. We're going to use ngrok for this example.

    💡  Slack requires event requests be delivered over SSL, so you'll want to
    use the HTTPS URL provided by ngrok.

Run ngrok and copy the **HTTPS** URL

.. code::

  ngrok http 3000

.. code::

  ngrok by @inconshreveable (Ctrl+C to quit)

  Session status                      online
  Version                             2.1.18
  Region                  United States (us)
  Web Interface        http://127.0.0.1:4040

  Forwarding http://h7465j.ngrok.io -> localhost:9292
  Forwarding https://h7465j.ngrok.io -> localhost:9292

**🤖  Run the app:**

You'll need to have your server and ngrok running in order for Slack to post
message actions to your bot's server

.. code::

  python example.py

🤔  Support
------------

Need help? Join `Bot Developer Hangout`_ and talk to us in `#slack-api`_.

You can also `create an Issue`_ right here on GitHub.

.. _Bot Developer Hangout: http://dev4slack.xoxco.com/
.. _#slack-api: https://dev4slack.slack.com/messages/slack-api/
.. _create an Issue: https://github.com/slackapi/node-slack-events-api/issues/new
