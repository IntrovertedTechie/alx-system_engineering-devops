Postmortem: Outage in Web Application

 ![Alt Text](https://github.com/IntrovertedTechie/alx-system_engineering-devops/blob/master/0x19-postmortem/200%20(5).gif
)



Issue Summary:

Duration of the outage: May 6, 2023, 12:00 PM - May 6, 2023, 2:30 PM (WAT) 

Impact: The web application was down, and users were unable to access it. Approximately 80% of the users were affected.

Root Cause: The root cause of the outage was a database server issue. One of the database servers crashed, which caused the application to lose connectivity with the database. The application was configured to use the faulty server as the primary database, and it was unable to switch to the secondary database automatically.

Timeline:

12:00 PM: The issue was first detected when users started reporting that they were unable to access the application.

12:05 PM: The monitoring system triggered an alert, indicating that the database server was unresponsive.

12:10 PM: The DevOps team started investigating the issue and assumed that it was a networking problem, as they were able to ping the server.

12:20 PM: The team found that the issue was not with the network but with the database server. They attempted to restart the server, but it did not resolve the issue.

12:30 PM: Further investigation revealed that the primary database server was faulty and was not switching to the secondary server automatically.

12:45 PM: The team escalated the issue to the database administrators, who started working on the issue.

1:30 PM: The database administrators found that the database server had a corrupted file system, which caused it to crash. They were able to recover the file system and restart the server.

2:30 PM: The database server was back online, and the application was fully functional.

Misleading Investigation/Debugging Paths: The initial assumption that the issue was with the network caused a delay in identifying the root cause of the issue. The team should have investigated the database server first, as it was the most likely cause of the issue.

Incident Escalation: The incident was escalated to the database administrators, who had more expertise in dealing with database server issues.

Resolution: The database administrators found that the database server had a corrupted file system, which caused it to crash. They were able to recover the file system and restart the server. Once the server was back online, the application was able to connect to the database server and became fully functional.

Corrective and Preventative Measures: To prevent similar incidents from happening in the future, the following corrective and preventative measures will be implemented:

Set up automatic failover to the secondary database server to ensure that the application can switch to the secondary database automatically if the primary database fails.

Set up monitoring alerts for file system errors on the database server to detect potential issues before they cause an outage.

Conduct a thorough review of the application's configuration to ensure that it is properly configured to use the failover mechanism.

Conduct a post-incident review to identify areas for improvement and to ensure that the incident response process is updated accordingly.

Tasks:

Configure automatic failover to the secondary database server.

Set up monitoring alerts for file system errors on the database server.

Review the application's configuration and ensure that it is properly configured to use the failover mechanism.

Conduct a post-incident review to identify areas for improvement in the incident response process
