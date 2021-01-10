from selenium import webdriver
import pandas as pd
import folium

options = webdriver.ChromeOptions()
options.add_argument("headless")
desired_capabilities = options.to_capabilities()
driver = webdriver.Chrome(desired_capabilities=desired_capabilities)


file_encoding = 'cp1252'        # set file_encoding to the file encoding (utf8, latin1, etc.)


#Display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

path = 'C:/Users/a_khl/PycharmProjects/longitude/data/'

hotel_infos = 'infos.json'
#
hotel_infos_fd = f"{path}{hotel_infos}"



df_info = pd.read_json(hotel_infos_fd, lines=True)

gmaps_url = 'https://www.google.com/maps/search/'


def latitude(address):

    if address:


        search_url = gmaps_url + address

        driver.get(search_url)
        url = driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content')

        latitude = url.split('?center=')[1].split('&zoom=')[0].split('%2C')[0]

        # driver.close()

    else:
        latitude = 0

    return latitude

def longitude(address):

    if address:

        search_url = gmaps_url + address

        driver.get(search_url)
        url = driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content')

        longitude = url.split('?center=')[1].split('&zoom=')[0].split('%2C')[1]

        # driver.close()

    else:
        longitude = 0

    return longitude

#
df_info['latitude'] = df_info['address'].apply(latitude)
df_info['longitude'] = df_info['address'].apply(longitude)

print(df_info.head())
print(df_info['general_appreciation'].unique())

df_info.to_json(f"{path}infos2.json", orient='records', lines=True)