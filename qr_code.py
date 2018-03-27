from pygooglechart import QRChart
import os.path 
import random

f = open('url.csv')
urls=f.readlines()

ctr = 0
for each in urls:
     ctr=ctr+1
     
     cols = each.split('|')
     
     url = cols[0]
     filename = cols[1]
     imgsize = cols[2].split(',')
     
     imgwidth = int(imgsize[0])
     imgheight = int(imgsize[1])     
     
     saveas =  r"%s\%s" % (cols[3].strip(),filename)
     #print saveas
          
     if os.path.exists("%s%s" % (saveas,".png")):
          saveas  = "%s_dup%s" % (saveas,random.randint(1, 1000))
          #print "exists", saveas
     

     chart = QRChart(imgwidth,imgheight)          
     chart.add_data(url)
     chart.set_ec('H', 0)     
#     Trocar o H por um L faz com que aparecem menos pontos da geracao do codigo     

     chart.download("%s.png" % (saveas))
     
     #var = raw_input("Press any key to continue...")     
     

#print "end"     