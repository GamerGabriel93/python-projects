import requests


class Check:
    def GetUserName(self):
        self.name = input("Name to check:")
        return self.name

    def End(self):
        print('Process Finished!')

    def LoadSites(self):
        self.GetUserName()
        self.url = ['https://twitter.com/', 'https://hu-hu.facebook.com/', 'https://www.youtube.com/user/',
                    'https://www.tiktok.com/@', 'https://open.spotify.com/user/', 'https://br.pinterest.com/']
        return self.name, self.url

    def CheckStatus(self):
        self.LoadSites()
        for self.item in self.url:
            self.webaddress = requests.get(self.item + self.name)
            if self.webaddress.status_code == 200:
                print(self.item + self.name)
        self.End()


Check().CheckStatus()
