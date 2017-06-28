var friends = require('./friends');
var logics = require('./logics');

var async = require('async');

function complete(result, obj) {
    if (!obj.friendData) {
        return;
    }
    result.json(logics.calculateSuspition(obj));
}

module.exports = {
    handleRequest: function (req, result) {
        var finalObj = {};

        friends.getFriendStatisticsById(req.body.userId, function (res) {
            finalObj.friendData = res;
            complete(result, finalObj);
        });
    }

};
