import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
import sys

# 실시간 서울의 날씨정보를 저장하는 클래스 city_weather_current
class city_weather_current():
    def __init__(self, cityName, temp, weather_id, weather_descrip):
        self.__cityName = cityName
        self.__temp = temp
        self.__weather_id = weather_id
        self.__weather_descrip = weather_descrip
    def get_cityName(self):
        return self.__cityName
    def get_temp(self):
        return self.__temp
    def get_weather_id(self):
        return self.__weather_id
    def get_weather_descrip(self):
        return self.__weather_descrip



#OpenWeatherMap_api에서 제공하는 kelvin온도 -> 섭씨온도
def Kelvin_temp_to_celsius(Kelvin_temp):
  celsius = Kelvin_temp - 273.15
  return celsius

apikey = "5d8f332ec63368693ae586fc9e84d2de"
city = "Seoul"

#OpenWeatherMap_api 불러오기
OpenWeatherMap_api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(OpenWeatherMap_api)
weather_response = json.loads(result.text)

res_cityName = weather_response["name"]

#임의의 날씨 id 값을 받고싶을 때 수정가능
#ex. res_weather_id = 201
res_weather_id = weather_response["weather"][0]["id"]

res_weather_descrip = weather_response["weather"][0]["description"]
res_temp = Kelvin_temp_to_celsius(weather_response["main"]["temp"])

#실시간으로 받아온 날씨정보 객체화
seoul_weather_data = city_weather_current(res_cityName, res_temp, res_weather_id, res_weather_descrip)

print("[ 현재 {}의 날씨 정보 ]\n".format(seoul_weather_data.get_cityName()))
print("현재 온도(섭씨) : {} 도".format(seoul_weather_data.get_temp()))
print("날씨 : {}(id = {})".format(seoul_weather_data.get_weather_descrip(), seoul_weather_data.get_weather_id()))


