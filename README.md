Oracle WebLogic Server
=====

Version 0.1.0
-------------

![](http://www.oracle.com/ocom/groups/public/@otn/documents/digitalasset/352606.gif)

Installs and configures Oracle Weblogic Server 11g Release

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://github.com/qubell-bazaar/component-oracle-weblogic/raw/master/meta.yml)

Features
--------

 - Install and configure Oracle WebLogic Server

Configurations
--------------
[![Build Status](https://travis-ci.org/qubell-bazaar/component-oracle-weblogic.png?branch=master)](https://travis-ci.org/qubell-bazaar/component-oracle-weblogic)

 - Oracle Weblogic Server 11g, CentOS 6.4 (us-east-1/ami-ee698586) AWS EC2 m1.xlarge, root
 - Oracle Weblogic Server 11g, Amazon Linux (us-east-1/ami-1ba18d72) AWS EC2 m1.xlarge, ec2-user

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
  - Oracle WebLogic Server 11g distribution: [Download](http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-main-097127.html)
  - Oracle JRockit 6r28 distribution: [Download](http://www.oracle.com/technetwork/middleware/jrockit/downloads/index.html?ssSourceSiteId=otnpt) 
  - S3 bucket with Chef recipes: ** (TBD)
  - If Chef is not installed: ** (TBD)

Implementation notes
--------------------
 - Installation is based on Chef recipes

Example usage
-------------
```
- launch-vm:
    action: provisionVms
    parameters:
      hardwareId: "{$.instance-size}"
      imageId: "{$.image}"
      vmIdentity: "{$.image-user}"
      roleName: default
    output:
      wl-hosts: ips

- mount-storage:
    action: execrun
    precedingPhases: [launch-vm]
    parameters:
      roles: [ default ]
      command:
        - |
          mkdir -p /media/ephemeral0
          mount | grep /media/ephemeral0 || mount `curl -s http://169.254.169.254/latest/meta-data/block-device-mapping/ephemeral0 | tr 'a-d' 'e-h' | sed 's#^..#/dev/xvd#'` /media/ephemeral0
          yum -y install dejavu*

- set-hostname:
    action: execrun
    phase: set-hostname
    precedingPhases: [ mount-storage ]
    parameters:
      roles: [ default ]
      isSudo: true
      command:
        - curl -s http://169.254.169.254/latest/meta-data/public-hostname
    output:
      dns: stdout

- install-weblogic:
    action: chefsolo
    precedingPhases: [set-hostname]
    parameters:
      roles: [default]
      recipeUrl: "{$.recipe-url}"
      runList: ["recipe[weblogic_component::default]"]
      jattrs:
        weblogic:
          user: "{$.weblogic-user}"
          password: "{$.weblogic-user-password}"
          binary_url: "{$.weblogic-binary-url}"
          bea_home: "{$.installation-dir}"
          tmp_path: "{$.tmp-dir}"
        jrockit:
          binary_url: "{$.jrokit-binary-url}"
          bea_home: "{$.installation-dir}"
          tmp_path: "{$.tmp-dir}"
```
