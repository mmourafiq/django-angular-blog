'use strict';

var Blog = angular.module("Tipstry", ["ui.bootstrap", "ngResource", "ngCookies"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

Tipstry.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

Blog.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "media/js/app/views/feed.html",
            controller: "FeedController",
            resolve: {
                tips: function (PostService) {
                    return PostService.list();
                }
            }
        })
        .when("/post/:id", {
            templateUrl: "media/js/app/views/posts/view.html",
            controller: "PostController",
            resolve: {
                post: function ($route, PostService) {
                    var postId = $route.current.params.id
                    return BoardService.get(postId);
                }
            }
        })
        .otherwise({
            redirectTo: '/'
        })
})