def Get_RecomendMusic():
    #스포티파이api 라이브러리 불러오기
    cid = '01227784bc6c4b5984ec45096b774caa'
    secret = '7ac77010ccea44ebbc0eef4eef672427'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # 각 날씨 id값 정보에 어울리는 임의의 추천곡들 삽입
    if(seoul_weather_data.get_weather_id() == 200):
        trackId_list = ["1i1fxkWeaMmKEB4T7zqbzK","2yPoXCs7BSIUrucMdK5PzV","1c8gk2PeTE04A1pIDH9YMk"]
    elif(201):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "34gCuhDGsG4bRPIf9bb02f", "6nek1Nin9q48AVZcWs9e9D"]
    elif(202):
        trackId_list = ["2dLLR6qlu5UJ5gk0dKz0h3", "34gCuhDGsG4bRPIf9bb02f", "6nek1Nin9q48AVZcWs9e9D"]
    elif(210):
        trackId_list = ["0u7b8p0mxUUNT7xeuYUtlP", "50kpGaPAhYJ3sGmk6vplg0", "27tNWlhdAryQY04Gb2ZhUI"]
    elif(211):
        trackId_list = ["6sy3LkhNFjJWlaeSMNwQ62", "0u7b8p0mxUUNT7xeuYUtlP", "4G8gkOterJn0Ywt6uhqbhp"]
    elif(212):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "4G8gkOterJn0Ywt6uhqbhp"]
    elif(221):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "4G8gkOterJn0Ywt6uhqbhp"]
    elif(230):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "4G8gkOterJn0Ywt6uhqbhp"]
    elif(231):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "4G8gkOterJn0Ywt6uhqbhp"]
    elif(232):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "4G8gkOterJn0Ywt6uhqbhp"]
    elif(300):
        trackId_list = ["1CS7Sd1u5tWkstBhpssyjP", "1zwMYTA5nlNjZxYrvBB2pV", "7vRriwrloYVaoAe3a9wJHe"]
    elif(301):
        trackId_list = ["34gCuhDGsG4bRPIf9bb02f", "6nek1Nin9q48AVZcWs9e9D", "7vRriwrloYVaoAe3a9wJHe"]
    elif(302):
        trackId_list = ["34gCuhDGsG4bRPIf9bb02f", "6nek1Nin9q48AVZcWs9e9D", "7vRriwrloYVaoAe3a9wJHe"]
    elif(310):
        trackId_list = ["1i1fxkWeaMmKEB4T7zqbzK", "7vRriwrloYVaoAe3a9wJHe", "1c8gk2PeTE04A1pIDH9YMk"]
    elif(311):
        trackId_list = ["6sy3LkhNFjJWlaeSMNwQ62", "2yPoXCs7BSIUrucMdK5PzV", "1c8gk2PeTE04A1pIDH9YMk"]
    elif(312):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "0VjIjW4GlUZAMYd2vXMi3b"]
    elif(313):
        trackId_list = ["1i1fxkWeaMmKEB4T7zqbzK", "0VjIjW4GlUZAMYd2vXMi3b", "3CRDbSIZ4r5MsZ0YwxuEkn"]
    elif(314):
        trackId_list = ["2QjOHCTQ1Jl3zawyYOpxh6", "3CRDbSIZ4r5MsZ0YwxuEkn", "0VjIjW4GlUZAMYd2vXMi3b"]
    elif(321):
        trackId_list = ["2QjOHCTQ1Jl3zawyYOpxh6", "3CRDbSIZ4r5MsZ0YwxuEkn", "0VjIjW4GlUZAMYd2vXMi3b"]
    elif(500):
        trackId_list = ["1CS7Sd1u5tWkstBhpssyjP", "1zwMYTA5nlNjZxYrvBB2pV", "3goSVuTt3fDYDP6kRnFwuL"]
    elif(501):
        trackId_list = ["34gCuhDGsG4bRPIf9bb02f", "3goSVuTt3fDYDP6kRnFwuL", "50kpGaPAhYJ3sGmk6vplg0"]
    elif(502):
        trackId_list = ["34gCuhDGsG4bRPIf9bb02f", "0nJW01T7XtvILxQgC5J7Wh", "2tJulUYLDKOg9XrtVkMgcJ"]
    elif(503):
        trackId_list = ["1i1fxkWeaMmKEB4T7zqbzK", "2tJulUYLDKOg9XrtVkMgcJ", "0nJW01T7XtvILxQgC5J7Wh"]
    elif(504):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "3CRDbSIZ4r5MsZ0YwxuEkn", "22oEJW6r2rMb9z4IntfyEa"]
    elif(511):
        trackId_list = ["1c8gk2PeTE04A1pIDH9YMk", "1zwMYTA5nlNjZxYrvBB2pV", "5xhJmd0I15jFcEdqxfCzKk"]
    elif(520):
        trackId_list = ["4lY95OMGb9WxP6IYut64ir", "4RL77hMWUq35NYnPLXBpih", "7tmtOEDxPN7CWaQWBsG1DY"]
    elif(521):
        trackId_list = ["003vvx7Niy0yvhvHt4a68B", "0ntQJM78wzOLVeCUAW7Y45", "1mea3bSkSGXuIRvnydlB5b"]
    elif(522):
        trackId_list = ["4G8gkOterJn0Ywt6uhqbhp", "6sy3LkhNFjJWlaeSMNwQ62", "0u7b8p0mxUUNT7xeuYUtlP"]
    elif(531):
        trackId_list = ["2dLLR6qlu5UJ5gk0dKz0h3", "5Nm9ERjJZ5oyfXZTECKmRt", "0u7b8p0mxUUNT7xeuYUtlP"]
    elif(600):
        trackId_list = ["0lizgQ7Qw35od7CYaoMBZb", "2IprIjGNRlj3TfqUWCAo0C", "4PS1e8f2LvuTFgUs1Cn3ON"]
    elif(601):
        trackId_list = ["0lizgQ7Qw35od7CYaoMBZb", "2IprIjGNRlj3TfqUWCAo0C", "7vQbuQcyTflfCIOu3Uzzya"]
    elif(602):
        trackId_list = ["0lizgQ7Qw35od7CYaoMBZb", "2IprIjGNRlj3TfqUWCAo0C", "5yNgdD8E6WruhULb4n2Con"]
    elif(611):
        trackId_list = ["3DkmjMBrOmYOzxxCL4rrL5", "2IprIjGNRlj3TfqUWCAo0C", "5yNgdD8E6WruhULb4n2Con"]
    elif(612):
        trackId_list = ["161DnLWsx1i3u1JT05lzqU", "0gplL1WMoJ6iYaPgMCL0gX", "25KybV9BOUlvcnv7nN3Pyo"]
    elif(613):
        trackId_list = ["161DnLWsx1i3u1JT05lzqU", "2yPoXCs7BSIUrucMdK5PzV", "25KybV9BOUlvcnv7nN3Pyo"]
    elif(615):
        trackId_list = ["2gMXnyrvIjhVBUZwvLZDMP", "0VjIjW4GlUZAMYd2vXMi3b", "4l0Mvzj72xxOpRrp6h8nHi"]
    elif(616):
        trackId_list = ["6Mb0OgMvbb7FYQejZ6rusz", "3DkmjMBrOmYOzxxCL4rrL5", "79qxwHypONUt3AFq0WPpT9"]
    elif(620):
        trackId_list = ["1InPL1Qm8qJC3FIIvFruNt", "3UoULw70kMsiVXxW0L3A33", "0tgVpDi06FyKpA1z0VMD4v"]
    elif(621):
        trackId_list = ["3WlbeuhfRSqU7ylK2Ui5U7", "3UoULw70kMsiVXxW0L3A33", "0tgVpDi06FyKpA1z0VMD4v"]
    elif(622):
        trackId_list = ["3WlbeuhfRSqU7ylK2Ui5U7", "3UoULw70kMsiVXxW0L3A33", "0tgVpDi06FyKpA1z0VMD4v"] 
    elif(701):
        trackId_list = ["43zdsphuZLzwA9k4DJhU0I", "06cCziAHtDg6pcsidZHu03", "2QjOHCTQ1Jl3zawyYOpxh6"]
    elif(711):
        trackId_list = ["5olgfv0LjMoUtFe11djz32", "7vRriwrloYVaoAe3a9wJHe", "3XRosKfSgFSDIb6YVpApIl"]
    elif(721):
        trackId_list = ["2QjOHCTQ1Jl3zawyYOpxh6", "06cCziAHtDg6pcsidZHu03", "1ZMiCix7XSAbfAJlEZWMCp"]
    elif(731):
        trackId_list = ["152lZdxL1OR0ZMW6KquMif", "0Thqjtu54vKMP06pwZkAWp", "2QjOHCTQ1Jl3zawyYOpxh6"]
    elif(741):
        trackId_list = ["2cSiyndkQZRPmYOfrk9WlC", "26OhjtaTamFocE08t83ml6", "06cCziAHtDg6pcsidZHu03"]
    elif(751):
        trackId_list = ["152lZdxL1OR0ZMW6KquMif", "0Thqjtu54vKMP06pwZkAWp", "2QjOHCTQ1Jl3zawyYOpxh6"]
    elif(761):
        trackId_list = ["152lZdxL1OR0ZMW6KquMif", "0Thqjtu54vKMP06pwZkAWp", "2QjOHCTQ1Jl3zawyYOpxh6"]
    elif(762):
        trackId_list = ["2Fxmhks0bxGSBdJ92vM42m", "0VjIjW4GlUZAMYd2vXMi3b", "4oeaIftdpT3JuZLcCkKmVE"]
    elif(771):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "4oeaIftdpT3JuZLcCkKmVE", "0VjIjW4GlUZAMYd2vXMi3b"]
    elif(781):
        trackId_list = ["1zB4vmk8tFRmM9UULNzbLB", "4oeaIftdpT3JuZLcCkKmVE", "0VjIjW4GlUZAMYd2vXMi3b"]
    elif(800):
        trackId_list = ["1WkMMavIMc4JZ8cfMmxHkI", "2iuZJX9X9P0GKaE93xcPjk", "6b8Be6ljOzmkOmFslEb23P"]
    elif(801):
        trackId_list = ["22PMfvdz35fFKYnJyMn077", "1mWdTewIgB3gtBM3TOSFhB", "1WkMMavIMc4JZ8cfMmxHkI"]
    elif(802):
        trackId_list = ["5HCyWlXZPP0y6Gqq8TgA20", "1RMJOxR6GRPsBHL8qeC2ux", "2fXwCWkh6YG5zU1IyvQrbs"]
    elif(803):
        trackId_list = ["2QZ7WLBE8h2y1Y5Fb8RYbH", "1RMJOxR6GRPsBHL8qeC2ux", "2fXwCWkh6YG5zU1IyvQrbs"]
    elif(804):
        trackId_list = ["6sy3LkhNFjJWlaeSMNwQ62", "7qiZfU4dY1lWllzX7mPBI3", "7JJmb5XwzOO8jgpou264Ml"]
    else:
        print("error : 알수없는 ID값 입니다.")

    #limit : 추천받고 싶은 트랙 수 변경 가능
    #ex. limit = 5
    recommend_result = sp.recommendations(seed_tracks=trackId_list, limit=5, country='KR')
    pprint.pprint(recommend_result)

    #추천곡들의 정보를 가지는 클래스
    class recommend_playlist:
        recommended_count = 0
        
        def __init__(self, track, artist, album, track_uri, preview_url):
            self.__track = track
            self.__artist = artist
            self.__album = album
            self.__track_uri = track_uri
            self.__preview_url = preview_url
            self.__lyrics = ""
            
            recommend_playlist.recommended_count += 1
            
            self.__order = recommend_playlist.recommended_count
            
        def get_track(self):
            return self.__track
        def get_artist(self):
            return self.__artist
        def get_album(self):
            return self.__album
        def get_track_uri(self):
            return self.__track_uri
        def get_preview_url(self):
            return self.__preview_url
        def get_order(self):
            return self.__order
        def set_lyrics(self, lyrics):
            self.__lyrics = lyrics
        def get_lyrics(self):
            return self.__lyrics

        #스포티파이에서 제공하는 각 노래의 특징 정보 반환(danceability, energy, acousticness, valence, tempo)
        def get_features(self):
            track_features = sp.audio_features(self.__track_uri)
            if track_features:
                danceability = track_features[0]["danceability"]
                energy = track_features[0]["energy"]
                acousticness = track_features[0]["acousticness"]
                valence = track_features[0]["valence"]
                tempo = track_features[0]["tempo"]
                result = {"acousticness" : acousticness,
                        "energy" : energy,
                        "danceability" : danceability,
                        "valence" : valence,
                        "tempo" : tempo
                        }
                return result
            else:
                return None  
            
    #추천곡들의  recommend_playlist 객체들을 리스트로 관리   
    recommend_playlist_lists = []

    for i in range(len(recommend_result["tracks"])):
        track = recommend_result["tracks"][i]["name"]
        artist = recommend_result["tracks"][i]["artists"][0]["name"]
        album = recommend_result["tracks"][i]["album"]["name"]
        track_uri = recommend_result["tracks"][i]["uri"]
        preview_url = recommend_result["tracks"][i]["preview_url"]

        recommended_playlist = recommend_playlist(track, artist, album, track_uri, preview_url)
        recommend_playlist_lists.append(recommended_playlist)


    return recommend_playlist_lists


class WeatherMusicApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather and Music App')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.weather_button = QPushButton('Get Weather and Music Recommendation', self)
        self.weather_button.clicked.connect(self.get_weather_and_music)
        self.layout.addWidget(self.weather_button)

        self.weather_label = QLabel(self)  
        self.layout.addWidget(self.weather_label)
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Track', 'Artist', 'Album', '30s Preview'])

        self.table.setColumnWidth(0, 300) 
        self.table.setColumnWidth(1, 150) 
        self.table.setColumnWidth(2, 200)  
        self.table.setColumnWidth(3, 200) 
    

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def get_weather_and_music(self):
        weather_info = (
            f"[ 현재 {seoul_weather_data.get_cityName()}의 날씨 정보 ]\n\n"
            f"현재 온도(섭씨) : {seoul_weather_data.get_temp()} 도\n"
            f"날씨 : {seoul_weather_data.get_weather_descrip()}(id = {seoul_weather_data.get_weather_id()})"
        )
        self.weather_label.setText(weather_info)


        recommend_playlist_lists = Get_RecomendMusic()

        self.table.setRowCount(len(recommend_playlist_lists))
        for i, playlist in enumerate(recommend_playlist_lists):
            self.table.setItem(i, 0, QTableWidgetItem(playlist.get_track()))
            self.table.setItem(i, 1, QTableWidgetItem(playlist.get_artist()))
            self.table.setItem(i, 2, QTableWidgetItem(playlist.get_album()))

            play_button = QPushButton('Play')
            play_button.clicked.connect(lambda state, url=playlist.get_preview_url(): self.play_preview(url))
            self.table.setCellWidget(i, 3, play_button)

    def play_preview(self, url):
        print(f"Playing preview: {url}")
        QDesktopServices.openUrl(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherMusicApp()
    ex.show()
    sys.exit(app.exec_())