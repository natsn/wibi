angular.module('homeCtrl', []).controller('homeCtrl', ['$scope', '$http', function($scope, $http) {
	$http.get('/api/users/1/').success(function(username) {
	    $scope.username = username.username;
	    console.log($scope.username);
	    });
  	}
]);