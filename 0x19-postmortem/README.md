Issue Summary

Duration: 75 minutes (10:15 AM EAT - 11:30 AM EAT)

Impact: Invalid credentials on the tracking platform. Several online users complained that they experienced extended page loading times and invalid credentials while trying to log in to the platform. 

Root Cause:
Database connection compatibility due to a recent database the recent AWS database upgrade from version 13 to 16

Timeline

10:15 AM EAT: Monitoring alerts flagged a significant increase in response times for the login API and failure to complete to fetch usernames and credentials.
10:30 AM EAT: The engineering team investigated and identified the runner had shooting requests that were holding the database impacting the database and service response times.
10 :30 AM EAT - 10:45 AM EAT: The Initial investigation focused on potential database server request overload. The team began to check the database server resources such as CPU, memory and data flows(both egress and ingress), which appeared abnormal.
10:45 AM EAT - 10:50 AM EAT: Investigation shifted towards analyzing slow queries and triggers on the database. 
11:00 AM EAT: The engineering team made a snap of the upgraded database and reverted the production database to v13.
11:05 AM EAT: Systems monitoring confirmed an immediate response from the web app where they noted connection and retrieval of data from the database/response times had returned to normal.
11:30 AM EAT: Post-mortem meeting convened to discuss this incident after it was monitored and established as working ok and ways to fix the compatibility issues using the snap image they created from V16
Root Cause and Resolution
The root cause was due to the automatic upgrade of the databases, This eventually led to the master database having compatibility issues with most of the supporting services like keyclock. Downgrading the database back to the previous version managed to temporarily resolve the issue and restored normal app functionality.

Corrective and Preventative Measures

Improve the automatic upgrade to start from the test environment: The current upgrade  process is automatical configured to run on both environment without testing phase.

Database scale in and out: The team decided to design read replica databases to handle frequent user requests to provide only for upsurge user requests during peak usage times. This would allow for scale out or scale in depending on peak usage times during business hours or holidays.

Automated Testing: Develop automated tests that simulate the login workflows and monitor performance metrics to catch regressions.

Performance Profiling: Perform continuous testing on all critical database queries to identify opportunities for optimization without compromising overall system stability. This will be automated and done during business hours or times when low traffic is present. The automation will provide reports that can be analyzed and then implemented with future planning.

This postmortem gives a clear picture of the importance of a thorough database monitoring/upgrade process and proactive monitoring for critical systems. By implementing the corrective and preventative measures outlined above, we can minimize the risk of similar incidents in the future.
