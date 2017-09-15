'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope', '$rootScope', '$http', '$location', '$interval', function($scope, $rootScope, $http, $location) {

		$scope.posts = null;

		$scope.showlist = function(){
			$http({
				method: 'GET',
				url: 'http://127.0.0.1:5000/',
			}).then(function(response) {
				$scope.posts = response.data;
				console.log($scope.posts);
			}, function(error) {
				console.log(error);
			});
		}

		$scope.showlist();

		setInterval(function(){
		  $scope.showlist();
		}, 5000)

}]);