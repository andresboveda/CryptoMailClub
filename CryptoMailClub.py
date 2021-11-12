Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

#!/usr/bin/python3.8
import urllib3
urllib3.disable_warnings()
import requests, bs4
from mailjet_rest import Client

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

#scraping all the websites

res7 = requests.get('https://ambcrypto.com/category/new-news/', headers=hdr)
res7.raise_for_status()
ambSoup = bs4.BeautifulSoup(res7.text, 'html.parser')

ambheadlines_raw = ambSoup.find_all('h2')
ambheadlines_clean = [el.text for el in ambheadlines_raw]
del ambheadlines_clean[0]

amblinks_raw = []
for link in ambSoup.find_all("section", {"id": "mvp-feat6-wrap"}):
    amblinks_raw.append(link.find('a')['href'])

amblinks_raw2 = []
for link in ambSoup.find_all("li", {"class": "mvp-blog-story-wrap left relative infinite-post"}):
    amblinks_raw2.append(link.find('a')['href'])

amblinks_final = amblinks_raw + amblinks_raw2

res8 = requests.get('https://bitcoinist.com/', headers=hdr)
res8.raise_for_status()
bitcoinistSoup = bs4.BeautifulSoup(res8.text, 'html.parser')

bitcoinist_h1 = bitcoinistSoup.find_all('h2', {"class": "jeg_post_title"})
bitcoinist_h2 = [el.text for el in bitcoinist_h1]
bitcoinist_l1 = []
for link in bitcoinistSoup.find_all('h2', {"class": "jeg_post_title"}):
    bitcoinist_l1.append(link.find('a')['href'])

bitcoinist_h3 = bitcoinistSoup.find_all('h3', {"class": "jeg_post_title"})
bitcoinist_h4 = [el.text for el in bitcoinist_h3]
bitcoinist_l2 = []
for link in bitcoinistSoup.find_all('h3', {"class": "jeg_post_title"}):
    bitcoinist_l2.append(link.find('a')['href'])

bitcoinist_hFinal = bitcoinist_h2 + bitcoinist_h4
bitcoinist_lFinal = bitcoinist_l1 + bitcoinist_l2

res3 = requests.get('https://bitcoinmagazine.com/', headers=hdr)
res3.raise_for_status()
bitcoinmagSoup = bs4.BeautifulSoup(res3.text, 'html.parser')

bitcoinmagRaw = bitcoinmagSoup.find_all("a", {"phx-track-id": "Title"})
bitcoinmag_headline = [el.text for el in bitcoinmagRaw]
bitcoinmag_head_clean = list(dict.fromkeys(bitcoinmag_headline))
del bitcoinmag_head_clean[4:8]

linksbitcoinmag_raw = bitcoinmagSoup.find_all("a", {"phx-track-id": "Title"})
linksbitcoinmag = [i.get('href') for i in linksbitcoinmag_raw]
linksbitcoinmag_full = ["https://bitcoinmagazine.com" + elem for elem in linksbitcoinmag]
linksbitcoinmag_final = list(dict.fromkeys(linksbitcoinmag_full))
del linksbitcoinmag_final[4:8]

res = requests.get('https://www.coindesk.com/', headers=hdr)
res.raise_for_status()
coindeskSoup = bs4.BeautifulSoup(res.text, 'html.parser')
titularescoindeskraw = coindeskSoup.find_all("div", {"class": "live-wirestyles__Title-sc-1xrlfqv-3 iNnArA"})
titularescoindesk = [el.text for el in titularescoindeskraw]

linkcoindesk1 = []
for link in coindeskSoup.find_all("div", {"class": "live-wirestyles__Title-sc-1xrlfqv-3 iNnArA"}):
    linkcoindesk1.append(link.find('a')['href'])
linkscoindeskfull = ["https://www.coindesk.com" + elem for elem in linkcoindesk1]

res13 = requests.get('https://coingape.com/category/news/', headers=hdr)
res13.raise_for_status()
gapeSoup = bs4.BeautifulSoup(res13.text, 'html.parser')

gape_h1 = gapeSoup.find_all('h3', {"class": "entry-title mh-posts-list-title"})
gape_h2 = [el.text for el in gape_h1]

