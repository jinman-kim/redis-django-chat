python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo docker-compose -f redis-compose.yml up -d
sudo docker-compose- f selenium-compose.yml up -d

