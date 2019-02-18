# Live view camera stream

## Objective
The goal is to host a static site that sends a live picture every ~5 seconds to all connected clients.

## Overview

* Image capture - fswebcam
* Site hosting - TBD ?apache?
  * Still need to decide between static site where client polls for updates vs websockets
* Site - simple one page
* Routing - ideally using noip for dns routing and vpn to hide ip
