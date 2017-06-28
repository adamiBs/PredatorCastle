$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

$('.collapse').collapse()

function userIDTypeChanged(){
  if(document.getElementById("UIDRadio").checked){
    document.getElementById("UIDInput").disabled = false;
    document.getElementById("UIDBtn").disabled = false;
    document.getElementById("URLInput").disabled = true;
    document.getElementById("URLBtn").disabled = true;
    document.getElementById("UIDInput").focus();
  } else if(document.getElementById("URLRadio").checked){
    document.getElementById("UIDInput").disabled = true;
    document.getElementById("UIDBtn").disabled = true;
    document.getElementById("URLInput").disabled = false;
    document.getElementById("URLBtn").disabled = false;
    document.getElementById("URLInput").focus();
  }
}

function UIDLoad(){
  
}

function URLLoad(){

}