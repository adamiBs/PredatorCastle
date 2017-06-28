var app = angular.module("mainApp", []);

app.controller('mainCtrl', ["$scope", "$http", function ($scope, $http) {

    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').focus()
    })
    
    $scope.UIDLoad = function() {
        var uId = document.getElementById("UIDInput").value;
        $scope.getUserProfileData(uId);
    }

    $scope.USERNAMELoad = function() {
        alert("Not yet implemented")
    }

    $scope.getUserProfileData = function(p_uID) {    
        var url = "https://graph.facebook.com/" + p_uID + "/picture?type=large&w%E2%80%8Cidth=720&height=720";
        document.getElementById("profilePicture").src = url;
        document.getElementById("uIdSpan").innerHTML = p_uID;
    }

    $scope.httpGetAsync = function(theUrl, callback) {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function () {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                callback(xmlHttp.responseText);
        }
        xmlHttp.open("GET", theUrl, true); // true for asynchronous 
        xmlHttp.send(null);
    }

    $scope.httpPostAsync = function(theUrl, Params, callback){
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function () {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                callback(xmlHttp.responseText);
        }
        xmlHttp.open("POST", theUrl, true); // true for asynchronous 
        xmlHttp.send(Params);
    }

    $scope.sendRequest = function() {
        var uId = undefined;

        if (document.getElementById("UIDRadio").checked) {
            uId = document.getElementById("UIDInput").value
        }
        
        $http.post("http://192.168.1.28:2424/api/data", "Tests").then(function(data) {
            alert(data);    
        });
    }
}]);

    function userIDTypeChanged() {
        if (document.getElementById("UIDRadio").checked) {
            document.getElementById("UIDInput").disabled = false;
            document.getElementById("UIDBtn").disabled = false;
            document.getElementById("USERNAMEInput").disabled = true;
            document.getElementById("USERNAMEBtn").disabled = true;
            document.getElementById("USERNAMEInput").value = "";
            document.getElementById("UIDInput").focus();
        } else if (document.getElementById("USERNAMERadio").checked) {
            document.getElementById("UIDInput").disabled = true;
            document.getElementById("UIDBtn").disabled = true;
            document.getElementById("USERNAMEInput").disabled = false;
            document.getElementById("USERNAMEBtn").disabled = false;
            document.getElementById("UIDInput").value = "";
            document.getElementById("USERNAMEInput").focus();
        }
    }