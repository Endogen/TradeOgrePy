import requests


class TradeOgre(object):
    """ Maintains a single session between this machine and TradeOgre.

    Specifying a key/secret pair is optional. If not specified, key and
    secret must be specified at the called method.

    Query responses, as received by :py:mod:`requests`, are retained
    as attribute :py:attr:`response` of this object. It is overwritten
    on each query.

    """
    def __init__(self, key=None, secret=None):
        """ Create an object with authentication information.

        :param key: (optional) key identifier for queries to the API
        :type key: str

        :param secret: (optional) actual private key used to sign messages
        :type secret: str

        :returns: None

        """
        self.key = key
        self.secret = secret
        self.uri = 'https://tradeogre.com/api/v1'
        self.response = None
        return

    def load_key(self, path):
        """ Load key and secret from file.
        Expected file format is key and secret on separate lines.

        :param path: path to keyfile
        :type path: str

        :returns: None

        """
        with open(path, 'r') as f:
            self.key = f.readline().strip()
            self.secret = f.readline().strip()
        return

    def markets(self):
        """ Retrieve a listing of all markets and basic information
        including current price, volume, high, low, bid and ask.

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        self.response = requests.get(self.uri + '/markets').json()
        return self.response

    def order_book(self, market):
        """ Retrieve the current order book for a market such as 'BTC-XMR'.

        :param market: market such as 'BTC-XMR'
        :type market: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        self.response = requests.get(self.uri + '/orders/' + market).json()
        return self.response

    def ticker(self, market):
        """ Retrieve the ticker for a market such as 'BTC-XMR', volume,
        high, and low are in the last 24 hours, initial price is the
        price from 24 hours ago.

        :param market: market such as 'BTC-XMR'
        :type market: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        self.response = requests.get(self.uri + '/ticker/' + market).json()
        return self.response

    def history(self, market):
        """ Retrieve the history of the last trades on {market} limited to 100
        of the most recent trades. The date is a Unix UTC timestamp.

        :param market: market such as 'BTC-XMR'
        :type market: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        self.response = requests.get(self.uri + '/history/' + market).json()
        return self.response

    def balance(self, currency, key=None, secret=None):
        """ Get the balance of a specific currency for you account. The currency
        field is required, such as 'BTC'. The total balance is returned and the
        available balance is what can be used in orders or withdrawn.

        :param currency: currency such as 'BTC'
        :type currency: str

        :param key: key identifier
        :type key: str

        :param secret: actual private key
        :type secret: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        data = {"currency": currency}
        self.response = requests.post(self.uri + '/account/balance', data=data, auth=(key, secret)).json()
        return self.response

    def balances(self, key=None, secret=None):
        """ Retrieve all balances for your account.

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        self.response = requests.get(self.uri + '/account/balances', auth=(key, secret)).json()
        return self.response

    def buy(self, market, qty, price, key=None, secret=None):
        """ Submit a buy order to the order book for a market. The success status
        will be false if there is an error, and error will contain the error message.
        Your available buy and sell balance for the market will be returned if
        successful. If your order is successful but not fully fulfilled, the order
        is placed onto the order book and you will receive a uuid for the order.

        :param market: market such as 'BTC-XMR'
        :type market: str

        :param qty: quantity to buy
        :type qty: str

        :param price: price to buy for
        :type price: str

        :param key: key identifier
        :type key: str

        :param secret: actual private key
        :type secret: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        data = {"market": market, "quantity": qty, "price": price}
        self.response = requests.post(self.uri + '/order/buy', data=data, auth=(key, secret)).json()
        return self.response

    def sell(self, market, qty, price, key=None, secret=None):
        """ Submit a sell order to the order book for a market. The success status
        will be false if there is an error, and error will contain the error
        message. Your available buy and sell balance for the market will be returned
        if successful. If your order is successful but not fully fulfilled, the order
        is placed onto the order book and you will receive a uuid for the order.

        :param market: market such as 'BTC-XMR'
        :type market: str

        :param qty: quantity to sell
        :type qty: str

        :param price: price to sell for
        :type price: str

        :param key: key identifier
        :type key: str

        :param secret: actual private key
        :type secret: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        data = {"market": market, "quantity": qty, "price": price}
        self.response = requests.post(self.uri + '/order/sell', data=data, auth=(key, secret)).json()
        return self.response

    def order(self, uuid, key=None, secret=None):
        """ Retrieve information about a specific order by the
        uuid of the order. Date is a Unix UTC timestamp.

        :param uuid: ID of order
        :type uuid: str

        :param key: key identifier
        :type key: str

        :param secret: actual private key
        :type secret: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        self.response = requests.get(self.uri + '/account/order/' + uuid, auth=(key, secret)).json()
        return self.response

    def orders(self, market=None, key=None, secret=None):
        """ Retrieve the active orders under your account. The market
        field is optional, and leaving it out will return all orders
        in every market. date is a Unix UTC timestamp.

        :param market: (optional) market to list orders from
        :type market: str

        :param key: key identifier
        :type key: str

        :param secret: actual private key
        :type secret: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        if market is None:
            market = ''

        data = {"market": market}
        self.response = requests.post(self.uri + '/account/orders', data=data, auth=(key, secret)).json()
        return self.response

    def cancel(self, uuid, key=None, secret=None):
        """ Cancel an order on the order book based on the order uuid.
        The uuid parameter can also be set to all and all of your
        orders will be cancelled across all markets.

        :param uuid: ID of order to cancel
        :type uuid: str

        :param key: key identifier
        :type key: str

        :param secret: actual private key
        :type secret: str

        :returns: :py:meth:`requests.Response.json`-deserialised Python object

        """
        if key is None or secret is None:
            key = self.key
            secret = self.secret

        if key is None or secret is None:
            raise Exception('Either key or secret is not set! (Use `load_key()`.')

        data = {"uuid": uuid}
        self.response = requests.post(self.uri + '/order/cancel', data=data, auth=(key, secret)).json()
        return self.response
