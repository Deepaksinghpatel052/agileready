/** @type {!Array} */
var _cf = _cf || [];
var bmak = bmak || {
    ver : 1.54,
    _sd_trace: "",
    ke_cnt_lmt : 150,
    mme_cnt_lmt : 100,
    mduce_cnt_lmt : 75,
    pme_cnt_lmt : 25,
    pduce_cnt_lmt : 25,
    tme_cnt_lmt : 25,
    tduce_cnt_lmt : 25,
    doe_cnt_lmt : 10,
    dme_cnt_lmt : 10,
    vc_cnt_lmt : 100,
    doa_throttle : 0,
    dma_throttle : 0,
    session_id : "default_session",
    js_post : false,
    loc : "",
    cf_url : ("https:" === document["location"]["protocol"] ? "https://" : "http://") + "apid.cformanalytics.com/api/v1/attempt",
    params_url : ("https:" === document["location"]["protocol"] ? "https://" : "http://") + document["location"]["hostname"] + "/get_params",
    auth : "",
    api_public_key : "afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq",
    aj_lmt_doact : 1,
    aj_lmt_dmact : 1,
    aj_lmt_tact : 1,
    ce_js_post : 0,
    init_time : 0,
    informinfo : "",
    prevfid : -1,
    fidcnt : 0,
    sensor_data : 0,
    ins : null,
    cns : null,
    enGetLoc : 0,
    enReadDocUrl : 1,
    disFpCalOnTimeout : 0,
    xagg : -1,
    pen : -1,
    brow : "",
    browver : "",
    psub : "-",
    lang : "-",
    prod : "-",
    plen : -1,
    doadma_en : 0,
    sdfn : [],
    d2 : 0,
    d3 : 0,
    thr : 0,
    cs : "0a46G5m17Vrp4o4c",
    hn : "unk",
    z1 : 0,
    o9 : 0,
    vc : "",
    y1 : 2016,
    ta : 0,
    tst : -1,
    t_tst : 0,
    ckie : "_abck",
    n_ck : "0",
    ckurl : 0,
    bm : false,
    mr : "-1",
    altFonts : false,
    rst : false,
    runFonts : false,
    fsp : false,
    firstLoad : true,
    pstate : false,
    mn_mc_lmt : 10,
    mn_state : 0,
    mn_mc_indx : 0,
    mn_sen : 0,
    mn_tout : 100,
    mn_stout : 1e3,
    mn_ct : 1,
    mn_cc : "",
    mn_cd : 1e4,
    mn_lc : [],
    mn_ld : [],
    mn_lcl : 0,
    mn_al : [],
    mn_il : [],
    mn_tcl : [],
    mn_r : [],
    mn_abck : "",
    mn_psn : "",
    mn_ts : "",
    mn_lg : [],
    ir : function() {
        bmak["start_ts"] = Date["now"] ? Date["now"]() : +new Date;
        bmak["kact"] = "";
        /** @type {number} */
        bmak["ke_cnt"] = 0;
        /** @type {number} */
        bmak["ke_vel"] = 0;
        bmak["mact"] = "";
        /** @type {number} */
        bmak["mme_cnt"] = 0;
        /** @type {number} */
        bmak["mduce_cnt"] = 0;
        /** @type {number} */
        bmak["me_vel"] = 0;
        bmak["pact"] = "";
        /** @type {number} */
        bmak["pme_cnt"] = 0;
        /** @type {number} */
        bmak["pduce_cnt"] = 0;
        /** @type {number} */
        bmak["pe_vel"] = 0;
        bmak["tact"] = "";
        /** @type {number} */
        bmak["tme_cnt"] = 0;
        /** @type {number} */
        bmak["tduce_cnt"] = 0;
        /** @type {number} */
        bmak["te_vel"] = 0;
        bmak["doact"] = "";
        /** @type {number} */
        bmak["doe_cnt"] = 0;
        /** @type {number} */
        bmak["doe_vel"] = 0;
        bmak["dmact"] = "";
        /** @type {number} */
        bmak["dme_cnt"] = 0;
        /** @type {number} */
        bmak["dme_vel"] = 0;
        bmak["vcact"] = "";
        /** @type {number} */
        bmak["vc_cnt"] = 0;
        /** @type {number} */
        bmak["aj_indx"] = 0;
        /** @type {number} */
        bmak["aj_ss"] = 0;
        /** @type {number} */
        bmak["aj_type"] = -1;
        /** @type {number} */
        bmak["aj_indx_doact"] = 0;
        /** @type {number} */
        bmak["aj_indx_dmact"] = 0;
        /** @type {number} */
        bmak["aj_indx_tact"] = 0;
        /** @type {number} */
        bmak["me_cnt"] = 0;
        /** @type {number} */
        bmak["pe_cnt"] = 0;
        /** @type {number} */
        bmak["te_cnt"] = 0;
        bmak["nav_perm"] = "";
    },
    get_cf_date : function() {
        return Date["now"] ? Date["now"]() : +new Date;
    },
    sd_debug : function(a, _sd_trace) {
        if (!bmak["js_post"]) {
            var hash_1 = a;

            if ("string" == typeof _sd_trace) {

                _sd_trace = _sd_trace + hash_1;
            } else {
                _sd_trace = hash_1;
            }
        }
    },
    pi : function(name) {
        return parseInt(name);
    },
    uar : function() {
        return window["navigator"]["userAgent"]["replace"](/\|"/g, "");
    },
    gd : function() {
        var artistTrack = bmak["uar"]();
        var t = "" + bmak["ab"](artistTrack);
        /** @type {number} */
        var e = bmak["start_ts"] / 2;
        var n = window["screen"] ? window["screen"]["availWidth"] : -1;
        var o = window["screen"] ? window["screen"]["availHeight"] : -1;
        var m = window["screen"] ? window["screen"]["width"] : -1;
        var r = window["screen"] ? window["screen"]["height"] : -1;
        var i = window["innerWidth"] || document["body"]["clientWidth"];
        var c = window["innerHeight"] || document["body"]["clientHeight"];
        var b = window["outerWidth"] || document["body"]["outerWidth"];
        bmak["z1"] = bmak["pi"](bmak["start_ts"] / (bmak["y1"] * bmak["y1"]));
        var SEARCH = Math["random"]();
        var sVectors = bmak["pi"](1e3 * SEARCH / 2);
        var s = SEARCH + "";
        return s = s["slice"](0, 11) + sVectors, bmak["get_browser"](), bmak["bc"](), bmak["bmisc"](), artistTrack + ",uaend," + bmak["xagg"] + "," + bmak["psub"] + "," + bmak["lang"] + "," + bmak["prod"] + "," + bmak["plen"] + "," + bmak["pen"] + "," + bmak["wen"] + "," + bmak["den"] + "," + bmak["z1"] + "," + bmak["d3"] + "," + n + "," + o + "," + m + "," + r + "," + i + "," + c + "," + b + "," +
        bmak["bd"]() + "," + t + "," + s + "," + e + ",loc:" + bmak["loc"];
    },
    get_browser : function() {
        if (navigator["productSub"]) {
            bmak["psub"] = navigator["productSub"];
        }
        if (navigator["language"]) {
            bmak["lang"] = navigator["language"];
        }
        if (navigator["product"]) {
            bmak["prod"] = navigator["product"];
        }
        bmak["plen"] = void 0 !== navigator["plugins"] ? navigator["plugins"]["length"] : -1;
    },
    bc : function() {
        /** @type {number} */
        var a = window["addEventListener"] ? 1 : 0;
        /** @type {number} */
        var b = window["XMLHttpRequest"] ? 1 : 0;
        /** @type {number} */
        var c = window["XDomainRequest"] ? 1 : 0;
        /** @type {number} */
        var n = window["emit"] ? 1 : 0;
        /** @type {number} */
        var o = window["DeviceOrientationEvent"] ? 1 : 0;
        /** @type {number} */
        var m = window["DeviceMotionEvent"] ? 1 : 0;
        /** @type {number} */
        var r = window["TouchEvent"] ? 1 : 0;
        /** @type {number} */
        var i = window["spawn"] ? 1 : 0;
        /** @type {number} */
        var e = window["innerWidth"] ? 1 : 0;
        /** @type {number} */
        var t = window["outerWidth"] ? 1 : 0;
        /** @type {number} */
        var d = window["chrome"] ? 1 : 0;
        /** @type {number} */
        var k = Function["prototype"]["bind"] ? 1 : 0;
        /** @type {number} */
        var s = window["Buffer"] ? 1 : 0;
        /** @type {number} */
        var l = window["PointerEvent"] ? 1 : 0;
        /** @type {number} */
        bmak["xagg"] = a + (b << 1) + (c << 2) + (n << 3) + (o << 4) + (m << 5) + (r << 6) + (i << 7) + (e << 8) + (t << 9) + (d << 10) + (k << 11) + (s << 12) + (l << 13);
    },
    bmisc : function() {
        /** @type {number} */
        bmak["pen"] = window["_phantom"] ? 1 : 0;
        /** @type {number} */
        bmak["wen"] = window["webdriver"] ? 1 : 0;
        /** @type {number} */
        bmak["den"] = window["domAutomation"] ? 1 : 0;
    },
    bd : function() {
        /** @type {!Array} */
        var EnvJasmine = [];
        /** @type {number} */
        var DOMContentLoaded = window["callPhantom"] ? 1 : 0;
        EnvJasmine["push"](",cpen:" + DOMContentLoaded);
        try {
            /** @type {number} */
            var code = (new Function("return/*@cc_on!@*/!1"))() ? 1 : 0;
        } catch (a) {
            /** @type {number} */
            code = 0;
        }
        EnvJasmine["push"]("i1:" + code);
        /** @type {number} */
        var _V5 = "number" == typeof document["documentMode"] ? 1 : 0;
        EnvJasmine["push"]("dm:" + _V5);
        /** @type {number} */
        var PL$23 = window["chrome"] && window["chrome"]["webstore"] ? 1 : 0;
        EnvJasmine["push"]("cwen:" + PL$23);
        /** @type {number} */
        var PL$20 = navigator["onLine"] ? 1 : 0;
        EnvJasmine["push"]("non:" + PL$20);
        /** @type {number} */
        var PL$15 = window["opera"] ? 1 : 0;
        EnvJasmine["push"]("opc:" + PL$15);
        /** @type {number} */
        var status = "undefined" != typeof InstallTrigger ? 1 : 0;
        EnvJasmine["push"]("fc:" + status);
        /** @type {number} */
        var passed = window["HTMLElement"] && Object["prototype"]["toString"]["call"](window["HTMLElement"])["indexOf"]("Constructor") > 0 ? 1 : 0;
        EnvJasmine["push"]("sc:" + passed);
        /** @type {number} */
        var failed = "function" == typeof window["RTCPeerConnection"] || "function" == typeof window["mozRTCPeerConnection"] || "function" == typeof window["webkitRTCPeerConnection"] ? 1 : 0;
        EnvJasmine["push"]("wrc:" + failed);
        var d = "mozInnerScreenY" in window ? window["mozInnerScreenY"] : 0;
        EnvJasmine["push"]("isc:" + d);
        bmak["d2"] = bmak["pi"](bmak["z1"] / 23);
        /** @type {number} */
        var k = "function" == typeof navigator["vibrate"] ? 1 : 0;
        EnvJasmine["push"]("vib:" + k);
        /** @type {number} */
        var s = "function" == typeof navigator["getBattery"] ? 1 : 0;
        EnvJasmine["push"]("bat:" + s);
        /** @type {number} */
        var l = Array["prototype"]["forEach"] ? 0 : 1;
        EnvJasmine["push"]("x11:" + l);
        /** @type {number} */
        var u = "FileReader" in window ? 1 : 0;
        return EnvJasmine["push"]("x12:" + u), EnvJasmine["join"](",");
    },
    fas : function() {
        try {
            return Boolean(navigator["credentials"]) + (Boolean(navigator["appMinorVersion"]) << 1) + (Boolean(navigator["bluetooth"]) << 2) + (Boolean(navigator["storage"]) << 3) + (Boolean(Math["imul"]) << 4) + (Boolean(navigator["getGamepads"]) << 5) + (Boolean(navigator["getStorageUpdates"]) << 6) + (Boolean(navigator["hardwareConcurrency"]) << 7) + (Boolean(navigator["mediaDevices"]) << 8) + (Boolean(navigator["mozAlarms"]) << 9) + (Boolean(navigator["mozConnection"]) << 10) + (Boolean(navigator["mozIsLocallyAvailable"]) << 11) + (Boolean(navigator["mozPhoneNumberService"]) << 12) + (Boolean(navigator["msManipulationViewsEnabled"]) <<
                13) + (Boolean(navigator["permissions"]) << 14) + (Boolean(navigator["registerProtocolHandler"]) << 15) + (Boolean(navigator["requestMediaKeySystemAccess"]) << 16) + (Boolean(navigator["requestWakeLock"]) << 17) + (Boolean(navigator["sendBeacon"]) << 18) + (Boolean(navigator["serviceWorker"]) << 19) + (Boolean(navigator["storeWebWideTrackingException"]) << 20) + (Boolean(navigator["webkitGetGamepads"]) << 21) + (Boolean(navigator["webkitTemporaryStorage"]) << 22) + (Boolean(Number["parseInt"]) << 23) + (Boolean(Math["hypot"]) << 24);
        } catch (a) {
            return 0;
        }
    },
    getmr : function() {
        try {
            if ("undefined" == typeof performance || void 0 === performance["now"] || "undefined" == typeof JSON) {
                return void(bmak["mr"] = "undef");
            }
            var a = "";
            /** @type {number} */
            var t = 1E3;
            /** @type {!Array} */
            var PL$13 = [Math["abs"], Math["acos"], Math["asin"], Math["atanh"], Math["cbrt"], Math["exp"], Math["random"], Math["round"], Math["sqrt"], isFinite, isNaN, parseFloat, parseInt, JSON["parse"]];
            /** @type {number} */
            var PL$17 = 0;
            for (; PL$17 < PL$13["length"]; PL$17++) {
                /** @type {!Array} */
                var o = [];
                /** @type {number} */
                var yDiff = 0;
                var yMin = performance["now"]();
                /** @type {number} */
                var xDiff = 0;
                /** @type {number} */
                var up = 0;
                if (void 0 !== PL$13[PL$17]) {
                    /** @type {number} */
                    xDiff = 0;
                    for (; xDiff < t && yDiff < .6; xDiff++) {
                        var cornerRad = performance["now"]();
                        /** @type {number} */
                        var d = 0;
                        for (; d < 4E3; d++) {
                            PL$13[PL$17](3.14);
                        }
                        var yMax = performance["now"]();
                        o["push"](Math["round"](1E3 * (yMax - cornerRad)));
                        /** @type {number} */
                        yDiff = yMax - yMin;
                    }
                    var s = o["sort"]();
                    /** @type {number} */
                    up = s[Math["floor"](s["length"] / 2)] / 5;
                }
                a = a + up + ",";
            }
            bmak["mr"] = a;
        } catch (a) {
            bmak["mr"] = "exception";
        }
    },
    sed : function() {
        var a;
        a = window["$cdc_asdjflasutopfhvcZLmcfl_"] || document["$cdc_asdjflasutopfhvcZLmcfl_"] ? "1" : "0";
        var t;
        t = null != window["document"]["documentElement"]["getAttribute"]("webdriver") ? "1" : "0";
        var e;
        e = void 0 !== navigator["webdriver"] && navigator["webdriver"] ? "1" : "0";
        var n;
        n = void 0 !== window["webdriver"] ? "1" : "0";
        var o;
        o = void 0 !== window["XPathResult"] || void 0 !== document["XPathResult"] ? "1" : "0";
        var m;
        m = null != window["document"]["documentElement"]["getAttribute"]("driver") ? "1" : "0";
        var r;
        return r = null != window["document"]["documentElement"]["getAttribute"]("selenium") ? "1" : "0", [a, t, e, n, o, m, r]["join"](",");
    },
    cma : function(event, tempalte) {
        try {
            if (1 == tempalte && bmak["mme_cnt"] < bmak["mme_cnt_lmt"] || 1 != tempalte && bmak["mduce_cnt"] < bmak["mduce_cnt_lmt"]) {
                var e = event || window["event"];
                /** @type {number} */
                var tfm = -1;
                /** @type {number} */
                var i = -1;
                if (e && e["pageX"] && e["pageY"]) {
                    tfm = Math["floor"](e["pageX"]);
                    i = Math["floor"](e["pageY"]);
                } else {
                    if (e && e["clientX"] && e["clientY"]) {
                        tfm = Math["floor"](e["clientX"]);
                        i = Math["floor"](e["clientY"]);
                    }
                }
                var ofs = e["toElement"];
                if (null == ofs) {
                    ofs = e["target"];
                }
                var r = bmak["gf"](ofs);
                /** @type {number} */
                var jQId = bmak["get_cf_date"]() - bmak["start_ts"];
                var s = bmak["me_cnt"] + "," + tempalte + "," + jQId + "," + tfm + "," + i;
                if (1 != tempalte) {
                    s = s + "," + r;
                    var n = void 0 !== e["which"] ? e["which"] : e["button"];
                    if (null != n && 1 != n) {
                        s = s + "," + n;
                    }
                }
                if (void 0 !== e["isTrusted"] && false === e["isTrusted"]) {
                    s = s + ",it0";
                }
                s = s + ";";
                bmak["me_vel"] = bmak["me_vel"] + bmak["me_cnt"] + tempalte + jQId + tfm + i;
                bmak["mact"] = bmak["mact"] + s;
                bmak["ta"] += jQId;
            }
            if (1 == tempalte) {
                bmak["mme_cnt"]++;
            } else {
                bmak["mduce_cnt"]++;
            }
            bmak["me_cnt"]++;
            if (bmak["js_post"] && 3 == tempalte) {
                /** @type {number} */
                bmak["aj_type"] = 1;
                bmak["bpd"]();
                bmak["pd"](true);
                /** @type {number} */
                bmak["ce_js_post"] = 1;
            }
        } catch (a) {
        }
    },
    x2 : function() {
        var pad = bmak["ff"];
        var s = pad(98) + pad(109) + pad(97) + pad(107) + pad(46) + pad(103) + pad(101) + pad(116);
        return s = s + pad(95) + pad(99) + pad(102) + pad(95), s = "return " + s + pad(100) + pad(97) + pad(116) + pad(101) + pad(40) + pad(41), s = s + ";", (new Function(s))();
    },
    np : function() {
        /** @type {!Array} */
        var animationConfigs = [];
        /** @type {!Array} */
        var t = ["geolocation", "notifications", "push", "midi", "camera", "microphone", "speaker", "device-info", "background-sync", "bluetooth", "persistent-storage", "ambient-light-sensor", "accelerometer", "gyroscope", "magnetometer", "clipboard", "accessibility-events", "clipboard-read", "clipboard-write", "payment-handler"];
        try {
            if (!navigator["permissions"]) {
                return 6;
            }
            /**
             * @param {string} name
             * @param {?} event
             * @return {?}
             */
            var send = function(name, event) {
                return navigator["permissions"]["query"]({
                    name : name
                })["then"](function(canCreateDiscussions) {
                    switch(canCreateDiscussions["state"]) {
                        case "prompt":
                            /** @type {number} */
                            animationConfigs[event] = 1;
                            break;
                        case "granted":
                            /** @type {number} */
                            animationConfigs[event] = 2;
                            break;
                        case "denied":
                            /** @type {number} */
                            animationConfigs[event] = 0;
                            break;
                        default:
                            /** @type {number} */
                            animationConfigs[event] = 5;
                    }
                })["catch"](function(canCreateDiscussions) {
                    /** @type {number} */
                    animationConfigs[event] = -1 !== canCreateDiscussions["message"]["indexOf"]("is not a valid enum value of type PermissionName") ? 4 : 3;
                });
            };
            var promises = t["map"](function(pkg, prev) {
                return send(pkg, prev);
            });
            Promise["all"](promises)["then"](function() {
                bmak["nav_perm"] = animationConfigs["join"]("");
            });
        } catch (a) {
            return 7;
        }
    },
    cpa : function(p, a) {
        try {
            /** @type {boolean} */
            var e = false;
            if (1 == a && bmak["pme_cnt"] < bmak["pme_cnt_lmt"] || 1 != a && bmak["pduce_cnt"] < bmak["pduce_cnt_lmt"]) {
                var props = p || window["event"];
                if (props && "mouse" != props["pointerType"]) {
                    /** @type {boolean} */
                    e = true;
                    /** @type {number} */
                    var pad = -1;
                    /** @type {number} */
                    var px = -1;
                    if (props && props["pageX"] && props["pageY"]) {
                        pad = Math["floor"](props["pageX"]);
                        px = Math["floor"](props["pageY"]);
                    } else {
                        if (props && props["clientX"] && props["clientY"]) {
                            pad = Math["floor"](props["clientX"]);
                            px = Math["floor"](props["clientY"]);
                        }
                    }
                    /** @type {number} */
                    var r = bmak["get_cf_date"]() - bmak["start_ts"];
                    var toppx = bmak["pe_cnt"] + "," + a + "," + r + "," + pad + "," + px;
                    if (void 0 !== props["isTrusted"] && false === props["isTrusted"]) {
                        toppx = toppx + ",0";
                    }
                    bmak["pe_vel"] = bmak["pe_vel"] + bmak["pe_cnt"] + a + r + pad + px;
                    bmak["pact"] = bmak["pact"] + toppx + ";";
                    bmak["ta"] += r;
                    if (1 == a) {
                        bmak["pme_cnt"]++;
                    } else {
                        bmak["pduce_cnt"]++;
                    }
                }
            }
            if (1 == a) {
                bmak["pme_cnt"]++;
            } else {
                bmak["pduce_cnt"]++;
            }
            bmak["pe_cnt"]++;
            if (bmak["js_post"] && 3 == a && e) {
                /** @type {number} */
                bmak["aj_type"] = 2;
                bmak["bpd"]();
                bmak["pd"](true);
                /** @type {number} */
                bmak["ce_js_post"] = 1;
            }
        } catch (a) {
        }
    },
    ab : function(b) {
        if (null == b) {
            return -1;
        }
        try {
            /** @type {number} */
            var b = 0;
            /** @type {number} */
            var a = 0;
            for (; a < b["length"]; a++) {
                var d = b["charCodeAt"](a);
                if (d < 128) {
                    b = b + d;
                }
            }
            return b;
        } catch (a) {
            return -2;
        }
    },
    ff : function(date) {
        return String["fromCharCode"](date);
    },
    to : function() {
        /** @type {number} */
        var x = bmak["x2"]() % 1E7;
        /** @type {number} */
        bmak["d3"] = x;
        /** @type {number} */
        var fn = x;
        /** @type {number} */
        var e = 0;
        for (; e < 5; e++) {
            /** @type {number} */
            var n = bmak["pi"](x / Math["pow"](10, e)) % 10;
            /** @type {number} */
            var count = n + 1;
            var markerFactoryBody = "return a" + bmak["cc"](n) + count + ";";
            fn = (new Function("a", markerFactoryBody))(fn);
        }
        bmak["o9"] = fn;
    },
    gf : function(a) {
        var rv;
        if (rv = null == a ? document["activeElement"] : a, null == document["activeElement"]) {
            return -1;
        }
        var e = rv["getAttribute"]("name");
        if (null == e) {
            var n = rv["getAttribute"]("id");
            return null == n ? -1 : bmak["ab"](n);
        }
        return bmak["ab"](e);
    },
    cc : function(options) {
        /** @type {number} */
        var crop_growth = options % 4;
        if (2 == crop_growth) {
            /** @type {number} */
            crop_growth = 3;
        }
        /** @type {number} */
        var next_grow = 42 + crop_growth;
        return String["fromCharCode"](next_grow);
    },
    isIgn : function(a) {
        var el = document["activeElement"];
        if (null == document["activeElement"]) {
            return 0;
        }
        var val = el["getAttribute"]("type");
        return 1 == (null == val ? -1 : bmak["get_type"](val)) && bmak["fidcnt"] > 12 && -2 == a ? 1 : 0;
    },
    cka : function(event, number) {
        try {
            var e = event || window["event"];
            /** @type {number} */
            var n = -1;
            /** @type {number} */
            var s = 1;
            if (bmak["ke_cnt"] < bmak["ke_cnt_lmt"] && e) {
                n = e["keyCode"];
                var f = e["charCode"];
                /** @type {number} */
                var r = e["shiftKey"] ? 1 : 0;
                /** @type {number} */
                var g = e["ctrlKey"] ? 1 : 0;
                /** @type {number} */
                var b = e["metaKey"] ? 1 : 0;
                /** @type {number} */
                var alen = e["altKey"] ? 1 : 0;
                /** @type {number} */
                var j = 8 * r + 4 * g + 2 * b + alen;
                /** @type {number} */
                var m = bmak["get_cf_date"]() - bmak["start_ts"];
                var s = bmak["gf"](null);
                /** @type {number} */
                var l = 0;
                if (f && n) {
                    n = 0 != f && 0 != n && f != n ? -1 : 0 != n ? n : f;
                }
                if (0 == g && 0 == b && 0 == alen && n >= 32) {
                    /** @type {number} */
                    n = 3 == number && n >= 32 && n <= 126 ? -2 : n >= 33 && n <= 47 ? -3 : n >= 112 && n <= 123 ? -4 : -2;
                }
                if (s != bmak["prevfid"]) {
                    /** @type {number} */
                    bmak["fidcnt"] = 0;
                    bmak["prevfid"] = s;
                } else {
                    bmak["fidcnt"] = bmak["fidcnt"] + 1;
                }
                if (0 == bmak["isIgn"](n)) {
                    var value = bmak["ke_cnt"] + "," + number + "," + m + "," + n + "," + l + "," + j + "," + s;
                    if (void 0 !== e["isTrusted"] && false === e["isTrusted"]) {
                        value = value + ",0";
                    }
                    value = value + ";";
                    bmak["kact"] = bmak["kact"] + value;
                    bmak["ke_vel"] = bmak["ke_vel"] + bmak["ke_cnt"] + number + m + n + j + s;
                    bmak["ta"] += m;
                } else {
                    /** @type {number} */
                    s = 0;
                }
            }
            if (s && e) {
                bmak["ke_cnt"]++;
            }
            if (!(!bmak["js_post"] || 1 != number || 13 != n && 9 != n)) {
                /** @type {number} */
                bmak["aj_type"] = 3;
                bmak["bpd"]();
                bmak["pd"](true);
                /** @type {number} */
                bmak["ce_js_post"] = 1;
            }
        } catch (a) {
        }
    },
    cta : function(event, min) {
        try {
            if (1 == min && bmak["tme_cnt"] < bmak["tme_cnt_lmt"] || 1 != min && bmak["tduce_cnt"] < bmak["tduce_cnt_lmt"]) {
                var e = event || window["event"];
                /** @type {number} */
                var title = -1;
                /** @type {number} */
                var extension = -1;
                if (e && e["pageX"] && e["pageY"]) {
                    title = Math["floor"](e["pageX"]);
                    extension = Math["floor"](e["pageY"]);
                } else {
                    if (e && e["clientX"] && e["clientY"]) {
                        title = Math["floor"](e["clientX"]);
                        extension = Math["floor"](e["clientY"]);
                    }
                }
                /** @type {number} */
                var m = bmak["get_cf_date"]() - bmak["start_ts"];
                var srcUrl = bmak["te_cnt"] + "," + min + "," + m + "," + title + "," + extension;
                if (void 0 !== e["isTrusted"] && false === e["isTrusted"]) {
                    srcUrl = srcUrl + ",0";
                }
                bmak["tact"] = bmak["tact"] + srcUrl + ";";
                bmak["ta"] += m;
                bmak["te_vel"] = bmak["te_vel"] + bmak["te_cnt"] + min + m + title + extension;
                /** @type {number} */
                bmak["doa_throttle"] = 0;
                /** @type {number} */
                bmak["dma_throttle"] = 0;
            }
            if (1 == min) {
                bmak["tme_cnt"]++;
            } else {
                bmak["tduce_cnt"]++;
            }
            bmak["te_cnt"]++;
            if (bmak["js_post"] && 2 == min && bmak["aj_indx_tact"] < bmak["aj_lmt_tact"]) {
                /** @type {number} */
                bmak["aj_type"] = 5;
                bmak["bpd"]();
                bmak["pd"](true);
                /** @type {number} */
                bmak["ce_js_post"] = 1;
                bmak["aj_indx_tact"]++;
            }
        } catch (a) {
        }
    },
    getFloatVal : function(a) {
        try {
            if (-1 != bmak["chknull"](a) && !isNaN(a)) {
                /** @type {number} */
                var t = parseFloat(a);
                if (!isNaN(t)) {
                    return t["toFixed"](2);
                }
            }
        } catch (a) {
        }
        return -1;
    },
    cdoa : function(a) {
        try {
            if (bmak["doe_cnt"] < bmak["doe_cnt_lmt"] && bmak["doa_throttle"] < 2 && a) {
                /** @type {number} */
                var t = bmak["get_cf_date"]() - bmak["start_ts"];
                var e = bmak["getFloatVal"](a["alpha"]);
                var n = bmak["getFloatVal"](a["beta"]);
                var hexString = bmak["getFloatVal"](a["gamma"]);
                var s = bmak["doe_cnt"] + "," + t + "," + e + "," + n + "," + hexString;
                if (void 0 !== a["isTrusted"] && false === a["isTrusted"]) {
                    s = s + ",0";
                }
                bmak["doact"] = bmak["doact"] + s + ";";
                bmak["ta"] += t;
                bmak["doe_vel"] = bmak["doe_vel"] + bmak["doe_cnt"] + t;
                bmak["doe_cnt"]++;
            }
            if (bmak["js_post"] && bmak["doe_cnt"] > 1 && bmak["aj_indx_doact"] < bmak["aj_lmt_doact"]) {
                /** @type {number} */
                bmak["aj_type"] = 6;
                bmak["bpd"]();
                bmak["pd"](true);
                /** @type {number} */
                bmak["ce_js_post"] = 1;
                bmak["aj_indx_doact"]++;
            }
            bmak["doa_throttle"]++;
        } catch (a) {
        }
    },
    cdma : function(a) {
        try {
            if (bmak["dme_cnt"] < bmak["dme_cnt_lmt"] && bmak["dma_throttle"] < 2 && a) {
                /** @type {number} */
                var t = bmak["get_cf_date"]() - bmak["start_ts"];
                /** @type {number} */
                var e = -1;
                /** @type {number} */
                var n = -1;
                /** @type {number} */
                var o = -1;
                if (a["acceleration"]) {
                    e = bmak["getFloatVal"](a["acceleration"]["x"]);
                    n = bmak["getFloatVal"](a["acceleration"]["y"]);
                    o = bmak["getFloatVal"](a["acceleration"]["z"]);
                }
                /** @type {number} */
                var m = -1;
                /** @type {number} */
                var r = -1;
                /** @type {number} */
                var i = -1;
                if (a["accelerationIncludingGravity"]) {
                    m = bmak["getFloatVal"](a["accelerationIncludingGravity"]["x"]);
                    r = bmak["getFloatVal"](a["accelerationIncludingGravity"]["y"]);
                    i = bmak["getFloatVal"](a["accelerationIncludingGravity"]["z"]);
                }
                /** @type {number} */
                var c = -1;
                /** @type {number} */
                var b = -1;
                /** @type {number} */
                var gap_len = 1;
                if (a["rotationRate"]) {
                    c = bmak["getFloatVal"](a["rotationRate"]["alpha"]);
                    b = bmak["getFloatVal"](a["rotationRate"]["beta"]);
                    gap_len = bmak["getFloatVal"](a["rotationRate"]["gamma"]);
                }
                var len = bmak["dme_cnt"] + "," + t + "," + e + "," + n + "," + o + "," + m + "," + r + "," + i + "," + c + "," + b + "," + gap_len;
                if (void 0 !== a["isTrusted"] && false === a["isTrusted"]) {
                    len = len + ",0";
                }
                bmak["dmact"] = bmak["dmact"] + len + ";";
                bmak["ta"] += t;
                bmak["dme_vel"] = bmak["dme_vel"] + bmak["dme_cnt"] + t;
                bmak["dme_cnt"]++;
            }
            if (bmak["js_post"] && bmak["dme_cnt"] > 1 && bmak["aj_indx_dmact"] < bmak["aj_lmt_dmact"]) {
                /** @type {number} */
                bmak["aj_type"] = 7;
                bmak["bpd"]();
                bmak["pd"](true);
                /** @type {number} */
                bmak["ce_js_post"] = 1;
                bmak["aj_indx_dmact"]++;
            }
            bmak["dma_throttle"]++;
        } catch (a) {
        }
    },
    get_type : function(body) {
        return body = body["toLowerCase"](), "text" == body || "search" == body || "url" == body || "email" == body || "tel" == body || "number" == body ? 0 : "password" == body ? 1 : 2;
    },
    chknull : function(a) {
        return null == a ? -1 : a;
    },
    getforminfo : function() {
        var a = "";
        var t = "";
        var PL$13 = document["getElementsByTagName"]("input");
        /** @type {number} */
        var n = -1;
        /** @type {number} */
        var PL$17 = 0;
        for (; PL$17 < PL$13["length"]; PL$17++) {
            var matches = PL$13[PL$17];
            var r = bmak["ab"](matches["getAttribute"]("name"));
            var i = bmak["ab"](matches["getAttribute"]("id"));
            var c = matches["getAttribute"]("required");
            /** @type {number} */
            var b = null == c ? 0 : 1;
            var artistTrack = matches["getAttribute"]("type");
            var up = null == artistTrack ? -1 : bmak["get_type"](artistTrack);
            var s = matches["getAttribute"]("autocomplete");
            if (null == s) {
                /** @type {number} */
                n = -1;
            } else {
                s = s["toLowerCase"]();
                /** @type {number} */
                n = "off" == s ? 0 : "on" == s ? 1 : 2;
            }
            var lead = matches["defaultValue"];
            var type = matches["value"];
            /** @type {number} */
            var GearType = 0;
            /** @type {number} */
            var weight_col = 0;
            if (lead && 0 != lead["length"]) {
                /** @type {number} */
                weight_col = 1;
            }
            if (!(!type || 0 == type["length"] || weight_col && type == lead)) {
                /** @type {number} */
                GearType = 1;
            }
            if (2 != up) {
                a = a + up + "," + n + "," + GearType + "," + b + "," + i + "," + r + "," + weight_col + ";";
            }
            t = t + GearType + ";";
        }
        return null == bmak["ins"] && (bmak["ins"] = t), bmak["cns"] = t, a;
    },
    startdoadma : function() {
        if (0 == bmak["doadma_en"] && window["addEventListener"]) {
            window["addEventListener"]("deviceorientation", bmak["cdoa"], true);
            window["addEventListener"]("devicemotion", bmak["cdma"], true);
            /** @type {number} */
            bmak["doadma_en"] = 1;
        }
        /** @type {number} */
        bmak["doa_throttle"] = 0;
        /** @type {number} */
        bmak["dma_throttle"] = 0;
    },
    updatet : function() {
        return bmak["get_cf_date"]() - bmak["start_ts"];
    },
    htm : function(a) {
        bmak["cta"](a, 1);
    },
    hts : function(a) {
        bmak["cta"](a, 2);
    },
    hte : function(a) {
        bmak["cta"](a, 3);
    },
    htc : function(a) {
        bmak["cta"](a, 4);
    },
    hmm : function(i) {
        bmak["cma"](i, 1);
    },
    hc : function(httpCode) {
        bmak["cma"](httpCode, 2);
    },
    hmd : function(a) {
        bmak["cma"](a, 3);
    },
    hmu : function(a) {
        bmak["cma"](a, 4);
    },
    hpd : function(a) {
        bmak["cpa"](a, 3);
    },
    hpu : function(a) {
        bmak["cpa"](a, 4);
    },
    hkd : function(a) {
        bmak["cka"](a, 1);
    },
    hku : function(a) {
        bmak["cka"](a, 2);
    },
    hkp : function(a) {
        bmak["cka"](a, 3);
    },
    form_submit : function() {
        try {
            if (bmak["bpd"](), 0 == bmak["sdfn"]["length"]) {
                if (document["getElementById"]("bm-telemetry") && (document["getElementById"]("bm-telemetry")["value"] = bmak["sensor_data"]), void 0 !== document["getElementsByName"]("bm-telemetry")) {
                    var fftBinsOfFreq = document["getElementsByName"]("bm-telemetry");
                    /** @type {number} */
                    var i = 0;
                    for (; i < fftBinsOfFreq["length"]; i++) {
                        fftBinsOfFreq[i]["value"] = bmak["sensor_data"];
                    }
                }
            } else {
                /** @type {number} */
                i = 0;
                alert(bmak["sdfn"]["length"]);
                for (; i < bmak["sdfn"]["length"]; i++) {
                    if (document["getElementById"](bmak["sdfn"][i])) {
                        document["getElementById"](bmak["sdfn"][i])["value"] = bmak["sensor_data"];
                    }
                }
            }
        } catch (a) {
            bmak["sd_debug"](",s7:" + a + "," + bmak["sensor_data"]);
        }
    },
    get_telemetry : function() {
        return bmak["bpd"](), bmak["sensor_data"];
    },
    getdurl : function() {
        return bmak["enReadDocUrl"] ? document["URL"]["replace"](/\|"/g, "") : "";
    },
    x1 : function() {
        return Math["floor"](16777216 * (1 + Math["random"]()))["toString"](36);
    },
    gck : function() {
        var i = bmak["x1"]() + bmak["x1"]() + bmak["x1"]() + bmak["x1"]();
        return bmak["set_cookie"](bmak["ckie"], i + "_" + bmak["ab"](i)), i;
    },
    set_cookie : function(name, value) {
        if (void 0 !== document["cookie"]) {
            document["cookie"] = name + "=" + value + "; path=/; expires=Fri, 01 Feb 2025 08:00:00 GMT;";
        }
    },
    get_cookie : function() {
        var CookieFound = "0";
        try {
            CookieFound = bmak["cookie_chk_read"](bmak["ckie"]);
            if (!CookieFound) {
                /** @type {number} */
                bmak["n_ck"] = 1;
                CookieFound = bmak["bm"] ? "2" : "1";
            }
        } catch (a) {
        }
        return CookieFound;
    },
    cookie_chk_read : function(_tile) {
        if (document["cookie"]) {
            var data = _tile + "=";
            var PL$13 = document["cookie"]["split"]("; ");
            /** @type {number} */
            var PL$17 = 0;
            for (; PL$17 < PL$13["length"]; PL$17++) {
                var packByNumType = PL$13[PL$17];
                if (0 === packByNumType["indexOf"](data)) {
                    var c_user = packByNumType["substring"](data["length"], packByNumType["length"]);
                    if (-1 != c_user["indexOf"]("~") || -1 != decodeURIComponent(c_user)["indexOf"]("~")) {
                        return c_user;
                    }
                }
            }
        }
        return false;
    },
    bpd : function() {
        bmak["sd_debug"]("<bpd>");
        /** @type {number} */
        var $start = 0;
        try {
            $start = bmak["get_cf_date"]();
            var mma_frontpage_item_course_search = bmak["updatet"]();
            var _maskLayer = "3";
            if (bmak["ckie"]) {
                _maskLayer = bmak["get_cookie"]();
            }
            var n = bmak["gd"]();
            var moz = window["DeviceOrientationEvent"] ? "do_en" : "do_dis";
            var remainder = window["DeviceMotionEvent"] ? "dm_en" : "dm_dis";
            var size1 = window["TouchEvent"] ? "t_en" : "t_dis";
            var i = moz + "," + remainder + "," + size1;
            var c = bmak["getforminfo"]();
            var b = bmak["getdurl"]();
            var d = bmak["aj_type"] + "," + bmak["aj_indx"];
            if (!bmak["fpcf"]["fpValCalculated"] && (0 == bmak["js_post"] || bmak["aj_indx"] > 0)) {
                bmak["fpcf"]["fpVal"]();
            }
            var mma_frontpage_item_all_course_list = bmak["ke_vel"] + bmak["me_vel"] + bmak["doe_vel"] + bmak["dme_vel"] + bmak["te_vel"] + bmak["pe_vel"];
            /** @type {number} */
            var s = bmak["get_cf_date"]() - bmak["start_ts"];
            var l = bmak["pi"](bmak["d2"] / 6);
            var u = bmak["fas"]();
            /** @type {!Array} */
            var frontpageItems = [bmak["ke_vel"] + 1, bmak["me_vel"] + 32, bmak["te_vel"] + 32, bmak["doe_vel"], bmak["dme_vel"], bmak["pe_vel"], mma_frontpage_item_all_course_list, mma_frontpage_item_course_search, bmak["init_time"], bmak["start_ts"], bmak["fpcf"]["td"], bmak["d2"], bmak["ke_cnt"], bmak["me_cnt"], l, bmak["pe_cnt"], bmak["te_cnt"], s, bmak["ta"], bmak["n_ck"], _maskLayer, bmak["ab"](_maskLayer), bmak["fpcf"]["rVal"], bmak["fpcf"]["rCFP"], u];
            var f = frontpageItems["join"](",");
            var p = "" + bmak["ab"](bmak["fpcf"]["fpValstr"]);
            bmak["np"]();
            var v = bmak["sed"]();
            var org = bmak["mn_get_current_challenges"]();
            var trackedBy = "";
            var subwiki = "";
            var firstepisode = "";
            if (void 0 !== org[1]) {
                var i = org[1];
                if (void 0 !== bmak["mn_r"][i]) {
                    trackedBy = bmak["mn_r"][i];
                }
            }
            if (void 0 !== org[2]) {
                var i = org[2];
                if (void 0 !== bmak["mn_r"][i]) {
                    subwiki = bmak["mn_r"][i];
                }
            }
            if (void 0 !== org[3]) {
                var i = org[3];
                if (void 0 !== bmak["mn_r"][i]) {
                    firstepisode = bmak["mn_r"][i];
                }
            }
            // bmak["sensor_data"] = bmak["ver"] + "-1,2,-94,-100," + n + "-1,2,-94,-101," + i + "-1,2,-94,-105," + bmak["informinfo"] + "-1,2,-94,-102," + c + "-1,2,-94,-108," + bmak["kact"] + "-1,2,-94,-110," + bmak["mact"] + "-1,2,-94,-117," + bmak["tact"] + "-1,2,-94,-111," + bmak["doact"] + "-1,2,-94,-109," + bmak["dmact"] + "-1,2,-94,-114," + bmak["pact"] + "-1,2,-94,-103," + bmak["vcact"] + "-1,2,-94,-112," + b + "-1,2,-94,-115," + f + "-1,2,-94,-106," + d;
            // bmak["sensor_data"] = bmak["sensor_data"] + "-1,2,-94,-119," + bmak["mr"] + "-1,2,-94,-122," + v + "-1,2,-94,-123," + trackedBy + "-1,2,-94,-124," + subwiki + "-1,2,-94,-126," + firstepisode + "-1,2,-94,-127," + bmak["nav_perm"];
            /** @type {number} */
            bmak["sensor_data"] = ""
            var j = 24 ^ bmak["ab"](bmak["sensor_data"]);
            // bmak["sensor_data"] = bmak["sensor_data"] + "-1,2,-94,-70," + bmak["fpcf"]["fpValstr"] + "-1,2,-94,-80," + p + "-1,2,-94,-116," + bmak["o9"] + "-1,2,-94,-118," + j + "-1,2,-94,-121,";
            bmak["sensor_data"] = ""
            bmak["sd_debug"](",s1:" + bmak["sensor_data"]["slice"](0, 10));
        } catch (filter) {
            try {
                bmak["sd_debug"](",s2:" + filter);
                bmak["sensor_data"] = ""
                // bmak["sensor_data"] = bmak["ver"] + "-1,2,-94,-100," + bmak["uar"]() + "-1,2,-94,-120," + filter["replace"](/"/g, "\'");
            } catch (a) {
                bmak["sd_debug"](",s3:" + a);
            }
        }
        try {
            var m_key = bmak["od"](bmak["cs"], bmak["api_public_key"])["slice"](0, 16);
            var m_buffer = Math["floor"](bmak["get_cf_date"]() / 36E5);
            var A = bmak["get_cf_date"]();
            var $eol = m_key + bmak["od"](m_buffer, m_key) + bmak["sensor_data"];
            // bmak["sensor_data"] = $eol + ";" + (bmak["get_cf_date"]() - $start) + ";" + bmak["tst"] + ";" + (bmak["get_cf_date"]() - A);
            bmak["sensor_data"] = ""
        } catch (a) {
        }
        bmak["sd_debug"]("</bpd>");
    },
    od : function(c, n) {
        try {
            /** @type {string} */
            c = String(c);
            /** @type {string} */
            n = String(n);
            /** @type {!Array} */
            var bonusTraitModifiers = [];
            var nn = n["length"];
            if (nn > 0) {
                /** @type {number} */
                var i = 0;
                for (; i < c["length"]; i++) {
                    var result = c["charCodeAt"](i);
                    var person = c["charAt"](i);
                    var igts = n["charCodeAt"](i % nn);
                    result = bmak["rir"](result, 47, 57, igts);
                    if (result != c["charCodeAt"](i)) {
                        person = String["fromCharCode"](result);
                    }
                    bonusTraitModifiers["push"](person);
                }
                if (bonusTraitModifiers["length"] > 0) {
                    return bonusTraitModifiers["join"]("");
                }
            }
        } catch (a) {
        }
        return c;
    },
    rir : function(value, min, max, n) {
        return value > min && value <= max && (value = value + n % (max - min)) > max && (value = value - max + min), value;
    },
    lvc : function(a) {
        try {
            if (bmak["vc_cnt"] < bmak["vc_cnt_lmt"]) {
                /** @type {number} */
                var b = bmak["get_cf_date"]() - bmak["start_ts"];
                var e = a + "," + b + ";";
                bmak["vcact"] = bmak["vcact"] + e;
            }
            bmak["vc_cnt"]++;
        } catch (a) {
        }
    },
    hvc : function() {
        try {
            /** @type {number} */
            var artistTrack = 1;
            if (document[bmak["hn"]]) {
                /** @type {number} */
                artistTrack = 0;
            }
            bmak["lvc"](artistTrack);
        } catch (a) {
        }
    },
    hb : function(callback) {
        bmak["lvc"](2);
    },
    hf : function(type) {
        bmak["lvc"](3);
    },
    rve : function() {
        if (void 0 !== document["hidden"]) {
            bmak["hn"] = "hidden";
            bmak["vc"] = "visibilitychange";
        } else {
            if (void 0 !== document["mozHidden"]) {
                bmak["hn"] = "mozHidden";
                bmak["vc"] = "mozvisibilitychange";
            } else {
                if (void 0 !== document["msHidden"]) {
                    bmak["hn"] = "msHidden";
                    bmak["vc"] = "msvisibilitychange";
                } else {
                    if (void 0 !== document["webkitHidden"]) {
                        bmak["hn"] = "webkitHidden";
                        bmak["vc"] = "webkitvisibilitychange";
                    }
                }
            }
        }
        if (document["addEventListener"]) {
            if ("unk" != bmak["hn"]) {
                document["addEventListener"](bmak["vc"], bmak["hvc"], true);
            }
        } else {
            if (document["attachEvent"] && "unk" != bmak["hn"]) {
                document["attachEvent"](bmak["vc"], bmak["hvc"]);
            }
        }
        window["onblur"] = bmak["hb"];
        window["onfocus"] = bmak["hf"];
    },
    startTracking : function() {
        bmak["startdoadma"]();
        try {
            bmak["to"]();
        } catch (a) {
            /** @type {number} */
            bmak["o9"] = -654321;
        }
        setInterval(function() {
            bmak["startdoadma"]();
        }, 3E3);
        if (document["addEventListener"]) {
            document["addEventListener"]("touchmove", bmak["htm"], true);
            document["addEventListener"]("touchstart", bmak["hts"], true);
            document["addEventListener"]("touchend", bmak["hte"], true);
            document["addEventListener"]("touchcancel", bmak["htc"], true);
            document["addEventListener"]("mousemove", bmak["hmm"], true);
            document["addEventListener"]("click", bmak["hc"], true);
            document["addEventListener"]("mousedown", bmak["hmd"], true);
            document["addEventListener"]("mouseup", bmak["hmu"], true);
            document["addEventListener"]("pointerdown", bmak["hpd"], true);
            document["addEventListener"]("pointerup", bmak["hpu"], true);
            document["addEventListener"]("keydown", bmak["hkd"], true);
            document["addEventListener"]("keyup", bmak["hku"], true);
            document["addEventListener"]("keypress", bmak["hkp"], true);
        } else {
            if (document["attachEvent"]) {
                document["attachEvent"]("touchmove", bmak["htm"]);
                document["attachEvent"]("touchstart", bmak["hts"]);
                document["attachEvent"]("touchend", bmak["hte"]);
                document["attachEvent"]("touchcancel", bmak["htc"]);
                document["attachEvent"]("onmousemove", bmak["hmm"]);
                document["attachEvent"]("onclick", bmak["hc"]);
                document["attachEvent"]("onmousedown", bmak["hmd"]);
                document["attachEvent"]("onmouseup", bmak["hmu"]);
                document["attachEvent"]("onpointerdown", bmak["hpd"]);
                document["attachEvent"]("onpointerup", bmak["hpu"]);
                document["attachEvent"]("onkeydown", bmak["hkd"]);
                document["attachEvent"]("onkeyup", bmak["hku"]);
                document["attachEvent"]("onkeypress", bmak["hkp"]);
            }
        }
        bmak["rve"]();
        bmak["informinfo"] = bmak["getforminfo"]();
        if (bmak["js_post"]) {
            /** @type {number} */
            bmak["aj_type"] = 0;
            bmak["bpd"]();
            bmak["pd"](true);
        }
        /** @type {boolean} */
        bmak["firstLoad"] = false;
    },
    gb : function($el, val) {
        var d = $el["charCodeAt"](val);
        return d = d > 255 ? 0 : d;
    },
    encode : function(script) {
        if ("undefined" != typeof btoa) {
            return btoa(script);
        }
        var n;
        var e;
        var first;
        var bBody;
        var real_day;
        var aBody;
        var setValue;
        var c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var real_year = "";
        /** @type {number} */
        var oALen = 3 * Math["floor"](script["length"] / 3);
        /** @type {number} */
        var len = 0;
        for (; len < oALen; len = len + 3) {
            n = bmak["gb"](script, len);
            e = bmak["gb"](script, len + 1);
            first = bmak["gb"](script, len + 2);
            /** @type {number} */
            bBody = n >> 2;
            /** @type {number} */
            real_day = ((3 & n) << 4) + (e >> 4);
            /** @type {number} */
            aBody = ((15 & e) << 2) + (first >> 6);
            /** @type {number} */
            setValue = 63 & first;
            real_year = real_year + c["charAt"](bBody) + c["charAt"](real_day) + c["charAt"](aBody) + c["charAt"](setValue);
        }
        return script["length"] % 3 == 1 && (n = bmak["gb"](script, len), bBody = n >> 2, real_day = (3 & n) << 4, real_year = real_year + c["charAt"](bBody) + c["charAt"](real_day) + "=="), script["length"] % 3 == 2 && (n = bmak["gb"](script, len), e = bmak["gb"](script, len + 1), bBody = n >> 2, real_day = ((3 & n) << 4) + (e >> 4), aBody = (15 & e) << 2, real_year = real_year + c["charAt"](bBody) + c["charAt"](real_day) + c["charAt"](aBody) + "="), real_year;
    },
    ie9OrLower : function() {
        try {
            if ("string" == typeof navigator["appVersion"] && -1 != navigator["appVersion"]["indexOf"]("MSIE")) {
                if (parseFloat(navigator["appVersion"]["split"]("MSIE")[1]) <= 9) {
                    return true;
                }
            }
        } catch (a) {
        }
        return false;
    },
    parse_gp : function(a) {
    },
    call_gp : function() {
        var xhr;
        if (void 0 !== window["XMLHttpRequest"]) {
            /** @type {!XMLHttpRequest} */
            xhr = new XMLHttpRequest;
        } else {
            if (void 0 !== window["XDomainRequest"]) {
                /** @type {!XDomainRequest} */
                xhr = new XDomainRequest;
                /**
                 * @return {undefined}
                 */
                xhr["onload"] = function() {
                    /** @type {number} */
                    this["readyState"] = 4;
                    if (this["onreadystatechange"] instanceof Function) {
                        this["onreadystatechange"]();
                    }
                };
            } else {
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }
        }
        xhr["open"]("GET", bmak["params_url"], true);
        /**
         * @return {undefined}
         */
        xhr["onreadystatechange"] = function() {
            if (xhr["readyState"] > 3 && bmak["parse_gp"]) {
                bmak["parse_gp"](xhr);
            }
        };
        xhr["send"]();
    },
    apicall : function(value, expectedCos) {
        var query;
        query = window["XDomainRequest"] ? new XDomainRequest : window["XMLHttpRequest"] ? new XMLHttpRequest : new ActiveXObject("Microsoft.XMLHTTP");
        query["open"]("POST", value, expectedCos);
        var id = bmak["encode"](bmak["api_public_key"] + ":");
        bmak["auth"] = ",",auth,  ":",  "" + id + "";
        if (query["setRequestHeader"]) {
            query["setRequestHeader"]("Content-type", "application/json");
            query["setRequestHeader"]("Authorization", "Basic " + id);
            bmak["auth"] = "";
        }
        var fakeContinuationToken = {"session_id" : "" + bmak["session_id"] + "",sensor_data: "" + bmak["sensor_data"] + "" + bmak["auth"] + ""};
        query["send"](fakeContinuationToken);
    },
    apicall_bm : function(url, c, t) {
        var xhr;
        if (void 0 !== window["XMLHttpRequest"]) {
            /** @type {!XMLHttpRequest} */
            xhr = new XMLHttpRequest;
        } else {
            if (void 0 !== window["XDomainRequest"]) {
                /** @type {!XDomainRequest} */
                xhr = new XDomainRequest;
                /**
                 * @return {undefined}
                 */
                xhr["onload"] = function() {
                    /** @type {number} */
                    this["readyState"] = 4;
                    if (this["onreadystatechange"] instanceof Function) {
                        this["onreadystatechange"]();
                    }
                };
            } else {
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }
        }
        xhr["open"]("POST", url, c);
        if (void 0 !== xhr["withCredentials"]) {
            /** @type {boolean} */
            xhr["withCredentials"] = true;
        }

        var mime = {sensor_data:"" + bmak["sensor_data"] + ""};
        /**
         * @return {undefined}
         */
        xhr["onreadystatechange"] = function() {
            if (xhr["readyState"] > 3 && t) {
                t(xhr);
            }
        };
        xhr["send"](mime);
    },
    pd : function(name) {
        if (bmak["check_stop_protocol"]()) {
            bmak["apicall_bm"](bmak["cf_url"], name, bmak["patp"]);
            bmak["aj_indx"] = bmak["aj_indx"] + 1;
        }
    },
    check_stop_protocol : function() {
        var tiledImageTLs = bmak["get_stop_signals"]();
        var tiledImageBR = tiledImageTLs[0];
        if (!bmak["rst"] && tiledImageBR > -1) {
            bmak["ir"]();
            /** @type {boolean} */
            bmak["rst"] = true;
        }
        var tiledImageTL = tiledImageTLs[1];
        return -1 == tiledImageTL || bmak["aj_ss"] < tiledImageTL;
    },
    get_stop_signals : function() {
        /** @type {!Array} */
        var ref = [-1, -1];
        var c_user = bmak["cookie_chk_read"](bmak["ckie"]);
        if (false !== c_user) {
            try {
                var e = decodeURIComponent(c_user)["split"]("~");
                if (e["length"] >= 4) {
                    var level = bmak["pi"](e[1]);
                    var repeat = bmak["pi"](e[3]);
                    level = isNaN(level) ? -1 : level;
                    repeat = isNaN(repeat) ? -1 : repeat;
                    /** @type {!Array} */
                    ref = [repeat, level];
                }
            } catch (a) {
            }
        }
        return ref;
    },
    patp : function(a) {
        bmak["aj_ss"]++;
        /** @type {boolean} */
        bmak["rst"] = false;
    },
    get_mn_params_from_abck : function() {
        /** @type {!Array} */
        var a = [[]];
        try {
            var c_user = bmak["cookie_chk_read"](bmak["ckie"]);
            if (false !== c_user) {
                var tiledImageTLs = decodeURIComponent(c_user)["split"]("~");
                if (tiledImageTLs["length"] >= 5) {
                    var start = tiledImageTLs[0];
                    var tiledImageTL = tiledImageTLs[4];
                    var options = tiledImageTL["split"]("||");
                    if (options["length"] > 0) {
                        /** @type {number} */
                        var i = 0;
                        for (; i < options["length"]; i++) {
                            var filterOption = options[i];
                            var pipedCommands = filterOption["split"]("-");
                            if (pipedCommands["length"] >= 5) {
                                var k = bmak["pi"](pipedCommands[0]);
                                var cmd = pipedCommands[1];
                                var C = bmak["pi"](pipedCommands[2]);
                                var s = bmak["pi"](pipedCommands[3]);
                                var l = bmak["pi"](pipedCommands[4]);
                                /** @type {number} */
                                var u = 1;
                                if (pipedCommands["length"] >= 6) {
                                    u = bmak["pi"](pipedCommands[5]);
                                }
                                /** @type {!Array} */
                                var argument = [k, start, cmd, C, s, l, u];
                                if (2 == u) {
                                    a["splice"](0, 0, argument);
                                } else {
                                    a["push"](argument);
                                }
                            }
                        }
                    }
                }
            }
        } catch (a) {
        }
        return a;
    },
    mn_get_current_challenges : function() {
        var a = bmak["get_mn_params_from_abck"]();
        /** @type {!Array} */
        var in_data = [];
        if (null != a) {
            /** @type {number} */
            var key = 0;
            for (; key < a["length"]; key++) {
                var line = a[key];
                if (line["length"] > 0) {
                    var datas_temp = line[1] + line[2];
                    var field = line[6];
                    in_data[field] = datas_temp;
                }
            }
        }
        return in_data;
    },
    mn_update_challenge_details : function(a) {
        bmak["mn_sen"] = a[0];
        bmak["mn_abck"] = a[1];
        bmak["mn_psn"] = a[2];
        bmak["mn_cd"] = a[3];
        bmak["mn_tout"] = a[4];
        bmak["mn_stout"] = a[5];
        bmak["mn_ct"] = a[6];
        bmak["mn_ts"] = bmak["start_ts"];
        bmak["mn_cc"] = bmak["mn_abck"] + bmak["start_ts"] + bmak["mn_psn"];
    },
    mn_get_new_challenge_params : function(a) {
        /** @type {null} */
        var predicate = null;
        /** @type {null} */
        var sortKey = null;
        /** @type {null} */
        var j = null;
        if (null != a) {
            /** @type {number} */
            var key = 0;
            for (; key < a["length"]; key++) {
                var m = a[key];
                if (m["length"] > 0) {
                    var username = m[0];
                    var undefined = bmak["mn_abck"] + bmak["start_ts"] + m[2];
                    var reqVal = m[3];
                    var nodeBoxType = m[6];
                    /** @type {number} */
                    var reqVar = 0;
                    for (; reqVar < bmak["mn_lcl"] && (1 == username && bmak["mn_lc"][reqVar] != undefined && bmak["mn_ld"][reqVar] != reqVal); reqVar++) {
                    }
                    if (reqVar == bmak["mn_lcl"]) {
                        /** @type {number} */
                        predicate = key;
                        if (2 == nodeBoxType) {
                            /** @type {number} */
                            sortKey = key;
                        }
                        if (3 == nodeBoxType) {
                            /** @type {number} */
                            j = key;
                        }
                    }
                }
            }
        }
        return null != j && bmak["pstate"] ? a[j] : null == sortKey || bmak["pstate"] ? null == predicate || bmak["pstate"] ? null : a[predicate] : a[sortKey];
    },
    mn_poll : function() {
        if (0 == bmak["mn_state"]) {
            var button2 = bmak["get_mn_params_from_abck"]();
            var button2Component = bmak["mn_get_new_challenge_params"](button2);
            if (null != button2Component) {
                bmak["mn_update_challenge_details"](button2Component);
                if (bmak["mn_sen"]) {
                    /** @type {number} */
                    bmak["mn_state"] = 1;
                    /** @type {number} */
                    bmak["mn_mc_indx"] = 0;
                    /** @type {!Array} */
                    bmak["mn_al"] = [];
                    /** @type {!Array} */
                    bmak["mn_il"] = [];
                    /** @type {!Array} */
                    bmak["mn_tcl"] = [];
                    /** @type {!Array} */
                    bmak["mn_lg"] = [];
                    setTimeout(bmak["mn_w"], bmak["mn_tout"]);
                }
            }
        }
    },
    mn_init : function() {
        if (bmak["pstate"]) {
            setInterval(bmak["mn_poll"], 500);
        } else {
            setInterval(bmak["mn_poll"], 1E3);
        }
    },
    rotate_left : function(n, s) {
        return n << s | n >>> 32 - s;
    },
    encode_utf8 : function(s) {
        return unescape(encodeURIComponent(s));
    },
    mn_h : function(uly) {
        /** @type {number} */
        var H2 = 1732584193;
        /** @type {number} */
        var f = 4023233417;
        /** @type {number} */
        var offset = 2562383102;
        /** @type {number} */
        var s = 271733878;
        /** @type {number} */
        var state = 3285377520;
        var y = bmak["encode_utf8"](uly);
        /** @type {number} */
        var label = 8 * y["length"];
        y = y + String["fromCharCode"](128);
        /** @type {number} */
        var delta = y["length"] / 4 + 2;
        var len = Math["ceil"](delta / 16);
        /** @type {!Array} */
        var ret = new Array(len);
        /** @type {number} */
        var n = 0;
        for (; n < len; n++) {
            /** @type {!Array} */
            ret[n] = new Array(16);
            /** @type {number} */
            var i = 0;
            for (; i < 16; i++) {
                /** @type {number} */
                ret[n][i] = y["charCodeAt"](64 * n + 4 * i) << 24 | y["charCodeAt"](64 * n + 4 * i + 1) << 16 | y["charCodeAt"](64 * n + 4 * i + 2) << 8 | y["charCodeAt"](64 * n + 4 * i + 3) << 0;
            }
        }
        /** @type {number} */
        var value = label / Math["pow"](2, 32);
        ret[len - 1][14] = Math["floor"](value);
        /** @type {number} */
        ret[len - 1][15] = 4294967295 & label;
        /** @type {number} */
        var p = 0;
        for (; p < len; p++) {
            var runsgroup_by;
            var E;
            var d;
            /** @type {!Array} */
            var W = new Array(80);
            var c = H2;
            var g = f;
            var j = offset;
            var i = s;
            var key = state;
            /** @type {number} */
            n = 0;
            for (; n < 80; n++) {
                W[n] = n < 16 ? ret[p][n] : bmak["rotate_left"](W[n - 3] ^ W[n - 8] ^ W[n - 14] ^ W[n - 16], 1);
                if (n < 20) {
                    /** @type {number} */
                    runsgroup_by = g & j | ~g & i;
                    /** @type {number} */
                    E = 1518500249;
                } else {
                    if (n < 40) {
                        /** @type {number} */
                        runsgroup_by = g ^ j ^ i;
                        /** @type {number} */
                        E = 1859775393;
                    } else {
                        if (n < 60) {
                            /** @type {number} */
                            runsgroup_by = g & j | g & i | j & i;
                            /** @type {number} */
                            E = 2400959708;
                        } else {
                            /** @type {number} */
                            runsgroup_by = g ^ j ^ i;
                            /** @type {number} */
                            E = 3395469782;
                        }
                    }
                }
                d = bmak["rotate_left"](c, 5) + runsgroup_by + key + E + W[n];
                key = i;
                i = j;
                j = bmak["rotate_left"](g, 30);
                g = c;
                c = d;
            }
            H2 = H2 + c;
            f = f + g;
            offset = offset + j;
            s = s + i;
            state = state + key;
        }
        return [H2 >> 24 & 255, H2 >> 16 & 255, H2 >> 8 & 255, 255 & H2, f >> 24 & 255, f >> 16 & 255, f >> 8 & 255, 255 & f, offset >> 24 & 255, offset >> 16 & 255, offset >> 8 & 255, 255 & offset, s >> 24 & 255, s >> 16 & 255, s >> 8 & 255, 255 & s, state >> 24 & 255, state >> 16 & 255, state >> 8 & 255, 255 & state];
    },
    bdm : function(arr, max) {
        /** @type {number} */
        var ret = 0;
        /** @type {number} */
        var n = 0;
        for (; n < arr["length"]; ++n) {
            /** @type {number} */
            ret = (ret << 8 | arr[n]) >>> 0;
            /** @type {number} */
            ret = ret % max;
        }
        return ret;
    },
    mn_w : function() {
        try {
            /** @type {number} */
            var a = 0;
            /** @type {number} */
            var currentColumn = 0;
            /** @type {number} */
            var resumeTimeout = 0;
            var end = "";
            var imgW = bmak["get_cf_date"]();
            var artistTrack = bmak["mn_cd"] + bmak["mn_mc_indx"];
            for (; 0 == a;) {
                end = Math["random"]()["toString"](16);
                var r = bmak["mn_cc"] + artistTrack["toString"]() + end;
                var specificResourceHandler = bmak["mn_h"](r);
                if (0 == bmak["bdm"](specificResourceHandler, artistTrack)) {
                    /** @type {number} */
                    a = 1;
                    /** @type {number} */
                    resumeTimeout = bmak["get_cf_date"]() - imgW;
                    bmak["mn_al"]["push"](end);
                    bmak["mn_tcl"]["push"](resumeTimeout);
                    bmak["mn_il"]["push"](currentColumn);
                    if (0 == bmak["mn_mc_indx"]) {
                        bmak["mn_lg"]["push"](bmak["mn_abck"]);
                        bmak["mn_lg"]["push"](bmak["mn_ts"]);
                        bmak["mn_lg"]["push"](bmak["mn_psn"]);
                        bmak["mn_lg"]["push"](bmak["mn_cc"]);
                        bmak["mn_lg"]["push"](bmak["mn_cd"]["toString"]());
                        bmak["mn_lg"]["push"](artistTrack["toString"]());
                        bmak["mn_lg"]["push"](end);
                        bmak["mn_lg"]["push"](r);
                        bmak["mn_lg"]["push"](specificResourceHandler);
                    }
                } else {
                    if ((currentColumn = currentColumn + 1) % 1E3 == 0 && (resumeTimeout = bmak["get_cf_date"]() - imgW) > bmak["mn_stout"]) {
                        return void setTimeout(bmak["mn_w"], 1E3 + bmak["mn_stout"]);
                    }
                }
            }
            bmak["mn_mc_indx"] += 1;
            if (bmak["mn_mc_indx"] < bmak["mn_mc_lmt"]) {
                setTimeout(bmak["mn_w"], bmak["mn_tout"] + resumeTimeout);
            } else {
                /** @type {number} */
                bmak["mn_mc_indx"] = 0;
                bmak["mn_lc"][bmak["mn_lcl"]] = bmak["mn_cc"];
                bmak["mn_ld"][bmak["mn_lcl"]] = bmak["mn_cd"];
                bmak["mn_lcl"] = bmak["mn_lcl"] + 1;
                /** @type {number} */
                bmak["mn_state"] = 0;
                bmak["mn_r"][bmak["mn_abck"] + bmak["mn_psn"]] = bmak["mn_pr"]();
                if (bmak["js_post"]) {
                    /** @type {number} */
                    bmak["aj_type"] = 8;
                    bmak["bpd"]();
                    bmak["pd"](true);
                }
            }
        } catch (a) {
            bmak["sd_debug"](",mn_w:" + a);
        }
    },
    mn_pr : function() {
        return bmak["mn_al"]["join"](",") + ";" + bmak["mn_tcl"]["join"](",") + ";" + bmak["mn_il"]["join"](",") + ";" + bmak["mn_lg"]["join"](",") + ";";
    },
    calc_fp : function() {
        bmak["fpcf"]["fpVal"]();
        if (bmak["js_post"]) {
            /** @type {number} */
            bmak["aj_type"] = 9;
            bmak["bpd"]();
            bmak["pd"](true);
        }
    },
    listFunctions : {
        _setJsPost : function(a) {
            bmak["js_post"] = a;
            if (bmak["js_post"]) {
                /** @type {number} */
                bmak["enReadDocUrl"] = 1;
            }
        },
        _setSessionId : function(value) {
            bmak["session_id"] = value;
        },
        _setJavaScriptKey : function(a) {
            bmak["api_public_key"] = a;
        },
        _setEnAddHidden : function(a) {
            bmak["enAddHidden"] = a;
        },
        _setInitTime : function(a) {
            bmak["init_time"] = a;
        },
        _setApiUrl : function(a) {
            bmak["cf_url"] = a;
        },
        _setEnGetLoc : function(a) {
            bmak["enGetLoc"] = a;
        },
        _setEnReadDocUrl : function(a) {
            bmak["enReadDocUrl"] = a;
        },
        _setDisFpCalOnTimeout : function(a) {
            bmak["disFpCalOnTimeout"] = a;
        },
        _setCookie : function(value) {
            bmak["ckie"] = value;
        },
        _setCS : function(slackName) {
            bmak["cs"] = (String(slackName) + bmak["cs"])["slice"](0, 16);
        },
        _setFsp : function(a) {
            bmak["fsp"] = a;
            if (bmak["fsp"]) {
                bmak["cf_url"] = bmak["cf_url"]["replace"](/^http:\/\//i, "https://");
            }
        },
        _setBm : function(a) {
            bmak["bm"] = a;
            if (bmak["bm"]) {
                bmak["cf_url"] = (bmak["fsp"] ? "https:" : document["location"]["protocol"]) + "//" + document["location"]["hostname"] + "/_bm/_data";
                /** @type {boolean} */
                bmak["js_post"] = true;
            } else {
                bmak["params_url"] = (bmak["fsp"] ? "https:" : document["location"]["protocol"]) + "//" + document["location"]["hostname"] + "/get_params";
            }
        },
        _setAu : function(a) {
            if ("string" == typeof a) {
                if (0 === a["lastIndexOf"]("/", 0)) {
                    bmak["cf_url"] = (bmak["fsp"] ? "https:" : document["location"]["protocol"]) + "//" + document["location"]["hostname"] + a;
                } else {
                    bmak["cf_url"] = a;
                }
            }
        },
        _setSDFieldNames : function() {
            try {
                var x;
                /** @type {number} */
                x = 0;
                for (; x < arguments["length"]; x = x + 1) {
                    bmak["sdfn"]["push"](arguments[x]);
                }
            } catch (a) {
                bmak["sd_debug"](",setSDFN:" + a);
            }
        },
        _setUseAltFonts : function(a) {
            bmak["altFonts"] = a;
        },
        _setPowState : function(a) {
            bmak["pstate"] = a;
        },
        _setPow : function(a) {
            bmak["pstate"] = a;
        }
    },
    applyFunc : function() {
        var x;
        var indexLookupKey;
        var batch;
        /** @type {number} */
        x = 0;
        for (; x < arguments["length"]; x = x + 1) {
            batch = arguments[x];
        }
        indexLookupKey = batch["shift"]();
        if (bmak["listFunctions"][indexLookupKey]) {
            bmak["listFunctions"][indexLookupKey]["apply"](bmak["listFunctions"], batch);
        }
    }
};
if (function(context) {
    var arr = {};
    context["fpcf"] = arr;
    /**
     * @return {?}
     */
    arr["sf4"] = function() {
        var a = bmak["uar"]();
        return !(!~a["indexOf"]("Version/4.0") || !(~a["indexOf"]("iPad;") || ~a["indexOf"]("iPhone") || ~a["indexOf"]("Mac OS X 10_5")));
    };
    arr["fpValstr"] = "-1";
    /** @type {boolean} */
    arr["fpValCalculated"] = false;
    arr["rVal"] = "-1";
    arr["rCFP"] = "-1";
    arr["cache"] = {};
    /** @type {number} */
    arr["td"] = -999999;
    /**
     * @return {undefined}
     */
    arr["clearCache"] = function() {
        arr["cache"] = {};
    };
    /**
     * @return {undefined}
     */
    arr["fpVal"] = function() {
        /** @type {boolean} */
        arr["fpValCalculated"] = true;
        try {
            /** @type {number} */
            var b = 0;
            b = Date["now"] ? Date["now"]() : +new Date;
            var filter = arr["data"]();
            arr["fpValstr"] = filter["replace"](/"/g, "\\");
            /** @type {number} */
            var a = 0;
            a = Date["now"] ? Date["now"]() : +new Date;
            /** @type {number} */
            arr["td"] = a - b;
        } catch (a) {
        }
    };
    /**
     * @return {?}
     */
    arr["timezoneOffsetKey"] = function() {
        return (new Date)["getTimezoneOffset"]();
    };
    /**
     * @return {?}
     */
    arr["data"] = function() {
        var a = screen["colorDepth"] ? screen["colorDepth"] : -1;
        var e = screen["pixelDepth"] ? screen["pixelDepth"] : -1;
        var n = navigator["cookieEnabled"] ? navigator["cookieEnabled"] : -1;
        var o = navigator["javaEnabled"] ? navigator["javaEnabled"]() : -1;
        var m = navigator["doNotTrack"] ? navigator["doNotTrack"] : -1;
        var r = "default";
        return r = bmak["runFonts"] ? bmak["altFonts"] ? arr["fonts_optm"]() : arr["fonts"]() : "dis", [arr["canvas"]("<@nv45. F1n63r,Pr1n71n6!"), arr["canvas"]("m,Ev!xV67BaU> eh2m<f3AG3@"), r, arr["pluginInfo"](), arr["sessionStorageKey"](), arr["localStorageKey"](), arr["indexedDbKey"](), arr["timezoneOffsetKey"](), arr["webrtcKey"](), a, e, n, o, m]["join"](";");
    };
    /** @type {!Array} */
    arr["PLUGINS"] = ["WebEx64 General Plugin Container", "YouTube Plug-in", "Java Applet Plug-in", "Shockwave Flash", "iPhotoPhotocast", "SharePoint Browser Plug-in", "Chrome Remote Desktop Viewer", "Chrome PDF Viewer", "Native Client", "Unity Player", "WebKit-integrierte PDF", "QuickTime Plug-in", "RealPlayer Version Plugin", "RealPlayer(tm) G2 LiveConnect-Enabled Plug-In (32-bit)", "Mozilla Default Plug-in", "Adobe Acrobat", "AdobeAAMDetect", "Google Earth Plug-in", "Java Plug-in 2 for NPAPI Browsers", "Widevine Content Decryption Module", "Microsoft Office Live Plug-in", "Windows Media Player Plug-in Dynamic Link Library", "Google Talk Plugin Video Renderer", "Edge PDF Viewer", "Shockwave for Director", "Default Browser Helper", "Silverlight Plug-In"];
    /**
     * @return {?}
     */
    arr["pluginInfo"] = function() {
        if (void 0 === navigator["plugins"]) {
            return null;
        }
        var extendedCount = arr["PLUGINS"]["length"];
        var valList = "";
        /** @type {number} */
        var i = 0;
        for (; i < extendedCount; i++) {
            var k1_key = arr["PLUGINS"][i];
            if (void 0 !== navigator["plugins"][k1_key]) {
                valList = valList + "," + i;
            }
        }
        return valList;
    };
    /**
     * @param {?} data
     * @return {?}
     */
    arr["canvas"] = function(data) {
        try {
            if (void 0 !== arr["cache"]["canvas"]) {
                return arr["cache"]["canvas"];
            }
            /** @type {number} */
            var h = -1;
            if (!arr["sf4"]()) {
                var n = document["createElement"]("canvas");
                if (n["width"] = 280, n["height"] = 60, n["style"]["display"] = "none", "function" == typeof n["getContext"]) {
                    var command_codes = n["getContext"]("2d");
                    command_codes["fillStyle"] = "rgb(102, 204, 0)";
                    command_codes["fillRect"](100, 5, 80, 50);
                    command_codes["fillStyle"] = "#f60";
                    command_codes["font"] = "16pt Arial";
                    command_codes["fillText"](data, 10, 40);
                    command_codes["strokeStyle"] = "rgb(120, 186, 176)";
                    command_codes["arc"](80, 10, 20, 0, Math["PI"], false);
                    command_codes["stroke"]();
                    var PL$42 = n["toDataURL"]();
                    /** @type {number} */
                    h = 0;
                    /** @type {number} */
                    var PL$41 = 0;
                    for (; PL$41 < PL$42["length"]; PL$41++) {
                        h = (h << 5) - h + PL$42["charCodeAt"](PL$41);
                        /** @type {number} */
                        h = h & h;
                    }
                    h = h["toString"]();
                    var high = document["createElement"]("canvas");
                    /** @type {number} */
                    high["width"] = 16;
                    /** @type {number} */
                    high["height"] = 16;
                    var umecob = high["getContext"]("2d");
                    umecob["font"] = "6pt Arial";
                    arr["rVal"] = Math["floor"](1E3 * Math["random"]())["toString"]();
                    umecob["fillText"](arr["rVal"], 1, 12);
                    var PL$120 = high["toDataURL"]();
                    /** @type {number} */
                    var hash = 0;
                    /** @type {number} */
                    var PL$24 = 0;
                    for (; PL$24 < PL$120["length"]; PL$24++) {
                        hash = (hash << 5) - hash + PL$120["charCodeAt"](PL$24);
                        /** @type {number} */
                        hash = hash & hash;
                    }
                    arr["rCFP"] = hash["toString"]();
                }
            }
            return h;
        } catch (a) {
            return "exception";
        }
    };
    /**
     * @return {?}
     */
    arr["fonts_optm"] = function() {
        /** @type {number} */
        var maxvalue = 200;
        var dec_step = bmak["get_cf_date"]();
        /** @type {!Array} */
        var n = [];
        if (!arr["sf4"]()) {
            /** @type {!Array} */
            var sharePlaylist = ["sans-serif", "monospace"];
            /** @type {!Array} */
            var item = [0, 0];
            /** @type {!Array} */
            var newJoinDoc = [0, 0];
            var store = document["createElement"]("div");
            store["style"]["cssText"] = "position: relative; left: -9999px; visibility: hidden; display: block !important";
            var _id;
            /** @type {number} */
            _id = 0;
            for (; _id < sharePlaylist["length"]; _id++) {
                var id = document["createElement"]("span");
                id["innerHTML"] = "abcdefhijklmnopqrstuvxyz1234567890;+-.";
                id["style"]["fontSize"] = "90px";
                id["style"]["fontFamily"] = sharePlaylist[_id];
                store["appendChild"](id);
            }
            document["body"]["appendChild"](store);
            /** @type {number} */
            _id = 0;
            for (; _id < store["childNodes"]["length"]; _id++) {
                id = store["childNodes"][_id];
                item[_id] = id["offsetWidth"];
                newJoinDoc[_id] = id["offsetHeight"];
            }
            if (document["body"]["removeChild"](store), bmak["get_cf_date"]() - dec_step > maxvalue) {
                return "";
            }
            /** @type {!Array} */
            var PL$58 = ["Geneva", "Lobster", "New York", "Century", "Apple Gothic", "Minion Pro", "Apple LiGothic", "Century Gothic", "Monaco", "Lato", "Fantasque Sans Mono", "Adobe Braille", "Cambria", "Futura", "Bell MT", "Courier", "Courier New", "Calibri", "Avenir Next", "Birch Std", "Palatino", "Ubuntu Regular", "Oswald", "Batang", "Ubuntu Medium", "Cantarell", "Droid Serif", "Roboto", "Helvetica Neue", "Corsiva Hebrew", "Adobe Hebrew", "TI-Nspire", "Comic Neue", "Noto", "AlNile", "Palatino-Bold", "ArialHebrew-Light", "Avenir", "Papyrus", "Open Sans", "Times", "Quicksand", "Source Sans Pro", "Damascus", "Microsoft Sans Serif"];
            var container = document["createElement"]("div");
            container["style"]["cssText"] = "position: relative; left: -9999px; visibility: hidden; display: block !important";
            /** @type {!Array} */
            var PL$78 = [];
            /** @type {number} */
            var PL$79 = 0;
            for (; PL$79 < PL$58["length"]; PL$79++) {
                var data = document["createElement"]("div");
                /** @type {number} */
                _id = 0;
                for (; _id < sharePlaylist["length"]; _id++) {
                    id = document["createElement"]("span");
                    id["innerHTML"] = "abcdefhijklmnopqrstuvxyz1234567890;+-.";
                    id["style"]["fontSize"] = "90px";
                    id["style"]["fontFamily"] = PL$58[PL$79] + "," + sharePlaylist[_id];
                    data["appendChild"](id);
                }
                container["appendChild"](data);
            }
            if (bmak["get_cf_date"]() - dec_step > maxvalue) {
                return "";
            }
            document["body"]["appendChild"](container);
            /** @type {number} */
            PL$79 = 0;
            for (; PL$79 < container["childNodes"]["length"]; PL$79++) {
                /** @type {boolean} */
                var inactiveTag = false;
                data = container["childNodes"][PL$79];
                /** @type {number} */
                _id = 0;
                for (; _id < data["childNodes"]["length"]; _id++) {
                    id = data["childNodes"][_id];
                    if (id["offsetWidth"] !== item[_id] || id["offsetHeight"] !== newJoinDoc[_id]) {
                        /** @type {boolean} */
                        inactiveTag = true;
                        break;
                    }
                }
                if (inactiveTag && PL$78["push"](PL$79), bmak["get_cf_date"]() - dec_step > maxvalue) {
                    break;
                }
            }
            document["body"]["removeChild"](container);
            n = PL$78["sort"]();
        }
        return n["join"](",");
    };
    /**
     * @return {?}
     */
    arr["fonts"] = function() {
        /** @type {!Array} */
        var a = [];
        if (!arr["sf4"]()) {
            /** @type {!Array} */
            var dynacAttrs = ["serif", "sans-serif", "monospace"];
            /** @type {!Array} */
            var testStyle = [0, 0, 0];
            /** @type {!Array} */
            var declarations = [0, 0, 0];
            var style = document["createElement"]("span");
            style["innerHTML"] = "abcdefhijklmnopqrstuvxyz1234567890;+-.";
            style["style"]["fontSize"] = "90px";
            var property;
            /** @type {number} */
            property = 0;
            for (; property < dynacAttrs["length"]; property++) {
                style["style"]["fontFamily"] = dynacAttrs[property];
                document["body"]["appendChild"](style);
                testStyle[property] = style["offsetWidth"];
                declarations[property] = style["offsetHeight"];
                document["body"]["removeChild"](style);
            }
            /** @type {!Array} */
            var lookup = ["Geneva", "Lobster", "New York", "Century", "Apple Gothic", "Minion Pro", "Apple LiGothic", "Century Gothic", "Monaco", "Lato", "Fantasque Sans Mono", "Adobe Braille", "Cambria", "Futura", "Bell MT", "Courier", "Courier New", "Calibri", "Avenir Next", "Birch Std", "Palatino", "Ubuntu Regular", "Oswald", "Batang", "Ubuntu Medium", "Cantarell", "Droid Serif", "Roboto", "Helvetica Neue", "Corsiva Hebrew", "Adobe Hebrew", "TI-Nspire", "Comic Neue", "Noto", "AlNile", "Palatino-Bold", "ArialHebrew-Light", "Avenir", "Papyrus", "Open Sans", "Times", "Quicksand", "Source Sans Pro", "Damascus", "Microsoft Sans Serif"];
            /** @type {!Array} */
            var columnsScalesMap = [];
            /** @type {number} */
            var val = 0;
            for (; val < lookup["length"]; val++) {
                /** @type {boolean} */
                var d = false;
                /** @type {number} */
                property = 0;
                for (; property < dynacAttrs["length"]; property++) {
                    if (style["style"]["fontFamily"] = lookup[val] + "," + dynacAttrs[property], document["body"]["appendChild"](style), style["offsetWidth"] === testStyle[property] && style["offsetHeight"] === declarations[property] || (d = true), document["body"]["removeChild"](style), d) {
                        columnsScalesMap["push"](val);
                        break;
                    }
                }
            }
            a = columnsScalesMap["sort"]();
        }
        return a["join"](",");
    };
    /**
     * @return {?}
     */
    arr["webrtcKey"] = function() {
        return "function" == typeof window["RTCPeerConnection"] || "function" == typeof window["mozRTCPeerConnection"] || "function" == typeof window["webkitRTCPeerConnection"];
    };
    /**
     * @return {?}
     */
    arr["indexedDbKey"] = function() {
        return !!arr["hasIndexedDB"]();
    };
    /**
     * @return {?}
     */
    arr["sessionStorageKey"] = function() {
        return !!arr["hasSessionStorage"]();
    };
    /**
     * @return {?}
     */
    arr["localStorageKey"] = function() {
        return !!arr["hasLocalStorage"]();
    };
    /**
     * @return {?}
     */
    arr["hasSessionStorage"] = function() {
        try {
            return !!window["sessionStorage"];
        } catch (a) {
            return false;
        }
    };
    /**
     * @return {?}
     */
    arr["hasLocalStorage"] = function() {
        try {
            return !!window["localStorage"];
        } catch (a) {
            return false;
        }
    };
    /**
     * @return {?}
     */
    arr["hasIndexedDB"] = function() {
        return !!window["indexedDB"];
    };
}(bmak), bmak["firstLoad"]) {
    bmak["sd_debug"]("<init/>");
    /** @type {number} */
    var i = 0;
    for (; i < _cf["length"]; i++) {
        bmak["applyFunc"](_cf[i]);
    }
    bmak["sd_debug"]("<setSDFN>" + bmak["sdfn"]["join"]() + "</setSDFN>");
    _cf = {
        push : bmak["applyFunc"]
    };
    try {
        bmak["ir"]();
        bmak["t_tst"] = bmak["get_cf_date"]();
        bmak["startTracking"]();
        /** @type {number} */
        bmak["tst"] = bmak["get_cf_date"]() - bmak["t_tst"];
        if (!bmak["disFpCalOnTimeout"]) {
            setTimeout(bmak["calc_fp"], 500);
        }
        /** @type {number} */
        i = 0;
        for (; i < 3; i++) {
            setTimeout(bmak["getmr"], 400 + 5E3 * i);
        }
        setTimeout(bmak["mn_init"], 1E3);
    } catch (a) {
    }
}
;
console.log(bmak.sensor_data);
console.log("=============");
console.log(document["getElementById"]("bm-telemetry"))