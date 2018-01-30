$(document).ready(function () {
    var navOrbit1 = document.getElementById("nav-orbit1");
    var navOrbit2 = document.getElementById("nav-orbit2");
    var navOrbit3 = document.getElementById("nav-orbit3");
    var navOrbit4 = document.getElementById("nav-orbit4");
    var navOrbit5 = document.getElementById("nav-orbit5");
    var start;
    var stopId;

        
    function step(timestamp) {
        var speed = parseInt(this.dataset.speed);
        var rotation = getRotation(this);
        rotation -= speed * 0.5;        
        setRotation(this, rotation);
        stopId = window.requestAnimationFrame(step.bind(this));
    }

    function setRotation(element, deg) {
        $(element).css({
                '-webkit-transform': 'rotate(' + deg + 'deg)',
                '-moz-transform': 'rotate(' + deg + 'deg)',
                '-ms-transform': 'rotate(' + deg + 'deg)',
                'transform': 'rotate(' + deg + 'deg)'
        });
    }

    function getRotation(elem) {
        var el = elem;
        var st = window.getComputedStyle(el, null);
        var tr = st.getPropertyValue("-webkit-transform") ||
                st.getPropertyValue("-moz-transform") ||
                st.getPropertyValue("-ms-transform") ||
                st.getPropertyValue("-o-transform") ||
                st.getPropertyValue("transform") ||
                "fail...";

        // With rotate(30deg)...
        // matrix(0.866025, 0.5, -0.5, 0.866025, 0px, 0px)
        // console.log('Matrix: ' + tr);

        // rotation matrix - http://en.wikipedia.org/wiki/Rotation_matrix

        var values = tr.split('(')[1];
            values = values.split(')')[0];
            values = values.split(',');
        var a = values[0];
        var b = values[1];
        var c = values[2];
        var d = values[3];

        var scale = Math.sqrt(a*a + b*b);

        // arc sin, convert from radians to degrees, round
        // DO NOT USE: see update below
        var sin = b/scale;
        var angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
        // works!        
        return angle;
    }

    // http://paulirish.com/2011/requestanimationframe-for-smart-animating/
    // http://my.opera.com/emoller/blog/2011/12/20/requestanimationframe-for-smart-er-animating

    // requestAnimationFrame polyfill by Erik Möller. fixes from Paul Irish and Tino Zijdel

    // MIT license

    (function() {
        var lastTime = 0;
        var vendors = ['ms', 'moz', 'webkit', 'o'];
        for(var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
            window.requestAnimationFrame = window[vendors[x]+'RequestAnimationFrame'];
            window.cancelAnimationFrame = window[vendors[x]+'CancelAnimationFrame'] 
                                    || window[vendors[x]+'CancelRequestAnimationFrame'];
        }
    
        if (!window.requestAnimationFrame)
            window.requestAnimationFrame = function(callback, element) {
                var currTime = new Date().getTime();
                var timeToCall = Math.max(0, 16 - (currTime - lastTime));
                var id = window.setTimeout(function() { callback(currTime + timeToCall); }, 
                timeToCall);
                lastTime = currTime + timeToCall;
                return id;
            };
    
        if (!window.cancelAnimationFrame)
            window.cancelAnimationFrame = function(id) {
                clearTimeout(id);
            };
    }());


    window.requestAnimationFrame(step.bind(navOrbit1));
    window.requestAnimationFrame(step.bind(navOrbit2));
    window.requestAnimationFrame(step.bind(navOrbit3));
    window.requestAnimationFrame(step.bind(navOrbit4));
    window.requestAnimationFrame(step.bind(navOrbit5));
});
