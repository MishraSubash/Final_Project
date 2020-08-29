# Final_Project

# **Equity-Trading with Bot**
![](https://github.com/MishraSubash/Final_Project/blob/master/Images/python%20trading%20bot.jpg)

## Team Members: 
  * Subash Mishra
  * Samir Sidi
  * Kevin Lacap
  * Matt Newman
  * Moses Devanesan 

## Motivation & Objective: 

### Trading Analyst believes there is tremendious opportunity to beat equity market because of low regulation, public information and significantly low active investors. So, we decided to come up with real time auto-trading platfom in developed python environment to grab the upside potential to make money in cryptotrading. Rather than paying expensive terminal fees like Bloomberg, Coinrule, etc. We want to create our own superfast automated platform. 
### **Advantages of our platfrom**
  * Automated prompt decission making ability
  * Transperancy
  * Efficiency: Use of real-time data
  * Cost Saving 
 
## Overview: How it works?


## Data Management: 
### 
  
  
## Indicators: The Theory of the basic Indicators
### We are using three indicators to evaluate the performance of our trading. All three indicators are embeded with code so that it would automatically guides "Trading Bot" as directed in the code about when to buy and sell stocks. By default, we will make a use of 30-minute candles to see the general trend of the asset and 5-minute candles for deciding entry and exiting points.
  * **Exponential Moving Average (EMA)** : An [exponential moving average](https://www.investopedia.com/terms/e/ema.asp) (EMA) is a type of moving average (MA) that places a greater weight and significance on the most recent data points.
      #### Why EMA: We are using EMA to answer the question of ***"IS THE TREND CLEARLY DEFINED? IF YES, WILL IT GO UP OR DOWN?"***

To generate trends, we will be working with three different windows sizes: 9 for fast, 26 for the medium and 50 for the slow .      Obviously, the 50-value EMA will reveal a much longer-term trend than the 9-value EMA. Our code automatically evaluate the trens by itslelf and able to oder bot on the bais of: 
  * If the fast EMA is over the medium, and the medium is over the slow, the trend goes up.
  * If the fast EMA is below the medium, and the medium is below the slow, the trend goes down.
 
As an example, the figure below illustrates a trend going up, where the blue line is the fast EMA, the yellow is the medium EMA and the red one is the slow EMA.
![](https://github.com/MishraSubash/Final_Project/blob/master/Images/EMA%20Image.png)
 
 * **Relative Strength Index (RSI)** :The [Relative Strength Index](https://www.investopedia.com/terms/r/rsi.asp) consists of an oscillator that charts the directional price movements. When the price of a stock has an increasing trend, it has a high RSI. The more accentuated and constant the positive changes, the higher the RSI value. And vice versa.

      #### Why RSI: We are using RSI to answer the question of ***"HOW HARD IS PEOPLE BUYING -OR SELLING THIS VALUE?"***

This indicator are used to see buying and selling momentum, where: 
  * We set the value range from 0 to 100. (Which is normally a default value)
  * The mean value 50 means- a neutral position - Investors are neither buying nor selling
  * The value 70 and 30 is defined as turning point meaning surpassing these barriers means that rebound is likely happen.It also means if RSI is 70- the stock is over brought and if RSI is 10- it has been oversold. 
  
The graphs belows clearly shows where RSI hits the ceiling and bottom and rebounds back.

![](https://github.com/MishraSubash/Final_Project/blob/master/Images/RSI%20Sample.gif)


  * **Stochastic Analysis**: The [Stochastic](https://www.investopedia.com/terms/s/stochastic-modeling.asp) is also an oscillator indicating the momentum of the current price in relation to its price range over a period of time. It intends to predict price turning points, working with the close, high and low price, believing the price tends to close near the extremes of the recent candles.

      #### Why Stochastic: We are using RSI to answer the question of ***"HOW IS THE ASSET PRICE CURRENTLY, COMPARED TO ITS RECENT HISTORICAL RANGE?"****

This indicator will be used to check how much room for carrying on with the current trend does the value have.
  * It is composed of two curves . The fast one, which will react quicker to the price, and the slow one.
  * This index provides us with the specific instant where the price has reached its upper or lower limit –in comparison to the last  values, remember–, thus it indicates a change of trend.
  * This index also provides us with the proximity to this limit , which means that, even though the curves still haven’t crossed, it is not likely to go much upper –or lower–.
The following graph clearly precede a price change trend. 
![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Stochastic%20sample%20image.png)

## Entry Strategy 
### Preparing to enter into Trade: Why this strategy? 

 ![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Entry%20Strategy.png)
 
 
 
 ## Trading Strategy
 ### Buying and Selling: How bot places entry/exit order? 
 ![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Trading%20Strategy.png)
 
 
 ## Exit Strategy
 ### Analysing factors: Why we want to get out from that trade? 
 ![](https://github.com/MishraSubash/Final_Project/blob/master/Images/Exit%20Strategy.png)
 
 ### Factors to keep in Mind
  * Getting Started: General discussion about the project
  * SWAT Analysis 
  * Fetching and cleaning data
  * Developing coding Framework 
  
  
 ## Conclusion 
 
 ## postmortem
  
  
 

  
