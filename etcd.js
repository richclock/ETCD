const { Etcd3 } = require('etcd3');
const client = new Etcd3();

(async () => {

    const lease = client.lease(5);
    await lease.put("iapps/").value('lease test');
})();

