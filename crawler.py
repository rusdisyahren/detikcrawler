__author__ = 'rusdi'

import requests,urllib
from bs4 import BeautifulSoup

def crawler(URL):
    getResponse  = requests.get(URL)
    if getResponse.status_code == 200 :
        getContent = BeautifulSoup(getResponse.text, "html.parser")
        imageTag = getContent.find_all("img");
        totalImage = len(imageTag)
        totalImageSize = 0;

        for image in imageTag:
            srcTag = image.get('src')
            if srcTag.startswith("//"):
                srcTag = "http:" + srcTag
            elif srcTag.startswith("http"):
                srcTag = srcTag
            else:
                srcTag = URL + "/" + srcTag

            getImage = urllib.urlopen(srcTag)

            imageSize = getImage.headers.get("content-length")
            getImage.close()
            totalImageSize += int(imageSize)

        print ("Total Tag Image : %d" % totalImage)
        print ("Total Size Image : %d" % totalImageSize)

# crawler("http://google.com")
crawler("http://detik.com")







