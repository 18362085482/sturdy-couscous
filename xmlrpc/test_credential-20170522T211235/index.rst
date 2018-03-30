======================
FunkLoad_ bench report
======================


:date: 2017-05-22 21:12:35
:abstract: Try to test all xml rpc method
           Bench result of ``Credential.test_credential``: 
           Check all credentiald methods

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-05-22 21:12:35
* From: chenghaodeMacBook-Pro.local
* Test: ``test_Credential.py Credential.test_credential``
* Target server: http://localhost:44401/
* Cycles of concurrent users: [1, 20, 40, 60, 80, 100]
* Cycle duration: 10s
* Sleeptime between requests: from 0.1s to 0.2s
* Sleeptime between test cases: 0.5s
* Startup delay between threads: 0.05s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.17.1


Bench content
-------------

The test ``Credential.test_credential`` contains: 

* 0 pages
* 0 redirects
* 0 links
* 0 images
* 5 XML-RPC calls

The bench contains:

* 1159 tests
* 5804 pages
* 5804 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  1              0.800                  8                  8             0.00%
                 20             15.700                157                157             0.00%
                 40             24.200                242                242             0.00%
                 60             25.000                250                250             0.00%
                 80             25.100                251                251             0.00%
                100             25.100                251                251             0.00%
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
                  1              1.000          Excellent              3.900              5.000                 39                 39             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                 20              1.000          Excellent             79.100             84.000                791                791             0.00%              0.001              0.003              0.017              0.002              0.003              0.004              0.004
                 40              1.000          Excellent            121.300            169.000               1213               1213             0.00%              0.001              0.065              1.061              0.002              0.003              0.005              1.029
                 60              1.000          Excellent            125.000            182.000               1250               1250             0.00%              0.001              0.234              1.063              0.002              0.003              1.034              1.042
                 80              0.982          Excellent            125.000            233.000               1250               1250             0.00%              0.001              0.370              3.160              0.002              0.003              1.046              1.059
                100              0.955          Excellent            126.100            226.000               1261               1261             0.00%              0.001              0.514              4.236              0.002              0.004              1.067              2.095
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
                  1              1.000          Excellent              3.900              5.000                 39                 39             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                 20              1.000          Excellent             79.100             84.000                791                791             0.00%              0.001              0.003              0.017              0.002              0.003              0.004              0.004
                 40              1.000          Excellent            121.300            169.000               1213               1213             0.00%              0.001              0.065              1.061              0.002              0.003              0.005              1.029
                 60              1.000          Excellent            125.000            182.000               1250               1250             0.00%              0.001              0.234              1.063              0.002              0.003              1.034              1.042
                 80              0.982          Excellent            125.000            233.000               1250               1250             0.00%              0.001              0.370              3.160              0.002              0.003              1.046              1.059
                100              0.955          Excellent            126.100            226.000               1261               1261             0.00%              0.001              0.514              4.236              0.002              0.004              1.067              2.095
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **60** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.59s, xmlrpc: ``http://localhost:44401/#getStatus``
  `Check getStatus`
* In page 002, Apdex rating: Excellent, avg response time: 0.17s, xmlrpc: ``http://localhost:44401/#getCredential``
  `Get a credential from a file`
* In page 003, Apdex rating: Excellent, avg response time: 0.14s, xmlrpc: ``http://localhost:44401/#listGroups``
  `list groups from the group file`
* In page 004, Apdex rating: Excellent, avg response time: 0.14s, xmlrpc: ``http://localhost:44401/#listCredentials``
  `list all credential of the file`
* In page 005, Apdex rating: Excellent, avg response time: 0.13s, xmlrpc: ``http://localhost:44401/#listCredentials``
  `list credentials of group AdminZope`

Page detail stats
-----------------


PAGE 001: Check getStatus
~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, xmlrpc, url ``http://localhost:44401/#getStatus``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  7                  7             0.00%              0.002              0.002              0.003              0.002              0.002              0.003              0.003
                     20              1.000          Excellent                159                159             0.00%              0.001              0.003              0.011              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                244                244             0.00%              0.001              0.105              1.059              0.002              0.003              0.005              1.037
                     60              1.000          Excellent                249                249             0.00%              0.001              0.595              1.063              0.002              1.029              1.050              1.054
                     80              0.984          Excellent                255                255             0.00%              0.001              0.840              3.158              0.003              1.035              1.059              1.067
                    100              0.926               Good                277                277             0.00%              0.001              1.193              4.236              1.028              1.051              2.094              3.134
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 002: Get a credential from a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, xmlrpc, url ``http://localhost:44401/#getCredential``

     .. image:: request_002.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                     20              1.000          Excellent                158                158             0.00%              0.001              0.003              0.005              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                245                245             0.00%              0.001              0.036              1.033              0.002              0.003              0.004              0.005
                     60              1.000          Excellent                249                249             0.00%              0.001              0.172              1.038              0.002              0.003              1.031              1.034
                     80              0.975          Excellent                255                255             0.00%              0.001              0.244              3.156              0.002              0.003              1.032              2.111
                    100              0.953          Excellent                255                255             0.00%              0.001              0.375              3.162              0.002              0.003              1.042              2.094
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 003: list groups from the group file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, xmlrpc, url ``http://localhost:44401/#listGroups``

     .. image:: request_003.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                     20              1.000          Excellent                158                158             0.00%              0.001              0.003              0.005              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                248                248             0.00%              0.001              0.049              1.061              0.002              0.003              0.004              0.006
                     60              1.000          Excellent                248                248             0.00%              0.001              0.140              1.039              0.002              0.003              1.029              1.033
                     80              0.982          Excellent                244                244             0.00%              0.001              0.241              3.158              0.002              0.003              1.032              1.034
                    100              0.968          Excellent                238                238             0.00%              0.001              0.293              3.161              0.002              0.003              1.041              2.091
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 004: list all credential of the file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, xmlrpc, url ``http://localhost:44401/#listCredentials``

     .. image:: request_004.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                     20              1.000          Excellent                157                157             0.00%              0.002              0.003              0.017              0.002              0.003              0.004              0.005
                     40              1.000          Excellent                239                239             0.00%              0.001              0.063              1.059              0.002              0.003              0.005              1.028
                     60              1.000          Excellent                254                254             0.00%              0.001              0.137              1.038              0.002              0.003              1.026              1.031
                     80              0.994          Excellent                245                245             0.00%              0.001              0.209              3.154              0.002              0.003              1.032              1.034
                    100              0.971          Excellent                243                243             0.00%              0.001              0.295              3.161              0.002              0.003              1.041              2.091
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 005: list credentials of group AdminZope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, xmlrpc, url ``http://localhost:44401/#listCredentials``

     .. image:: request_005.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              1.000          Excellent                  8                  8             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                     20              1.000          Excellent                159                159             0.00%              0.002              0.003              0.005              0.002              0.003              0.004              0.005
                     40              1.000          Excellent                237                237             0.00%              0.001              0.073              1.061              0.002              0.003              0.005              1.029
                     60              1.000          Excellent                250                250             0.00%              0.001              0.131              1.037              0.002              0.003              1.028              1.032
                     80              0.974          Excellent                251                251             0.00%              0.001              0.301              3.160              0.002              0.003              1.032              2.115
                    100              0.962          Excellent                248                248             0.00%              0.001              0.327              3.162              0.002              0.003              1.041              2.091
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