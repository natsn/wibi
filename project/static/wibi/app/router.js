angular.module('wibi-routes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.when('/', {
      templateUrl: '/static/templates/application.html',
      controller: 'homeCtrl'
    })
    $locationProvider.html5Mode(true); //enables url change abilities without refreshing browser
}]);
