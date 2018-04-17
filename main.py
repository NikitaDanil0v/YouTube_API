import requests

class YouTube_API():

    def __init__(self):
        self.token = "" #provide your token
        self.data = None

    def parse(self, channel_id):
        try:
            self.data = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={}".format(channel_id),
                           headers={
                               "Authorization": "Bearer {}".format(self.token)
                           }).json()['items'][0]
            print(self.data)
        except Exception as e:
            print(e)
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

YouTube = YouTube_API()

YouTube.parse("UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(YouTube.getCustomUrl(), YouTube.getCreationDate(), YouTube.getDescription(), YouTube.getTitle())
