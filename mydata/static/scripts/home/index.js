var app = angular.module('myapp',[])

app.controller('MydataCtrl', function($scope,$http) {
  $http({
    method: 'get',
    url:'/api/user_daily_mobility_segments/'
  }).success(function(data, status) {
    $scope.user_daily_mobility_segments_data = data;
     alert(data.message)
    // alert($scope.meal.name)

  }).error(function(data, status) {
    //alert('Server Is Done');
  });

$scope.initialize = function() {
  var mapCanvas = document.getElementById('map-canvas');
  var mapOptions = {
    center: new google.maps.LatLng(44.5403, -78.5463),
    zoom: 8,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  var map = new google.maps.Map(mapCanvas, mapOptions)

  var flightPlanCoordinates = [
  new google.maps.LatLng(44.5403, -78.5463),
  new google.maps.LatLng(47.5403, -79.5463)
  ];
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
google.maps.event.addDomListener(window, 'load', $scope.initialize());

});
