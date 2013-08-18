Blog.controller('PostController', function ($scope, $routeParams, $location, PostService, TagService, GlobalService, post) {
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
        if (action === 'edit'){
            $scope.postModalEdit = true;
        };
    };
    //close modals
    $scope.close = function (action) {
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
    $scope.getTag = function (text) {
        return TagService.query(text).then(function (data) {
            return data;
        }, function (status) {
            console.log(status);
        });
    };
    $scope.selectTag = function () {
        if (typeof $scope.selectedTag === 'object') {
            $scope.post.tags.push($scope.selectedTag.url);
            $scope.post.tags_details.push($scope.selectedTag);
            $scope.selectedTag = null;
        }
    };
    $scope.removeTag = function (category) {
        var index = $scope.post.tags_details.indexOf(category);
        $scope.post.tags_details.splice(index, 1);
        var index = $scope.post.tags.indexOf(category.url);
        $scope.post.tags.splice(index, 1);
    };
});