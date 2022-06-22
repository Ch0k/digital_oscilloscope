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

sudo docker run \
    -d --restart always
    -p 9090:9090 --network host \
    -v /home/pi/ina_project/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
    
pip install prometheus_client

    
