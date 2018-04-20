import requests

class YouTube_Parser():

    def __init__(self):
        self.token = "" #provide your token
        self.data = None

    def parse(self, channel_id):
        try:
            r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={}".format(channel_id),
                           headers={
                               "Authorization": "Bearer {}".format(self.token)
                           }).json()
           self.data = r['items'][0]
        except Exception as e:
            print(e)
            if 'error' in r:
                print("ERROR: ", r['error']['code'], r['error']['message'])
            pass

    def getID(self):
        if self.data is not None:
            return self.data['id']

        return None

    def getCommentCount(self):
        if self.data is not None:
            return self.data['statistics']['commentCount']
        
        return None

    def getViewCount(self):
        if self.data is not None:
            return self.data['statistics']['viewCount']

        return None

    def getVideoCount(self):
        if self.data is not None:
            return self.data['statistics']['videoCount']

        return None

    def getSubscriberCount(self):
        if self.data is not None:
            return self.data['statistics']['subscriberCount']

        return None

    def getHiddenSubscriberCount(self):
        if self.data is not None:
            return self.data['statistics']['hiddenSubscriberCount']

        return None

    def getTitle(self):
        if self.data is not None:
            return self.data['snippet']['title']

        return None

    def getDescription(self):
        if self.data is not None:
            return self.data['snippet']['description']

        return None

    def getCustomUrl(self):
        if self.data is not None:
            return self.data['snippet']['customUrl']

        return None

    def getCreationDate(self):
        if self.data is not None:
            return self.data['snippet']['publishedAt']

        return None

YouTube = YouTube_Parser()

YouTube.parse("UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(YouTube.getCustomUrl(), YouTube.getCreationDate(), YouTube.getDescription(), YouTube.getTitle())
