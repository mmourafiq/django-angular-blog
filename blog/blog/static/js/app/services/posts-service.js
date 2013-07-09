Blog.factory('PostService', function ($http, $q) {
    var api_url = "/post/";
    var successcb = function(data, status, headers, config) {
                    defer.resolve(data);
                    };
    var errorcb = function(data, status, headers, config) {
                    defer.reject(status);
                }
    return {
        get: function(post_id){
            var url = api_url + post_id+ "/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(successcb).error(errorcb);
            return defer.promise;
        },
        list: function(){
            var defer = $q.defer();
            $http({method: 'GET', url: api_url}).
                success(successcb).error(errorcb);
            return defer.promise;
        },
        update: function(post){
            var url = api_url + post.id+ "/";
            var defer = $q.defer();
            $http({method: 'PUT',
                    url: url,
                    data: post}).
                success(successcb).error(errorcb);
            return defer.promise;
        },
        save: function(post){
            var url = api_url;
            var defer = $q.defer();
            $http({method: 'POST',
                    url: url,
                    data: post}).
                success(successcb).error(errorcb);
            return defer.promise;
        },
    }
});