import etcd3

etcd = etcd3.client()


# watch_count = 0
# events_iterator, cancel = etcd.watch("iapps/")
# for event in events_iterator:
#     print(event)
#     watch_count += 1
#     if watch_count > 10:
#         cancel()

# watch_count = 0
# events_iterator, cancel = etcd.watch_prefix("/iapps/")
# for event in events_iterator:
#     print(event)
#     watch_count += 1
#     if watch_count > 10:
#         cancel()


for x in etcd.get_all():
    print(x)