gape_l1 = []
for link in gapeSoup.find_all("h3", {"class": "entry-title mh-posts-list-title"}):
    gape_l1.append(link.find('a')['href'])

res1 = requests.get('https://cointelegraph.com/', headers=hdr)
res1.raise_for_status()
cointeleSoup = bs4.BeautifulSoup(res1.text, 'html.parser')
carouselcointeleRaw = cointeleSoup.find_all("a", {"class": "main-news-controls__link"})
headline_carousel_cointele = [el.text for el in carouselcointeleRaw]
postcardRaw = cointeleSoup.find_all("a", {"class": "post-card__title-link"})
postcardClean = [el.text for el in postcardRaw]
total_cointele_headline = headline_carousel_cointele + postcardClean
total_cointele_headline2 = list(dict.fromkeys(total_cointele_headline))


linkscointele_carousel_raw = cointeleSoup.select("[class~=main-news-controls__link]")
linkscointele_carousel_clean = [i.get('href') for i in linkscointele_carousel_raw]
links_cointele_carousel_full = ["https://cointelegraph.com" + elem for elem in linkscointele_carousel_clean]
links_postcard_raw = cointeleSoup.select("[class~=post-card__title-link]")
links_postcard_clean = [i.get('href') for i in links_postcard_raw]
links_postcard_full = ["https://cointelegraph.com" + elem for elem in links_postcard_clean]
total_links = links_cointele_carousel_full + links_postcard_full
total_links2 = list(dict.fromkeys(total_links))

res6 = requests.get('https://cryptoslate.com/', headers=hdr)
res6.raise_for_status()
csSoup = bs4.BeautifulSoup(res6.text, 'html.parser')

headlines1_raw = []
for headline in csSoup.find_all("div", {"class": "list-post clearfix"}):
    headlines1_raw.append(headline.find('a')['title'])
for headline in csSoup.find_all("div", {"class": "list-post clearfix edge"}):
    headlines1_raw.append(headline.find('a')['title'])
csheadlines_final = list(dict.fromkeys(headlines1_raw))

links1_raw = []
for link in csSoup.find_all("div", {"class": "list-post clearfix"}):
    links1_raw.append(link.find('a')['href'])
for link in csSoup.find_all("div", {"class": "list-post clearfix edge"}):
    links1_raw.append(link.find('a')['href'])

cslinks_final = list(dict.fromkeys(links1_raw))

res10 = requests.get('https://dailyhodl.com/news/', headers=hdr)
res10.raise_for_status()
dailyhodlSoup = bs4.BeautifulSoup(res10.text, 'html.parser')

dailyheadline1 = dailyhodlSoup.find_all('h3')
dailyheadline2 = [el.text for el in dailyheadline1]
dailyheadline3 = list(dict.fromkeys(dailyheadline2))

dailylinks1 = []
for link in dailyhodlSoup.find_all("h3"):
    dailylinks1.append(link.find('a')['href'])

dailylinks2 = list(dict.fromkeys(dailylinks1))

res11 = requests.get('https://decrypt.co', headers=hdr)
res11.raise_for_status()
decryptSoup = bs4.BeautifulSoup(res11.text, 'html.parser')

decrypt_h1 = decryptSoup.find_all('h2')
decrypt_h2 = [el.text for el in decrypt_h1]
decrypt_h3 = decrypt_h2[:6]

decrypt_l1 = []
for links in decryptSoup.find_all('div', {"class": "sc-1kjt2eu-1 bOEcTJ GridItem"}):
    decrypt_l1.append(links.find('a')['href'])

decrypt_l2 = []
for links in decryptSoup.find('ul', {"class": "sc-17zo80w-0 eMmRzd"}):
    decrypt_l2.append(links.find('a')['href'])

decrypt_l3 = decrypt_l1 + decrypt_l2
decrypt_l4 = ["https://decrypt.co" + elem for elem in decrypt_l3]

res9 = requests.get('https://www.theblockcrypto.com/', headers=hdr)
res9.raise_for_status()
theblockSoup = bs4.BeautifulSoup(res9.text, 'html.parser')

theblock_h1 = theblockSoup.find_all('h3', {"class": "font-headline mb-2 font-size-15"})
theblock_h2 = [el.text for el in theblock_h1]

