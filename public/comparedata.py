import json

"""
期望数据与实际数据对比
type:string  对比的数据类型
"""


def is_satisfy(expect1, actual, is_json=False):
    """
    判定实际数据是否与期望数据匹配
    :param expect1:
    :param actual:
    :param is_json:
    :return: Boolean
    """
    result = False

    if expect1 == "*":
        return True
    if is_json:
        actual = json.load(expect1)
        print(type(actual))
        print("期望数据：{}, \n, 实际数据为：{}".format(expect1, actual))

    if expect1 != "*":
        assert type(expect1) == type(actual), "数据类型不一致:{}\n{}".format(type(expect1), actual)

    if isinstance(expect1, dict):
        assert len(expect1) == len(actual), '字典长度不一致，期望长度{}，实际长度{}'.format(len(expect1), len(actual))
        for key in expect1.keys():
            assert key in actual.keys(), "Actual contains key:{}, that not in expect keys，".format(key)
            result = is_satisfy(expect1[key], actual[key], False)
    if isinstance(expect1, list):
        assert len(expect1) == len(actual), \
            'List length is not compared: actual {} not equal expect {}'.format(len(expect1), len(actual))
        # 将列表数据进行排序并进行对比
        for l, e in zip(sorted(expect1), sorted(actual)):
            result = is_satisfy(l, e, False)
    elif expect1 == actual or expect1 == "*":
        print(expect1, actual)
        return True
    else:
        print('Data check fail: expect: {}，actual is: {}'.format(str(actual), str(expect1)))
        return False

    return result


# a = [[1, 2, 3], [1, 3]]
# b = [[1, 2], [1, 2]]
with open('E:\\automatic\\apitestfwk\\test_data\\jsonfile.json', 'r', encoding='utf-8') as json_f:
    c = json.load(json_f)
    print(c)
d = {'id': '2310549', 'domain': '2601334', 'title': '双排冲分中！', 'broadcast_begin': '1537509296', 'broadcast_status': '1',
     'lockable': False, 'fee': 0, 'live_source': [[1, 3], [3]], 'stream_types': '9', 'stream_ratelevel': '',
     'stream_id': '', 'viewers': 48312, 'isDynamic': 0, 'heatValue': 5512, 'moreinfo': "*"}

"""
d = {'id': '2310549', 'domain': '2601334', 'title': '双排冲分中！', 'broadcast_begin': '1537509296', 'broadcast_status': '1',
     'lockable': False, 'fee': 0, 'live_source': [[1, 3], [3]], 'stream_types': '9', 'stream_ratelevel': '',
     'stream_id': '', 'viewers': 48312, 'isDynamic': 0, 'heatValue': 5512, 'moreinfo': [
        {'id': '2310549', 'domain': '2601334', 'title': '双排冲分中！', 'broadcast_begin': '1537509296',
         'broadcast_status': '1', 'lockable': False, 'fee': 0, 'live_source': [[1, 3], [3]], 'stream_types': '9',
         'stream_ratelevel': '', 'stream_id': '', 'viewers': 48312, 'isDynamic': 0, 'heatValue': 5512},
        {'id': '2310549', 'domain': '2601334', 'title': '双排冲分中！', 'broadcast_begin': '1537509296',
         'broadcast_status': '1', 'lockable': False, 'fee': 0, 'live_source': [[1, 3], [3]], 'stream_types': '9',
         'stream_ratelevel': '', 'stream_id': '', 'viewers': 48312, 'isDynamic': 0, 'heatValue': 5512}]}
"""

# print(is_satisfy(a, b))
print(is_satisfy(d, c))
