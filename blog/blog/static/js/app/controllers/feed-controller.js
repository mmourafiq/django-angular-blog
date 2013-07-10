Blog.controller('FeedController', function ($scope, GlobalService, PostService, posts) {
    $scope.posts = posts;
    $scope.globals = GlobalService;
    //options for modals
    $scope.opts = {
        backdropFade: true,
        dialogFade: true
    };
    //open modals
    $scope.open = function (action) {
        if (action === 'create'){
            $scope.postModalCreate = true;
            $scope.post = new Object();
        };
    };
    //close modals
    $scope.close = function (action) {
        if (action === 'create'){
            $scope.postModalCreate = false;
        };
    };
    //calling board service
    $scope.create = function () {
        PostService.save($scope.post).then(function (data) {
            $scope.post = data;
            $scope.posts.push(data);
            $scope.postModalCreate = false;
        }, function(status){
            console.log(status);
        });
    };
});