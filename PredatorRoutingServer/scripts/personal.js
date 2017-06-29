var rp = require('request-promise');
var seleniumServerDns = '127.0.0.1:8080'

module.exports = {
    getPersonalDataById: function (id, sucess) {
        var options = {
            uri: 'http://' + seleniumServerDns + '/personal/?userid=' + id,
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
    }, 
    getImageDuplicates: function(id, success) {
        var options = {
            uri: 'http://' + seleniumServerDns + '/imagedata/?userid=' + id,
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
