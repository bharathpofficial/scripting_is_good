from dotenv import load_dotenv
import requests, os, time, fontstyle

def configure():
    load_dotenv()
configure()

# def check_IP(self, ip):
#     self.CHK_IP=ip

class CheckThisIP:
	def __init__(self, ips=0):
		self.CHK_IP='0.0.0.0'
		self.data=''
		self.raw=''
		if ips == 0:
			return
		self.looper(ips)
	
	def get_raw(self):
		"""Actuall GET request and Receives .json Output"""
		url = "https://fraudsentinel.p.rapidapi.com/sentinel.json"
		querystring = {"ip": self.CHK_IP}
		headers = {
			"X-RapidAPI-Key": os.getenv('api_key'),
			"X-RapidAPI-Host": "fraudsentinel.p.rapidapi.com"
		}
		response = requests.get(url, headers=headers, params=querystring)
		raw = response.json()
		# print(raw) # Testing Purpose
		return raw
	

	# Test ip 49.205.197.139
	def normalize(self):
		"""used to make ease the work of typing loong get('')"""
		self.raw = self.get_raw()
		
		data = {
			'Flag' : self.raw.get('Flag'),
			'IP' : self.raw.get('IP'),
			'User-Agent' : self.raw.get('User-Agent'),
			'Timestamp' : self.raw.get('Timestamp'),
			'GEO' : self.raw.get('GEO'),
			'Tags' : self.raw.get('Tags'), # List to access [index]
		}
		try:
			more_data = {
				'karma' : self.raw.get('live').get('karma'),
				'good_karma' : self.raw.get('live').get('good_karma'),
				'isDynamic' : self.raw.get('live').get('details').get('DYNAMICIP')
				}
			data.update(more_data)
		except AttributeError as noDynamic:
			pass
		try:
			more_data = {
				'Reason' : self.raw.get('Reason'),
				'db' : self.raw.get('Non-Residential')
				}
			data.update(more_data)
		except AttributeError as nothing:
			pass
		# print(data) # Testing Purpose
		return data
		
	
	def outify(self):
		data = self.normalize()
		print(f'''
		===================================================================================
			{fontstyle.apply('note: consider this to be not even "first layer" of securiy.','ITALIC/FAINT')}
				{time.ctime(data.get('Timestamp'))}''')
		if data.get('Flag') != 'Allow':
			print(f'''
				{fontstyle.apply(f'{self.CHK_IP} is Fishy.','RED_BG/WHITE/BOLD')}''')
		else:
			print(f'''
				{fontstyle.apply(f'{self.CHK_IP} seems Legit.','GREEN_BG/WHITE/BOLD')}''')
		try:
			print(f"""
		 	Reason: {data.get('Reason')}
			dynamicIP: {data.get('isDynamic')}""")
		except:
			pass
		print(f"""
			GEO: {data.get('GEO')}
			Tags: {data.get('Tags')}
			""")

	# def printC(self):
		# print(self.CHK_IP)
	def isOk(self):
		try:
			self.outify()
		except requests.exceptions.JSONDecodeError as invalidIP:
			print(f'INVALID IP --> {self.CHK_IP}')

	def looper(self, ips):
		if isinstance(ips, list):
			for serial,ip in enumerate(ips):
				print(serial+1)
				self.CHK_IP=ip
				self.isOk()
		else:
			self.CHK_IP = ips
			self.isOk()
		return

ipList = ['103.255.190.123', '103.207.4.222']
chkObj = CheckThisIP('91.92.249.48')
# print(type(chkObj))
# chkObj.CHK_IP='188.132.232.227'
# chkObj.isOk()
# chkObj.printC()
# for ip in ipList:
# 	chkObj.CHK_IP = ip
# 	chkObj.isOk()
# 122.170.10.21 fishy IP
# 12.44.216.98  fishy IP
# 43.153.78.101
# requests.exceptions.JSONDecodeError  when IP is invalid
# chkObj.printC()


    