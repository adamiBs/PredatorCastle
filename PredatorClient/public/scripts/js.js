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
    document.getElementById("USERNAMEInput").disabled = true;
    document.getElementById("USERNAMEBtn").disabled = true;
    document.getElementById("USERNAMEInput").value = "";
    document.getElementById("UIDInput").focus();
  } else if(document.getElementById("USERNAMERadio").checked){
    document.getElementById("UIDInput").disabled = true;
    document.getElementById("UIDBtn").disabled = true;
    document.getElementById("USERNAMEInput").disabled = false;
    document.getElementById("USERNAMEBtn").disabled = false;
    document.getElementById("UIDInput").value = "";
    document.getElementById("USERNAMEInput").focus();
  }
}



function UIDLoad(){
    var uId = document.getElementById("UIDInput").value;
    getUserProfileData(uId);    
}

function USERNAMELoad(){   
    alert("Not yet implemented")
}

function getUserProfileData(p_uID){
    var access_token ="EAACEdEose0cBAF0kWBMiznqwj5RTzpm9GadhcX7LmBJ38IYYezzyRVBORUu6v7zeDYO0dOi4tksUCStpwEtntIDMCZA2ZBRaOxxs7WihgG0iAsqkUc8NtYhwZB2D2UFHJPQYdPJMRo49VVszZC1txFlVDGNXxZBSXhKYykqZAHTW5BKxSphGnmBoWg0HCjLzMZD";
    
    var url = "https://graph.facebook.com/"+p_uID+"/picture?type=large&w%E2%80%8Cidth=720&height=720";
    document.getElementById("profilePicture").src = url;
    document.getElementById("uIdSpan").innerHTML = p_uID;
    
    var url = "https://graph.facebook.com/"+p_uID+"?fields=name&access_token="+access_token;
    httpGetAsync(url,function(x){
        document.getElementById("nameSpan").innerHTML = JSON.parse(x).name;
    })
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
    var uId = undefined;
    
    if(document.getElementById("UIDRadio").checked){
        uId = document.getElementById("UIDInput").value
    }
    
}