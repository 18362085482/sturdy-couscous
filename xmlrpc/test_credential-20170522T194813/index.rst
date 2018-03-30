======================
FunkLoad_ bench report
======================


:date: 2017-05-22 19:48:13
:abstract: Try to test all xml rpc method
           Bench result of ``Credential.test_credential``: 
           Check all credentiald methods

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-05-22 19:48:13
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

* 1163 tests
* 5775 pages
* 5775 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  1              0.800                  8                  8             0.00%
                 20             15.900                159                159             0.00%
                 40             23.900                239                239             0.00%
                 60             25.200                252                252             0.00%
                 80             24.600                246                246             0.00%
                100             25.900                259                259             0.00%
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
                 20              1.000          Excellent             77.900             81.000                779                779             0.00%              0.001              0.003              0.007              0.002              0.003              0.004              0.004
                 40              1.000          Excellent            119.000            167.000               1190               1190             0.00%              0.001              0.065              1.059              0.002              0.003              0.005              1.031
                 60              1.000          Excellent            125.000            194.000               1250               1250             0.00%              0.001              0.236              1.073              0.002              0.003              1.038              1.046
                 80              0.981          Excellent            124.900            224.000               1249               1249             0.00%              0.001              0.372              3.166              0.002              0.003              1.044              1.063
                100              0.958          Excellent            126.800            212.000               1268               1268             0.00%              0.001              0.514              4.250              0.002              0.004              1.068              3.157
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
                 20              1.000          Excellent             77.900             81.000                779                779             0.00%              0.001              0.003              0.007              0.002              0.003              0.004              0.004
                 40              1.000          Excellent            119.000            167.000               1190               1190             0.00%              0.001              0.065              1.059              0.002              0.003              0.005              1.031
                 60              1.000          Excellent            125.000            194.000               1250               1250             0.00%              0.001              0.236              1.073              0.002              0.003              1.038              1.046
                 80              0.981          Excellent            124.900            224.000               1249               1249             0.00%              0.001              0.372              3.166              0.002              0.003              1.044              1.063
                100              0.958          Excellent            126.800            212.000               1268               1268             0.00%              0.001              0.514              4.250              0.002              0.004              1.068              3.157
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **60** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.58s, xmlrpc: ``http://localhost:44401/#getStatus``
  `Check getStatus`
* In page 002, Apdex rating: Excellent, avg response time: 0.19s, xmlrpc: ``http://localhost:44401/#getCredential``
  `Get a credential from a file`
* In page 004, Apdex rating: Excellent, avg response time: 0.14s, xmlrpc: ``http://localhost:44401/#listCredentials``
  `list all credential of the file`
* In page 003, Apdex rating: Excellent, avg response time: 0.13s, xmlrpc: ``http://localhost:44401/#listGroups``
  `list groups from the group file`
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
                      1              1.000          Excellent                  7                  7             0.00%              0.002              0.003              0.003              0.002              0.003              0.003              0.003
                     20              1.000          Excellent                156                156             0.00%              0.001              0.003              0.005              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                241                241             0.00%              0.001              0.101              1.046              0.002              0.003              0.006              1.034
                     60              1.000          Excellent                251                251             0.00%              0.001              0.580              1.073              0.002              1.027              1.057              1.064
                     80              0.986          Excellent                257                257             0.00%              0.001              0.834              3.166              0.002              1.034              1.061              1.071
                    100              0.951          Excellent                268                268             0.00%              0.001              1.094              4.250              0.004              1.046              1.078              3.157
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
                     20              1.000          Excellent                154                154             0.00%              0.001              0.003              0.005              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                236                236             0.00%              0.001              0.020              1.058              0.002              0.003              0.004              0.005
                     60              1.000          Excellent                245                245             0.00%              0.001              0.192              1.045              0.002              0.003              1.033              1.039
                     80              0.968          Excellent                251                251             0.00%              0.001              0.278              3.161              0.002              0.003              1.032              2.122
                    100              0.978          Excellent                250                250             0.00%              0.001              0.254              3.172              0.002              0.003              1.036              1.043
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
                     20              1.000          Excellent                156                156             0.00%              0.001              0.003              0.004              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                239                239             0.00%              0.001              0.067              1.035              0.002              0.003              0.005              1.030
                     60              1.000          Excellent                250                250             0.00%              0.001              0.134              1.041              0.002              0.003              1.025              1.033
                     80              0.984          Excellent                243                243             0.00%              0.001              0.238              3.160              0.002              0.003              1.030              1.032
                    100              0.955          Excellent                245                245             0.00%              0.001              0.392              3.174              0.002              0.003              1.041              3.162
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
                     20              1.000          Excellent                156                156             0.00%              0.002              0.003              0.007              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                238                238             0.00%              0.001              0.055              1.056              0.002              0.003              0.005              1.030
                     60              1.000          Excellent                251                251             0.00%              0.001              0.143              1.042              0.002              0.003              1.028              1.036
                     80              0.982          Excellent                252                252             0.00%              0.001              0.217              3.162              0.002              0.003              1.029              1.032
                    100              0.943          Excellent                246                246             0.00%              0.001              0.422              3.175              0.002              0.003              2.119              3.166
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
                     20              1.000          Excellent                157                157             0.00%              0.001              0.003              0.005              0.002              0.003              0.004              0.004
                     40              1.000          Excellent                236                236             0.00%              0.001              0.082              1.059              0.002              0.003              0.005              1.032
                     60              1.000          Excellent                253                253             0.00%              0.001              0.129              1.046              0.002              0.003              1.026              1.035
                     80              0.984          Excellent                246                246             0.00%              0.001              0.277              3.161              0.002              0.003              1.031              1.034
                    100              0.961          Excellent                259                259             0.00%              0.001              0.366              3.169              0.002              0.003              1.039              3.155
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