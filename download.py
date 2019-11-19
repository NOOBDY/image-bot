from google_images_download import google_images_download

i = input("Search something: ")

def download(i, limit):
    response = google_images_download.googleimagesdownload()

    args = {
        "keywords": "{}".format(i),
        "limit": 10,
        "print_urls": True
    }

    paths = response.download(args)
    print(paths)