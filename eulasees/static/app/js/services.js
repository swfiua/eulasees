var eulaseesServices = angular.module('myApp.eulaseesServices',['ngResource']);

eulaseesServices.factory('Eula', ['$resource',
  function($resource){
    return $resource('http://192.168.1.8:8000/eulasees/everythingforeula/', {}, {
      query: {method:'GET', params:{eulaId:'Eula'}, isArray:true}
    });
  }]);

