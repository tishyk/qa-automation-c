import requests
import os
import zipfile


def download_file(url, path):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    filename=os.path.join(path, local_filename)
    f = open(filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return filename


def download_new_driver(download_path: str, exename: str):
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(os.path.join(here, exename)):
        if os.path.exists(os.path.join(here, exename + ".bak")):
            os.remove(os.path.join(here, exename + ".bak"))
        os.rename(os.path.join(here, exename), os.path.join(here, exename + ".bak"))
    try:
        filename = download_file(download_path, here)
        print("Downloaded %s" % os.path.basename(filename))
        z = zipfile.ZipFile(file=filename)
        z.extract(path=here, member=exename)
        print("Extracted " + exename)
        z.close()
    finally:
        if not os.path.exists(os.path.join(here, exename)):
            print("FAILED: restore former " + exename)
            os.rename(os.path.join(here, exename + ".bak"), os.path.join(here, exename))
        os.remove(filename)


def get_current_vesion_webdriver(exename: str):

    def we_need_update(version_number, exename):
        here = os.path.dirname(os.path.abspath(__file__))
        ver_file = os.path.join(here, f"{exename}.ver")
        if not os.path.exists(ver_file):
            with open(ver_file, 'w+') as v:
                v.write(version_number)
        else:
            with open(ver_file, 'r') as v:
                curr = v.read()
            if version_number in curr:
                return False
            else:
                with open(ver_file, 'w+') as v:
                    v.write(version_number)
        return True

    if exename == "chromedriver.exe":
        # get the latest chrome driver version number
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text
        print(version_number)
        if not we_need_update(version_number, exename):
            return None
        # build the download url
        try:
            download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_win32.zip"
        except:
            static_ver_driver_chrome = "90.0.4430.24/chromedriver_win32.zip"
            download_url = "https://chromedriver.storage.googleapis.com/" + static_ver_driver_chrome
        return download_url
    elif exename == "geckodriver.exe":
        # get the latest gecko-mozilla driver version number
        url = "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
        r = requests.get(url)
        # build the download url
        try:
            download_url = r.json().get("assets", [])[-1].get("browser_download_url")
            print(download_url.replace("https://github.com/mozilla/geckodriver/releases/download/", ""))
            if not we_need_update(download_url, exename):
                return None
        except:
            static_ver_driver_ff = "v0.29.1/geckodriver-v0.29.1-win64.zip"
            download_url = "https://github.com/mozilla/geckodriver/releases/download/" + static_ver_driver_ff
        return download_url


if __name__== "__main__":
    if os.name == "nt":
        exe_names = ["chromedriver.exe", "geckodriver.exe"]
        for name in exe_names:
            url = get_current_vesion_webdriver(name)
            if url is not None:
                download_new_driver(url, name)
    else:
        print("it's works only with NT-like OS")
