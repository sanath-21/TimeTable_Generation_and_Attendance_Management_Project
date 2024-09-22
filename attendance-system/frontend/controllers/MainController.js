angular.module('attendanceApp', [])
    .controller('MainController', function ($scope, $http) {
        $scope.isModalOpen = false;
        $scope.userRole = null;  // Track user role (student/teacher)

        // Open modal
        $scope.openModal = function () {
            $scope.isModalOpen = true;
        };

        // Close modal
        $scope.closeModal = function () {
            $scope.isModalOpen = false;
        };

        // Handle Login Submission
        $scope.submitLogin = function () {
            $http.post('/login', $scope.loginData).then(function (response) {
                alert("Login successful!");
                $scope.userRole = response.data.role;
                $scope.closeModal();
            }).catch(function (error) {
                if (error.status === 401) {
                    alert("Invalid login credentials!");
                } else if (error.status === 404) {
                    alert("User not found! Please sign up.");
                } else {
                    alert("An error occurred during login.");
                }
            });
        };

        // Handle Sign-up Submission
        $scope.submitSignup = function () {
            $http.post('/signup', $scope.signupData).then(function (response) {
                alert("Signup successful!");
                $scope.userRole = $scope.signupData.role;  // Set role after signup
                $scope.closeModal();
            }).catch(function (error) {
                if (error.status === 400) {
                    alert("User already exists!");
                } else {
                    alert("Signup failed! Please try again.");
                }
            });
        };

        // Handle Logout
        $scope.logout = function () {
            $scope.userRole = null;
            alert("You have logged out.");
        };

        // Initialize empty data objects
        $scope.loginData = {
            email: '',
            password: ''
        };

        $scope.signupData = {
            name: '',
            email: '',
            phone_number: '',
            password: '',
            repeatPassword: '',
            role: 'student'
        };
    });
