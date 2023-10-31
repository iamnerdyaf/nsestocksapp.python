#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

from tkinter import *
import customtkinter as cs
from ttkthemes import ThemedTk                                                  
from tktooltip import ToolTip
from PIL import Image, ImageTk
from playsound import playsound
import datetime
import time
from jugaad_data.nse import NSELive

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

root = ThemedTk(theme='breeze')                                                     
b=Frame(root,bg='black')                                                            
b.pack()
img=ImageTk.PhotoImage(Image.open('Path of stvis.jpg'))         
label=Label(b,image=img,bg='black')                                                 
label.grid(row=0,column=0)
width=685                                                                           
height=388
screen_width=root.winfo_screenwidth()                                               
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)
root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.overrideredirect(True)
root.configure(bg='black')
root.after(5000,lambda:root.destroy())      
root.mainloop()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

root=ThemedTk(theme='breeze')
root.title('  Trading Titan')
icon_photo=PhotoImage(file='Path of logo.png')
root.iconphoto(False,icon_photo)
root.geometry('1536x789+-3+0')
root.resizable(0,0)
root.configure(background='light blue')

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

n=NSELive()

def config_text(n1,n2,n3,n4,n5,n6,t1,t2,t3,t4,t5,t6):
    n1.config(text=t1)
    n2.config(text=t2)
    n3.config(text=t3)
    n4.config(text=t4)
    n5.config(text=t5)
    n6.config(text=t6)
    
