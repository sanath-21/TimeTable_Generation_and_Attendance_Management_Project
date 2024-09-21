angular.module('attendanceApp', ['ngRoute'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/home', {
                templateUrl: 'views/home.html',
                controller: 'MainController'
            })
            .when('/attendance', {
                templateUrl: 'views/attendance.html',
                controller: 'AttendanceController'
            })
            .when('/timetable', {
                templateUrl: 'views/timetable.html',
                controller: 'TimetableController'
            })
            .when('/blogs', {
                templateUrl: 'views/blogs.html',
                controller: 'BlogsController'
            })
            .otherwise({
                redirectTo: '/home'
            });
    }]);
