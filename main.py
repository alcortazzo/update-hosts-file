import os
import conf
import requests
import platform


os_ = platform.system()
paths = {
    "Linux": "/etc/hosts",
    "Darwin": "/etc/hosts",
    "Windows": "C:\Windows\System32\drivers\etc\hosts",
}
hosts = {
    "hosts": "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "hosts+fakenews": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts",
    "hosts+gambling": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts",
    "hosts+porn": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts",
    "hosts+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social/hosts",
    "hosts+fakenews+gambling": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts",
    "hosts+fakenews+porn": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-porn/hosts",
    "hosts+fakenews+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-social/hosts",
    "hosts+gambling+porn": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn/hosts",
    "hosts+gambling+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-social/hosts",
    "hosts+porn+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn-social/hosts",
    "hosts+fakenews+gambling+porn": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts",
    "hosts+fakenews+gambling+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-social/hosts",
    "hosts+fakenews+porn+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-porn-social/hosts",
    "hosts+gambling+porn+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn-social/hosts",
    "hosts+fakenews+gambling+porn+social": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts",
}


def backup_file():
    os.replace(paths[os_], f"{paths[os_]}.old")


def download_file():
    hosts_file = requests.get(hosts[conf.hosts_type])
    open(paths[os_], "wb").write(hosts_file.content)
    with open(paths[os_], "wb") as file_:
        file_.write(hosts_file.content)


def remove_addresses():
    with open(paths[os_], "r") as file_:
        hosts_lines = file_.readlines()

    num = 0
    file_lines_ = hosts_lines[0:]

    for line in hosts_lines:
        for blacklink in conf.blacklist:
            if blacklink in line:
                file_lines_.remove(line)
                print(
                    f"Line #{num + 1} will be removed due to blacklist rule: {blacklink}"
                )
                continue
        num += 1

    with open(paths[os_], "w") as file_:
        for line in file_lines_:
            file_.write(line)


if __name__ == "__main__":
    try:
        backup_file()
        download_file()
        if conf.blacklist:
            remove_addresses()
    except Exception as ex:
        print(f"{type(ex).__name__}: {ex}")
