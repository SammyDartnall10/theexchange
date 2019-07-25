


function upvote(e){
    var pk = $(e).attr('id');
        
        var colour = document.getElementById(pk).style.cssText;
        console.log(colour);
        
        if ( colour = "black") {
            console.log("turn it red");
            console.log(document.getElementById(pk));
            document.getElementById(pk).style = "color: red";
            $.ajax({
                type: "POST",
                url: "upvote",
                data: { pk: pk },
                success: function(response){
                   console.log(response);
                   document.location.href = 'exchange';
                   document.getElementById(pk).scrollIntoView();
                            }
                });
                    
        } 
        else 
        {
                
            console.log("it must be red, so turn it black");
            console.log(document.getElementById(pk));
            document.getElementById(pk).style = "color: black";
            $.ajax({
                type: "POST",
                url: "downvote",
                data: { pk: pk },
                success: function (response){
                   console.log(response);
                   document.location.href = 'exchange';
                   document.getElementById(pk).scrollIntoView();
                        }
            });
        }
    }

/*---------Places API - Google------------------------------------------------*/
/*
    
var map;
var service;
var infowindow;

      function initMap() {
        var input = document.getElementById("companyCity");
        var city = input.innerHTML;
        
        console.log(city)
        console.log("started map function")  
        
        var sydney = new google.maps.LatLng(-33.867, 151.195);

        infowindow = new google.maps.InfoWindow();

        map = new google.maps.Map(
            document.getElementById('map'), {center: sydney, zoom: 15});

        var request = {
          query: 'Museum of Contemporary Art Australia',
          fields: ['name', 'geometry'],
        };

        service = new google.maps.places.PlacesService(map);

        service.findPlaceFromQuery(request, function(results, status) {
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {
              createMarker(results[i]);
            }

            map.setCenter(results[0].geometry.location);
          }
        });
      }

      function createMarker(place) {
        var marker = new google.maps.Marker({
          map: map,
          position: place.geometry.location
        });

        google.maps.event.addListener(marker, 'click', function() {
          infowindow.setContent(place.name);
          infowindow.open(map, this);
        });
      }
      
*/

/*----------------------------------------------------------------------------*/
var map;
var service;
var infowindow;
var geocoder;
var markers;
var endLocation;


function initMap() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-41.28664, 174.77557);
    var mapOptions = {
        zoom: 13,
        center: latlng
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    
    var input = document.getElementById("companyCity");
        var city = input.innerHTML;
        
        console.log(city);
        console.log("started map function");

        /*geocoding API from Google */

        geocoder.geocode({ 'address': city }, function(results, status) {

            if (status == 'OK') {
                var location = {};

                location['lat'] = results[0].geometry.location.lat();
                location['lng'] = results[0].geometry.location.lng();

                map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location

                });
                markers.push(marker);

                marker.addListener('click', function() {
                    map.setZoom(16);
                    map.setCenter(marker.getPosition());
                    endLocation = marker.getPosition();
                    var infowindow = new google.maps.InfoWindow({
                        content: '<p>Marker Location:' + marker.getPosition() + '</p>'
                    });

                    google.maps.event.addListener(marker, 'click', function() {
                        infowindow.open(map, marker);
                    });
                });

                location['marker'] = marker;

                /*selection.geolocation global variable - pass the lat and lng to the object declared at beginning of code*/

                selection.geolocation = location;

                return location;
                //console logging to make sure code is running.. 
            }
            else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
}




/*----------------------------------------------------------------------------







# urls.py
urlpatterns = [
   url(r'^$', views.index, name = 'index'),
   path('my-ajax-test/', views.testcall),
]

<!-- index.html -->
<script>
....

var text = "test successful";

$.ajax({
   type: "POST",
   url: '{{ 'my-ajax-test/' }}',
   data: { csrfmiddlewaretoken: '{{ csrf_token }}', text: text },
   success: function callback(response){
               console.log(response);
            }
});
</script>

# views.py
def testcall(request):
   return HttpResponse(request.POST['text'])
   
      
----------------------------------------------------------------------------
   
function request_access($this){
    console.log("button clicked");
    var request_data = $this.id;
    console.log("data: " + request_data);
    $.ajax({
        url: "request_access/",
        data : { request_data: request_data},
        success : function(json) {
            $("#request-access").hide();
            console.log("requested access complete");
        }
    })
}
*/
