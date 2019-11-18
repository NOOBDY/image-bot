from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

i = input("Search something: ")

args = {
    "keywords": "{}".format(i),
    "limit": 10,
    "print_urls": True
}

paths = response.download(args)
print(paths)