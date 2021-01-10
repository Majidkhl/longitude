# from IPython.display import IFrame
# import folium
#

#
#
# hotel_excel = df_info[df_info['avg_review'] == 'Excellent']
# hotel_tb = df_info[df_info['avg_review'] == 'Très bon']
# hotel_moyen = df_info[df_info['avg_review'] == 'Moyen']
# hotel_mediocre = df_info[df_info['avg_review'] == 'Médiocre']
# hotel_horrible = df_info[df_info['avg_review'] == 'Horrible']
# hotel_none = df_info[df_info['avg_review'] == None]

#
# mel_map = folium.Map([-37.8, 145], tiles='CartoDB positron')
#
# for lat, long, name, full_address in zip(mel_large.lat, mel_large.long, mel_large.Charity_Legal_Name,
#                                          mel_large.Full_Address):
#     folium.Marker([lat, long],
#                   icon=folium.CustomIcon(icon_image='https://i.imgur.com/CYx04oC.png', icon_size=(10, 10)),
#                   popup=name + '\n\n' + full_address).add_to(mel_map)
#
# for lat, long, name, full_address in zip(mel_medium.lat, mel_medium.long, mel_medium.Charity_Legal_Name,
#                                          mel_medium.Full_Address):
#     folium.Marker([lat, long],
#                   icon=folium.CustomIcon(icon_image='https://imgur.com/Rzs4Zpa.png', icon_size=(8, 8)),
#                   popup=name + '\n\n' + full_address).add_to(mel_map)
#
# for lat, long, name, full_address in zip(mel_small.lat, mel_small.long, mel_small.Charity_Legal_Name,
#                                          mel_small.Full_Address):
#     folium.Marker([lat, long],
#                   icon=folium.CustomIcon(icon_image='https://imgur.com/6TWrNOY.png', icon_size=(6, 6)),
#                   popup=name + '\n\n' + full_address).add_to(mel_map)
#
# for lat, long, name, full_address in zip(mel_other.lat, mel_other.long, mel_other.Charity_Legal_Name,
#                                          mel_other.Full_Address):
#     folium.Marker([lat, long],
#                   icon=folium.CustomIcon(icon_image='https://imgur.com/C1MXk3r.png', icon_size=(4, 4)),
#                   popup=name + '\n\n' + full_address).add_to(mel_map)
#
# mel_map.save('mel_map.html')
# IFrame(src='mel_map.html', width='100%', height=500)
