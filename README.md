# ecommerce-website
This is clothing e-commerce web application that was conceptualise, design, and developed using Django, an open-source online framework based on Python, that not only fits with current market trends but also fulfils the varied needs and expectations of modern consumers. It is perfect for building web pages and offers an excellent advantage of a dependable database access component. My project's main objective is to develop a user-friendly and intuitive platform that enables clients to easily explore, find, and buy apparel goods. I used Kaggle, a community platform for practitioners, researchers, and enthusiasts interested in data science and machine learning.
## steps for Installation
1. Git clone git@github.com:ZaraIkelua/ecommerceWebsite.git into your repository

2. Navigate into the project folder and set up your environment by using this command
   ```
   cd ecommerceWebsite
   ```
3. Set up your environment within the project folder:
   ```
   pyenv local 3.10.7 # this sets the local version of python to 3.10.7
   python3 -m venv .venv # this creates the virtual environment for you
   source .venv/bin/activate # this activates the virtual environment
   pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
   ```
4. Install django using bellow command using your configured pip or pip3
   ```
   pip install Django==4.1.2
   ```
5. install the requirements.txt file by running this command:
   ```
   pip install -r requirements.txt
   ```
6. Create superuser 
   ```
   python manage.py createsuperuser
   ```
7. Migrate all the database
   ```
   python manage.py migrate
   ```

8. # Start the Server
   ## To run on Local Machine
   ```
   python3 manage.py runserver
   ```
   ## To run on Codio
   ```
   python3 manage.py runserver 0.0.0.0:8000
   ```


