<h1>Hardware </h1>

Raspbery Pi, ina260 sensors, ads1115

<h1>Software </h1>

Raspberypi_os, python

<h1>How do install </h1>

sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
    
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo systemctl enable docker.service

sudo systemctl enable containerd.service

sudo docker run -d --restart always -p 3000:3000 --name grafana --net=host grafana/grafana
 
#run script in prometheus.txt
#run script in node.txt
#run script in rpi.txt   
pip install prometheus_client

#Add to crontab python script
#and add backup script for prometheus data

crontab -e

@reboot python /home/pi/ina_project/main.py
0 12 * * * tar -zcf /var/backups/prometheus.tgz /home/pi/prometheus

