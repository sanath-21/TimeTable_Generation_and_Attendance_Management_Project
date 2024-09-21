angular.module('attendanceApp')
    .controller('MainController', ['$scope', function($scope) {
        $scope.isModalOpen = false;
        $scope.isLogin = true; // Default to login view
        $scope.loginData = {};
        $scope.signupData = {};

        $scope.openModal = function() {
            $scope.isModalOpen = true;
        };

        $scope.closeModal = function() {
            $scope.isModalOpen = false;
            $scope.isLogin = true; // Reset to login view on close
        };

        $scope.toggleLogin = function() {
            $scope.isLogin = !$scope.isLogin; // Toggle between login and signup
        };

        $scope.submitLogin = function() {
            // Logic for logging in
            console.log('Logging in:', $scope.loginData);
        };

        $scope.submitSignup = function() {
            // Logic for signing up
            console.log('Signing up:', $scope.signupData);
        };
    }]);
