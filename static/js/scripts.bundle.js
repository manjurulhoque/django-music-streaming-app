"use strict";
var AppConfig = AppConfig || {};
$(function () {
    AppConfig = {
        init: function () {
            AppConfig.langCheckedToApply(), AppConfig.initAppScrollbars(), AppConfig.initSlickCarousel(), AppConfig.search(), AppConfig.buttonClickEvents(), AppConfig.materialTab(), AppConfig.initCountdown(), AppConfig.addFavorite(), AppConfig.initTheme()
        }, initTheme: function () {
            $("body").themeSettings()
        }, langCheckedToApply: function () {
            var s = $("#lang .custom-control-input");
            s.on("change", function () {
                $("#langApply").prop("disabled", !s.filter(":checked").length)
            }).trigger("change")
        }, initAppScrollbars: function () {
            $('[data-scrollable="true"]').each(function () {
                new PerfectScrollbar(this, {
                    wheelSpeed: .5,
                    swipeEasing: !0,
                    wheelPropagation: !1,
                    minScrollbarLength: 40,
                    suppressScrollX: !0
                })
            })
        }, slickCarousel: function (s, t, e, i, a) {
            $(s).slick({
                arrows: !0,
                dots: !1,
                infinite: !1,
                slidesToShow: t,
                slidesToScroll: 1,
                speed: 1e3,
                prevArrow: '<button class="btn-prev btn btn-pill btn-air btn-default btn-icon-only"><i class="la la-angle-left"></i></button>',
                nextArrow: '<button class="btn-next btn btn-pill btn-air btn-default btn-icon-only"><i class="la la-angle-right"></i></button>',
                responsive: [{breakpoint: 1440, settings: {slidesToShow: e}}, {
                    breakpoint: 1200,
                    settings: {slidesToShow: i}
                }, {breakpoint: 640, settings: {slidesToShow: a}}, {
                    breakpoint: 380,
                    settings: {slidesToShow: 1, arrows: !1}
                }]
            })
        }, initSlickCarousel: function () {
            AppConfig.slickCarousel(".carousel-item-4", 4, 3, 2, 1), AppConfig.slickCarousel(".carousel-item-5", 5, 4, 3, 2), AppConfig.slickCarousel(".carousel-item-6", 6, 5, 4, 2)
        }, buttonClickEvents: function () {
            $("#toggleSidebar").on("click", function () {
                s.toggleClass("iconic-sidebar")
            }), $("#openSidebar").on("click", function (i) {
                i.stopPropagation(), s.removeClass("open-search"), s.addClass("open-sidebar"), e.addClass("show"), t.removeClass("show")
            }), $("#hideSidebar").on("click", function () {
                s.removeClass("open-sidebar"), e.removeClass("show")
            }), $("#playList").on("click", function () {
                s.toggleClass("open-right-sidebar")
            })
        }, search: function () {
            $("#searchForm").on("click", function (e) {
                e.stopPropagation(), s.addClass("open-search"), t.addClass("show")
            }), s.on("click", function () {
                s.removeClass("open-search"), t.removeClass("show")
            })
        }, materialTab: function () {
            var s = $(".line-tabs .nav-item .active"), t = $(".line-tabs .nav-item");
            $(".line-tabs").append("<span class='tabs-link-line'></span>");
            var e = s.position(), i = s.parent().width();
            $(".tabs-link-line").stop().css({width: i}), t.on("click", function () {
                e = $(this).position(), i = $(this).width(), $(this).parent().parent().find(".tabs-link-line").stop().css({
                    left: e.left,
                    width: i
                })
            })
        }, initCountdown: function () {
            var s = $(".countdown"), t = new Date;
            t.setDate(t.getDate() + 5), s.countdown(t, function (s) {
                $(this).html(s.strftime('<div class="timer-wrapper"><div class="timer-data">%D</div></div><span class="time-separate">:</span><div class="timer-wrapper"><div class="timer-data">%H</div></div><span class="time-separate">:</span><div class="timer-wrapper"><div class="timer-data">%M</div></div><span class="time-separate">:</span><div class="timer-wrapper"><div class="timer-data">%S</div></div>'))
            })
        }, addFavorite: function () {
            var s = $(".favorite"),
                t = '<li><span class="badge badge-pill badge-danger"><i class="la la-heart"></i></span></li>';
            s.on("click", function (s) {
                s.stopPropagation();
                var e = $(this).closest(".custom-card--info"), i = e.find(".custom-card--labels");
                if (i.length && !e.find(".custom-card--labels li .la-heart").length) i.append(t); else {
                    e.prepend('<ul class="custom-card--labels d-flex"><li><span class="badge badge-pill badge-danger"><i class="la la-heart"></i></span></li></ul>')
                }
            })
        }
    };
    var s = $("body"), t = $(".header-backdrop"), e = $(".sidebar-backdrop");
    $(document).ready(AppConfig.init)
}), $(window).on("load", function () {
    // $("#loading").fadeOut(1e3);
    $("#loading").fadeOut(1000);
    // $("#login").modal("show");
}), $("#wrapper").on("scroll", function () {
    $("#header").toggleClass("scrolled", $(this).scrollTop() > 80)
});
// var AudioPlayer = AudioPlayer || {};
// $(function () {
//     AudioPlayer = {
//         init: function () {
//             AudioPlayer.initAudioPlayer(), AudioPlayer.volumeDropdownClick(), AudioPlayer.volumeIconClick(), AudioPlayer.addAudioInPlayer()
//         }, initAudioPlayer: function () {
//             Amplitude.init({
//                 songs: [{
//                     name: "I Love You Mummy",
//                     artist: "Arebica Luna",
//                     album: "Mummy",
//                     url: "../assets/audio/ringtone-1.mp3",
//                     cover_art_url: "../assets/images/cover/small/1.jpg"
//                 }]
//                 // , playlists: {
//                 //     special: {
//                 //         songs: [{
//                 //             name: "I Love You Mummy",
//                 //             artist: "Arebica Luna",
//                 //             album: "Mummy",
//                 //             url: "",
//                 //             cover_art_url: ""
//                 //         }
//                 //     }
//                 // }
//             })
//         }, volumeDropdownClick: function () {
//             $(document).on("click", ".volume-dropdown-menu", function (s) {
//                 s.stopPropagation()
//             })
//         }, volumeIconClick: function () {
//             var s = $('.audio-volume input[type="range"]'), t = $(".audio-volume .btn");
//             s.on("change", function () {
//                 let s = $(this), e = parseInt(s.val(), 10);
//                 0 === e ? t.html('<i class="ion-md-volume-mute"></i>') : e > 0 && e < 70 ? t.html('<i class="ion-md-volume-low"></i>') : e > 70 && t.html('<i class="ion-md-volume-high"></i>')
//             })
//         }, addAudioInPlayer: function () {
//             $("a[data-audio]").on("click", function () {
//                 var s = $(this).data("audio");
//                 Amplitude.removeSong(0);
//                 Amplitude.playNow(s);
//             })
//         }
//     }, $(document).ready(AudioPlayer.init)
// });
$(function (s, t, e, i) {
    function a(e, i) {
        this.$body = s("body"), this.options = s.extend({}, a.Defaults, i), this.cookiesOptions = {
            themeDark: this.options.darkTheme,
            header: this.options.header,
            sidebar: this.options.sidebar,
            player: this.options.player
        }, null != s.cookie("themeSetting") && !1 === i && (this.cookiesOptions = JSON.parse(s.cookie("themeSetting")), this.options.darkTheme = this.cookiesOptions.themeDark, this.options.header = this.cookiesOptions.header, this.options.sidebar = this.cookiesOptions.sidebar, this.options.player = this.cookiesOptions.player), this.optionList = [{
            text: "Dark Theme",
            value: this.options.darkTheme
        }];
        var o = t.location.pathname.split("/").pop().split(".")[0], n = ["index", "error"].includes(o);
        o && !n && this.initialize()
    }

    a.Defaults = {
        darkTheme: !1,
        header: 0,
        sidebar: 0,
        player: 0,
        themeClass: ["primary", "danger", "success", "warning", "info", "brand", "dark"],
        settingsButton: "button",
        settingsButtonId: "customSettings",
        settingsButtonClass: "btn btn-pill btn-air btn-brand btn-icon-only",
        settingIcon: '<i class="ion-md-settings"></i>',
        itemElement: "div",
        wrapperId: "settingsWrapper",
        listClass: "custom-list",
        listItemClass: "custom-list--item"
    }, a.prototype.initialize = function () {
        var t = s("#header"), e = s("#sidebar"), i = s("#audioPlayer");
        this.options.darkTheme && this.$body.addClass("theme-dark"), t.addClass("bg-" + this.options.themeClass[this.options.header]), e.addClass("sidebar-" + this.options.themeClass[this.options.sidebar]), i.addClass("player-" + this.options.themeClass[this.options.player]), this.settingsButtonElement(), this.skinClicks()
    }, a.prototype.settingsButtonElement = function () {
        var s = {type: "button", id: this.options.settingsButtonId, className: this.options.settingsButtonClass},
            t = e.createElement(this.options.settingsButton);
        Object.assign(t, s), t.innerHTML = this.options.settingIcon, this.$body.append(t), this.themeOptions()
    }, a.prototype.themeOptions = function () {
        var s = e.createElement(this.options.itemElement);
        s.setAttribute("id", this.options.wrapperId);
        for (var t = '<div class="theme-settings-body"><ul class="' + this.options.listClass + '">', i = 0; i < this.optionList.length; i++) {
            var a = this.optionList[i].value ? "checked" : "";
            t += '<li class="' + this.options.listItemClass + '"><label for="to' + i + '">' + this.optionList[i].text + '</label><div class="custom-control custom-checkbox ml-auto"><input type="checkbox" class="custom-control-input" id="to' + i + '" ' + a + '><label class="custom-control-label" for="to' + i + '"></label></div></li>'
        }
        t += '<li class="custom-list-group--item-separator"></li><li class="custom-list-group--item custom-list-group--item-header">Header Colors</li><li class="' + this.options.listItemClass + '">';
        for (var o = 0; o < this.options.themeClass.length; o++) {
            var n = o === this.options.header ? "active" : "";
            t += '<a href="javascript:void(0);" class="header-skin bg-' + this.options.themeClass[o] + " " + n + '" data-header-skin="' + o + '"></a>'
        }
        t += "</li>", t += '<li class="custom-list-group--item-separator"></li><li class="custom-list-group--item custom-list-group--item-header">Sidebar Colors</li><li class="' + this.options.listItemClass + '">';
        for (var l = 0; l < this.options.themeClass.length; l++) {
            var r = l === this.options.sidebar ? "active" : "";
            t += '<a href="javascript:void(0);" class="sidebar-skin bg-' + this.options.themeClass[l] + " " + r + '" data-sidebar-skin="' + l + '"></a>'
        }
        t += "</li>", t += '<li class="custom-list-group--item-separator"></li><li class="custom-list-group--item custom-list-group--item-header">Player Colors</li><li class="' + this.options.listItemClass + '">';
        for (var d = 0; d < this.options.themeClass.length; d++) {
            var c = d === this.options.player ? "active" : "";
            t += '<a href="javascript:void(0);" class="player-skin bg-' + this.options.themeClass[d] + " " + c + '" data-player-skin="' + d + '"></a>'
        }
        t += "</li>", t += "</ul></div>", s.innerHTML = '<header><span class="title-bold font-md text-uppercase">Theme Settings</span><a href="javascript:void(0)" class="ml-auto"><i class="ion-md-close"></i></a></header>' + t, this.$body.append(s)
    }, a.prototype.skinClicks = function () {
        var t = this, e = "#" + t.options.settingsButtonId, i = s("#" + t.options.wrapperId), a = s("#header"),
            o = s("#sidebar"), n = s("#audioPlayer"), l = s(".header-skin"), r = s(".sidebar-skin"),
            d = s(".player-skin");
        this.$body.on("click", "#to0", function () {
            var e = s(this);
            t.cookiesOptions.themeDark = e[0].checked, t.$body.toggleClass("theme-dark"), t.setCookies()
        }), this.$body.on("click", ".header-skin", function () {
            var e = s(this), i = e.data("header-skin");
            t.cookiesOptions.header = i, a.removeClass(), a.addClass("bg-" + t.options.themeClass[i]), l.removeClass("active"), e.addClass("active"), t.setCookies()
        }), this.$body.on("click", ".sidebar-skin", function () {
            var e = s(this), i = e.data("sidebar-skin");
            t.cookiesOptions.sidebar = i, o.removeClass(), o.addClass("sidebar-" + t.options.themeClass[i]), r.removeClass("active"), e.addClass("active"), t.setCookies()
        }), this.$body.on("click", ".player-skin", function () {
            var e = s(this), i = e.data("player-skin");
            t.cookiesOptions.player = i, n.removeClass(), n.addClass("player-" + t.options.themeClass[i]), d.removeClass("active"), e.addClass("active"), t.setCookies()
        }), this.$body.on("click", e, function () {
            i.toggleClass("open-settings")
        }), this.$body.on("click", "header a", function () {
            i.removeClass("open-settings")
        })
    }, a.prototype.setCookies = function () {
        s.cookie("themeSetting", JSON.stringify(this.cookiesOptions), {expires: 7, path: "/"})
    }, s.fn.themeSettings = function (t) {
        return this.each(function () {
            s(this), new a(this, "object" == typeof t && t)
        })
    }, s.fn.themeSettings.Constructor = a
}(jQuery, window, document));
