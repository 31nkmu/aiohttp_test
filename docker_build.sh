docker build -t test_image:0.0.1 . && docker run -d --rm --name=test_image -p 5001:5000 test_image:0.0.1 python3 main.py
