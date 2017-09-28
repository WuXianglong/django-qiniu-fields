# -*- coding: utf-8 -*-
import hashlib

from django.conf import settings

from qiniu import Auth, BucketManager, put_file, build_batch_delete


EXPIRE_TIME = 24 * 3600   # 1 day

Q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


def get_token():
    token = Q.upload_token(settings.QINIU_BUCKET, expires=EXPIRE_TIME)
    return token


def delete_data(urls, key_prefix=''):
    keys = []
    for url in urls:
        if not url.endswith('/'):
            url += '/'
        key = url.split('/')[-2]
        if key_prefix:
            key = '%s/%s' % (key_prefix, key)
        keys.append(key)

    ops = build_batch_delete(settings.QINIU_BUCKET, keys)
    b = BucketManager(Q)
    ret, info = b.batch(ops)
    print(ret, info)


def upload_file(file_data, key_prefix=''):
    file_ext = file_data.name.split('.')[-1]
    file_name = '.'.join([hashlib.md5(file_data.read()).hexdigest(), file_ext])
    if key_prefix and not key_prefix.endswith('/'):
        key_prefix += '/'
    key = '%s%s' % (key_prefix, file_name)
    token = get_token()

    ret, info = put_file(token, key, file_data.temporary_file_path(), check_crc=False)
    if not ret or ret.get('key') != key:
        print('fail to upload image to qiniu, info: %s' % info)

    return settings.QINIU_DOMAIN + key
