/*global requirejs, require, OpenLayers, jQuery, $, Raphael, stations, console  */
/*jslint indent: 4 */
"use strict";
requirejs.config({
    paths: {
        'jquery' : 'lib/jquery',
        'underscore' : 'lib/underscore',
        'bootstrap': 'lib/bootstrap',
        'openlayers': 'lib/OpenLayers',
    },
    shim: {
        'bootstrap' : {
            'deps' : ['jquery']
        },
    }
});
require(['jquery', 'underscore', 'bootstrap', 'openlayers'], function ($, _) {

layers =  jQuery.parseJSON(layers)
for (var layer in layers) {
    console.log(layer, layers[layer]);
}


}); // end requirejs
