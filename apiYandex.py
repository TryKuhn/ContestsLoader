from __future__ import annotations

import json
import os.path
import re
import time
from typing import List, Tuple, Any, Optional, Mapping

import requests as req

from apiBase import Api


class YandexApi(Api):
    def __init__(self, key: str = None, secret: str = None, host: str = None,
                 device_id: str = None, device_name: str = None, access_token: str = None, refresh_token: str = None):
        super().__init__(key, secret, host, device_id, device_name)
        self.access_token = access_token
        self.refresh_token = refresh_token

    def sign(self, params: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        new_params = params + [
            ("client_id", self.key),
            ("client_secret", self.secret),
            ("device_id", self.device_id),
            ("device_name", self.device_name)
        ]
        return new_params

    def perform_request(self, method_name: str = None, current_host: str = None, **kwargs):
        if current_host is None:
            current_host = self.host

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        signed_params = self.sign(list(map((lambda x: (x[0], str(x[1]))), kwargs.items())))

        url = f"{current_host}/{method_name}?" if method_name is not None else f"{current_host}"

        response = req.post(
            url,
            data={k: v for k, v in signed_params}
        )
        if response.status_code != 200:
            raise RuntimeError("Yandex API error: " + response.json())
        time.sleep(1)
        return response.json()

    def __save_to_cache(self, host: List[Any]):
        data = dict()
        data['access_token'] = self.access_token
        data['refresh_token'] = self.refresh_token

        write_token = open(f'cache/Token{host[3]}.json', 'w')
        json.dump(data, write_token)
        write_token.close()

    def login(self, host: str = 'https://api.contest.yandex.net/api/public/v2/'):
        super().login(host)
        host = host.replace('.', '')
        host = re.split('[/:]', host)
        if os.path.exists(f'cache/Token{host[3]}.json'):
            token = open(f'cache/Token{host[3]}.json')
            data = json.load(token)
            token.close()

            self.access_token = data['access_token']
            self.refresh_token = data['refresh_token']
        else:
            request_code = req.get(f'https://oauth.yandex.ru/authorize?response_type=code&client_id={self.key}')
            print(request_code.url)

            code = input()

            params = {'client_id': self.key, 'client_secret': self.secret, 'code': code,
                      'grant_type': 'authorization_code',
                      'device_id': self.device_id, 'device_name': self.device_name}

            OAuthToken = self.perform_request(current_host='https://oauth.yandex.ru/token', **params)

            self.access_token = OAuthToken['access_token']
            self.refresh_token = OAuthToken['refresh_token']

            self.__save_to_cache(host)

    # TODO
    def get_standings(self, contest_id: int | str,
                      from_: Optional[int | str] = None,
                      count: Optional[int | str] = None,
                      handle: Optional[List[str]] = None,
                      group: Optional[str | int] = None,
                      as_manager: bool = False,
                      show_virtual: bool = False) -> Mapping[str, Mapping[str, Any]]:
        params = {"contestId": contest_id}

        if from_ is not None:
            params["from"] = from_

        if count is not None:
            params["count"] = count

        if handle is not None and len(handle) > 0:
            params["handles"] = ";".join(handle)

        if group is not None:
            params["room"] = group

        if show_virtual:
            params['showVirtual'] = "true"

        if as_manager:
            params["forJudge"] = "true"

        lol = req.post(f"https://api.contest.yandex.net/api/public/v2/contests/{54443}/standings?"
                       f"Authorization: {self.access_token}")

        # lol

        return lol.json()
