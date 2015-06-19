var app = angular.module('wibiAngApp', ['ngRoute', 'ngResource'])

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.
    when('/', {
      templateUrl: '/static/templates/login.html',
      controller: 'authController'
    })
    $locationProvider.html5Mode(true); //enables url change abilities without refreshing browser
}]);

app.config(['$httpProvider', function($httpProvider){
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    }])

app.service('authState', function () {
        return {
            //redirect the user to login form
        };
    })

app.factory('api', function($resource){
        function add_auth_header(data, headersGetter){
            var headers = headersGetter();
            headers['Authorization'] = ('Basic ' + btoa(data.username +
                                        ':' + data.password));
        }
        return {
            auth: $resource('/api/auth\\/', {}, {
                login:  {method: 'POST', transformRequest: add_auth_header},
                logout: {method: 'DELETE'}
            }),
        };
    })

app.controller('authController', function($scope, api, authState) {
        
        $('#id_auth_form input').checkAndTriggerAutoFillEvent();

        $scope.authState = authState;

        $scope.getCredentials = function(){
            return {username: $scope.username, password: $scope.password};
        };
        $scope.login = function(){
            api.auth.login($scope.getCredentials()).
                $promise.
                    then(function(data){
                        authState.user = data.username;
                    }).
                    catch(function(data){
                        alert(data.data.detail);
                    });
        };
        $scope.logout = function(){
            api.auth.logout(function(){
                authState.user = undefined;
            });
        };
    });
