/*global requirejs, require, OpenLayers, jQuery, $, Raphael, stations, console  */
/*jslint indent: 4 */
"use strict";
requirejs.config({
    paths: {
        'jquery' : 'lib/jquery',
        'underscore' : 'lib/underscore',
        'bootstrap': 'lib/bootstrap',
        'openlayers': 'lib/OpenLayers',
        'stamen': 'http://maps.stamen.com/js/tile.stamen.js?v1.2.1'
    },
    shim: {
        'bootstrap' : {
            'deps' : ['jquery']
        }
    }
});
require(['jquery', 'underscore', 'bootstrap', 'openlayers', 'stamen'], function ($, _) {

    layers = jQuery.parseJSON(layers);

    //for (layer in layers) {
    //    console.log(layer, layers[layer]);
    //}

    // stamen maps
    var toner = new L.StamenTileLayer("toner-lite");

    var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/2a821ef633ec46428cbb11db251bac65/{styleId}/256/{z}/{x}/{y}.png',
        cloudmadeAttribution = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>';

    var minimal = L.tileLayer(cloudmadeUrl, {styleId: 22677, attribution: cloudmadeAttribution}),
        standard = L.tileLayer(cloudmadeUrl, {styleId: 997, attribution: cloudmadeAttribution}),
        midnight = L.tileLayer(cloudmadeUrl, {styleId: 999, attribution: cloudmadeAttribution});

    var baseMaps = {
        "Minimal": minimal,
        "Standard": standard,
        "Midnight": midnight,
        "Toner": toner
    };

    var overlayMaps = {}, popupContent = '';
    // data layer
    var addUserLayers = function (layers) {
        var i = 0, userLayers = [], layer;
        for (layer in layers) {
            console.log(layer);
            popupContent = "FILEID: "; // feature.properties.FID
            userLayers[i] = L.geoJson(layers[layer].data, {
                onEachFeature: function (feature, layer) {
                    layer.bindPopup(popupContent + feature.properties.FID);
                }
            });

            overlayMaps[layer] = userLayers[i];
        }
        return [userLayers, overlayMaps];
    }
    
    var userMaps = addUserLayers(layers);
    var userLayers = userMaps[0];
    var overlayMaps = userMaps[1];

    var map = L.map('map', {layers: [minimal]}).setView([52.4, 5.8], 9);

    L.control.layers(baseMaps, overlayMaps).addTo(map);

    // popups for the data layer
    var popup = L.popup();
    function onDataClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(map);
    }

    // jQuery UI shizzle
    $('#informationtoggle').on('click', function (e) {
        if ($('#mapcontainer').attr('class') === 'span12') {
            $(this).addClass('btn-primary');
            $("#mapcontainer").removeClass('span12').addClass('span8');
            $("#map").animate({height: '-=100', width: '-=400'});
            $("#information").toggle();
        } else {
            $(this).removeClass('btn-primary');
            $("#mapcontainer").removeClass('span8').addClass('span12');
            $("#map").animate({height: '+=100', width: '+=400'});
            $("#information").toggle();
        }
    });

}); // end requirejs
