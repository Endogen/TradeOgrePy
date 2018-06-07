# TradeOgre Python API Wrapper

## Preconditions
In order to use this API wrapper you need to have API keys from [TradeOgre](https://tradeogre.com).

Open `Account` --> `Settings` --> `API Keys`

## Load API keys

__From file__
```python
import TradeOgre

trade_ogre = TradeOgre.API()
trade_ogre.load_key('TradeOgre.key')
```
In this case the key must be on the first line and the secret must be on the second line

__As direct input in class__
```python
import TradeOgre

trade_ogre = TradeOgre.API(key=some_key, secret=some_secret)
```

__As direct input in method__
```python
import TradeOgre

trade_ogre = TradeOgre.API()
trade_ogre.balances(key=some_key, secret=same_currency)
```

## Example usage

#### Markets
Retrieve a listing of all markets
```
trade_ogre.markets()
```

#### Orders
Retrieve the current order book for a market
```
trade_ogre.orders('BTC-XMR')
```

#### Ticker
Retrieve the ticker for a market
```
trade_ogre.ticker('BTC-XMR')
```

#### History
Retrieve the history of the last trades on a market
```
trade_ogre.history('BTC-XTL')
```

#### Balance
Get the balance of a specific currency
```
trade_ogre.balance('BTC')
```

#### Balances
Retrieve all balances for your account
```
trade_ogre.balance('BTC')
```

#### Buy
Submit a buy order to the order book for a market
```
trade_ogre.buy('BTC-XMR', '10', '0.0123')  # market, quantity, price
```

#### Sell
Submit a sell order to the order book for a market
```
trade_ogre.sell('BTC-XMR', '10', '0.0123')  # market, quantity, price
```

#### Order
Retrieve information about a specific order
```
trade_ogre.order('BTC-XMR')
```

#### Orders
Retrieve the active orders under your account
```
trade_ogre.orders('BTC-XMR')
```

#### Cancel
Cancel an order on the order book
```
trade_ogre.cancel('a40ac710-8dc5-b5a8-aa69-389715197b14')
```