from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from pyairmore.services.device import DeviceService
from pyairmore.services.messaging import MessagingService

class Messenger :    
   
    def sendMessage (ip,mobileNumber,textMessage) :
       # ip="192.168.1.3"
        androidIP = IPv4Address(str(ip))
        androidSession = AirmoreSession(androidIP)
        print(androidSession.is_server_running)
        # importing required modules
        # getting receiver mobile number
       # mobileNumber = "+20120040626"
        # getting text message
        #textMessage = "Test python app"
      
        # creating session
        androidSession = AirmoreSession(androidIP)
        # creating an instance of messaging service of AirMore among all services available
        smsService = MessagingService(androidSession)
        # sending text message using messaging service of AirMore
        smsService.send_message(mobileNumber,textMessage)
        #print(output)
        service = DeviceService(androidSession)
        details = service.fetch_device_details()
        details.power  # 0.65
        print(details.brand)  # True
        details.resolution  # (1080, 1920) tuple
        service = MessagingService(androidSession)
        messages = service.fetch_message_history()
        print(messages)