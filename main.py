import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread("res/screenshot.jpg")
height, width, _ = img.shape
roi = img[0:height, 450:width]

url_api = "https://api.ocr.space/parse/image"
_, compre_img = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compre_img)


result = requests.post(url_api,
              files={"screenshot.jpg": file_bytes},
              data={"apikey": "YOUR_PRODUCT_KEY"})

result = (result.content.decode())
result = json.loads(result)
text_det = result.get("ParsedResults")[0].get("ParsedText")
print(text_det)

cv2.imshow("roi", roi)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
