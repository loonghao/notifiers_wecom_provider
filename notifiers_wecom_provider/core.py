"""WeCom provider for Notifiers."""
# Import future modules
# Import third-party modules
from notifiers.core import Provider
from notifiers.core import Response
from notifiers.utils import requests


class WeCom(Provider):
    """WeCom provider for Notifiers."""

    name = "wecom"
    site_url = "https://work.weixin.qq.com/"
    base_url = "https://qyapi.weixin.qq.com/"
    _required = {"required": ["msgtype", "api_key", "message"]}
    _schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string", "title": "Message content"},
            "msgtype": {"type": "string", "title": "User email"},
            "api_key": {"type": "string", "title": "API Key"},
        },
        "additionalProperties": False,
    }

    def _prepare_data(self, data: dict) -> dict:
        return {
            "api_key": data["api_key"],
            "data": {
                "msgtype": data["msgtype"],
                data["msgtype"]: {
                    "content": data["message"],
                },
            },
        }

    def _assemble_url(self, api_key):
        return f"{self.base_url}cgi-bin/webhook/send?key={api_key}"

    def _send_notification(self, data: dict) -> Response:
        url = self._assemble_url(data.pop("api_key"))
        json = data.pop("data")
        response, errors = requests.post(url, json=json)
        return self.create_response(data, response, errors)
