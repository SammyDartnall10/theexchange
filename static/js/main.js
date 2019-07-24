


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
    
    


/*
----------------------------------------------------------------------------

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
