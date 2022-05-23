import sys
args = sys.argv
directory = args[1]
import os
if os.access(directory, os.F_OK) == False:
    os.mkdir(directory)
else:
    pass


while True:
    url = input()
    if url == 'exit':
        break
    elif '.' not in url:
       print("Incorrect URL")
    else:
        import requests
        response = requests.get(f'https://{url}')
        if response.status_code != 200:
            print("Incorrect URL")
        else:
            from bs4 import  BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            soup.prettify()
            content = soup.find_all(["p", "a", "ul", "ol", "li"])
            output = []
            from colorama import Fore, Style
            for line in content:
                output.append(line.text)
                if line.name == 'a':
                    print(Fore.BLUE + line.text + Style.RESET_ALL)
                else:
                    print(line.text)

            file = open(f'{directory}/{url}', 'w', encoding='utf-8')
            for i in output:
                file.write(i)
            file.close()








