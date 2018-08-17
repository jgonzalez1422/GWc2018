var lat;
var lng;

function sunriseTime () {
  lat = document.getElementById("lat").value;
  lng = document.getElementById("lng").value;
  var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
  //gets us to doc that has info about user latitude/longitude values
  var request = new XMLHttpRequest();
  request.open('GET', query, false);
  request.send();
  var requestInfo = JSON.parse(request.responseText);
  var sunriseTime = requestInfo.results.sunrise;
  alert("The sunrise time is " + sunriseTime);

}
 function sunsetTime() {
   lat = document.getElementById("lat").value;
   lng = document.getElementById("lng").value;
   var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
   //gets us to doc that has info about user latitude/longitude values
   var request = new XMLHttpRequest();
   request.open('GET', query, false);
   request.send();
   var requestInfo = JSON.parse(request.responseText);
   var sunsetTime = requestInfo.results.sunset;
   alert("The sunset time is " + sunsetTime);

 }
