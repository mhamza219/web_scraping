# import requests

# def fetchAndSaveToFile(url, path):
# 	r = requests.get(url)
# 	with open(path, "w") as f:
# 		f.write(r.text)

# url = "https://timesofindia.indiatimes.com/india/karnataka-cm-announces-4-lakh-life-accident-cover-for-gig-workers/articleshow/101584388.cms"

# fetchAndSaveToFile(url, "data/times.html")



# import requests
# from bs4 import BeautifulSoup
# import random
# import stem.process

'''
def rotate_proxy():
    with stem.process.launch_tor_with_config(
            tor_cmd="tor",
            config={
                'SocksPort': str(random.randint(5000, 9999)),
                'ExitNodes': '{us}',
            },
    ) as tor_process:
        session = requests.session()
        session.proxies = {
            'http': 'socks5://127.0.0.1:{}'.format(tor_process.socks_port),
            'https': 'socks5://127.0.0.1:{}'.format(tor_process.socks_port),
        }
        return session
'''




# def scrape_twitter_profile(profile_url):
#     # Send a GET request to the profile URL
#     response = requests.get(profile_url)

#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract the required information from the parsed HTML
#     biography_elem = soup.find('div', {'class': 'ProfileHeaderCard-bio'})
#     biography = biography_elem.text.strip() if biography_elem else None

#     followers_count_elem = soup.find('a', {'href': '/{}/followers'.format(profile_url.split('/')[-1])})
#     followers_count = int(followers_count_elem.find('span', {'class': 'css-901oao'}).text.replace(',', '')) if followers_count_elem else None

#     following_count_elem = soup.find('a', {'href': '/{}/following'.format(profile_url.split('/')[-1])})
#     following_count = int(following_count_elem.find('span', {'class': 'css-901oao'}).text.replace(',', '')) if following_count_elem else None

#     likes_count_elem = soup.find('a', {'href': '/{}/likes'.format(profile_url.split('/')[-1])})
#     likes_count = int(likes_count_elem.find('span', {'class': 'css-901oao'}).text.replace(',', '')) if likes_count_elem else None

#     user_id_elem = soup.find('input', {'name': 'user_id'})
#     user_id = int(user_id_elem['value']) if user_id_elem and 'value' in user_id_elem.attrs else None

#     # Return the scraped data
#     return {
#         'biography': biography,
#         'followers_count': followers_count,
#         'following_count': following_count,
#         'likes_count': likes_count,
#         'user_id': user_id
#     }


# profile_url = 'https://twitter.com/sachin_rt'
# scraped_data = scrape_twitter_profile(profile_url)
# print(scraped_data)





'''
# proxy
import requests
import random
from bs4 import BeautifulSoup as bs
import traceback

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content
    soup = bs(requests.get(url).content, 'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxies

url = "http://httpbin.org/ip"
proxies = get_free_proxies()

for i in range(len(proxies)):

    #printing req number
    print("Request Number : " + str(i+1))
    proxy = proxies[i]
    try:
        response = requests.get(url, proxies = {"http":proxy, "https":proxy})
        print(response.json())
    except:
        # if the proxy Ip is pre occupied
        print("Not Available")
'''


import requests
from bs4 import BeautifulSoup
import json

def scrape_twitter_profile(url):
    # Send a GET request to the profile URL
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the profile details
    profile_name_element = soup.find("div", class_="ProfileHeaderCard-name")
    profile_name = profile_name_element.text.strip() if profile_name_element else ""
    
    username_element = soup.find("span", class_="username")
    username = username_element.text.strip() if username_element else ""
    
    location_element = soup.find("span", class_="ProfileHeaderCard-locationText")
    location = location_element.text.strip() if location_element else ""
    
    description_element = soup.find("p", class_="ProfileHeaderCard-bio")
    description = description_element.text.strip() if description_element else ""
    
    followers_count_element = soup.find("li", class_="ProfileNav-item--followers")
    followers_count = followers_count_element.find("span", class_="ProfileNav-value")["data-count"] if followers_count_element else "0"
    
    following_count_element = soup.find("li", class_="ProfileNav-item--following")
    following_count = following_count_element.find("span", class_="ProfileNav-value")["data-count"] if following_count_element else "0"
    
    join_date_element = soup.find("span", class_="ProfileHeaderCard-joinDateText")
    join_date = join_date_element.find("span").text.strip() if join_date_element else ""
    
    tweets_count_element = soup.find("li", class_="ProfileNav-item--tweets")
    tweets_count = tweets_count_element.find("span", class_="ProfileNav-value")["data-count"] if tweets_count_element else "0"
    
    profile_image_url_element = soup.find("img", class_="ProfileAvatar-image")
    profile_image_url = profile_image_url_element["src"] if profile_image_url_element else ""
    
    # Store the data in a dictionary
    data = {
        "name": profile_name,
        "username": username,
        "location": location,
        "description": description,
        "followers_count": int(followers_count),
        "following_count": int(following_count),
        "join_date": join_date,
        "tweets_count": int(tweets_count),
        "profile_image_url": profile_image_url
    }
    
    return data

# Example usage
url = "https://twitter.com/sachin_rt"
profile_data = scrape_twitter_profile(url)
json_data = json.dumps(profile_data, indent=4)
print(json_data)

