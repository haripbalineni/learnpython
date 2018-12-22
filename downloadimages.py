import urllib.request


def download_jpg(url,file_path,file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)


url = input('Enter image url to download :')
filename = input('Enter filename to save as :')


download_jpg(url,'Images/',filename)