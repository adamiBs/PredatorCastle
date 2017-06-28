var rp = require('request-promise');
var seleniumServerDns = '127.0.0.1:8080'

module.exports = {
    getAllFriendsById: function (id, sucess) {
        var options = {
            uri: 'http://' + seleniumServerDns + '/friends/?userid=' + id,
            headers: {
                'User-Agent': 'Request-Promise'
            },
            json: true // Automatically parses the JSON string in the response
        };

        rp(options)
            .then(sucess)
            .catch(function (err) {
                console.log('Error');
            });
    }
};