theblock_l1 = theblockSoup.find_all('a', {"class": "theme color-outer-space"})
theblock_l2 = [i.get('href') for i in theblock_l1]
theblock_l3 = ["https://www.theblockcrypto.com" + elem for elem in theblock_l2]

res15 = requests.get('https://coinmarketcap.com/headlines/news/', headers=hdr)
res15.raise_for_status()
cmcSoup = bs4.BeautifulSoup(res15.text, 'html.parser')

cmc_h1 = cmcSoup.find_all('div', {"class": "sc-16r8icm-0 bvDXFe"})
cmc_h2 = [el.text for el in cmc_h1]

cmc_l1 = []
for link in cmcSoup.find_all('div', {"class": "sc-16r8icm-0 bvDXFe"}):
    cmc_l1.append(link.find('a')['href'])

cmc_l2 = [w.replace('/headlines/news/', 'https://coinmarketcap.com/headlines/news/') for w in cmc_l1]



#sending mail

api_key = 'MAILJET API KEY HERE'
api_secret = 'MAILJET SECRET API KEY HERE'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
	{
	  "From": {
		"Email": "YOUR SENDER EMAIL HERE",
		"Name": "YOUR SENDER NAME HERE"
	  },
	  "To": [
		{
		  "Email": "RECEIVER EMAIL HERE",
		  "Name": "RECEIVER NAME HERE"
		}
	  ],
	  "Subject": "Your Daily Crypto Headlines",
	  "HTMLPart": "<img src='https://i.postimg.cc/66MVkkkD/Logo-Crypto-Mail-Club-web-002.jpg' alt='email header' width='156' height='156'><br /><br />Follow us on  <a href='https://www.instagram.com/cryptomailclub/'><img src='https://i.postimg.cc/t4H5yT7Z/insta-logo.png' alt='email header' width='16' height='16'></a><br /><br />Today's Featured Stories:<br /><br /><b>CoinDesk</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>Cointelegraph</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>Coinmarketcap - Just In Aggregator</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>Decrypt</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>AMBCrypto</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>CoinGape</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>The Block</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>The Daily Hodl</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>Bitcoin Magazine</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br />" \
	  "<b>CryptoSlate</b><br />" \
	  "<ul><li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a><br /></li>" \
	  "<li><a href='{}'>{}</a></li></ul><br /><br />" \
	  "<b>Happy reading!</b><br />**************<br /><br /><br />" \
	  "Crypto Mail Club is a free service. If you are finding it useful, you can make donations <a href='https://cryptomailclub.org/crypto-mail-club-donations/'>here</a>.<br />" \
	  "Feel free to share <a href ='http://cryptomailclub.org'>cryptomailclub.org</a> with others who might enjoy it.<br /><br />" \
	  "You can also unsubscribe anytime, just click <a href='[[UNSUB_LINK_EN]]'>here</a>.<br />".format(linkscoindeskfull[0],titularescoindesk[0], \
	  linkscoindeskfull[1],titularescoindesk[1], \
	  linkscoindeskfull[2],titularescoindesk[2], \
	  linkscoindeskfull[3],titularescoindesk[3], \
	  linkscoindeskfull[4],titularescoindesk[4], \
	  linkscoindeskfull[5],titularescoindesk[5], \
	  linkscoindeskfull[6],titularescoindesk[6], \
	  linkscoindeskfull[7],titularescoindesk[7], \
	  total_links2[0],total_cointele_headline2[0], \
	  total_links2[1],total_cointele_headline2[1], \
	  total_links2[2],total_cointele_headline2[2], \
	  total_links2[3],total_cointele_headline2[3], \
	  total_links2[4],total_cointele_headline2[4], \
	  total_links2[5],total_cointele_headline2[5], \
	  total_links2[6],total_cointele_headline2[6], \
	  cmc_l2[0],cmc_h2[0], \
	  cmc_l2[1],cmc_h2[1], \
	  cmc_l2[2],cmc_h2[2], \
	  cmc_l2[3],cmc_h2[3], \
	  cmc_l2[4],cmc_h2[4], \
	  cmc_l2[5],cmc_h2[5], \
	  cmc_l2[6],cmc_h2[6], \
	  cmc_l2[7],cmc_h2[7], \
	  cmc_l2[8],cmc_h2[8], \
	  cmc_l2[9],cmc_h2[9], \
	  cmc_l2[10],cmc_h2[10], \
	  cmc_l2[11],cmc_h2[11], \
	  cmc_l2[12],cmc_h2[12], \
	  cmc_l2[13],cmc_h2[13], \
	  cmc_l2[14],cmc_h2[14], \
	  decrypt_l4[0],decrypt_h3[0], \
	  decrypt_l4[1],decrypt_h3[1], \
	  decrypt_l4[2],decrypt_h3[2], \
	  decrypt_l4[3],decrypt_h3[3], \
	  decrypt_l4[4],decrypt_h3[4], \
	  amblinks_final[0],ambheadlines_clean[0], \
	  amblinks_final[1],ambheadlines_clean[1], \
	  amblinks_final[2],ambheadlines_clean[2], \
	  amblinks_final[3],ambheadlines_clean[3], \
	  amblinks_final[4],ambheadlines_clean[4], \
	  amblinks_final[5],ambheadlines_clean[5], \
	  amblinks_final[6],ambheadlines_clean[6], \
	  amblinks_final[7],ambheadlines_clean[7], \
	  gape_l1[0],gape_h2[0], \
	  gape_l1[1],gape_h2[1], \
	  gape_l1[2],gape_h2[2], \
	  gape_l1[3],gape_h2[3], \
	  gape_l1[4],gape_h2[4], \
	  gape_l1[5],gape_h2[5], \
	  gape_l1[6],gape_h2[6], \
	  gape_l1[7],gape_h2[7], \
	  gape_l1[8],gape_h2[8], \
	  gape_l1[9],gape_h2[9], \
	  theblock_l3[0],theblock_h2[0], \
	  theblock_l3[1],theblock_h2[1], \
	  theblock_l3[2],theblock_h2[2], \
	  theblock_l3[3],theblock_h2[3], \
	  theblock_l3[4],theblock_h2[4], \
	  theblock_l3[5],theblock_h2[5], \
	  theblock_l3[6],theblock_h2[6], \
	  theblock_l3[7],theblock_h2[7], \
	  dailylinks2[0],dailyheadline3[0], \
	  dailylinks2[1],dailyheadline3[1], \
	  dailylinks2[2],dailyheadline3[2], \
	  dailylinks2[3],dailyheadline3[3], \
	  dailylinks2[4],dailyheadline3[4], \
	  dailylinks2[5],dailyheadline3[5], \
	  dailylinks2[6],dailyheadline3[6], \
	  linksbitcoinmag_final[0],bitcoinmag_head_clean[0], \
	  linksbitcoinmag_final[1],bitcoinmag_head_clean[1], \
	  linksbitcoinmag_final[2],bitcoinmag_head_clean[2], \
	  linksbitcoinmag_final[3],bitcoinmag_head_clean[3], \
	  linksbitcoinmag_final[4],bitcoinmag_head_clean[4], \
	  linksbitcoinmag_final[5],bitcoinmag_head_clean[5], \
	  linksbitcoinmag_final[6],bitcoinmag_head_clean[6], \
	  linksbitcoinmag_final[7],bitcoinmag_head_clean[7], \
	  linksbitcoinmag_final[8],bitcoinmag_head_clean[8], \
	  linksbitcoinmag_final[9],bitcoinmag_head_clean[9], \
	  cslinks_final[0],csheadlines_final[0], \
	  cslinks_final[1],csheadlines_final[1], \
	  cslinks_final[2],csheadlines_final[2], \
	  cslinks_final[3],csheadlines_final[3], \
	  cslinks_final[4],csheadlines_final[4], \
	  cslinks_final[5],csheadlines_final[5], \
	  cslinks_final[6],csheadlines_final[6], \
	  cslinks_final[7],csheadlines_final[7], \
	  cslinks_final[8],csheadlines_final[8], \
	  cslinks_final[9],csheadlines_final[9])
	}
  ]
}
result = mailjet.send.create(data=data)

print("Program is running OK")

