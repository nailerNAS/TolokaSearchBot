#! /bin/bash

systemctl status toloka
sudo systemctl enable toloka
sudo systemctl restart toloka
systemctl status toloka
