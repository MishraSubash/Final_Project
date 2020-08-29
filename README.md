# **Equity-Trading with Bot**
![](https://github.com/MishraSubash/Final_Project/blob/master/Images/python%20trading%20bot.jpg)

## Team Members: 
  * Subash Mishra
  * Samir Sidi
  * Kevin Lacap
  * Matt Newman
  * Moses Devanesan 

## Motivation & Objective: 
We want a system that is systematic, emotionless, and works 24/7.

Unlike humans, trading bots can consistently execute strategies that are precise. Trading bots can execute orders within milliseconds of an event occurring. Humans don’t have the reflexes or capacity to effectively implement such a strategy without some sort of trading bot. 

More generally than simply what is possible, traders want something that is reliable and deterministic. That way there is no opportunity for error. When the strategy is set, the strategy will be executed based on the parameters of the algorithm. That’s really all there is to it. 


## Overview: How it works?
## Setup
Before we can begin, we must set up our environment. This will involve a few steps to get access to trading APIs and our exchange accounts, but once set up, we won’t need to make any changes to our development environment.  
 
 ### Generate & Store API Keys: 
Before we can start using the Alpace Trade APIs, we will need to generate our API keys. This can be done by logging into your [Alpaca Developer](https://app.alpaca.markets/brokerage/new-account/greeting) account and sign up for paper trading then grap necessary API keys. 

### Setting Up Our Python Environment: 
There are a few things we will need to set up for our Python environment before we can start coding. First, start by installing some libarries that includes beautifulsoup4, SciPy, requests. 

### Store Pricing Data
 For this project we ahve created separate CSV file to store all tickes (you can customize as you like) and in the coding, we interlinked CSV file with code. so this bot is hassle free if investor wants to change tickers. 
  
## The Coding Parameters 
## Indicators: The Theory of the basic Indicators
We are using three indicators to evaluate the performance of our trading. All three indicators are embeded with code so that it would automatically guides "Trading Bot" as directed in the code about when to buy and sell stocks. By default, we will make a use of 30-minute candles to see the general trend of the asset and 5-minute candles for deciding entry and exiting points.
  * **Exponential Moving Average (EMA)** : An [exponential moving average](https://www.investopedia.com/terms/e/ema.asp) (EMA) is a type of moving average (MA) that places a greater weight and significance on the most recent data points.
  
Why EMA: We are using EMA to answer the question of ***"IS THE TREND CLEARLY DEFINED? IF YES, WILL IT GO UP OR DOWN?"***

To generate trends, we will be working with three different windows sizes: 9 for fast, 26 for the medium and 50 for the slow .      Obviously, the 50-value EMA will reveal a much longer-term trend than the 9-value EMA. Our code automatically evaluate the trens by itslelf and able to oder bot on the bais of: 
  * If the fast EMA is over the medium, and the medium is over the slow, the trend goes up.
  * If the fast EMA is below the medium, and the medium is below the slow, the trend goes down.
 
As an example, the figure below illustrates a trend going up, where the blue line is the fast EMA, the yellow is the medium EMA and the red one is the slow EMA.
![](https://github.com/MishraSubash/Final_Project/blob/master/Images/EMA%20Image.png)
 
 * **Relative Strength Index (RSI)** :The [Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp) consists of an oscillator that charts the directional price movements. When the price of a stock has an increasing trend, it has a high RSI. The more accentuated and constant the positive changes, the higher the RSI value. And vice versa.

Why RSI: We are using RSI to answer the question of ***"HOW HARD IS PEOPLE BUYING -OR SELLING THIS VALUE?"***

This indicator are used to see buying and selling momentum, where: 
  * We set the value range from 0 to 100. (Which is normally a default value)
  * The mean value 50 means- a neutral position - Investors are neither buying nor selling
  * The value 70 and 30 is defined as turning point meaning surpassing these barriers means that rebound is likely happen.It also means if RSI is 70- the stock is over brought and if RSI is 10- it has been oversold. 
  
The graphs belows clearly shows where RSI hits the ceiling and bottom and rebounds back.

![](https://github.com/MishraSubash/Final_Project/blob/master/Images/RSI%20Sample.gif)


  * **Stochastic Analysis**: The [Stochastic](https://www.investopedia.com/terms/s/stochastic-modeling.asp) is also an oscillator indicating the momentum of the current price in relation to its price range over a period of time. It intends to predict price turning points, working with the close, high and low price, believing the price tends to close near the extremes of the recent candles.

Why Stochastic: We are using RSI to answer the question of ***"HOW IS THE ASSET PRICE CURRENTLY, COMPARED TO ITS RECENT HISTORICAL RANGE?"****

This indicator will be used to check how much room for carrying on with the current trend does the value have.
  * It is composed of two curves . The fast one, which will react quicker to the price, and the slow one.
  * This index provides us with the specific instant where the price has reached its upper or lower limit –in comparison to the last  values, remember–, thus it indicates a change of trend.
  * This index also provides us with the proximity to this limit , which means that, even though the curves still haven’t crossed, it is not likely to go much upper –or lower–.
The following graph clearly precede a price change trend. 
![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Stochastic%20sample%20image.png)

## Entry Strategy 
Before entering into the trade, it analysie the general trends for 30 mins time frame using EMA . 

Our decision making will go through a total of 4 steps. We may also call them filters , gates ,
enablers or authorizers , since these are the ones that will confirm a possible entry . The
order goes this way:

 ![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Entry%20Strategy.png)
 
  
 ## Trading Strategy
 After entering into the market, it will remain there until investors directed to do otherwise. 
 ![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Trading%20Strategy.png)
 
 
 ## Exit Strategy
 This may be the most important step to fefine when to get out from the market, This bot is directed to get out under two circumstances: 
 * Gain Check: 
      * The Take Profit: It will be the upper limit where the position will be closed. If the share reaches that price, then you have taken the maximum amount you wanted to take.
      * The Stop Loss: It will be the lower limit. This is the most important measure against your losses and in favour of your gains. More on that later.
      
  * The Stochastic Curves: The stochastic oscillator are also in place, in this strategy, to close a position. The value will be constantly fluctuating, and this oscillator will tell us that it may have reached its highest/lowest point. If the oscillator crosses itself in the other direction, the system will read that signal and it will close the position.
  
  Graphical representation of Exit Position
 ![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Exit%20Strategy.png)
 
## Conclusion
Equity Trading is a hugh and complex market. As we expand into the foreseeable future, we will need to continue developing trading resources that help us better automate our portfolio and trading strategy. So, We have utilized what we have gained in this course to develop our own vitual trading bot to automate and senseless trading platform. Our team think this is new ways of trading in digital age. Mo more Quotron, no more clicking, no more monitoring stocks all day, no calculation of figures and numbers for pnl - we directed machine to do all and everything in one place. 

## postmortem
* Quality prior to quantity: This guide does not describe a high frequency trading system. Going through the 4 filters described above will sometimes lead to an open position, but some days not a single order will be placed.

* Stop loss may be unrealistic: Not capping on stop loss could be more benificial in highly volatile situation. Investor must allow the price to fluctuate before entering the positive gain zone.

* In the future we would like to extend our platform in more sophesticated ways in a sense that it will have more paraments to evaluate, making it flexible, and deploy it in virtual environment. 
  
Don’t hesitate to reach out to our team if you have any questions about how to build a trading bot, need help constructing a new trading strategy, or want us to integrate new features

  
