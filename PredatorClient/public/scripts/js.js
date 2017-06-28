var ProgressBar = require('progressbar.js')


$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

$('.collapse').collapse()

var bar = new ProgressBar.Circle(suspectPercent, {
  strokeWidth: 6,
  easing: 'easeInOut',
  duration: 1400,
  color: '#FFEA82',
  trailColor: '#eee',
  trailWidth: 1,
  svgStyle: null
});

bar.animate(1.0);

function userIDTypeChanged(){
  if(document.getElementById("UIDRadio").checked){
    document.getElementById("UIDInput").disabled = false;
    document.getElementById("UIDBtn").disabled = false;
    document.getElementById("URLInput").disabled = true;
    document.getElementById("URLBtn").disabled = true;
    document.getElementById("URLInput").value = "";
    document.getElementById("UIDInput").focus();
  } else if(document.getElementById("URLRadio").checked){
    document.getElementById("UIDInput").disabled = true;
    document.getElementById("UIDBtn").disabled = true;
    document.getElementById("URLInput").disabled = false;
    document.getElementById("URLBtn").disabled = false;
    document.getElementById("UIDInput").value = "";
    document.getElementById("URLInput").focus();
  }
}


function UIDLoad(){
    var uId = document.getElementById("UIDInput").value;
    getUserProfilePicture(uId);
}

function URLLoad(){   
}

function getUserProfilePicture(p_uID){
    var url = "https://graph.facebook.com/"+p_uID+"/picture?type=large&w%E2%80%8Cidth=720&height=720";
    document.getElementById("profilePicture").src = url;  
}

function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function sendRequest(){

}