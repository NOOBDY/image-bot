from google_images_download import google_images_download



def download(keyowrd, limit):

    response = google_images_download.googleimagesdownload()

    args = {
        "keywords": "{}".format(keyowrd),
        "limit": limit,
        "print_urls": False,
        "no_download": True,
        "format": "jpg"
    }
    urls=[]
    paths, errors = response.download(args)
    for path in paths[keyowrd]:
        urls.append(path)
    return urls


