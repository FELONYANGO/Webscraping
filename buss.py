import bs4  
import requests  
from datetime import datetime
  
#Creating the requests  
  
res = requests.get("https://myride.ometro.com/Schedule?stopCode=3060&routeNumber=5&directionName=EAST")  

  
# Convert the request object to the Beautiful Soup Object  
soup = bs4.BeautifulSoup(res.text,'html5lib')  


soup.select('.schedule')  
for i in soup.select('.schedule'):  
         now = datetime.now()
         

         current_time = now.strftime("%H:%M")
         print("Current Time =", current_time,'\n') 
         print("the next bus will follow in :",soup.stop,'\n')
         print ("the following bus willl arrive in: ",soup.stop,"\n")   
         
         #print(i.text,end = ',')  