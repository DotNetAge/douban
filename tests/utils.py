from scrapy.http import HtmlResponse, Request


def mock_response(target_url, mock_file):
    with open(mock_file, 'r') as tag_file:
        body = tag_file.read()

    return HtmlResponse(url=target_url,
                        request=Request(target_url),
                        body=body, encoding="utf-8")
