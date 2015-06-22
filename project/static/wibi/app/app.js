var app = angular.module('wibiAngApp', ['ngRoute', 'ngResource'])

app.config(['$routeProvider', '$locationProvider', '$httpProvider', function($routeProvider, $locationProvider, $httpProvider) {
    $routeProvider.
    when('/', {
      templateUrl: '/static/templates/login.html',
      controller: 'authController'
    }).
    when('/particpant/', {
      templateUrl: '/static/templates/participant.html',
      controller: 'partiController'
    }).
    when('/coach/', {
      templateUrl: '/static/templates/coach.html',
      controller: 'coachController'
    }).
    when('/trainer/', {
      templateUrl: '/static/templates/trainer.html',
      controller: 'trainerController'
    })
    $locationProvider.html5Mode(true); //enables url change abilities without refreshing browser
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


app.controller('authController', ['$scope', '$http', '$location', function($scope, $http, $location){
    $scope.message = '';
    $scope.alert_type = ""
    $scope.login = function(){
        var data = {'username':$scope.username, 'password':$scope.password};
        console.log(data)
        $http.post('/login/', data).
          success(function(data, status, headers, config) {
            if(data.success){
                $scope.alert_type = "alert-success"
                $scope.message = data.message;
                $location.path('/particpant/');
                console.log('yeah!'); // Change the UI
            } else {
                $scope.alert_type = "alert-danger"
                $scope.message = data.message;
                console.log('NOOO!!'); // Display message
            }
            // this callback will be called asynchronously
            // when the response is available
          }).
          error(function(data, status, headers, config) {
            console.log('crap!')
            // called asynchronously if an error occurs
            // or server returns response with an error status.
          });
    };
}]);

app.controller('partiController', ['$scope', function($scope){
    $scope.username = 'testing';
}]);
