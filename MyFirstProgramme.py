import requests
import time
from datetime import datetime 

def check_website(url):
        try:
                response = requests.get(url)
                if response.status_code == 200:
                        return True
        except Exception as e:
                print(f"Error: {e}")
                return False

def main():
        website_url = "https://www.google.com"
        while True:
                is_available = check_website (website_url)
                
                if is_available:
                        print("up hhhnow")
                else:
                        print ("down")

                        

if __name__ == "__main__":
    main()