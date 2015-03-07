'use strict';

var services = angular.module('protocolosServices', []);
/* Services */

services.factory('protocolosAPI', ['$http', '$filter',
    function($http, $filter){
        var protocolosAPI = {};

        protocolosAPI.getProtocolos = function getProtocolos() {
           return _get('protocolos.json');
        };

        protocolosAPI.sendStatus = function sendStatus(protocolo_id, status) {
            var data = {
                protocolo_id: protocolo_id,
                status: status,
            };
            return _post('/status/', data);
        }

        var _get = function(url, params) {
            return $http({
                method: 'GET',
                url: '/protocolos/' + url,
                params: params
            });
        }

        var _post = function (url, data) {
            return $http({
                method: 'POST',
                url: '/protocolos/' + data['protocolo_id'] + url,
                data: data
            });
        }

        return protocolosAPI;
    }
]);


var protocolosControllers = angular.module('protocolosControllers', ['pusher-angular']);

/*var pusherClient = new Pusher(window.pusherToken, {
    encrypted: true
})*/

protocolosControllers.controller('ProtocolosListaController', ['$scope', '$filter', '$pusher', 'protocolosAPI',
  function($scope, $filter, $pusher, protocolosAPI) {
    moment.locale('pt-br');

    //$scope.user = JSON.parse($('input[name=current_user]').val());

    $scope.statusProtocolos = ['NOVO', 'INVALIDO', 'PROCESSADO']

    $scope.loadProtocolos = function loadProtocolos() {
        return protocolosAPI
                .getProtocolos()
                .then(function(response) {
                    $scope.protocolos = response.data.payload;
                });
    }

    $scope.sendStatus = function sendStatus(protocolo, status) {
        return protocolosAPI
            .sendStatus(protocolo.id, status)
            .then(function(response) {
                console.log(response.data);
            });
    }

    /*var pusher = $pusher(pusherClient),
        protocolos_channel = pusher.subscribe("private-protocolos");

    protocolos_channel.bind('novo-pedido', function(pedido) {
        pedido.show = false;
        $scope.protocolos.push(pedido);
        $scope.notification('Novo pedido', pedido.id_gan || "Antecipação da análise de crédito");
    });*/

    $scope.loadProtocolos();
  }
]);

var protocolosDirectives = angular.module('protocolosDirectives', []);
/* Directives */

protocolosDirectives.directive('elapsedTimeSince', function($interval, dateFilter) {
    moment.lang('pt-br')
    var link = function(scope, element, attrs) {
        function pad(num) {
            var s = "0" + num;
            return s.substr(s.length-2);
        }

        var timeoutId,
            initialTime = moment(scope.time);

        function updateTime() {
            var diffms = moment().diff(initialTime),
                duration = moment.duration(diffms);
            if (duration.days() > 0){
                element.text(duration.humanize())
            } else {
                element.text(pad(duration.hours()) + ':' + pad(duration.minutes()) + ':' + pad(duration.seconds()));
            }
        }

        scope.$watch(attrs.elapsedTimeSince, function(value) {
            updateTime();
        });

        timeoutId = $interval(updateTime, 1000);

        element.on('$destroy', function() {
            $interval.cancel(timeoutId);
        });
    }
    return {
        restrict: 'A',
        scope : {
            time: '='
        },
        link: link
    };
});

protocolosDirectives.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });
                event.preventDefault();
            }
        });
    };
});

var protocolosFilters = angular.module('protocolosFilters', []);
/* Filters */

protocolosFilters.filter('checkmark', function() {
    return function(input) {
        return input ? '\u2713' : '\u2718';
    };
});

var protocolosApp = angular.module('protocolosApp', [
    'protocolosFilters',
    'protocolosServices',
    'protocolosControllers',
    'protocolosDirectives',
]);

protocolosApp.constant('moment', moment)

protocolosApp.config(['$interpolateProvider',
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
     }
 ]);



