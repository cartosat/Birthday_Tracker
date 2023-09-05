sudo chown -R vips \
    /home/vips \
    /workspace
sudo chmod 600 ~/.ssh/*
source /home/vips/.bashrc
python3 manage.py runserver 0.0.0.0:8000
