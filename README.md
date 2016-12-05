# **Text RIPTA** ([HackRI 2016](http://hackri.com/) - Fourth Place Finalists)

**Text RIPTA** is a dual-language software project developed chiefly by [Darius Strasel](https://github.com/dariusstrasel), [Ryan Scullin](https://github.com/RCScullin) (**[Python]()**) and [Will Daly](https://github.com/willdaly), [Lu Nathan](https://github.com/neugierige), and [Rafael Fernandez](https://github.com/myztajay) (**[Ruby](https://github.com/willdaly/ripta-rails)**) with Anne Wolfe as our design/presentation specialist, during the HackRI 2016 Hackathon. 

This software allows users to text a stop ID number (bus stop number) to a Twilio enabled phone number and learn how close it is! (Relative to the number of stops)
This uses the [RIPTA Realtime API](realtime.ripta.com:81), which is standardised via GTFS.

* The Python-based implementation uses Flask and werkzeug libraries to consume the HTTP requests from the Twilio API which are then passed into data-parsing functions which calculate a result using the RIPTA real-time API.

[![](https://i.imgsafe.org/5bd71ecb06.png)](https://www.youtube.com/watch?v=QAHl9NNQ_0o&feature=youtu.be)
