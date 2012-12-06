/*global requirejs, require, OpenLayers, jQuery, $, Raphael, stations, console  */
/*jslint indent: 4 */
"use strict";
requirejs.config({
    paths: {
        'jquery' : 'lib/jquery',
        'underscore' : 'lib/underscore',
        'bootstrap': 'lib/bootstrap',
        'openlayers': 'lib/OpenLayers'
    },
    shim: {
        'bootstrap' : {
            'deps' : ['jquery']
        },
    }
});
require(['jquery', 'underscore', 'bootstrap', 'openlayers'], function ($, _) {

    var layers = jQuery.parseJSON(layers), layer = null;

    for (layer in layers) {
        console.log(layer, layers[layer]);
    }

    var map = L.map('map').setView([52.4, 5.8], 9);

    L.tileLayer('http://{s}.tile.cloudmade.com/2a821ef633ec46428cbb11db251bac65/{styleId}/256/{z}/{x}/{y}.png', {
        styleId: 999,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18
    }).addTo(map);

}); // end requirejs
