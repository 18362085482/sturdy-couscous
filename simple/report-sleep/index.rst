======================
FunkLoad_ bench report
======================


:date: 2018-03-30 16:30:34
:abstract: Simply testing a default static page
           Bench result of ``Simple.test_simple``: 
           Access the main URL 20 times

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2018-03-30 16:30:34
* From: chenghaodeMacBook-Pro.local
* Test: ``test_Simple.py Simple.test_simple``
* Label: allcpu
* Target server: http://localhost/simBatch/public
* Cycles of concurrent users: [1, 2, 3, 4, 5, 6, 8, 10, 16]
* Cycle duration: 4s
* Sleeptime between requests: from 0.0s to 0.0s
* Sleeptime between test cases: 0.0s
* Startup delay between threads: 0.2s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.17.1


Bench content
-------------

The test ``Simple.test_simple`` contains: 

* 1 page
* 1 redirect
* 0 links
* 0 images
* 0 XML-RPC calls

The bench contains:

* 586 tests
* 1068 pages
* 1068 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  1              4.250                 17                 17             0.00%
                  2              9.250                 37                 37             0.00%
                  3             14.500                 58                 58             0.00%
                  4             16.000                 64                 64             0.00%
                  5             16.750                 67                 67             0.00%
                  6             20.000                 80                 80             0.00%
                  8             20.750                 83                 83             0.00%
                 10             22.750                 91                 91             0.00%
                 16             22.250                 89                 89             0.00%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note: an XML-RPC call counts as a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  1              1.000          Excellent              8.000              9.000                 32                 32             0.00%              0.103              0.120              0.166              0.107              0.119              0.127              0.146
                  2              1.000          Excellent             17.250             19.000                 69                 69             0.00%              0.098              0.119              0.264              0.102              0.111              0.140              0.175
                  3              1.000          Excellent             26.500             27.000                106                106             0.00%              0.102              0.114              0.142              0.104              0.113              0.129              0.135
                  4              1.000          Excellent             29.250             30.000                117                117             0.00%              0.117              0.137              0.333              0.122              0.131              0.150              0.157
                  5              1.000          Excellent             31.250             32.000                125                125             0.00%              0.132              0.158              0.360              0.139              0.150              0.186              0.197
                  6              1.000          Excellent             34.750             36.000                139                139             0.00%              0.139              0.172              0.402              0.152              0.167              0.191              0.201
                  8              1.000          Excellent             38.750             40.000                155                155             0.00%              0.165              0.205              0.610              0.170              0.192              0.228              0.239
                 10              1.000          Excellent             40.250             42.000                161                161             0.00%              0.174              0.244              0.887              0.195              0.232              0.283              0.295
                 16              1.000          Excellent             41.000             44.000                164                164             0.00%              0.302              0.390              1.431              0.332              0.384              0.437              0.456
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) (successful or not) over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png
 .. image:: time_rps.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  1              1.000          Excellent              8.000              9.000                 32                 32             0.00%              0.103              0.120              0.166              0.107              0.119              0.127              0.146
                  2              1.000          Excellent             17.250             19.000                 69                 69             0.00%              0.098              0.119              0.264              0.102              0.111              0.140              0.175
                  3              1.000          Excellent             26.500             27.000                106                106             0.00%              0.102              0.114              0.142              0.104              0.113              0.129              0.135
                  4              1.000          Excellent             29.250             30.000                117                117             0.00%              0.117              0.137              0.333              0.122              0.131              0.150              0.157
                  5              1.000          Excellent             31.250             32.000                125                125             0.00%              0.132              0.158              0.360              0.139              0.150              0.186              0.197
                  6              1.000          Excellent             34.750             36.000                139                139             0.00%              0.139              0.172              0.402              0.152              0.167              0.191              0.201
                  8              1.000          Excellent             38.750             40.000                155                155             0.00%              0.165              0.205              0.610              0.170              0.192              0.228              0.239
                 10              1.000          Excellent             40.250             42.000                161                161             0.00%              0.174              0.244              0.887              0.195              0.232              0.283              0.295
                 16              1.000          Excellent             41.000             44.000                164                164             0.00%              0.302              0.390              1.431              0.332              0.384              0.437              0.456
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **16** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.41s, get: ``/simBatch/public/noauth/login``
  ``
* In page 001, Apdex rating: Excellent, avg response time: 0.37s, get: ``/simBatch/public/servicerAdmin/customers``
  `Get URL`

Page detail stats
-----------------


PAGE 001: Get URL
~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/simBatch/public/servicerAdmin/customers``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                 17                 17             0.00%              0.103              0.119              0.166              0.107              0.113              0.146              0.166
                      2              1.000          Excellent                 37                 37             0.00%              0.098              0.117              0.264              0.101              0.105              0.144              0.175
                      3              1.000          Excellent                 59                 59             0.00%              0.102              0.112              0.142              0.103              0.107              0.133              0.139
                      4              1.000          Excellent                 66                 66             0.00%              0.117              0.135              0.307              0.120              0.126              0.155              0.160
                      5              1.000          Excellent                 70                 70             0.00%              0.132              0.158              0.360              0.137              0.146              0.195              0.197
                      6              1.000          Excellent                 82                 82             0.00%              0.139              0.173              0.402              0.150              0.164              0.193              0.202
                      8              1.000          Excellent                 85                 85             0.00%              0.165              0.192              0.610              0.169              0.182              0.213              0.220
                     10              1.000          Excellent                 93                 93             0.00%              0.174              0.240              0.887              0.189              0.216              0.290              0.305
                     16              1.000          Excellent                 89                 89             0.00%              0.302              0.369              0.507              0.325              0.357              0.454              0.463
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, get, url ``/simBatch/public/noauth/login``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                 15                 15             0.00%              0.110              0.120              0.127              0.115              0.120              0.126              0.127
                      2              1.000          Excellent                 32                 32             0.00%              0.108              0.122              0.262              0.109              0.116              0.125              0.178
                      3              1.000          Excellent                 47                 47             0.00%              0.111              0.116              0.136              0.113              0.115              0.121              0.126
                      4              1.000          Excellent                 51                 51             0.00%              0.127              0.139              0.333              0.131              0.135              0.141              0.142
                      5              1.000          Excellent                 55                 55             0.00%              0.142              0.157              0.215              0.146              0.154              0.181              0.188
                      6              1.000          Excellent                 57                 57             0.00%              0.155              0.170              0.199              0.161              0.168              0.188              0.195
                      8              1.000          Excellent                 70                 70             0.00%              0.179              0.222              0.593              0.187              0.199              0.239              0.514
                     10              1.000          Excellent                 68                 68             0.00%              0.203              0.249              0.877              0.220              0.239              0.264              0.272
                     16              1.000          Excellent                 75                 75             0.00%              0.364              0.415              1.431              0.378              0.400              0.429              0.443
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/XML-RPC request.
* Page: a request with redirects and resource links (image, css, js) for an HTML page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index,
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s. This means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerable and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation, the Apdex score is also represented
  as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.


Report generated with FunkLoad_ 1.17.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.