import requests, pprint
from myjab_cowin_client import CowinClient

def getStateByID(states, findState):
	for state in states:
		state_name = state.get("state_name")
		state_id = state.get("state_id")
		if state_name.replace(" ","").lower() == findState.lower():
			return state_id

def getDistrictByID(districts, findDistrict):
	for district in districts:
		district_name = district.get("district_name")
		district_id = district.get("district_id")
		if district_name.replace(" ","").lower() == findDistrict.lower():
			return district_id

## Host Domain for the vaccine enquiries
hostDomain = "https://cdn-api.co-vin.in/"

## Api version may change.
## This is the version at the time of development
apiVersion = "api/v2/"

myState = "madhyapradesh"
myDistrict = "gwalior"

ALL_STATES = [{"state_id":1,"state_name":"Andaman and Nicobar Islands"},
		      {"state_id":2,"state_name":"Andhra Pradesh"},
		      {"state_id":3,"state_name":"Arunachal Pradesh"},
		      {"state_id":4,"state_name":"Assam"},
		      {"state_id":5,"state_name":"Bihar"},
		      {"state_id":6,"state_name":"Chandigarh"},
		      {"state_id":7,"state_name":"Chhattisgarh"},
		      {"state_id":8,"state_name":"Dadra and Nagar Haveli"},
		      {"state_id":9,"state_name":"Delhi"},
		      {"state_id":10,"state_name":"Goa"},
		      {"state_id":11,"state_name":"Gujarat"},
		      {"state_id":12,"state_name":"Haryana"},
		      {"state_id":13,"state_name":"Himachal Pradesh"},
		      {"state_id":14,"state_name":"Jammu and Kashmir"},
		      {"state_id":15,"state_name":"Jharkhand"},
		      {"state_id":16,"state_name":"Karnataka"},
		      {"state_id":17,"state_name":"Kerala"},
		      {"state_id":18,"state_name":"Ladakh"},
		      {"state_id":19,"state_name":"Lakshadweep"},
		      {"state_id":20,"state_name":"Madhya Pradesh"},
		      {"state_id":21,"state_name":"Maharashtra"},
		      {"state_id":22,"state_name":"Manipur"},
		      {"state_id":23,"state_name":"Meghalaya"},
		      {"state_id":24,"state_name":"Mizoram"},
		      {"state_id":25,"state_name":"Nagaland"},
		      {"state_id":26,"state_name":"Odisha"},
		      {"state_id":27,"state_name":"Puducherry"},
		      {"state_id":28,"state_name":"Punjab"},
		      {"state_id":29,"state_name":"Rajasthan"},
		      {"state_id":30,"state_name":"Sikkim"},
		      {"state_id":31,"state_name":"Tamil Nadu"},
		      {"state_id":32,"state_name":"Telangana"},
		      {"state_id":33,"state_name":"Tripura"},
		      {"state_id":34,"state_name":"Uttar Pradesh"},
		      {"state_id":35,"state_name":"Uttarakhand"},
		      {"state_id":36,"state_name":"West Bengal"},
		      {"state_id":37,"state_name":"Daman and Diu"}]

MP_DISTRICTS = [{"district_id":320,"district_name":"Agar"},
				{"district_id":357,"district_name":"Alirajpur"},
				{"district_id":334,"district_name":"Anuppur"},
				{"district_id":354,"district_name":"Ashoknagar"},
				{"district_id":338,"district_name":"Balaghat"},
				{"district_id":343,"district_name":"Barwani"},
				{"district_id":362,"district_name":"Betul"},
				{"district_id":351,"district_name":"Bhind"},
				{"district_id":312,"district_name":"Bhopal"},
				{"district_id":342,"district_name":"Burhanpur"},
				{"district_id":328,"district_name":"Chhatarpur"},
				{"district_id":337,"district_name":"Chhindwara"},
				{"district_id":327,"district_name":"Damoh"},
				{"district_id":350,"district_name":"Datia"},
				{"district_id":324,"district_name":"Dewas"},
				{"district_id":341,"district_name":"Dhar"},
				{"district_id":336,"district_name":"Dindori"},
				{"district_id":348,"district_name":"Guna"},
				{"district_id":313,"district_name":"Gwalior"},
				{"district_id":361,"district_name":"Harda"},
				{"district_id":360,"district_name":"Hoshangabad"},
				{"district_id":314,"district_name":"Indore"},
				{"district_id":315,"district_name":"Jabalpur"},
				{"district_id":340,"district_name":"Jhabua"},
				{"district_id":353,"district_name":"Katni"},
				{"district_id":339,"district_name":"Khandwa"},
				{"district_id":344,"district_name":"Khargone"},
				{"district_id":335,"district_name":"Mandla"},
				{"district_id":319,"district_name":"Mandsaur"},
				{"district_id":347,"district_name":"Morena"},
				{"district_id":352,"district_name":"Narsinghpur"},
				{"district_id":323,"district_name":"Neemuch"},
				{"district_id":326,"district_name":"Panna"},
				{"district_id":359,"district_name":"Raisen"},
				{"district_id":358,"district_name":"Rajgarh"},
				{"district_id":322,"district_name":"Ratlam"},
				{"district_id":316,"district_name":"Rewa"},
				{"district_id":317,"district_name":"Sagar"},
				{"district_id":333,"district_name":"Satna"},
				{"district_id":356,"district_name":"Sehore"},
				{"district_id":349,"district_name":"Seoni"},
				{"district_id":332,"district_name":"Shahdol"},
				{"district_id":321,"district_name":"Shajapur"},
				{"district_id":346,"district_name":"Sheopur"},
				{"district_id":345,"district_name":"Shivpuri"},
				{"district_id":331,"district_name":"Sidhi"},
				{"district_id":330,"district_name":"Singrauli"},
				{"district_id":325,"district_name":"Tikamgarh"},
				{"district_id":318,"district_name":"Ujjain"},
				{"district_id":329,"district_name":"Umaria"},
				{"district_id":355,"district_name":"Vidisha"}]

cowin = CowinClient(host_domain=hostDomain, credentials=None, api_version=apiVersion)

try:
	states = cowin.get_states()
except:
	print("API could not be reached for accessing states. Accessing cached value")
	states = ALL_STATES

stateID = getStateByID(states, findState=myState)

try:
	districts = cowin.get_districts_list(stateID)
except:
	print("API could not be reached for accessing districts. Accessing cached value")
	districts = MP_DISTRICTS

district_id = getDistrictByID(districts, findDistrict=myDistrict)
print(district_id)