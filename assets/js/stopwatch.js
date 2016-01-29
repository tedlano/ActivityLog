$( document ).ready(function() {
    
    var stopwatch_sec = $('#stopwatch_sec').val(0);
    var stopwatch_min = $('#stopwatch_min').val(0);
    var stopwatch_hr  = $('#stopwatch_hr').val(0);
    var interval;
    
    $('#play_pause').click(function () {
    
        var _this = $(this);
        var glyph = _this.find('.glyphicon');
        
        function updateStopwatch(){
            var timeCount = (parseInt(stopwatch_hr.val()) * 3600) + parseInt(stopwatch_min.val() * 60) + parseInt(stopwatch_sec.val()) + 1;
            var hours = Math.floor(timeCount / 3600);
            var minutes = Math.floor( (timeCount/60) % 60);
            var seconds = timeCount % 60;
            
            stopwatch_hr.val(hours);
            stopwatch_min.val(minutes);
            stopwatch_sec.val(seconds);
        }
        
        if (glyph.hasClass('glyphicon-play')){
            _this.removeClass('btn-default');
            glyph.removeClass('glyphicon-play');
            _this.addClass('btn-success');
            glyph.addClass('glyphicon-pause');
            _this.html(glyph);
            _this.append(" Pause");
            interval = setInterval(updateStopwatch, 1000);
            
        } else {
            glyph.removeClass('glyphicon-pause');
            _this.removeClass('btn-success');
            glyph.addClass('glyphicon-play');
            _this.addClass('btn-default');
            _this.html(glyph);
            _this.append(" Resume");
            clearInterval(interval);
        }
    });
});