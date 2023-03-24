# Configuration management using puppet

What Is Puppet?
Puppet is a Configuration Management tool that is used for deploying,
configuring and managing servers. It performs the following functions:
- Defining distinct configurations for each and every host, and continuously
checking and confirming whether the required configuration is in place and is
not altered (if altered Puppet will revert back to the required configuration)
on the host.
- Dynamic scaling-up and scaling-down of machines.
- Providing control over all your configured machines, so a centralized
(master-server or repo-based) change gets propagated to all, automatically.

Puppet uses a Master Slave architecture in which the Master and Slave
communicate through a secure encrypted channel with the help of SSL.
