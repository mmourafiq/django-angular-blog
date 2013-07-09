Blog.controller('FeedController', function ($scope, GlobalService, posts) {
    $scope.posts = posts;
    $scope.globals = GlobalService;
});