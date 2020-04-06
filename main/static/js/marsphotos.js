$(document).ready(function () {
     




    var x = [];
    var stringToRover = 'https://api.nasa.gov/mars-photos/api/v1/rovers/';
    var stringToSol = '/photos?sol=';
    var stringToCam = "&camera=";
    var apiKey = '&api_key=h682M1TtACh5yUFgarcjpY16ExxNF8wVRDj9vXVi';

    $("#showPhoto").click(function () {
        $("#marsPhotos").empty();


        var rover = $('#selectRover').find(':selected').text();
        var cam = $('#selectCamera').find(':selected').text();
        var sol = parseInt($('#selectSol').val());

        $.ajax({

            url: stringToRover + rover + stringToSol + sol + stringToCam + cam + apiKey,
            success: function (result) {

                a = JSON.stringify(result);
                b = JSON.parse(a);

                var i = 1;
                var j = 0;
                //x[i] = result.photos[i].img_src;
                //console.log(b['photos'][0]);

                for (var k = 0; k < b['photos'].length; k++) {
                    console.log(b['photos'][k]);


                    src = b['photos'][k].img_src;


                    /*  for (var i = 0; i < 5; i++) {
                          src = data["photos"][i]["img_src"];
                          $("#marsPhotos").append("<li>" +
                              "<div class=\"preview\">" +
                              "<img alt=\" \" src=\"" + src + "\">" +
                              "<div class=\"overlay\">" +
                              "</div>" +
                              "<div class=\"links\">" +
                              "<a data-toggle=\"moda\" href=\"#modal-1\"><i class=\"icon-eye-open\"></i></a><a href=\"#\"><i class=\"icon-link\"></i></a>" +
                              "</div>" +
                              "</div>" +
                              "<div class=\"desc\">" +
                              "<h5>Lorem ipsum dolor sit amet</h5>" +
                              "<small>Portfolio item short description</small>" +
                              "</div>" +
                              "<div id=\"modal-1\" class=\"modal hide fade\">" +
                              "<a class=\"close-modal\" href=\"javascript:;\" data-dismiss=\"modal\" aria-hidden=\"true\"><i class=\"icon-remove\"></i></a>" +
                              "<div class=\"modal-body\">" +
                              "<img src=\"" + src + "\" alt=\" \" width=\"100%\" style=\"max-height:400px\">" +
                              "</div>" +
                              "</div>" +
                              "</li>");
                      }*/
                      
                    $("#marsPhotos").append("<li>" +
                        "<div class=\"preview\">" +
                        "<img alt=\" \" src=\"" + src + "\">" +
                        "<div class=\"overlay\">" +
                        "</div>" +
                        "<div class=\"links\">" +
                        "<a data-toggle=\"moda\" href=\"" + src + "\"><i class=\"icon-eye-open\"></i></a><a href=\"#\"><i class=\"icon-link\"></i></a>" +
                        "</div>" +
                        "</div>" +
                        "<div class=\"desc\">" +
                        "<h5>Lorem ipsum dolor sit amet</h5>" +
                        "<small>Portfolio item short description</small>" +
                        "</div>" +
                        "</li>");
                }




            }
        });
    });

});