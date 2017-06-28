var rp = require('request-promise');
var seleniumServerDns = '127.0.0.1:8080'

module.exports = {
    getFriendStatisticsById: function (id, sucess) {
        var options = {
            uri: 'http://' + seleniumServerDns + '/friends/?userid=' + id,
            headers: {
                'User-Agent': 'Request-Promise'
            },
            json: true // Automatically parses the JSON string in the response
        };

        rp(options)
            .then(function (res) {
                sucess(res);
            })
            .catch(function (err) {
                console.log('Error');
            });
    }
};
