from thispkg import base64
from time import perf_counter
from requests import get
import base64 as b64

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def get_image(w: int, h: int):
    url = f"https://picsum.photos/{w}/{h}"
    response = get(url, allow_redirects=False, headers=HEADERS)
    print(response.headers)
    image_url = response.headers.get("location", None)
    assert image_url is not None, "Image URL Empty"
    return image_url


def test_base64():
    image = get_image(300, 300)
    image_data = get(image).content
    s = perf_counter()
    encoded_stdlib = b64.b64encode(image_data)
    e = perf_counter()
    stdlib_time = e - s
    s = perf_counter()
    encoded_thispkg = base64.b64encode(image_data)
    e = perf_counter()
    thispkg_time = e - s
    assert (
        thispkg_time < stdlib_time
    ), f"thispkg_time: {thispkg_time}, stdlib_time: {stdlib_time}"
    assert encoded_stdlib == encoded_thispkg, "Mismatch in base64 encoding"
