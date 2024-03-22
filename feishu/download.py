import requests

import json

# 飞书开放平台的API endpoint

auth_url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'

doc_url = 'https://open.feishu.cn/open-apis/doc/v2/...'  # 假设这是获取文档下载链接的API endpoint

# 你的App信息

app_id = 'YOUR_APP_ID'

app_secret = 'YOUR_APP_SECRET'

# 获取访问令牌

payload = {

    'app_id': app_id,

    'app_secret': app_secret

}

response = requests.post(auth_url, json=payload)

token_data = response.json()

access_token = token_data.get('tenant_access_token')

# 使用访问令牌调用飞书文档API获取文档下载链接

headers = {

    'Authorization': f'Bearer {access_token}'

}

response = requests.get(doc_url, headers=headers)

doc_info = response.json()

# 假设doc_info中包含文档的下载链接

download_url = doc_info.get('download_url')

# 下载文档

with requests.get(download_url, stream=True) as r:
    with open('downloaded_document.docx', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

print("文档下载完成")