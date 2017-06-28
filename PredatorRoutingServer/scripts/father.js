var friends = require('./friends');
var async = require('async');

module.exports = {
        handleRequest: function (req, res) {
            var finalObj = {};
            var scrapingCallbacks = [];

            scrapingCallbacks.push(friends.getAllFriendsById(req.body.userId, function (res) {
                finalObj.friendData = res;
            }));

//            scrapingCallbacks.push(friends.getAllFriendsById(req.body.userId, function (res) {
//                finalObj.likeData = res.data;
//            }));

            async.parallel(scrapingCallbacks, function (err, result) {
                if (err)
                    return console.log(err);
                else if (result) {
                    res.json(finalObj);
                }
            });
        }
};
