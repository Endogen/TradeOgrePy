# TradeOgre Python API Wrapper

## Preconditions
In order to use this API wrapper you need to have API keys from [TradeOgre](https://tradeogre.com).

Open `Account` --> `Settings` --> `API Keys`

## Load API keys

__From file__
```python
from tradeogre import TradeOgre

trade_ogre = TradeOgre().load_key('TradeOgre.key')
```
In this case the key must be on the first line and the secret must be on the second line

__As direct input in class__
```python
from tradeogre import TradeOgre

trade_ogre = TradeOgre(key=some_key, secret=some_secret)
```

__As direct input in method__
```python
from tradeogre import TradeOgre

trade_ogre = TradeOgre()
reply = trade_ogre.balances(key=some_key, secret=some_secret)
```

## Example usage

#### Markets
Retrieve a listing of all markets
```
trade_ogre.markets()
```

#### Order book
Retrieve the current order book for a market
```
trade_ogre.order_book('BTC-XMR')
```

#### Ticker
Retrieve the ticker (current price) for a market
```
trade_ogre.ticker('BTC-XMR')
```

#### History
Retrieve the history of the last trades for a market
```
trade_ogre.history('BTC-XTL')
```

#### Balance
Get the balance of a specific currency  
You need to provide API key and secret for this method
```
trade_ogre.balance('BTC')
```

#### Balances
Retrieve all balances for your account  
You need to provide API key and secret for this method
```
trade_ogre.balance()
```

#### Buy
Submit a buy order to the order book for a market  
You need to provide API key and secret for this method
```
trade_ogre.buy('BTC-XMR', '10', '0.0123')  # market, quantity, price
```

#### Sell
Submit a sell order to the order book for a market  
You need to provide API key and secret for this method
```
trade_ogre.sell('BTC-XMR', '10', '0.0123')  # market, quantity, price
```

#### Orders
Retrieve the active orders for your account  
You need to provide API key and secret for this method
```
trade_ogre.orders('BTC-XMR')
```

#### Order
Retrieve information about a specific order  
You need to provide API key and secret for this method
```
trade_ogre.order('1702a7bc-6a18-92c0-c1fe-aaf581d2352d')
```

#### Cancel
Cancel an order on the order book  
You need to provide API key and secret for this method
```
trade_ogre.cancel('a40ac710-8dc5-b5a8-aa69-389715197b14')
```