#
# Example - Using uvatradier to fetch quote data for a given symbol
#

import os, dotenv
from uvatradier import Tradier, Quotes

# Create .env file within current working directory.
# Add the following to your .env file. Specify the correct account number and authorization token for your quote.
# 	tradier_acct = <ACCOUNT_NUMBER>
#	tradier_token = <AUTH_TOKEN>

dotenv.load_dotenv()

ACCOUNT_NUMBER = os.getenv('tradier_acct')
AUTH_TOKEN = os.getenv('tradier_token')

# Initializing new Quotes object
quotes = Quotes(ACCOUNT_NUMBER, AUTH_TOKEN);

test_quote = quotes.get_quote_day('KO')

print(test_quote)