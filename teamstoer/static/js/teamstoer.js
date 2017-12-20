/*
This widget_counter is based on code from https://www.roparun.nl/
 */
var widget_counter = $("#widget-counter");

(function(e) {
    e.fn.countdown = function(t, n) {
        function i() {
            eventDateStart = Date.parse(r.date_start) / 1e3;
            eventDateEnd = Date.parse(r.date_end) / 1e3;
            eventDateStartNextEvent = Date.parse(r.date_start_next_event) / 1e3;
            currentDate = Math.floor(e.now() / 1e3);
            if (eventDateStart > currentDate) {
                seconds = eventDateStart - currentDate;
            } else if (eventDateEnd > currentDate) {
                seconds = currentDate - eventDateStart;
            } else if (eventDateStartNextEvent > currentDate) {
                seconds = eventDateStartNextEvent - currentDate;
            }
            days = Math.floor(seconds / 86400);
            seconds -= days * 60 * 60 * 24;
            hours = Math.floor(seconds / 3600);
            seconds -= hours * 60 * 60;
            minutes = Math.floor(seconds / 60);
            seconds -= minutes * 60;
            days == 1 ? thisEl.find("#roparun-countdown-days-text").text("dag") : thisEl.find("#roparun-countdown-days-text").text("dagen");
            hours == 1 ? thisEl.find("#roparun-countdown-hours-text").text("uur") : thisEl.find("#roparun-countdown-hours-text").text("uren");
            minutes == 1 ? thisEl.find("#roparun-countdown-minutes-text").text("minuut") : thisEl.find("#roparun-countdown-minutes-text").text("minuten");
            seconds == 1 ? thisEl.find("#roparun-countdown-seconds-text").text("seconden") : thisEl.find("#roparun-countdown-seconds-text").text("seconden");
            if (r["format"] == "on") {
                days = String(days).length >= 2 ? days : "0" + days;
                hours = String(hours).length >= 2 ? hours : "0" + hours;
                minutes = String(minutes).length >= 2 ? minutes : "0" + minutes;
                seconds = String(seconds).length >= 2 ? seconds : "0" + seconds
            }
            if (!isNaN(eventDateStart)) {
                thisEl.find("#roparun-countdown-days").text(days);
                thisEl.find("#roparun-countdown-hours").text(hours);
                thisEl.find("#roparun-countdown-minutes").text(minutes);
                thisEl.find("#roparun-countdown-seconds").text(seconds)
            } else {
                clearInterval(interval)
            }
        }
        var thisEl = e(this);
        var r = {
            date_start: null,
            date_end: null,
            date_start_next_event: null,
            format: null
        };
        t && e.extend(r, t);
        i();
        interval = setInterval(i, 1e3)
    }
})(jQuery);

if (widget_counter.length > 0) {

    function e() {
        var e = new Date;
        e.setDate(e.getDate() + 60);
        dd = e.getDate();
        mm = e.getMonth() + 1;
        y = e.getFullYear();
        futureFormattedDate = mm + "/" + dd + "/" + y;
        return futureFormattedDate
    }
    widget_counter.countdown({
        date_start: $("#roparun_countdown_date_start").val(),
        date_end: $("#roparun_countdown_date_end").val(),
        date_start_next_event: $("#roparun_countdown_date_start_next_event").val(),
        format: "off"
    });
}