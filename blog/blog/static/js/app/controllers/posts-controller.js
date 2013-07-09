Blog.controller('PostController', function ($scope, $routeParams, $location, PostService, GlobalService, post) {
    $scope.post = post;
    $scope.globals = GlobalService;
    var failureCb = function (status) {
        console.log(status);
    }
    //options for modals
    $scope.opts = {
        backdropFade: true,
        dialogFade: true
    };
    //open modals
    $scope.open = function (action) {
        $scope.postName = $scope.post.name;
        $scope.postDescription = $scope.post.description;
        if (action === 'edit'){
            $scope.postModalEdit = true;
        };
    };
    //close modals
    $scope.close = function (action) {
        $scope.postName = "";
        $scope.postDescription = "";
        if (action === 'edit'){
            $scope.postModalEdit = false;
        };
    };
    //calling board service
    $scope.update = function () {
        PostService.update($scope.post).then(function (data) {
            $scope.post = data;
            $scope.postModalEdit = false;
        }, failureCb);
    };
});