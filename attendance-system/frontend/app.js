var app = angular.module('attendanceApp', ['ngRoute']);

// Configuring routes
app.config(function($routeProvider) {
    $routeProvider
        .when('/home', {
            templateUrl: 'home.html',
            controller: 'MainController'
        })
        .when('/attendance', {
            templateUrl: 'attendance.html',
            controller: 'AttendanceController'
        })
        .when('/timetable', {
            templateUrl: 'timetable.html',
            controller: 'TimetableController'
        })
        .when('/blogs', {
            templateUrl: 'blogs.html',
            controller: 'BlogsController'
        })
        .otherwise({
            redirectTo: '/home'
        });
});

// MainController: Handles user authentication and modals
app.controller('MainController', function($scope, $http) {
    $scope.userRole = null;
    $scope.isModalOpen = false;

    // Open the login/signup modal
    $scope.openModal = function() {
        $scope.isModalOpen = true;
    };

    // Close the modal
    $scope.closeModal = function() {
        $scope.isModalOpen = false;
    };

    // Submit login request
    $scope.submitLogin = function() {
        $http.post('/login', $scope.loginData).then(function(response) {
            $scope.userRole = response.data.role;  // Update the user's role upon successful login
            $scope.closeModal();
        }, function(error) {
            alert("Invalid credentials, please try again.");
        });
    };

    // Submit signup request
    $scope.submitSignup = function() {
        $http.post('/signup', $scope.signupData).then(function(response) {
            alert("Sign up successful! Please log in.");
            $scope.closeModal();
        }, function(error) {
            alert("Error during sign up.");
        });
    };

    // Logout function
    $scope.logout = function() {
        $scope.userRole = null;
    };
});
