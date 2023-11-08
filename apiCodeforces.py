from __future__ import annotations

import time
import hashlib
import random as rnd
import requests as req
from typing import Iterable, Tuple, List, Optional, Mapping, Any

from apiBase import Api


class CodeforcesApi(Api):
    def get_hash(self, method_name: str, params: Iterable[Tuple[str, str]]) -> str:
        params = sorted(params)
        rand = str(rnd.randint(0, 999999)).zfill(6)
        s = f'{rand}/{method_name}?' + '&'.join([x + '=' + y for x, y in params]) + '#' + str(self.secret)

        hasher = hashlib.sha512(s.encode()).hexdigest()
        return rand + hasher

    def sign(self, method_name: str, params: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        millis = int(round(time.time()))
        new_params = params + [
            ("time", str(millis)),
            ("apiKey", self.key)
        ]
        hash_ = self.get_hash(method_name, new_params)
        return new_params + [("apiSig", hash_)]

    def perform_request(self, method_name: str, **kwargs):
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        signed_params = self.sign(method_name, list(map((lambda x: (x[0], str(x[1]))), kwargs.items())))

        response = req.post(
            f"{self.host}/api/{method_name}",
            data={k: v for k, v in signed_params}
        )
        if response.status_code != 200:
            raise RuntimeError("Codeforces API error: " + response.json()["comment"])
        time.sleep(1)
        return response.json()["result"]

    def get_standings(self, contest_id: int | str,
                      from_: Optional[int | str] = None,
                      count: Optional[int | str] = None,
                      handles: Optional[List[str]] = None,
                      room: Optional[str | int] = None,
                      as_manager: bool = False,
                      show_unofficial: bool = False) -> Mapping[str, Mapping[str, Any]]:
        params = {"contestId": contest_id}

        if from_ is not None:
            params["from"] = from_

        if count is not None:
            params["count"] = count

        if handles is not None and len(handles) > 0:
            params["handles"] = ";".join(handles)

        if room is not None:
            params["room"] = room

        if show_unofficial:
            params["showUnofficial"] = "true"

        if as_manager:
            params["asManager"] = "true"

        return self.perform_request("contest.standings", **params)