def nifty_50():
    indices=n.all_indices()
    q=indices['data'][0]
    current_price,change,perc_change=q['last'],q['variation'],q['percentChange']
    day_low,day_high,open_price,year_low,year_high,prev_close=q['low'],q['high'],q['open'],q['yearLow'],q['yearHigh'],q['previousClose']
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="NIFTY 50                                      ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="NIFTY 50                                      ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change            {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                       {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                {:.2f}".format(open_price)
    t5="52 Week Range                {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                     {:.2f}".format(prev_close)
    config_text(nifty501,nifty502,nifty503,nifty504,nifty505,nifty506,t1,t2,t3,t4,t5,t6)
    nifty501.after(2000,nifty_50)

def nifty_bank():
    indices=n.all_indices()
    q=indices['data'][18]
    current_price,change,perc_change=q['last'],q['variation'],q['percentChange']
    day_low,day_high,open_price,year_low,year_high,prev_close=q['low'],q['high'],q['open'],q['yearLow'],q['yearHigh'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="NIFTY BANK                                ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change          +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="NIFTY BANK                                ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change            {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                       {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                {:.2f}".format(open_price)
    t5="52 Week Range                {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                     {:.2f}".format(prev_close)
    config_text(niftyb1,niftyb2,niftyb3,niftyb4,niftyb5,niftyb6,t1,t2,t3,t4,t5,t6)
    niftyb1.after(2000,nifty_bank)

def nifty_midcap_100():
    indices=n.all_indices()
    q=indices['data'][6]
    current_price,change,perc_change=q['last'],q['variation'],q['percentChange']
    day_low,day_high,open_price,year_low,year_high,prev_close=q['low'],q['high'],q['open'],q['yearLow'],q['yearHigh'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="NIFTY MIDCAP 100                      ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="NIFTY MIDCAP 100                      ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                       {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                {:.2f}".format(open_price)
    t5="52 Week Range                {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                     {:.2f}".format(prev_close)
    config_text(niftym1,niftym2,niftym3,niftym4,niftym5,niftym6,t1,t2,t3,t4,t5,t6)
    niftym1.after(2000,nifty_midcap_100)

def adani_enter_ltd():
    r=n.stock_quote('ADANIENT')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="ADANI ENTER LTD.                       ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="ADANI ENTER LTD.                       ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(adanient1,adanient2,adanient3,adanient4,adanient5,adanient6,t1,t2,t3,t4,t5,t6)
    adanient1.after(2000,adani_enter_ltd)

def reliance():
    r=n.stock_quote('RELIANCE')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="RELIANCE                                    ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="RELIANCE                                    ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(rel1,rel2,rel3,rel4,rel5,rel6,t1,t2,t3,t4,t5,t6)
    rel1.after(2000,reliance)

def tcs():
    r=n.stock_quote('TCS')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="TCS                                              ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="TCS                                              ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(tcs1,tcs2,tcs3,tcs4,tcs5,tcs6,t1,t2,t3,t4,t5,t6)
    tcs1.after(2000,tcs)
    
def hdfc():
    r=n.stock_quote('HDFCBANK')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="HDFC BANK LTD.                          ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="HDFC BANK LTD.                          ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(hdfc1,hdfc2,hdfc3,hdfc4,hdfc5,hdfc6,t1,t2,t3,t4,t5,t6)
    hdfc1.after(2000,hdfc)

def icici():
    r=n.stock_quote('ICICIBANK')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="ICICI BANK LTD.                             ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="ICICI BANK LTD.                             ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                              {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                   {:.2f}".format(open_price)
    t5="52 Week Range                     {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                        {:.2f}".format(prev_close)
    config_text(icici1,icici2,icici3,icici4,icici5,icici6,t1,t2,t3,t4,t5,t6)
    icici1.after(2000,icici)

def hul():
    r=n.stock_quote('HINDUNILVR')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="HUL                                              ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change            +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="HUL                                              ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change              {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(hul1,hul2,hul3,hul4,hul5,hul6,t1,t2,t3,t4,t5,t6)
    hul1.after(2000,hul)

def infy():
    r=n.stock_quote('INFY')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="INFOSYS                                      ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="INFOSYS                                      ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change              {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(infy1,infy2,infy3,infy4,infy5,infy6,t1,t2,t3,t4,t5,t6)
    infy1.after(2000,infy)

def itc():
    r=n.stock_quote('ITC')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="ITC LTD.                                         ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change             +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="ITC LTD.                                         ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change               {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                              {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                   {:.2f}".format(open_price)
    t5="52 Week Range                      {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                        {:.2f}".format(prev_close)
    config_text(itc1,itc2,itc3,itc4,itc5,itc6,t1,t2,t3,t4,t5,t6)
    infy1.after(2000,itc)

def bairtel():
    r=n.stock_quote('BHARTIARTL')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="BHARTI AIRTEL LTD.                      ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="BHARTI AIRTEL LTD.                      ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                             {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                   {:.2f}".format(open_price)
    t5="52 Week Range                      {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                        {:.2f}".format(prev_close)
    config_text(bairtel1,bairtel2,bairtel3,bairtel4,bairtel5,bairtel6,t1,t2,t3,t4,t5,t6)
    bairtel1.after(2000,bairtel)
    
def sbi():
    r=n.stock_quote('SBIN')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="SBI                                                 ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change             +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="SBI                                                 ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change               {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                             {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                   {:.2f}".format(open_price)
    t5="52 Week Range                      {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                       {:.2f}".format(prev_close)
    config_text(sbi1,sbi2,sbi3,sbi4,sbi5,sbi6,t1,t2,t3,t4,t5,t6)
    sbi1.after(2000,sbi)

def bajajfin():
    r=n.stock_quote('BAJFINANCE')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="BAJAJ FINANCE LTD.                    ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change             +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="BAJAJ FINANCE LTD.                    ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change               {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(bajajfin1,bajajfin2,bajajfin3,bajajfin4,bajajfin5,bajajfin6,t1,t2,t3,t4,t5,t6)
    bajajfin1.after(2000,bajajfin)

def larsen():
    r=n.stock_quote('LT')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="LARSEN & TURBO LTD.                ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="LARSEN & TURBO LTD.                ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(larsen1,larsen2,larsen3,larsen4,larsen5,larsen6,t1,t2,t3,t4,t5,t6)
    larsen1.after(2000,larsen)

def licin():
    r=n.stock_quote('LICI')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="LIC                                                 ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change             +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="LIC                                                 ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change              {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                             {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                  {:.2f}".format(open_price)
    t5="52 Week Range                      {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                       {:.2f}".format(prev_close)
    config_text(licin1,licin2,licin3,licin4,licin5,licin6,t1,t2,t3,t4,t5,t6)
    licin1.after(2000,licin)

def hclt():
    r=n.stock_quote('HCLTECH')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="HCL TECHNOLOGIES LTD.            ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change             +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="HCL TECHNOLOGIES LTD.            ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change               {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(hclt1,hclt2,hclt3,hclt4,hclt5,hclt6,t1,t2,t3,t4,t5,t6)
    hclt1.after(2000,hclt)

def ktkmah():
    r=n.stock_quote('KOTAKBANK')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="KOTAK MAHINDRA                       ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="KOTAK MAHINDRA                       ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                          {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                   {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(ktkmah1,ktkmah2,ktkmah3,ktkmah4,ktkmah5,ktkmah6,t1,t2,t3,t4,t5,t6)
    ktkmah1.after(2000,ktkmah)

def marsuj():
    r=n.stock_quote('MARUTI')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="MARUTI SUZUKI                          ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change          +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="MARUTI SUZUKI                          ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change            {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                       {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                {:.2f}".format(open_price)
    t5="52 Week Range                 {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                     {:.2f}".format(prev_close)
    config_text(marsuj1,marsuj2,marsuj3,marsuj4,marsuj5,marsuj6,t1,t2,t3,t4,t5,t6)
    marsuj1.after(2000,marsuj)

def axis():
    r=n.stock_quote('AXISBANK')
    q=r['priceInfo']
    current_price,change,perc_change=q['lastPrice'],q['change'],q['pChange']
    day_low,day_high=q['intraDayHighLow']['min'],q['intraDayHighLow']['max']
    open_price,year_low,year_high,prev_close=q['open'],q['weekHighLow']['min'],q['weekHighLow']['max'],q['previousClose']    
    if str(change)[0]!='-' or str(perc_change)[0]!='-':
        t1="AXIS BANK LTD.                            ▲{:.2f}".format(current_price)   
        t2="Change/Perc. Change           +{:.2f}/+{:.2f}%".format(change,perc_change)
    else:
        t1="AXIS BANK LTD.                            ▼{:.2f}".format(current_price)
        t2="Change/Perc. Change             {:.2f}/{:.2f}%".format(change,perc_change)
    t3="Day Range                           {:.2f}-{:.2f}".format(day_low,day_high)
    t4="Opening Price                                 {:.2f}".format(open_price)
    t5="52 Week Range                    {:.2f}-{:.2f}".format(year_low,year_high)
    t6="Prev. Close                                      {:.2f}".format(prev_close)
    config_text(axis1,axis2,axis3,axis4,axis5,axis6,t1,t2,t3,t4,t5,t6)
    axis1.after(2000,axis)
    
font1=('intelone-mono-font-family-bolditalic',10,'bold')

def button_function(n1,n2,n3,n4,n5,n6):
    n1.pack(padx=2,pady=1)
    n2.pack(padx=2,pady=1)
    n3.pack(padx=2,pady=1)
    n4.pack(padx=2,pady=1)
    n5.pack(padx=2,pady=1)
    n6.pack(padx=2,pady=1)

def button1(a):
    return Button(a,font=font1,anchor='nw',bg='white',width=34,height=1,activebackground='light blue',relief='sunken',bd=0)

sframe00=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe00.place(x=19,y=21)
nifty501,nifty502,nifty503=button1(sframe00),button1(sframe00),button1(sframe00)
nifty504,nifty505,nifty506=button1(sframe00),button1(sframe00),button1(sframe00)
button_function(nifty501,nifty502,nifty503,nifty504,nifty505,nifty506)
nifty_50()

sframe01=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe01.place(x=322,y=21)
niftyb1,niftyb2,niftyb3=button1(sframe01),button1(sframe01),button1(sframe01)
niftyb4,niftyb5,niftyb6=button1(sframe01),button1(sframe01),button1(sframe01)
button_function(niftyb1,niftyb2,niftyb3,niftyb4,niftyb5,niftyb6)
nifty_bank()

sframe02=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe02.place(x=625,y=21)
niftym1,niftym2,niftym3=button1(sframe02),button1(sframe02),button1(sframe02)
niftym4,niftym5,niftym6=button1(sframe02),button1(sframe02),button1(sframe02)
button_function(niftym1,niftym2,niftym3,niftym4,niftym5,niftym6)
nifty_midcap_100()

sframe03=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe03.place(x=929,y=21)
adanient1,adanient2,adanient3=button1(sframe03),button1(sframe03),button1(sframe03)
adanient4,adanient5,adanient6=button1(sframe03),button1(sframe03),button1(sframe03)
button_function(adanient1,adanient2,adanient3,adanient4,adanient5,adanient6)
adani_enter_ltd()

sframe04=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe04.place(x=1233,y=21)
rel1,rel2,rel3=button1(sframe04),button1(sframe04),button1(sframe04)
rel4,rel5,rel6=button1(sframe04),button1(sframe04),button1(sframe04)
button_function(rel1,rel2,rel3,rel4,rel5,rel6)
reliance()

sframe10=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe10.place(x=19,y=197)
tcs1,tcs2,tcs3=button1(sframe10),button1(sframe10),button1(sframe10)
tcs4,tcs5,tcs6=button1(sframe10),button1(sframe10),button1(sframe10)
button_function(tcs1,tcs2,tcs3,tcs4,tcs5,tcs6)
tcs()

sframe11=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe11.place(x=322,y=197)
hdfc1,hdfc2,hdfc3=button1(sframe11),button1(sframe11),button1(sframe11)
hdfc4,hdfc5,hdfc6=button1(sframe11),button1(sframe11),button1(sframe11)
button_function(hdfc1,hdfc2,hdfc3,hdfc4,hdfc5,hdfc6)
hdfc()

sframe12=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe12.place(x=625,y=197)
icici1,icici2,icici3=button1(sframe12),button1(sframe12),button1(sframe12)
icici4,icici5,icici6=button1(sframe12),button1(sframe12),button1(sframe12)
button_function(icici1,icici2,icici3,icici4,icici5,icici6)
icici()

sframe13=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe13.place(x=929,y=197)
hul1,hul2,hul3=button1(sframe13),button1(sframe13),button1(sframe13)
hul4,hul5,hul6=button1(sframe13),button1(sframe13),button1(sframe13)
button_function(hul1,hul2,hul3,hul4,hul5,hul6)
hul()

sframe14=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe14.place(x=1233,y=197)
infy1,infy2,infy3=button1(sframe14),button1(sframe14),button1(sframe14)
infy4,infy5,infy6=button1(sframe14),button1(sframe14),button1(sframe14)
button_function(infy1,infy2,infy3,infy4,infy5,infy6)
infy()

sframe20=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe20.place(x=19,y=374)
itc1,itc2,itc3=button1(sframe20),button1(sframe20),button1(sframe20)
itc4,itc5,itc6=button1(sframe20),button1(sframe20),button1(sframe20)
button_function(itc1,itc2,itc3,itc4,itc5,itc6)
itc()

sframe21=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe21.place(x=322,y=374)
bairtel1,bairtel2,bairtel3=button1(sframe21),button1(sframe21),button1(sframe21)
bairtel4,bairtel5,bairtel6=button1(sframe21),button1(sframe21),button1(sframe21)
button_function(bairtel1,bairtel2,bairtel3,bairtel4,bairtel5,bairtel6)
bairtel()

sframe22=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe22.place(x=625,y=374)
sbi1,sbi2,sbi3=button1(sframe22),button1(sframe22),button1(sframe22)
sbi4,sbi5,sbi6=button1(sframe22),button1(sframe22),button1(sframe22)
button_function(sbi1,sbi2,sbi3,sbi4,sbi5,sbi6)
sbi()

sframe23=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe23.place(x=929,y=374)
bajajfin1,bajajfin2,bajajfin3=button1(sframe23),button1(sframe23),button1(sframe23)
bajajfin4,bajajfin5,bajajfin6=button1(sframe23),button1(sframe23),button1(sframe23)
button_function(bajajfin1,bajajfin2,bajajfin3,bajajfin4,bajajfin5,bajajfin6)
bajajfin()

sframe24=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe24.place(x=1233,y=374)
larsen1,larsen2,larsen3=button1(sframe24),button1(sframe24),button1(sframe24)
larsen4,larsen5,larsen6=button1(sframe24),button1(sframe24),button1(sframe24)
button_function(larsen1,larsen2,larsen3,larsen4,larsen5,larsen6)
larsen()

sframe30=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe30.place(x=19,y=551)
licin1,licin2,licin3=button1(sframe30),button1(sframe30),button1(sframe30)
licin4,licin5,licin6=button1(sframe30),button1(sframe30),button1(sframe30)
button_function(licin1,licin2,licin3,licin4,licin5,licin6)
licin()

sframe31=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe31.place(x=322,y=551)
hclt1,hclt2,hclt3=button1(sframe31),button1(sframe31),button1(sframe31)
hclt4,hclt5,hclt6=button1(sframe31),button1(sframe31),button1(sframe31)
button_function(hclt1,hclt2,hclt3,hclt4,hclt5,hclt6)
hclt()

sframe32=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe32.place(x=625,y=551)
ktkmah1,ktkmah2,ktkmah3=button1(sframe32),button1(sframe32),button1(sframe32)
ktkmah4,ktkmah5,ktkmah6=button1(sframe32),button1(sframe32),button1(sframe32)
button_function(ktkmah1,ktkmah2,ktkmah3,ktkmah4,ktkmah5,ktkmah6)
ktkmah()

sframe33=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe33.place(x=929,y=551)
marsuj1,marsuj2,marsuj3=button1(sframe33),button1(sframe33),button1(sframe33)
marsuj4,marsuj5,marsuj6=button1(sframe33),button1(sframe33),button1(sframe33)
button_function(marsuj1,marsuj2,marsuj3,marsuj4,marsuj5,marsuj6)
marsuj()

sframe34=cs.CTkFrame(root,width=291,height=165,fg_color='white')
sframe34.place(x=1233,y=551)
axis1,axis2,axis3=button1(sframe34),button1(sframe34),button1(sframe34)
axis4,axis5,axis6=button1(sframe34),button1(sframe34),button1(sframe34)
button_function(axis1,axis2,axis3,axis4,axis5,axis6)
axis()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

frame=Frame(root,highlightbackground='white',highlightthickness=1)
frame.pack(side=BOTTOM,fill='x')
frame.configure(background='white')

def time_():

    time_string=time.strftime(' %A  |  %d-%m-%y  |  %H:%M')
    market_preopening_time=datetime.time(9,0,0)
    market_opening_time=datetime.time(9,15,0)
    market_closing_time=datetime.time(15,30,0)
    market_close_day=datetime.datetime.now().strftime('%A')
    current_time=datetime.datetime.now().time()
    if market_close_day!='Saturday' or market_close_day!='Sunday':
        if current_time>market_closing_time or current_time<market_preopening_time:
            timelbl.config(text=time_string+' IST\nIndian Markets Inactive')
        elif market_opening_time>current_time>=market_preopening_time:
            timelbl.config(text=time_string+' IST\nIndian Markets Active(Pre-opening session)')
        elif current_time>=market_opening_time:
            timelbl.config(text=time_string+' IST\nIndian Markets Active')
    elif market_close_day=='Saturday' or market_close_day=='Sunday':
        timelbl.config(text=time_string+' IST\nIndian Markets Inactive')     
    timelbl.after(1000,time_)

font=('Bahnschrift',8,'bold')
timelbl=Button(frame,font=font,bg='white',activebackground='white',fg='black',width=40,height=2,relief='sunken',bd=0)
timelbl.pack(side=RIGHT,padx= 50)
ToolTip(timelbl,msg='Time',delay=0.5)
time_()

img1=ImageTk.PhotoImage(Image.open('Path to home.png'))
home_button=Button(frame,image=img1,bg='white',activebackground='white',width=45,height=35,relief='sunken',bd=0)
home_button.pack(side=LEFT,padx= 143)
ToolTip(home_button,msg='Home',delay=0.5)

img2=ImageTk.PhotoImage(Image.open('Path to graph.png'))
markets_button=Button(frame,image=img2,bg='white',activebackground='white',width=39,height=35,relief='sunken',bd=0)
markets_button.pack(side=LEFT,padx= 128)
ToolTip(markets_button,msg='Markets',delay=0.5)

img3=ImageTk.PhotoImage(Image.open('Path to user.png'))
login_button=Button(frame,image=img3,bg='white',activebackground='white',width=35,height=35,relief='sunken',bd=0)
login_button.pack(side=RIGHT,padx= 118)
ToolTip(login_button,msg='Login/Sign-up',delay=0.5)

img4=ImageTk.PhotoImage(Image.open('Path to logotransparent.png'))
logo_button=Button(frame,image=img4,bg='white',activebackground='white',height=35,width=44,relief='sunken',bd=0)
logo_button.pack(side=BOTTOM,anchor=CENTER,pady=0.5)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

menubar=Menu(root)
home=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Home',menu=home)
home.add_command(label='Home Page')
home.add_separator()
home.add_command(label='Exit',command=root.destroy)

markets=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Markets',menu=markets)
markets.add_command(label='US Markets')
markets.add_command(label='Global Markets')

stocks_commodities=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Stocks/Commodities',menu=stocks_commodities)

mutual_funds=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Mutual Funds',menu=mutual_funds)

news=Menu(menubar,tearoff=0)
menubar.add_cascade(label='News',menu=news)

calculators=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Calculators',menu=calculators)

user=Menu(menubar,tearoff=0)
menubar.add_cascade(label='User',menu=user)

learn=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Learn',menu=learn)

feedback=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Feedback',menu=feedback)

root.config(menu=menubar)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

def alarmalert():
    market_preopening_time51=datetime.time(8,55,0)
    market_preopening_time52=datetime.time(8,56,0)
    market_preopening_time1=datetime.time(9,0,0)
    market_preopening_time2=datetime.time(9,1,0)
    market_opening_time51=datetime.time(9,10,0)
    market_opening_time52=datetime.time(9,11,0)
    market_opening_time1=datetime.time(9,15,0)
    market_opening_time2=datetime.time(9,16,0)
    market_closing_time51=datetime.time(15,25,0)
    market_closing_time52=datetime.time(15,26,0)
    market_closing_time1=datetime.time(15,30,0)
    market_closing_time2=datetime.time(15,31,0)
    now1=datetime.datetime.now().time()
    market_close_day1=datetime.datetime.now().strftime('%A')

    if market_close_day1!='Saturday' or market_close_day1!='Sunday':
        if market_preopening_time51<=now1<=market_preopening_time52:
            playsound('Path to warningbell.mp3')
        elif market_preopening_time1<=now1<=market_preopening_time2:
            playsound('Path to finalbell.mp3')
        elif market_opening_time51<=now1<=market_opening_time52:
            playsound('Path to warningbell.mp3')
        elif market_opening_time1<=now1<=market_opening_time2:
            playsound('Path to finalbell.mp3')
        elif market_closing_time51<=now1<=market_closing_time52:
            playsound('Path to warningbell.mp3')
        elif market_closing_time1<=now1<=market_closing_time2:
            playsound('Path to finalbell.mp3')
        else:
            root.after(998,alarmalert)
    elif market_close_day1=='Saturday' or market_close_day1=='Sunday':
        root.after(998,alarmalert)

alarmalert()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

root.mainloop()
