import json

import requests

cookies = {
    '.ASPXANONYMOUS': 'KYmaid9UDAQJJHmKOzImuGdeYNwSckVbiDWCuCTZ4R8PIvMLCgw5llxfy5BbSctLmbLugaj8uCdOR6UIs8KqFIiiSAvElRy3xXWD2BFltVEdkeSvoKKIdsWhWlpx81H6SJueIw2',
    'ASP.NET_SessionId': 'ck3htm1tlwpkymmufpn0lt4s',
    'CustomerId': '46f11f96e26647c69baab6df9a7a5c28',
    'ShouldSetDeliveryOptions': 'True',
    'ValidationToken': 'b274f0c1b8c19a4c2951a83f823c4028',
    'DontShowCookieNotification': 'true',
    'cookiesession1': '678B286D5C0CD00C37E142FD2431514A',
    '_tm_lt_sid': '1669760191321.173712',
    'oxxfgh': 'L!8b32634b-62cf-b303-de09-b5dc67d533b5#0#1800000#5000#1800000#44965',
    'KFP_DID': '94174e07-3680-28cb-d283-4a1d9249dc52',
    'IsAdult': 'True',
    'qrator_jsid': '1669760188.812.VdbQ7XQ7qQCxGQqI-4ar3qhkmh2ukb7t5cldjp31qcis8cihq',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Requests sorts cookies': 'alphabetically',
    'Cookie': '.ASPXANONYMOUS=KYmaid9UDAQJJHmKOzImuGdeYNwSckVbiDWCuCTZ4R8PIvMLCgw5llxfy5BbSctLmbLugaj8uCdOR6UIs8KqFIiiSAvElRy3xXWD2BFltVEdkeSvoKKIdsWhWlpx81H6SJueIw2; ASP.NET_SessionId=ck3htm1tlwpkymmufpn0lt4s; CustomerId=46f11f96e26647c69baab6df9a7a5c28; ShouldSetDeliveryOptions=True; ValidationToken=b274f0c1b8c19a4c2951a83f823c4028; DontShowCookieNotification=true; cookiesession1=678B286D5C0CD00C37E142FD2431514A; _tm_lt_sid=1669760191321.173712; oxxfgh=L!8b32634b-62cf-b303-de09-b5dc67d533b5#0#1800000#5000#1800000#44965; KFP_DID=94174e07-3680-28cb-d283-4a1d9249dc52; IsAdult=True; qrator_jsid=1669760188.812.VdbQ7XQ7qQCxGQqI-4ar3qhkmh2ukb7t5cldjp31qcis8cihq',
    'DNT': '1',
    'Origin': 'https://lenta.com',
    'Referer': 'https://lenta.com/catalog/alkogolnye-napitki/krepkijj-alkogol/viski/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

json_data = {
    'nodeCode': 'sb9f60f8f1c7af537820ce1ec3cc81f3d',
    'filters': [],
    'tag': '',
    'typeSearch': 1,
    'pricesRange': None,
    'sortingType': 'ByPopularity',
    'offset': 0,
    'limit': 24,
    'updateFilters': True,
}


# def get_json(url):
#     response = requests.post('https://lenta.com/api/v1/skus/list', cookies=cookies, headers=headers, json=json_data)
#
#     with open('response.json', 'w', encoding='utf-8') as file:
#         json.dump(response, file, indent=4, ensure_ascii=False)


def collect_data():
    response = requests.post('https://lenta.com/api/v1/skus/list/?PAGEN_1=1', cookies=cookies, headers=headers,
                             json=json_data)
    data = response.json()
    pagination_count = data.get("totalCount") // 24

    result_data = []

    for page_count in range(pagination_count + 1):
        url = f"https://lenta.com/api/v1/skus/list/?PAGEN_1={page_count}"
        r = requests.post(url=url, cookies=cookies, headers=headers,
                          json=json_data)
        data = r.json()
        print(data)

        products = data.get("skus")

        for product in products:

            product_promoPercent = product.get("promoPercent")

            if product_promoPercent >= 30:
                result_data.append(
                    {
                        "title": product.get("title"),
                        "subTitle": product.get("subTitle"),
                        "regularPrice": product.get("regularPrice").get("value"),
                        "cardPrice": product.get("cardPrice").get("value"),
                        "product_promoPercent": product.get("promoPercent"),
                        "link": f'{product.get("imageUrl")}'
                    }
                )

        with open('response.json', 'w', encoding='utf-8') as file:
            json.dump(result_data, file, indent=4, ensure_ascii=False)

        json_data["offset"] += 24


def main():
    # get_json(url='https://mavt.ru/catalog/strong_alcohol/whisky/?PAGEN_1=2')
    collect_data()


if __name__ == "__main__":
    main()
