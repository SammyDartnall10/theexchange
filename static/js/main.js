

function upvote(e){
    
    var pk = $(e).attr('id');
        
            console.log("upvoting");
            console.log(document.getElementById(pk));
            console.log("its black - turn it red");
            document.getElementById(pk).style = "color: red";
            $.ajax({
                type: "POST",
                url: "upvote",
                data: { pk: pk },
                success: function(response){
                    console.log("helloooooo");
                    var count = response;
                    console.log(`Upvotes is: ${count}`);
                    document.getElementById(`upvotecount${pk}`).innerHTML = `Upvotes: ${count}`;
                    document.getElementById(pk).onclick = "downvote(this)";
                  
                            }
                });
}
           
           
function downvote(e){
    
    var pk = $(e).attr('id');
    
            console.log("it must be red, so turn it black");
            console.log(document.getElementById(pk));
            document.getElementById(pk).style = "color: black";
            $.ajax({
                type: "POST",
                url: "downvote",
                data: { pk: pk },
                success: function (response){
                    console.log("downvote response");
                    var count = response;
                    console.log(`Upvotes is: ${count}`);
                    document.getElementById(`upvotecount${pk}`).innerHTML = `Upvotes: ${count}`;
                    document.getElementById(pk).onclick = "upvote(this)";
                        }
            });
       
    }

/*---------Places API - Google------------------------------------------------*/

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




/*----Changing Textt ---------------------------------------------------*/


$( "div.about" )
  .mouseover(function() {
    $( this ).find( "span" ).text( "☛" );
    $( this ).find( "span" ).css('color','black');
    $( this ).find( "a" ).css('text-decoration','none');
  })
  .mouseout(function() {
    $( this ).find( "span" ).text( "ABOUT" );
    $( this ).find( "span" ).css('color','grey');
    $( this ).find( "a" ).css('text-decoration','none');
    
  });
  
$( "div.register" )
  .mouseover(function() {
    $( this ).find( "span" ).text( "💡" );
    $( this ).find( "a" ).css('text-decoration','none');
  })
  .mouseout(function() {
    $( this ).find( "span" ).text( "REGISTER" );
    $( this ).find( "span" ).css('color','grey');
    $( this ).find( "a" ).css('text-decoration','none');
  });
  
$( "div.login" )
  .mouseover(function() {
    $( this ).find( "span" ).text( "☚" );
    $( this ).find( "span" ).css('color','black');
    $( this ).find( "a" ).css('text-decoration','none');
  })
  .mouseout(function() {
    $( this ).find( "span" ).text( "LOGIN" );
    $( this ).find( "span" ).css('color','grey');
    $( this ).find( "a" ).css('text-decoration','none');
  });
  
  


