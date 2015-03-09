var app = angular.module('myapp',[])

app.controller('MydataCtrl', function($scope,$http) {

  $http({
    method: 'get',
    url:'/api/user_daily_mobility_segments/'
  }).success(function(data, status) {
    $scope.user_daily_mobility_segments_data = data;
    // alert(data.length)
    // alert(Object.keys( $scope.user_daily_mobility_segments_data[0].body['segments'][0]['locations'][0]))//.header['segments'][2]['locations']))
    // alert(data[0].body['segments'][2]['locations'][0]['location']['latitude'])//longitude

    google.maps.event.addDomListener(window, 'load', $scope.initialize());

    //  alert(data.length)
    // alert($scope.meal.name)
  }).error(function(data, status) {
    alert(status)

    // alert(data);
  });


  $http({
    method: 'get',
    url:'/api/user_pam_figure'
  }).success(function(data, status) {
    // $scope.user_daily_mobility_segments_data = data;
    alert("data")

    alert(data)

  }).error(function(data, status) {
    alert(status)

    // alert(data);
  });

  $http({
    method: 'get',
    url:'/api/user_daily_mobility_summary/'
  }).success(function(data, status) {
    $scope.user_daily_mobility_summary = data;
    // alert(Object.keys(data[1]))
    // alert(Object.keys(data[1].body))
    // alert(data[0].body)

    // alert($scope.meal.name)
  }).error(function(data, status) {
    alert(status)

    // alert(data);
  });


$scope.initialize = function() {
  var mapCanvas = document.getElementById('map-canvas');
  var mapOptions = {
    center: new google.maps.LatLng(
       $scope.user_daily_mobility_segments_data[0].body['segments'][2]['median-location']['latitude'],
       $scope.user_daily_mobility_segments_data[0].body['segments'][2]['median-location']['longitude']
       ),
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  var map = new google.maps.Map(mapCanvas, mapOptions)
  // alert( $scope.user_daily_mobility_segments_data[0].body['segments'][0]['locations'][0]['location']['longitude'])
  // var flightPlanCoordinates = [  ];
  // flightPlanCoordinates.push(
  //
  // $scope.user_daily_mobility_segments_data[0].body['segments'][0]['locations'][0]['location']['latitude'],
  // $scope.user_daily_mobility_segments_data[0].body['segments'][0]['locations'][0]['location']['longitude']
  // )

  // var marker = new google.maps.Marker({
  //   position:
  //    new google.maps.LatLng(
  //     $scope.user_daily_mobility_segments_data[0].body['segments'][2]['median-location']['latitude'],
  //     $scope.user_daily_mobility_segments_data[0].body['segments'][2]['median-location']['longitude']
  //     ),
  //   map: map,
  //   title: 'Hello World!'
  // });

  var markers =[]
  for (var j = 0 ; j < $scope.user_daily_mobility_segments_data.length ; j++){
  // data[0].body['segments'][0]['locations'][0])
// alert($scope.user_daily_mobility_segments_data[0].body['segments'][0]['locations'].length )
// alert($scope.user_daily_mobility_segments_data[j].body['segments'])

      for (var i = 0 ; i < $scope.user_daily_mobility_segments_data[j].body['segments'][0]['locations'].length ; i++){
        markers.push(new google.maps.Marker({
        position:
        new google.maps.LatLng(
          $scope.user_daily_mobility_segments_data[j].body['segments'][0]['locations'][i]['location']['latitude'],
          $scope.user_daily_mobility_segments_data[j].body['segments'][0]['locations'][i]['location']['longitude']
        ),

        map: map,
        title:   $scope.user_daily_mobility_segments_data[j].body['segments'][0]['locations'][i]['timestamp'],
      })
    )
    }
  }
    // alert(markers.length)

    // google.maps.event.addListener(markers, 'click', function() {
    //   alert(this.customInfo);
    // });

  // var flightPlanCoordinates = [
  // new google.maps.LatLng(44.5403, -78.5463),
  // new google.maps.LatLng(47.5403, -79.5463)
  // ];

  // // for (var city in citymap) {
  //   var populationOptions = {
  //     strokeColor: '#FF0000',
  //     strokeOpacity: 0.8,
  //     strokeWeight: 2,
  //     fillColor: '#FF0000',
  //     fillOpacity: 0.35,
  //     map: map,
  //     center: $scope.user_daily_mobility_segments_data[0].body['segments'][2]['median-location']
  //     radius: Math.sqrt(citymap[city].population) * 100
  //   // };
  //   // Add the circle for this city to the map.
  //   cityCircle = new google.maps.Circle(populationOptions);
  // }

  var flightPath = new google.maps.Polyline({
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  flightPath.setMap(map);



}
// $scope.initialize()

});
