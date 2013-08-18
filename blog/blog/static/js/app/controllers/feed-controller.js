Blog.controller('FeedController', function ($scope, GlobalService, PostService, TagService, posts) {
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
            $scope.post.tags = [];
            $scope.post.tags_details = [];
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