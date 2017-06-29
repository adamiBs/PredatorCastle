var friends = require('./friends');
var personal = require('./personal');
var logics = require('./logics');

var async = require('async');

function complete(result, obj) {
    if (!obj.friendData) {
        return;
    }
    
    if (!obj.personalData) {
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
        
        personal.getPersonalDataById(req.body.userId, function (res) {
            finalObj.personalData = res;
            complete(result, finalObj);
        });
        
        personal.getPersonalDataById(req.body.userId, function (res) {
            finalObj.imageData = res;
            complete(result, finalObj);
        });
    }

};
