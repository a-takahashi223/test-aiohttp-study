from test_aiohttp_study import main


def test_main():
    """引数のURLにアクセスし、返ってきたJSONの.urlを返す"""
    url = "http://localhost:8080/get"
    assert main.main(url) == url
